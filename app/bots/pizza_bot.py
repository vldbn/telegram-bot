import logging

from telegram import Update
from telegram.ext import (
    Updater,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    ShippingQueryHandler
)

from services.pizza_service import Service
from state.pizza_state import PizzasStates
from core.types import ConfirmType

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logging.getLogger(__name__)

class PizzaBot:
    def __init__(self, token: str, port: str, service: Service) -> None:
        self.token = token
        self.port = int(port)
        self.updater = Updater(token, use_context=True)
        self.service = service
        self.dispatcher = self.updater.dispatcher
        self.__config_handlers()

    def set_size(self, update: Update, context: CallbackContext) -> PizzasStates:
        update.message.reply_text(text=self.service.start())
        return self.service.get_state()

    def from_size_to_payment(self, update: Update, context: CallbackContext) -> PizzasStates:
        update.message.reply_text(text=self.service.choose_size(update.message.text))
        return self.service.get_state()

    def from_payment_to_confirm(self, update: Update, context: CallbackContext) -> PizzasStates:
        reply_keyboard = [[ConfirmType.YES.value, ConfirmType.NO.value]]
        update.message.reply_text(self.service.choose_payment(update.message.text))
        return self.service.get_state()

    def confirm(self, update: Update, context: CallbackContext) -> PizzasStates:
        update.message.reply_text(self.service.confirm(update.message.text))
        return self.service.get_state()

    def success(self, update: Update, context: CallbackContext):
        return ConversationHandler.END

    def cancel(self, update: Update, context: CallbackContext) -> int:
        """Cancels and ends the conversation."""
        self.service.set_init()
        return ConversationHandler.END

    def error(self, update, context):
        """Log Errors caused by Updates."""
        logging.warning('Update "%s" caused error "%s"', update, context.error)

    def __config_handlers(self):
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler('start', self.set_size)],
            states={
                PizzasStates.INIT: [MessageHandler(Filters.text, self.from_size_to_payment)],
                PizzasStates.SIZE_IS_SET: [MessageHandler(Filters.text, self.from_payment_to_confirm)],
                PizzasStates.PAYMENT_IS_SET: [MessageHandler(Filters.text, self.confirm)],
                PizzasStates.CONFIRMED: [ShippingQueryHandler(self.success)],
            },
            fallbacks=[CommandHandler('cancel', self.cancel)]
        )
        self.dispatcher.add_handler(conv_handler)
        self.dispatcher.add_error_handler(self.error)

    def start(self) -> None:
        self.updater.start_polling()
        self.updater.idle()
