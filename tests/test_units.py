"""Tests for units."""

import enum

import pytest
from zigpy.quirks.v2.homeassistant import PERCENTAGE, UnitOfPower as QuirksUnitOfPower

from zha.units import InvalidUnitOfMeasureException, UnitOfPower, validate_unit


class NonQuirkUnitEnum(enum.Enum):
    """Non quirk unit enum."""

    ValidUnitPercentage = "%"
    InvalidUnitString = "fakeValue"
    InvalidUnitInt = 24
    InvalidUnitNone = None


class UnitOfMass(enum.Enum):
    """Unit of mass."""

    ValidUnitPercentage = "%"
    InvalidUnitString = "fakeValue"


@pytest.mark.parametrize(
    "inputUnit,expectedUnitResponse",
    [
        (QuirksUnitOfPower.WATT, UnitOfPower.WATT),
        (NonQuirkUnitEnum.ValidUnitPercentage, PERCENTAGE),
        (UnitOfMass.ValidUnitPercentage, PERCENTAGE),
    ],
)
def test_valid_enum_unit_return_unit_as_string(inputUnit, expectedUnitResponse) -> None:
    """Test validate_unit with valid unit returning unit."""

    validatedUnit = validate_unit(inputUnit)

    assert validatedUnit == expectedUnitResponse
    assert isinstance(validatedUnit, str)


@pytest.mark.parametrize(
    "inputUnit,expectedUnitResponse",
    [
        ("W", UnitOfPower.WATT),
        ("%", PERCENTAGE),
    ],
)
def test_valid_string_unit_return_unit_as_string(
    inputUnit, expectedUnitResponse
) -> None:
    """Test validate_unit with valid unit returning unit."""

    validatedUnit = validate_unit(inputUnit)

    assert validatedUnit == expectedUnitResponse
    assert isinstance(validatedUnit, str)


@pytest.mark.parametrize(
    "inputUnit",
    [
        NonQuirkUnitEnum.InvalidUnitString,
        NonQuirkUnitEnum.InvalidUnitInt,
        NonQuirkUnitEnum.InvalidUnitNone,
        UnitOfMass.InvalidUnitString,
        "fakeunit",
        42,
        None,
        "% ",  # Contains a valid unit, but has space
        "kwh",  # Is a valid unit, but invalid for casing.
        "WATT",  # Matches UnitOfPower.WATT Enum, not correct method to provide unit.
        "UnitOfPower.WATT",  # Matches UnitOfPower.WATT Enum, not correct method to provide unit.
    ],
)
def test_invalid_unit_exception_raised(inputUnit) -> None:
    """Test validate_unit with invalid unit raising InvalidUnitOfMeasureException."""

    with pytest.raises(InvalidUnitOfMeasureException):
        assert validate_unit(inputUnit)
