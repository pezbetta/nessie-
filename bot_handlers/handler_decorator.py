from telegram.ext import CommandHandler


def command_handler(command):
    def handler_decorator(func):
        return CommandHandler(command, func, pass_args=True)
    return handler_decorator
