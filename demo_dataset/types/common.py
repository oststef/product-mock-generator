from enum import Enum


class Brand(Enum):
    FERRO_SYNC = "FerroSync"
    ORBITAL_HOME = "Orbital Home"
    HOMETICS = "Hometics"
    CASACORE = "CasaCore"
    INTUIT_HOME = "Intuit Home"


class Platform(Enum):
    ALEXA = "Alexa"
    APPLE_HOME_KIT = "Apple Home Kit"
    GOOGLE_HOME = "Google Home"
    HOME_ASSISTANT = "Home Assistant"
    HUBITAT = "Hubitat"
    IFTTT = "IFTTT"
    MATTER = "Matter"
    SMART_THINGS = "SmartThings"
    TUYA = "Tuya"


class EnergyEfficiencyClass(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"


class CommunicationProtocol(Enum):
    BLUETOOTH = "BLUETOOTH"
    THREAD = "THREAD"
    WIFI = "WIFI"
    MATTER = "MATTER"
    Z_WAVE = "Z_WAVE"
    ZIGBEE = "ZIGBEE"


class Color(Enum):
    BLACK = "BLACK"
    BLUE = "BLUE"
    WHITE = "WHITE"
    SILVER = "SILVER"


class Shape(Enum):
    CIRCLE = "CIRCLE"
    OVAL = "OVAL"
    RECTANGLE = "RECTANGLE"
    SQUARE = "SQUARE"
    ROUNDED_SQUARE = "ROUNDED_SQUARE"
