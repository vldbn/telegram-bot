from bots.pizza_bot import PizzaBot
from core.conf import Config
from services.pizza_service import Service
from state.pizza_state import State


def configure_bot() -> PizzaBot:
    """Util for configuring application"""
    config = Config()
    state = State()
    service = Service(state)
    return PizzaBot(config.token, config.port, service)
