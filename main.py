import telebot
import random
from bs4 import BeautifulSoup
from telebot import types

bot = telebot.TeleBot('1511767750:AAFygVIbM1AyISAbOJ0PiAypuXmMSTQMZjE')

gameVariants = [1, 2, 3]

# keyboards
mainBoard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
mainPlayGameKey = types.KeyboardButton(text='Играть')
mainCheckMyStatsKey = types.KeyboardButton(text='Мой профиль')
mainRulesKey = types.KeyboardButton(text='Правила игры')
mainBoard.add(mainPlayGameKey, mainRulesKey, mainCheckMyStatsKey)

gameBoard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
gameStone = types.KeyboardButton(text='Камень')
gameScissors = types.KeyboardButton(text='Ножницы')
gamePaper = types.KeyboardButton(text='Бумага')
gameRandom = types.KeyboardButton(text='Рандом')
gameBack = types.KeyboardButton(text='Назад')
gameBoard.add(gameStone, gameScissors, gamePaper, gameRandom, gameBack)

# start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'hello', reply_markup=mainBoard)

# game command
@bot.message_handler(regexp='Играть')
def playGame(message):
    bot.send_message(message.chat.id, 'выберите кнопку', reply_markup=gameBoard)
@bot.message_handler(regexp='Камень')
def gamePlayStone(message):
    botChoice = random.choice(gameVariants)
    playerChoice = random.choice(gameVariants)
    if botChoice == playerChoice:
        bot.send_message(message.chat.id, '=')
    elif botChoice > playerChoice:
        bot.send_message(message.chat.id, '-')
    elif botChoice < playerChoice:
        bot.send_message(message.chat.id, '+')
@bot.message_handler(regexp='Ножницы')
def gamePlayScissors(message):
    botChoice = random.choice(gameVariants)
    playerChoice = random.choice(gameVariants)
    if botChoice == playerChoice:
        bot.send_message(message.chat.id, '=')
    elif botChoice > playerChoice:
        bot.send_message(message.chat.id, '-')
    elif botChoice < playerChoice:
        bot.send_message(message.chat.id, '+')
@bot.message_handler(regexp='Бумага')
def gamePlayPaper(message):
    botChoice = random.choice(gameVariants)
    playerChoice = random.choice(gameVariants)
    if botChoice == playerChoice:
        bot.send_message(message.chat.id, '=')
    elif botChoice > playerChoice:
        bot.send_message(message.chat.id, '-')
    elif botChoice < playerChoice:
        bot.send_message(message.chat.id, '+')
@bot.message_handler(regexp='Рандом')
def gamePlayRandom(message):
    botChoice = random.choice(gameVariants)
    playerChoice = random.choice(gameVariants)
    if botChoice == playerChoice:
        bot.send_message(message.chat.id, '=')
    elif botChoice > playerChoice:
        bot.send_message(message.chat.id, '-')
    elif botChoice < playerChoice:
        bot.send_message(message.chat.id, '+')


bot.infinity_polling(True)