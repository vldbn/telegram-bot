from app.core.types import SizeType, PaymentType, ConfirmType
from app.services.pizza_service import Service
from app.state.pizza_state import State, PizzasStates


class TestPizzaService:
    def test_start(self):
        state = State()
        service = Service(state)
        assert service.start()

    def test_choose_size(self):
        state = State()
        service = Service(state)
        response = service.choose_size(SizeType.BIG.value)
        assert response
        assert state.state == PizzasStates.SIZE_IS_SET

    def test_choose_size_invalid_size(self):
        state = State()
        service = Service(state)
        response = service.choose_size("invalid")
        assert response
        assert state.state == PizzasStates.INIT

    def test_choose_payment(self):
        state = State()
        service = Service(state)
        service.choose_size(SizeType.BIG.value)
        response = service.choose_payment(PaymentType.CASH.value)
        assert response
        assert state.state == PizzasStates.PAYMENT_IS_SET

    def test_choose_payment_invalid(self):
        state = State()
        service = Service(state)
        service.choose_size(SizeType.BIG.value)
        response = service.choose_payment("invalid")
        assert response
        assert state.state == PizzasStates.SIZE_IS_SET

    def test_confirm(self):
        state = State()
        service = Service(state)
        service.choose_size(SizeType.BIG.value)
        service.choose_payment(PaymentType.CASH.value)
        response = service.confirm(ConfirmType.YES.value)
        assert response
        assert state.state == PizzasStates.CONFIRMED

    def test_confirm_invalid(self):
        state = State()
        service = Service(state)
        service.choose_size(SizeType.BIG.value)
        service.choose_payment(PaymentType.CASH.value)
        response = service.confirm("invalid")
        assert response
        assert state.state == PizzasStates.PAYMENT_IS_SET
