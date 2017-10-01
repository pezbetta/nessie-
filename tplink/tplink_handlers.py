from tplink.pyHS100.smartbulb import SmartBulb
from tplink.pyHS100.smartplug import SmartPlug

from secrets.secrets import SAMRT_BULB_IP, SAMRT_PLUG_IP
from bot_handlers.handler_decorator import command_handler


@command_handler('luz')
def lights(bot, update, args):
    bulb = SmartBulb(SAMRT_BULB_IP)
    print('user:{} text:{} args:{}'.format(update.message.chat_id, update.message.text, args))
    if len(args) == 0:
        if bulb.state == 'ON':
            bulb.state = 'OFF'
            bot.send_message(chat_id=update.message.chat_id, text='He apagado la luz')
        else:
            bulb.state = 'ON'
            bot.send_message(chat_id=update.message.chat_id, text='He encendido la luz')
    else:
        bulb.brightness = int(args[0])
        bot.send_message(chat_id=update.message.chat_id, text='He ajustado la luz al {}%'.format(args[0]))


@command_handler('tv')
def tv(bot, update, args):
    plug = SmartPlug(SAMRT_PLUG_IP)
    print('user:{} text:{}'.format(update.message.chat_id, update.message.text))
    if plug.state == 'ON':
        plug.state = 'OFF'
        bot.send_message(chat_id=update.message.chat_id, text='He apagado la tv')
    else:
        plug.state = 'ON'
        bot.send_message(chat_id=update.message.chat_id, text='He encendido la tv')
