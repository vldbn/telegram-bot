from enum import Enum


class SizeType(Enum):
    """Pizza's size enum"""
    BIG = "большую"
    SMALL = "маленькую"


class PaymentType(Enum):
    """Payment type enum"""
    CASH = "наличкой"
    BY_CARD = "картой"


class ConfirmType(Enum):
    """Confirm type enum"""
    YES = "да"
    NO = "нет"
