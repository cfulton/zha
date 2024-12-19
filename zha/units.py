"""Units of measure for Zigbee Home Automation."""

from enum import Enum, StrEnum
from typing import Final


class InvalidUnitOfMeasureException(Exception):
    """Exception for invalid unit of measure."""

    pass


class UnitOfTemperature(StrEnum):
    """Temperature units."""

    CELSIUS = "°C"
    FAHRENHEIT = "°F"
    KELVIN = "K"


class UnitOfMass(StrEnum):
    """Mass units."""

    GRAMS = "g"
    KILOGRAMS = "kg"
    MILLIGRAMS = "mg"
    MICROGRAMS = "µg"
    OUNCES = "oz"
    POUNDS = "lb"
    STONES = "st"


class UnitOfPressure(StrEnum):
    """Pressure units."""

    PA = "Pa"
    HPA = "hPa"
    KPA = "kPa"
    BAR = "bar"
    CBAR = "cbar"
    MBAR = "mbar"
    MMHG = "mmHg"
    INHG = "inHg"
    PSI = "psi"


class UnitOfPower(StrEnum):
    """Power units."""

    WATT = "W"
    KILO_WATT = "kW"
    BTU_PER_HOUR = "BTU/h"


class UnitOfApparentPower(StrEnum):
    """Apparent power units."""

    VOLT_AMPERE = "VA"


class UnitOfElectricCurrent(StrEnum):
    """Electric current units."""

    MILLIAMPERE = "mA"
    AMPERE = "A"


# Electric_potential units
class UnitOfElectricPotential(StrEnum):
    """Electric potential units."""

    MILLIVOLT = "mV"
    VOLT = "V"


class UnitOfFrequency(StrEnum):
    """Frequency units."""

    HERTZ = "Hz"
    KILOHERTZ = "kHz"
    MEGAHERTZ = "MHz"
    GIGAHERTZ = "GHz"


class UnitOfVolumeFlowRate(StrEnum):
    """Volume flow rate units."""

    CUBIC_METERS_PER_HOUR = "m³/h"
    CUBIC_FEET_PER_MINUTE = "ft³/min"
    LITERS_PER_MINUTE = "L/min"
    GALLONS_PER_MINUTE = "gal/min"


class UnitOfVolume(StrEnum):
    """Volume units."""

    CUBIC_FEET = "ft³"
    CENTUM_CUBIC_FEET = "CCF"
    CUBIC_METERS = "m³"
    LITERS = "L"
    MILLILITERS = "mL"
    GALLONS = "gal"
    """Assumed to be US gallons in conversion utilities.

    British/Imperial gallons are not yet supported"""
    FLUID_OUNCES = "fl. oz."
    """Assumed to be US fluid ounces in conversion utilities.

    British/Imperial fluid ounces are not yet supported"""


class UnitOfTime(StrEnum):
    """Time units."""

    MICROSECONDS = "μs"
    MILLISECONDS = "ms"
    SECONDS = "s"
    MINUTES = "min"
    HOURS = "h"
    DAYS = "d"
    WEEKS = "w"
    MONTHS = "m"
    YEARS = "y"


class UnitOfLength(StrEnum):
    """Length units."""

    MILLIMETERS = "mm"
    CENTIMETERS = "cm"
    METERS = "m"
    KILOMETERS = "km"
    INCHES = "in"
    FEET = "ft"
    YARDS = "yd"
    MILES = "mi"


class UnitOfEnergy(StrEnum):
    """Energy units."""

    GIGA_JOULE = "GJ"
    KILO_WATT_HOUR = "kWh"
    MEGA_JOULE = "MJ"
    MEGA_WATT_HOUR = "MWh"
    WATT_HOUR = "Wh"


# Concentration units
CONCENTRATION_MICROGRAMS_PER_CUBIC_METER: Final = "µg/m³"
CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER: Final = "mg/m³"
CONCENTRATION_MICROGRAMS_PER_CUBIC_FOOT: Final = "μg/ft³"
CONCENTRATION_PARTS_PER_CUBIC_METER: Final = "p/m³"
CONCENTRATION_PARTS_PER_MILLION: Final = "ppm"
CONCENTRATION_PARTS_PER_BILLION: Final = "ppb"

# Signal_strength units
SIGNAL_STRENGTH_DECIBELS: Final = "dB"
SIGNAL_STRENGTH_DECIBELS_MILLIWATT: Final = "dBm"

# Light units
LIGHT_LUX: Final = "lx"

# Percentage units
PERCENTAGE: Final[str] = "%"

UNITS_OF_MEASURE_SET = frozenset(
    set(UnitOfApparentPower._value2member_map_.keys())
    | set(UnitOfPower._value2member_map_.keys())
    | set(UnitOfEnergy._value2member_map_.keys())
    | set(UnitOfElectricCurrent._value2member_map_.keys())
    | set(UnitOfElectricPotential._value2member_map_.keys())
    | set(UnitOfTemperature._value2member_map_.keys())
    | set(UnitOfTime._value2member_map_.keys())
    | set(UnitOfFrequency._value2member_map_.keys())
    | set(UnitOfPressure._value2member_map_.keys())
    | set(UnitOfVolume._value2member_map_.keys())
    | set(UnitOfVolumeFlowRate._value2member_map_.keys())
    | set(UnitOfLength._value2member_map_.keys())
    | set(UnitOfMass._value2member_map_.keys())
    | {
        CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
        CONCENTRATION_MILLIGRAMS_PER_CUBIC_METER,
        CONCENTRATION_MICROGRAMS_PER_CUBIC_FOOT,
        CONCENTRATION_PARTS_PER_CUBIC_METER,
        CONCENTRATION_PARTS_PER_MILLION,
        CONCENTRATION_PARTS_PER_BILLION,
        SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
        SIGNAL_STRENGTH_DECIBELS,
        LIGHT_LUX,
        PERCENTAGE,
    }
)


def validate_unit(unit: str | Enum) -> str:
    """Validate and return a unit of measure."""

    check_unit = unit.value if isinstance(unit, Enum) else unit

    if check_unit in UNITS_OF_MEASURE_SET:
        return check_unit

    raise InvalidUnitOfMeasureException(
        f"Invalid unit of measurement: '{check_unit}'. Valid units are: {', '.join(f"'{unit_of_measure}'" for unit_of_measure in UNITS_OF_MEASURE_SET)}."
    )
