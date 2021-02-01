import telebot
import random
import sqlite3 as sq
from telebot import types

bot = telebot.TeleBot('1511767750:AAFygVIbM1AyISAbOJ0PiAypuXmMSTQMZjE')

gameVariants = [1, 2, 3]


# data base
with sq.connect("users.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        telegram_id INTEGER PRIMARY KEY,
        name TEXT,
        balance INTEGER,
        rank INTEGER
    )""")


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
    try:
        with sq.connect("users.db") as con:
            cur = con.cursor()
            cur.execute(f"INSERT INTO users(telegram_id, name, balance, rank) VALUES({message.chat.id}, 'Не указано', 5000, 'Новичок')")
    except:
        pass

# main navigation
# game command
@bot.message_handler(regexp='Играть')
def playGame(message):
    bot.send_message(message.chat.id, 'выберите кнопку', reply_markup=gameBoard)
# game commands
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
# main | CheckMyStats
@bot.message_handler(regexp='Мой профиль')
def checkMyStats(message):
    with sq.connect("users.db") as con:
        cur = con.cursor()
        name = cur.execute(f"SELECT name FROM users WHERE telegram_id = {message.chat.id}")
        name = cur.fetchone()[0]
        balance = cur.execute(f"SELECT balance FROM users WHERE telegram_id = {message.chat.id}")
        balance = cur.fetchone()[0]
        rank = cur.execute(f"SELECT rank FROM users WHERE telegram_id = {message.chat.id}")
        rank = cur.fetchone()[0]
    bot.send_message(message.chat.id, f'Профиль:\n\nИмя: {name}\nБаланс: {balance}\nСкилл: {rank}')

bot.infinity_polling(True)