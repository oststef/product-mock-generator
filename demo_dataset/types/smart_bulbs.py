from enum import Enum


class LightColor(Enum):
    WHITE = "WHITE"
    RGB = "RGB"


class Socket(Enum):
    E12 = "E12"
    E27 = "E27"
    E40 = "E40"
    E14 = "E14"
    G9 = "G9"


class BulbFeatures(Enum):
    MOTION_SENSOR = "MOTION_SENSOR"
    LIGHTING_EFFECTS = "LIGHTING_EFFECTS"


class RequiresHub(Enum):
    FOR_ALL_FEATURES = "FOR_ALL_FEATURES"
    FOR_SOME_FEATURES = "FOR_SOME_FEATURES"
    NO_HUB_REQUIRED = "NO_HUB_REQUIRED"
