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
    cur.execute("""CREATE TABLE IF NOT EXISTS user_rank (
        telegram_id INTEGER PRIMARY KEY,
        wins INTEGER
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
gameBack = types.KeyboardButton(text='В меню')
gameBoard.add(gameStone, gameScissors, gamePaper, gameRandom, gameBack)

myProfileBoard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
myProfileName = types.KeyboardButton(text='Имя')
myProfileBalance = types.KeyboardButton(text='Баланс')
myProfileSkill = types.KeyboardButton(text='Скилл')
myProfileBack = types.KeyboardButton(text='В меню')
myProfileBoard.add(myProfileName, myProfileBalance, myProfileSkill, myProfileBack)

# start command
@bot.message_handler(commands=['start'])
def start(message):
    try:
        with sq.connect("users.db") as con:
            cur = con.cursor()
            cur.execute(f"INSERT INTO users(telegram_id, name, balance, rank) VALUES({message.chat.id}, 'Не указано', 5000, 'Новичок')")
            cur.execute(f"INSERT INTO user_rank(telegram_id, wins) VALUES({message.chat.id}, 0)")
            bot.send_message(message.chat.id, 'Запуск...', reply_markup=mainBoard)
    except:
        with sq.connect("users.db") as con:
            cur = con.cursor()
            name = cur.execute(f"SELECT name FROM users WHERE telegram_id = {message.chat.id}")
            name = cur.fetchone()[0]
            balance = cur.execute(f"SELECT balance FROM users WHERE telegram_id = {message.chat.id}")
            balance = cur.fetchone()[0]
            rank = cur.execute(f"SELECT rank FROM users WHERE telegram_id = {message.chat.id}")
            rank = cur.fetchone()[0]
        bot.send_message(message.chat.id, 'Привет, ты уже зарегестрирован.')
        bot.send_message(message.chat.id, f'Профиль:\n\nИмя: {name}\nБаланс: {balance}\nСкилл: {rank}', reply_markup=mainBoard)
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
        with sq.connect("users.db") as con:
            cur = con.cursor()
            cur.execute(f"UPDATE users SET balance = balance - 500 WHERE telegram_id = {message.chat.id}")
        bot.send_message(message.chat.id, '-')
    elif botChoice < playerChoice:
        with sq.connect("users.db") as con:
            cur = con.cursor()
            cur.execute(f"UPDATE users SET balance = balance + 500 WHERE telegram_id = {message.chat.id}")
            cur.execute(f"UPDATE user_rank SET wins = wins + 1 WHERE telegram_id = {message.chat.id}")
        bot.send_message(message.chat.id, '+')
@bot.message_handler(regexp='Ножницы')
def gamePlayScissors(message):
    botChoice = random.choice(gameVariants)
    playerChoice = random.choice(gameVariants)
    if botChoice == playerChoice:
        bot.send_message(message.chat.id, '=')
    elif botChoice > playerChoice:
        with sq.connect("users.db") as con:
            cur = con.cursor()
            cur.execute(f"UPDATE users SET balance = balance - 500 WHERE telegram_id = {message.chat.id}")
        bot.send_message(message.chat.id, '-')
    elif botChoice < playerChoice:
        with sq.connect("users.db") as con:
            cur = con.cursor()
            cur.execute(f"UPDATE users SET balance = balance + 500 WHERE telegram_id = {message.chat.id}")
            cur.execute(f"UPDATE user_rank SET wins = wins + 1 WHERE telegram_id = {message.chat.id}")
        bot.send_message(message.chat.id, '+')
@bot.message_handler(regexp='Бумага')
def gamePlayPaper(message):
    botChoice = random.choice(gameVariants)
    playerChoice = random.choice(gameVariants)
    if botChoice == playerChoice:
        bot.send_message(message.chat.id, '=')
    elif botChoice > playerChoice:
        with sq.connect("users.db") as con:
            cur = con.cursor()
            cur.execute(f"UPDATE users SET balance = balance - 500 WHERE telegram_id = {message.chat.id}")
        bot.send_message(message.chat.id, '-')
    elif botChoice < playerChoice:
        with sq.connect("users.db") as con:
            cur = con.cursor()
            cur.execute(f"UPDATE users SET balance = balance + 500 WHERE telegram_id = {message.chat.id}")
            cur.execute(f"UPDATE user_rank SET wins = wins + 1 WHERE telegram_id = {message.chat.id}")
        bot.send_message(message.chat.id, '+')
@bot.message_handler(regexp='Рандом')
def gamePlayRandom(message):
    botChoice = random.choice(gameVariants)
    playerChoice = random.choice(gameVariants)
    if botChoice == playerChoice:
        bot.send_message(message.chat.id, '=')
    elif botChoice > playerChoice:
        with sq.connect("users.db") as con:
            cur = con.cursor()
            cur.execute(f"UPDATE users SET balance = balance - 500 WHERE telegram_id = {message.chat.id}")
        bot.send_message(message.chat.id, '-')
    elif botChoice < playerChoice:
        with sq.connect("users.db") as con:
            cur = con.cursor()
            cur.execute(f"UPDATE users SET balance = balance + 500 WHERE telegram_id = {message.chat.id}")
            cur.execute(f"UPDATE user_rank SET wins = wins + 1 WHERE telegram_id = {message.chat.id}")
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
    bot.send_message(message.chat.id, f'Профиль:\n\nИмя: {name}\nБаланс: {balance}\nСкилл: {rank}', reply_markup=myProfileBoard)

@bot.message_handler(regexp='В меню')
def back(message):
    bot.send_message(message.chat.id, 'Мы в меню', reply_markup=mainBoard)

bot.infinity_polling(True)