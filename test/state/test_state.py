from app.core.types import SizeType, PaymentType, ConfirmType
from app.state.pizza_state import State, PizzasStates


class TestState:
    def test_init_state(self):
        state = State()
        assert state.state == PizzasStates.INIT

    def test_size_is_set(self):
        state = State()
        state.choose_size(SizeType.BIG)
        assert state.state == PizzasStates.SIZE_IS_SET
        assert state.size == SizeType.BIG

    def test_size_is_set(self):
        state = State()
        state.choose_size(SizeType.BIG)
        state.choose_payment(PaymentType.CASH)
        assert state.state == PizzasStates.PAYMENT_IS_SET
        assert state.size == SizeType.BIG
        assert state.payment == PaymentType.CASH

    def test_payment_is_set(self):
        state = State()
        state.choose_size(SizeType.BIG)
        state.choose_payment(PaymentType.CASH)
        state.confirm(ConfirmType.YES)
        assert state.state == PizzasStates.CONFIRMED
        assert state.size == SizeType.BIG
        assert state.payment == PaymentType.CASH
        assert state.confirmed == ConfirmType.YES
