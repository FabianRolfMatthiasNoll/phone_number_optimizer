"""
Phone number parsing logic.

Implements Functional Rules F‑01 … F‑09 from the spec.
Relies on the `phonenumbers` library and small heuristics for extensions.
"""

import re
import phonenumbers
from phonenumbers import NumberParseException, PhoneNumberFormat
from phonenumbers.phonenumberutil import length_of_geographical_area_code

ALLOWED_CHARS_PATTERN = re.compile(r"[\d\+\-\.\s/()\[\]]")


def _sanitize(raw: str) -> str:
    """Strip disallowed characters but keep semantic separators (F‑01)."""
    return "".join(ch for ch in raw if ALLOWED_CHARS_PATTERN.match(ch))


def _strip_leading_zeros(raw: str) -> str:
    """Convert 00🇨🇭 prefix to + (F‑02)."""
    return "+" + raw.lstrip()[2:] if raw.lstrip().startswith("00") else raw


_EXT_RE = re.compile(
    r"(?:[;,#xX]|\bext\.?\s*)(\d{1,5})$"  # phonenumbers ignores ";ext=23"
)


def _extract_extension(raw: str) -> tuple[str, str | None]:
    """Return number_without_ext, extension_or_None (F‑06)."""
    m = _EXT_RE.search(raw)
    if m:
        return raw[: m.start()].strip(), m.group(1)
    # Heuristic: ≤3 trailing digits after a separator
    m2 = re.search(r"(.*?[\-\.\s/])(\d{1,3})$", raw)
    if m2:
        return m2.group(1).rstrip(" -./"), m2.group(2)
    return raw, None


def _format_human(cc: str, ac: str, local: str, ext: str | None) -> str:
    """Construct +49 (0)711 123‑4567‑89 layout (F‑09)."""
    pieces: list[str] = [cc]
    if ac:
        pieces.append(f"(0){ac}")
    if local:
        # naive grouping 3‑4‑n
        if len(local) > 4:
            pieces.append(f"{local[:-4]}‑{local[-4:]}")
        else:
            pieces.append(local)
    human = " ".join(pieces)
    return f"{human}‑{ext}" if ext else human


def parse_phone_number(raw_input: str, default_country: str = "DE") -> dict:
    """Parse and split a phone number string.

    Returns a dict with keys:
      country_code, area_code, local_number, extension, e164, human
    Raises ValueError for invalid inputs (F‑08).
    """
    cleaned = _sanitize(raw_input)
    cleaned = _strip_leading_zeros(cleaned)
    cleaned, ext = _extract_extension(cleaned)

    try:
        num = phonenumbers.parse(cleaned, default_country)
    except NumberParseException as err:
        raise ValueError(str(err)) from None

    if not phonenumbers.is_valid_number(num):
        raise ValueError("Ungültige Telefonnummer laut phonenumbers.")

    country_code = f"+{num.country_code}"
    national = str(num.national_number)
    area_len = length_of_geographical_area_code(num)
    area_code = national[:area_len] if area_len else ""
    local_number = national[area_len:]

    e164 = phonenumbers.format_number(num, PhoneNumberFormat.E164)
    if ext:
        e164 = f"{e164}{ext}"

    human = _format_human(country_code, area_code, local_number, ext)

    return {
        "country_code": country_code,
        "area_code": area_code,
        "local_number": local_number,
        "extension": ext or "",
        "e164": e164,
        "human": human,
    }
