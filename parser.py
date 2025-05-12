"""
Phone number parsing logic
– Regeln F-01 … F-09
– Mobil-Aufspaltung für deutsche Rufnummern
– Zusatzinfos: country_name, area_desc (Ort) oder carrier_name
"""

import re
import phonenumbers
from phonenumbers import (
    NumberParseException,
    PhoneNumberFormat,
    PhoneNumberType,
    number_type,
    geocoder,
    carrier,
)
from phonenumbers.phonenumberutil import length_of_geographical_area_code

ALLOWED_CHARS_PATTERN = re.compile(r"[\d\+\-\.\s/()\[\]]")

# --------------------------------------------------------------------------- #
#  Hilfsfunktionen
# --------------------------------------------------------------------------- #
def _sanitize(raw: str) -> str:
    return "".join(ch for ch in raw if ALLOWED_CHARS_PATTERN.match(ch))


def _strip_leading_zeros(raw: str) -> str:
    return "+" + raw.lstrip()[2:] if raw.lstrip().startswith("00") else raw


_EXT_RE = re.compile(r"(?:[;,#xX]|\bext\.?\s*)(\d{1,5})$")


def _extract_extension(raw: str) -> tuple[str, str | None]:
    m = _EXT_RE.search(raw)
    if m:
        return raw[: m.start()].strip(), m.group(1)
    m2 = re.search(r"(.*?[\-\.\s/])(\d{1,3})$", raw)
    if m2:
        return m2.group(1).rstrip(" -./"), m2.group(2)
    return raw, None


def _split_mobile(national: str) -> tuple[str, str]:
    """Zerteilt deutsche Mobilnummern in (prefix, subscriber)."""
    m = re.match(r"1[5-7]\d{2}", national)  # 15xx / 16xx / 17xx
    if m:
        return m.group(0), national[m.end() :]
    return "", national


def _format_human(cc: str, ac: str, local: str, ext: str | None) -> str:
    pieces = [cc]
    if ac:
        pieces.append(f"(0){ac}")
    if local:
        pieces.append(local if len(local) <= 4 else f"{local[:-4]}-{local[-4:]}")
    human = " ".join(pieces)
    return f"{human}-{ext}" if ext else human


# --------------------------------------------------------------------------- #
#  Hauptfunktion
# --------------------------------------------------------------------------- #
def parse_phone_number(raw_input: str, default_country: str = "DE") -> dict:
    cleaned = _strip_leading_zeros(_sanitize(raw_input))
    cleaned, ext = _extract_extension(cleaned)

    try:
        num = phonenumbers.parse(cleaned, default_country)
    except NumberParseException as err:
        raise ValueError(str(err)) from None

    if not phonenumbers.is_valid_number(num):
        raise ValueError("Ungültige Telefonnummer laut Internationaler Datenbank.")

    country_code = f"+{num.country_code}"
    national = str(num.national_number)

    # Festnetz vs. Mobil (nur DE)
    if num.country_code == 49 and number_type(num) == PhoneNumberType.MOBILE:
        area_code, local_number = _split_mobile(national)
    else:
        area_len = length_of_geographical_area_code(num)
        area_code = national[:area_len] if area_len else ""
        local_number = national[area_len:]

    e164 = phonenumbers.format_number(num, PhoneNumberFormat.E164)
    if ext:
        e164 = f"{e164}{ext}"

    human = _format_human(country_code, area_code, local_number, ext)

    # Zusatzinfos
    country_name = geocoder.country_name_for_number(num, "de")
    area_desc = geocoder.description_for_number(num, "de")  # Stadt/Bundesland
    carrier_name = (
        carrier.name_for_number(num, "de")
        if number_type(num) == PhoneNumberType.MOBILE
        else ""
    )

    return {
        "country_code": country_code,
        "area_code": area_code,
        "local_number": local_number,
        "extension": ext or "",
        "e164": e164,
        "human": human,
        "country_name": country_name,
        "area_desc": area_desc,
        "carrier_name": carrier_name,
    }
