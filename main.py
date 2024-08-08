import telebot

bot = telebot.TeleBot("7413317567:AAG-zqGHV4cYUtOW8FNVSzp_a64nFiWolek")


@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "Салют,художник!")


@bot.message_handler(commands=["relaxation"])
def relaxation_handler(message):
    bot.send_message(message.chat.id, "[_Расслабься_](https://www.youtube.com/watch?v=1i-q1nClD0Y)",parse_mode='Markdown')

@bot.message_handler(commands=["recommendations"])
def recommendations_handler(message):
    bot.send_message(message.chat.id, "[*Что-то интерсное*](https://web-paint.site/uroki-risovaniya/idei-dlya-risovaniya/netradiczionnye-tehniki-risovaniya-dlya-vzroslyh-i-detej.html)", parse_mode = 'markdown')

@bot.message_handler(commands=["anecdote"])
def anecdote_handler(message):
    bot.send_message(message.chat.id,
                     "В мороз у уличных художников-портретистов на Невском проспекте в Питере быстрее всего заканчиваются синие карандаши.")


@bot.message_handler(commands=["photo"])
def photo_handler(message):
    bot.send_photo(message.chat.id,
                   "https://fotovmire.ru/wp-content/uploads/2019/07/21681/kotjonok-zevaet-na-divane-640x360.jpg")


@bot.message_handler(commands=["music"])
def music_handler(message):
    bot.send_audio(message.chat.id, "https://fonau.ru/station/fass-furious/")

bot.infinity_polling()





