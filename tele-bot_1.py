from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler

k = 0
percent = 0
percent_2 = 0
amount = 0

def start(bot, update):
    global k
    k = 0
    update.message.reply_text("Привет! Если хочешь проверить свои знания по географии, то ты обратился по адресу:) Викторина состоит из двух частей. Начнем с первой части. Я буду присылать тебе достопримечательности, а ты должен будешь угадать, в каком городе они находятся. За верный ответ ты получаешь балл. В конце викторины ответы суммируются, и я подвожу итоги о твоих знаниях по географии. Если захочешь завершить игру, напиши /stop. Когда будешь готов - напиши 'Готов', и мы начнём!")



def quiz(bot, update):
    global k, percent, amount, percent_2

    percent = 0
    percent_2 = 0

    m = k-1
    l = m-1
    a = l-1
    b = a-1
    c = b-1
    d = c-1
    e = d-1
    f = e-1
    g = f-1
    h = g-1
    i = h-1
    j = i-1
    o = j-1
    p = o-1
    q = p-1
    r = q-1
    s = r-1
    t = s-1
    u = t-1

    if k == 0:
        update.message.reply_text("В каком городе находится эта достопримечательность?")
        bot.sendPhoto(update.message.chat.id, 'http://www.kalinkatours.no/var/kalinkatours/storage/images/media/images/kunstmuseet-eremitasjen-i-vinterpalasset-16-93/61034-1-nor-NO/kunstmuseet-eremitasjen-i-vinterpalasset-16-9_size-large.jpg')
    if update.message.text == "Санкт-Петербург" and k == 1:
        update.message.reply_text("Верно! Молодец! А это откуда?")
        percent += 1
    elif k == 1 and update.message.text != "Санкт-Петербург":
        update.message.reply_text("Ошибочка вышла. Правильный ответ: Санкт-Петербург. А это откуда?")

    k += 1

    if m == 0:
        bot.sendPhoto(update.message.chat.id, 'http://www.kaluga-land.com/files/uploads/images/panorama_kreml_3(1).jpg')
    if update.message.text == "Казань" and m == 1:
        update.message.reply_text("Правильно! Где находится эта достопримечательность?")
        percent += 1
    elif m == 1 and update.message.text != "Казань":
        update.message.reply_text("Ошибочка вышла. Правильный ответ: Казань\nГде находится эта достопримечательность?")

    if l == 0:
        bot.sendPhoto(update.message.chat.id, 'https://www.votpusk.ru/country/ctimages/new/FR01.jpg')
    if update.message.text == "Париж" and l == 1:
        update.message.reply_text("Верно! А эта откуда?")
        percent += 1
    elif l == 1 and update.message.text != "Париж":
        update.message.reply_text("Ошибочка вышла. Правильный ответ: Париж\nА эта откуда?")

    if a == 0:
        bot.sendPhoto(update.message.chat.id, 'http://prirodadi.ru/wp-content/uploads/2013/09/Velikaya-Kitayskaya-Stena.jpg')
    if update.message.text == "Пекин" and a == 1:
        update.message.reply_text("Молодец! Где находится эта достопримечательность?")
        percent += 1
    elif a == 1 and update.message.text != "Пекин":
        update.message.reply_text("Ошибочка вышла. Правильный ответ: Пекин\nГде находится эта достопримечательность?")

    if b == 0:
        bot.sendPhoto(update.message.chat.id, 'https://static.tonkosti.ru/images/3/37/%D0%A0%D0%B8%D0%BC%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D0%BE%D0%BB%D0%B8%D0%B7%D0%B5%D0%B9.jpg')
    if update.message.text == "Рим" and b == 1:
        update.message.reply_text("Правильно! Откуда эта достопримечательность?")
        percent += 1
    elif b == 1 and update.message.text != "Рим":
        update.message.reply_text("Ошибочка вышла. Правильный ответ: Рим\nОткуда эта достопримечательность?")

    if c == 0:
        bot.sendPhoto(update.message.chat.id, 'http://tayga.info/media/images/news/121/121083/thumb.jpg')
    if update.message.text == "Лондон" and c == 1:
        update.message.reply_text("Верно! А эта откуда?")
        percent += 1
    elif c == 1 and update.message.text != "Лондон":
        update.message.reply_text("Ошибочка вышла. Правильный ответ: Лондон\nА эта откуда?")

    if d == 0:
        bot.sendPhoto(update.message.chat.id, 'https://www.burgessyachts.com/media/adminforms/locations/n/e/new_york_1.jpg')
    if update.message.text == "Нью-Йорк" and d == 1:
        update.message.reply_text("Правильно! Где находится эта достопримечательность?")
        percent += 1
    elif d == 1 and update.message.text != "Нью-Йорк":
        update.message.reply_text("Ошибочка вышла. Правильный ответ: Нью-Йорк\nГде находится эта достопримечательность?")

    if e == 0:
        bot.sendPhoto(update.message.chat.id, 'https://www.aeroflot.ru/media/aflfiles/gr/ath/ath_3.jpg')
    if update.message.text == "Афины" and e == 1:
        update.message.reply_text("Верно! Молодец! А это откуда?")
        percent += 1
    elif e == 1 and update.message.text != "Афины":
        update.message.reply_text("Ошибочка вышла. Правильный ответ: Афины. А это откуда?")

    if f == 0:
        bot.sendPhoto(update.message.chat.id, 'http://www.meros.org/uzc/wonder/avatar?id=464')
    if update.message.text == "Пиза" and f == 1:
        update.message.reply_text("Правильно! Откуда эта достопримечательность?")
        percent += 1
    elif f == 1 and update.message.text != "Пиза":
        update.message.reply_text("Ошибочка вышла. Правильный ответ: Пиза\nОткуда эта достопримечательность?")

    if g == 0:
        bot.sendPhoto(update.message.chat.id, 'https://i.ytimg.com/vi/oZY0TYeYTB8/maxresdefault.jpg')
    if update.message.text == "Сан-Франциско" and g == 1:
        update.message.reply_text("Верно!")
        percent += 1
        update.message.reply_text("Итак, первая часть вопросов подошла к концу. Пока что у тебя {} баллов. Перейдем ко второй части. Я буду присылать тебе вопросы по географии, которые, кстати, будут сложными, но интересными. За каждый верный ответ 1 балл. Пожалуй, начнём!\nИтак, первый вопрос: как называется остров, на котором, согласно древнегреческой легенде, находился лабиринт Минотавра?".format(percent))

    elif g == 1 and update.message.text != "Сан-Франциско":
        update.message.reply_text("Ошибочка вышла. Правильный ответ: Сан-Франциско")
        update.message.reply_text("Итак, первая часть вопросов подошла к концу. Пока что у тебя {} баллов. Перейдем ко второй части. Я буду присылать тебе вопросы по географии, которые, кстати, будут сложными, но интересными. За каждый верный ответ 1 балл. Пожалуй, начнём!\nИтак, первый вопрос: как называется остров, на котором, согласно древнегреческой легенде, находился лабиринт Минотавра?".format(percent))

    if h == 1 and update.message.text == "Крит":
        update.message.reply_text("В яблочко! Второй вопрос: как называется главный остров Японии?")
        percent_2 += 1
    elif h == 1 and update.message.text != "Крит":
        update.message.reply_text("К сожалению, это неверный ответ. Правильный ответ: Крит. Второй вопрос: как называется главный остров Японии?")

    if i == 1 and update.message.text == "Хонсю":
        update.message.reply_text("Верно! Третий вопрос: какой остров самый большой в Европе?")
        percent_2 += 1
    elif i == 1 and update.message.text != "Хонсю":
        update.message.reply_text("Ошибочка вышла. Правильный ответ: Хонсю. Четвёртый вопрос: какой остров самый большой в Европе?")

    if j == 1 and update.message.text == "Великобритания":
        update.message.reply_text("Молодец! Четвёртый вопрос: какой известный горный хребет и река носят одно и то же название?")
        percent_2 += 1
    elif j == 1 and update.message.text != "Великобритания":
        update.message.reply_text("Неверно. Правильный ответ: Великобритания. Четвёртый вопрос: какой известный горный хребет и река носят одно и то же название?")

    if o == 1 and update.message.text == "Урал":
        update.message.reply_text("Правильно! Пятый вопрос: какой материк пересекается всеми меридианами?")
        percent_2 += 1
    elif o == 1 and update.message.text != "Урал":
        update.message.reply_text("Ошибочка. Правильный ответ: Урал. Пятый вопрос: какой материк пересекается всеми меридианами?")

    if p == 1 and update.message.text == "Антарктида":
        update.message.reply_text("В яблочко! Шестой вопрос: в это озеро в России впадает 336 рек, а вытекает только одна. Что это за озеро?")
        percent_2 += 1
    elif p == 1 and update.message.text != "Антарктида":
        update.message.reply_text("Неверно. Правильный ответ: Антарктида. Шестой вопрос: в это озеро в России впадает 336 рек, а вытекает только одна. Что это за озеро?")

    if q == 1 and update.message.text == "Байкал":
        update.message.reply_text("Верно! Седьмой вопрос: как называется самая большая пустыня Евразии?")
        percent_2 += 1
    elif q == 1 and update.message.text != "Байкал":
        update.message.reply_text("Ошибочка вышла. Правильный ответ: Байкл. Седьмой вопрос: как называется самая большая пустыня Евразии?")

    if r == 1 and update.message.text == "Гоби":
        update.message.reply_text("Молодец! Восьмой вопрос: как называется страна, которой принадлежат Командорские острова?")
        percent_2 += 1
    elif r == 1 and update.message.text != "Гоби":
        update.message.reply_text("Неверно. Правильный ответ: Гоби. Восьмой вопрос: как называется страна, которой принадлежат Командорские острова?")

    if s == 1 and update.message.text == "Россия":
        update.message.reply_text("Правильно! Девятый вопрос: какое море самое большое в мире?")
        percent_2 += 1
    elif s == 1 and update.message.text != "Россия":
        update.message.reply_text("Ошибочка вышла. Правильный ответ: Россия. Девятый вопрос: какое море самое большое в мире?")

    if t == 1 and (update.message.text == "Саргассово" or update.message.text == "Саргассово море"):
        update.message.reply_text("Верно! Десятый вопрос: в какой части света находятся Скалистые горы?")
        percent_2 += 1
    elif t == 1 and update.message.text != "Саргассово" and update.message.text != "Саргассово море":
        update.message.reply_text("Неверно. Правильный ответ: Саргассово. Десятый вопрос: в какой части света находятся Скалистые горы?")

    if u == 1 and (update.message.text == "Северная Америка" or update.message.text == "Северная америка"):
        update.message.reply_text("Молодец!")
        percent_2 += 1
        sum = percent+percent_2
        if 0 <= sum < 5:
            word = "Что-то мне подсказывает, что географ из тебя так себе..."
        elif 5 <= sum < 10:
            word = "Ну, могло быть и хуже..."
        elif 10 <= sum <15:
            word = "Неплохо, но могло быть и лучше:)"
        else:
            word = "Отлично! Очень хороший результат:)"
        update.message.reply_text("Итак, вторая часть вопросов подошла к концу. За неё ты набрал {} баллов.".format(percent_2))
        update.message.reply_text("Итого ты набрал {} баллов из 20. {} Если хочешь пройти викторину заново, напиши /start".format(percent+percent_2, word))

    elif u == 1 and update.message.text != "Северная Америка" and update.message.text != "Северная америка":
        sum = percent+percent_2
        if 0 <= sum < 5:
            word = "Что-то мне подсказывает, что географ из тебя так себе..."
        elif 5 <= sum < 10:
            word = "Ну, могло быть и хуже..."
        elif 10 <= sum <15:
            word = "Неплохо, но могло быть и лучше:)"
        else:
            word = "Отлично! Очень хороший результат:)"
        update.message.reply_text("Неверно. Правильный ответ: Северная Америка")
        update.message.reply_text("Итого ты набрал {} баллов из 20. {} Если хочешь пройти викторину заново, напиши /start".format(percent+percent_2, word))


def stop(bot, update):
    update.message.reply_text(
        "До встречи!")
    return ConversationHandler.END

def main():

    updater = Updater("569682197:AAGiCAdMiMVFTzslmPfdF6AJu3X0KKpmMSY")

    dp = updater.dispatcher

    text_handler = MessageHandler(Filters.text, quiz)

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(text_handler)

    dp.add_handler(CommandHandler("stop", stop))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
