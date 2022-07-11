import telebot

# Api Bot Telegram
api = "" 
#example api = "hagvsdjhgdhjfgdjhfdyifvdyidfuyf"

bot = telebot.TeleBot(api)
@bot.message_hendler(commands=['start'])
def send_welcome(message, "Hallo Sir")

print("Bot Running..")
bot.polling()
