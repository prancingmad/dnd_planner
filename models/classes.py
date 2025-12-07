from config import (
    ARTI_MOD,
    BARB_MOD,
    BARD_MOD,
    CLER_MOD,
    DRUI_MOD,
    FIGH_MOD,
    MONK_MOD,
    PALA_MOD,
    RANG_MOD,
    ROGU_MOD,
    SORC_MOD,
    WARL_MOD,
    WIZA_MOD
)

class BaseClass:
    def __init__(self, name, level, mod):
        self.name = name
        self.level = level
        self.mod = mod

    def get_combat_value(self):
        return self.level * self.mod

class Artificer(BaseClass):
    def __init__(self, level):
        super().__init__("Artificer", level, ARTI_MOD)

class Barbarian(BaseClass):
    def __init__(self, level):
        super().__init__("Barbarian", level, BARB_MOD)

class Bard(BaseClass):
    def __init__(self, level):
        super().__init__("Bard", level, BARD_MOD)

class Cleric(BaseClass):
    def __init__(self, level):
        super().__init__("Cleric", level, CLER_MOD)

class Druid(BaseClass):
    def __init__(self, level):
        super().__init__("Druid", level, DRUI_MOD)

class Fighter(BaseClass):
    def __init__(self, level):
        super().__init__("Fighter", level, FIGH_MOD)

class Monk(BaseClass):
    def __init__(self, level):
        super().__init__("Monk", level, MONK_MOD)

class Paladin(BaseClass):
    def  __init__(self, level):
        super().__init__("Paladin", level, PALA_MOD)

class Ranger(BaseClass):
    def __init__(self, level):
        super().__init__("Ranger", level, RANG_MOD)

class Rogue(BaseClass):
    def __init__(self, level):
        super().__init__("Rogue", level, ROGU_MOD)

class Sorcerer(BaseClass):
    def __init__(self, level):
        super().__init__("Sorcerer", level, SORC_MOD)

class Warlock(BaseClass):
    def __init__(self, level):
        super().__init__("Warlock", level, WARL_MOD)

class Wizard(BaseClass):
    def __init__(self, level):
        super().__init__("Wizard", level, WIZA_MOD)