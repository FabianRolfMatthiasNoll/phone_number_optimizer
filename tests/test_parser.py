import pytest
from parser import parse_phone_number

# ----------------------- Valid numbers with exact expectations ----------------------- #
VALID_EXPECTED = [
    ("+49 711 1234567-34", ("+49", "711", "1234567", "34")),
    ("0049 711 1234567", ("+49", "711", "1234567", "")),
    ("(0711) 1234567", ("+49", "711", "1234567", "")),
    ("+49 0201 123456", ("+49", "201", "123456", "")),
    ("0049201123456", ("+49", "201", "123456", "")),
    ("(0)201 1234 56", ("+49", "201", "1234", "56")),
    ("+49 (941) 790-4780", ("+49", "941", "7904780", "")),
    ("015115011900", ("+49", "", "15115011900", "")),
    ("[+49] (0)89-800/849-50", ("+49", "89", "800849", "50")),
    ("+49 (8024) [990-477]", ("+49", "8024", "990477", "")),
    ("0033 0201/123456", ("+33", "2", "01123456", "")),
]


@pytest.mark.parametrize("raw,exp", VALID_EXPECTED)
def test_parse_valid_exact(raw, exp):
    res = parse_phone_number(raw)
    assert (
        res["country_code"],
        res["area_code"],
        res["local_number"],
        res["extension"],
    ) == exp


# ----------------------- Invalid numbers ----------------------- #
INVALID = [
    "+44 0201123456",  # UK: trunk '0' present, NSN length not valid
    "+91 09870987 899",
]


@pytest.mark.parametrize("raw", INVALID)
def test_parse_invalid(raw):
    with pytest.raises(ValueError):
        parse_phone_number(raw)
