import logging

from telegram.ext import Updater, CommandHandler
from secrets.secrets import TELEGRAM_TOKEN

from bot_handlers import HANDLERS


updater = Updater(token=TELEGRAM_TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def start(bot, update):
    """
    Dafault handler to start a conversation
    :param bot:
    :param update:
    :return:
    """
    bot.send_message(
        chat_id=update.message.chat_id,
        text="soy Nessie+, tu asistente de hogar"
    )

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

for handler in HANDLERS:
    dispatcher.add_handler(handler)


updater.start_polling()

