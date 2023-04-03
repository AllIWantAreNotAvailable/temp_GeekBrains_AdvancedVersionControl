import sys
import telebot


def main(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start(message, result: bool = False):
        bot.send_message(message.chat.id, 'Привет, я готов к работе!')

    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        bot.send_message(message.chat.id, f'Зачем вы написали мне: "{message.text}"?')

    bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    try:
        start_argv = sys.argv[1]
    except IndexError:
        print('Токен бота должен быть указан 1-м параметром запуска')
    else:
        main(start_argv)
