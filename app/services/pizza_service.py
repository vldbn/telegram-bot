from state.pizza_state import State
from core.types import SizeType, PaymentType, ConfirmType


class Service:
    """Pizza Bor service class."""

    def __init__(self, state: State) -> None:
        self.state = state

    def start(self) -> str:
        return self.state.response()

    def choose_size(self, size: str) -> str:
        try:
            size = SizeType(size.lower())
            self.state.choose_size(size)
            return self.state.response()
        except ValueError:
            return f"Указан неправильный размер. Отправьте '{SizeType.BIG.value}', либо '{SizeType.SMALL.value}'"

    def choose_payment(self, payment: str) -> str:
        try:
            payment = PaymentType(payment.lower())
            self.state.choose_payment(payment)
            return self.state.response()
        except ValueError:
            return f"Неверный способ оплаты. Отправьте '{PaymentType.CASH.value}', либо '{PaymentType.BY_CARD.value}'"

    def confirm(self, confirm: str) -> str:
        try:
            confirm = ConfirmType(confirm.lower())
            self.state.confirm_order(confirm)
            return self.state.response()
        except ValueError:
            return f"Неверный ответ. Отправьте '{ConfirmType.YES.value}', либо '{ConfirmType.NO.value}'"

    def set_init(self) -> None:
        self.state.to_INIT()

    def get_state(self) -> State:
        return self.state.state
