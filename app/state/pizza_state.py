from enum import Enum
from typing import Dict, List

from transitions import Machine

from core.types import SizeType, PaymentType, ConfirmType


class PizzasStates(Enum):
    """Pizza's states enum"""
    INIT = 0
    SIZE_IS_SET = 1
    PAYMENT_IS_SET = 2
    CONFIRMED = 3
    COMPLETE = 4


class State:
    """Pizza Bot State class."""
    size: SizeType = None
    payment: PaymentType = None
    confirmed: ConfirmType = None

    def __init__(self) -> None:
        self.machine = Machine(
            model=self,
            states=PizzasStates,
            initial=PizzasStates.INIT,
            transitions=self.__transitions()
        )

    def set_size(self, size: SizeType) -> None:
        self.size = size

    def set_payment(self, payment: PaymentType) -> None:
        self.payment = payment

    def confirm_order(self, confirm: ConfirmType) -> None:
        self.confirmed = confirm
        if confirm == ConfirmType.NO:
            self.to_INIT()
        else:
            self.to_CONFIRMED()

    def response(self) -> str:
        if self.is_INIT():
            return f"Какую вы хотите пиццу?  {SizeType.BIG.value} или {SizeType.SMALL.value}?"
        elif self.is_SIZE_IS_SET():
            return "Как вы будете платить?"
        elif self.is_PAYMENT_IS_SET():
            return f"Вы хотите {self.size.value} пиццу, оплата - {self.payment.value}?"
        elif self.is_CONFIRMED():
            return "Спасибо за заказ"

    def __transitions(self) -> List[Dict]:
        transitions = [
            {
                "trigger": "choose_size",
                "source": PizzasStates.INIT,
                "dest": PizzasStates.SIZE_IS_SET,
                "before": "set_size"
            },
            {
                "trigger": "choose_payment",
                "source": PizzasStates.SIZE_IS_SET,
                "dest": PizzasStates.PAYMENT_IS_SET,
                "before": "set_payment"
            },
            {
                "trigger": "confirm",
                "source": PizzasStates.PAYMENT_IS_SET,
                "dest": PizzasStates.CONFIRMED,
                "before": "confirm_order"
            },
        ]
        return transitions
