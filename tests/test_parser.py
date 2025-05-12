import pytest
from parser import parse_phone_number


@pytest.mark.parametrize(
    "raw,exp",
    [
        ("+49 711 1234567-34", ("+49", "711", "1234567", "34")),
        ("0049 711 1234567", ("+49", "711", "1234567", "")),
        ("(0711) 1234567", ("+49", "711", "1234567", "")),
    ],
)
def test_parse(raw, exp):
    res = parse_phone_number(raw)
    assert (
        res["country_code"],
        res["area_code"],
        res["local_number"],
        res["extension"],
    ) == exp
