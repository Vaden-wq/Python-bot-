import telebot
import random

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Hello im a bot.")

@bot.message_handler(commands=['bye'])
def bye_message(message):
    bot.send_message(message.chat.id, "Ok, bye bye.")
    

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
    
@bot.message_handler(commands=['password'])
def password_message(message):
    new_password = gen_pass(15)
    bot.reply_to(message, f"Here is your password,  {new_password}")

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)

bot.polling(non_stop = True)
