import sys
import telebot
import wikipedia


def main(token):
    bot = telebot.TeleBot(token)
    wikipedia.set_lang('ru')

    def get_wiki(article):
        try:
            spam = wikipedia.page(article)
            sentences = spam.content[:1000].split('.')[:-1]
            annotation = '.'.join(sentence for sentence in sentences if '==' not in sentence and 3 < len(sentence.strip()))
            annotation += '.'
        except Exception as ex:
            print(ex)
            return 'Ничего не знаю об этом ;\'('
        else:
            return annotation

    @bot.message_handler(commands=["start"])
    def start(message, result: bool = False):
        bot.send_message(message.chat.id, 'Хей, я прямо живая энциклопедия, верну тебе информацию о все чем скажешь!')

    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        bot.send_message(message.chat.id, get_wiki(message.text))

    bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    try:
        start_argv = sys.argv[1]
    except IndexError:
        print('Токен бота должен быть указан 1-м параметром запуска')
    else:
        main(start_argv)
