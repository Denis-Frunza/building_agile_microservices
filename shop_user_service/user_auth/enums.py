from enum import Enum

class GenderChoices(Enum):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class StatusChoices(Enum):
    ACTIVE = "Active"
    DELETED = "Deleted"
    SUSPENDED = "Suspended"
    BLOCKED = "Blocked"
    RESTRICTED = "Restricted"
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
