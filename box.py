import telebot

bot = telebot.TeleBot("5959592035:AAHFfTbtlGp6v59F4xK9DpO70O3eE2fAiZg", parse_mode=None) 
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "treasure, how was your day?")


    

bot.infinity_polling()