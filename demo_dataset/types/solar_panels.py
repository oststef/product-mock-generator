from enum import Enum


class SolarBrand(Enum):
    AURORA_PANEL = "Aurora Panel"
    SOLAR_TUITIVE = "SolarTuitive"
    YELLOW_DWARF_POWER = "Yellow Dwarf Power"


class PanelLength(Enum):
    SMALL = 1400
    MEDIUM = 1700
    LARGE = 1950


class PanelHeight(Enum):
    SMALL = 1000
    MEDIUM = 1200
    LARGE = 1500


class PanelWidth(Enum):
    THIN = 30
    MEDIUM = 40
    THICK = 50
