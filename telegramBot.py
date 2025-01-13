import asyncio
import logging
from aiogram import F, Bot, Dispatcher,types
from aiogram.filters import Command
from aiogram.types import Message,KeyboardButton,ReplyKeyboardMarkup,ContentType
import random 
import requests
import pyttsx3
import subprocess


logging.basicConfig(level=logging.INFO)
bot = Bot(token='7394920350:AAEFAEgxW4ZqQG9ShBZcjx33c7yjhubprN0')
dp=Dispatcher()

@dp.message(Command("start") )
async def cmd_name(message:Message):
    await message.answer("Hi, I am testing bot")

@dp.message(Command("info"))
async def cmd_name(message:Message):
    await message.reply("I have next command\n /start \n /info")
    
    
    
@dp.message(Command("name"))  
async def cmd_name(message:Message):
    args=message.text.split(maxsplit=1)
    if len(args)>1:
        await message.answer(f"Hi,<b>{args[1]}</b>",parse_mode="HTML")
    else:
        await message.answer("Please, enter your /name!")

@dp.message(Command("test"))
async def any_message(message:types.Message):
    await message.answer("Hello, <b>world</b>!",parse_mode="HTML")
    await message.answer("Hello,*world*\!",parse_mode="MarkdownV2")
        
@dp.message(Command("button"))   
async def cmd_start(message:Message):
    kb=[
        [types.KeyboardButton(text="First button")],
        [types.KeyboardButton(text="Second button")],
        [types.KeyboardButton(text="Third button")],
        [types.KeyboardButton(text="Fourt button")],
        [types.KeyboardButton(text="Fifth button")]
    ]
    keyboard=types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Choose button", reply_markup=keyboard)
    
    
@dp.message(lambda message: message.text=="First button")
async def first_btn(message:Message):
    await message.reply("You choose first button,My name is Bot")
    
@dp.message(lambda message: message.text=="Second button")
async def first_btn(message:Message):
    await message.reply("You choose second button, My favourite color is Blue")

@dp.message(lambda message: message.text=="Third button")
async def first_btn(message:Message):
    await message.reply("You choose third button, My  country is Russian")
    
@dp.message(lambda message: message.text=="Fourt button")
async def first_btn(message:Message):
    await message.reply("You choose fourth button, Jellyfish have existed on Earth for over 500 million years, making them older than dinosaurs!")

@dp.message (lambda message:message.text=="Fifth button")
async def first_btn(message:Message):
    await message.reply("You choose fifth button,Octopuses have three hearts, and two of them stop beating when they swim!")
    

@dp.message(Command("special_buttons"))
async def cmd_special_buttons(message:types.Message):
    kb=[
        [types.KeyboardButton(text="Choose contact",request_contact=True)],
        [types.KeyboardButton(text="Choose victorina",request_poll=types.KeyboardButtonPollType(type='quiz'))],
    ]
    keyboard=types.ReplyKeyboardMarkup(keyboard=kb)
    await message.reply("Choose action ", reply_markup=keyboard)

@dp.message(lambda message: message.text=="Choose victorina")
async def send_quiz(message:types.Message):
    question="What is the biggest ocean in the world?"
    options=["Atlantic"," Indian","Pacific ocean","Arctic" ]
    correct_option_id=2
    
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=options,
        type="quiz",
        correct_option_id=correct_option_id,
        is_anonymous=False
    )
@dp.message(F.content_type=="animation")
async def echo_gif(message:Message):
    await message.reply_animation(message.animation.file_id)

btn_keyboard=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Horror")],
        [KeyboardButton(text="Action")],
        [KeyboardButton(text="Comedy")],
        [KeyboardButton(text="Fantasy")],
        [KeyboardButton(text="Detective")],
        [KeyboardButton(text="Anime")],
        [KeyboardButton(text="Crime")],
        [KeyboardButton(text="Cartoon")],
        [KeyboardButton(text="Game")]
    ],
    resize_keyboard=True
)
horror=["https://www.kinopoisk.ru/series/589167/","https://www.kinopoisk.ru/series/1385287/","https://www.kinopoisk.ru/series/230571/","https://www.kinopoisk.ru/series/1202991/"]
action=["https://www.kinopoisk.ru/series/480160/","https://www.kinopoisk.ru/film/440616/","https://www.kinopoisk.ru/film/5024227/"]
fantasy=["https://www.kinopoisk.ru/series/983091/","https://www.kinopoisk.ru/film/462193/","https://www.kinopoisk.ru/film/670/"]
comedy=["https://www.kinopoisk.ru/series/740696/","https://www.kinopoisk.ru/film/6412/","https://www.kinopoisk.ru/series/565214/"]
detective=["https://www.kinopoisk.ru/film/681831/sr/1/","https://www.kinopoisk.ru/film/968767/sr/1/","https://www.kinopoisk.ru/film/4549968/sr/1/"]
anime=["https://www.kinopoisk.ru/film/5416975/sr/1/","https://www.kinopoisk.ru/series/425875/","https://www.kinopoisk.ru/series/4789626/"]
crime=["https://www.kinopoisk.ru/film/435/","https://www.kinopoisk.ru/series/5581178/","https://www.kinopoisk.ru/series/404900/"]
cartoon=["https://www.kinopoisk.ru/film/961694/","https://www.kinopoisk.ru/film/4791604/","https://www.kinopoisk.ru/film/989469/"]
game=["https://www.kinopoisk.ru/film/5451179/","https://www.kinopoisk.ru/series/525989/","https://www.kinopoisk.ru/film/734471/"]
@dp.message(Command("films"))
async def cmd_name(message:Message):
    await message.answer("Choose genre", reply_markup=btn_keyboard)
    
@dp.message(lambda message: message.text=="Horror")
async def show_horror(message:Message):
    await message.reply("This is good Horror "+random.choice(horror))


@dp.message(lambda message: message.text=="Action")
async def show_action(message:Message):
    await message.reply("This is good Action " + random.choice(action))
    
@dp.message(lambda message: message.text=="Fantasy")
async def show_fantasy(message:Message):
    await message.reply("This is good Fantasy "+random.choice(fantasy))

@dp.message(lambda message: message.text=="Comedy")
async def show_comedy(message:Message):
    await message.reply("This is good Comedy "+random.choice(comedy))
    
@dp.message(lambda message:message.text=="Detective")
async def show_detective(message:Message):
    await message.reply("This is good Detective "+random.choice(detective))

@dp.message(lambda message:message.text=="Anime")
async def show_anime(message:Message):
    await message.reply("This is good Anime "+random.choice(anime))

@dp.message(lambda message:message.text=="Crime")
async def show_anime(message:Message):
    await message.reply("This is good Crime "+random.choice(crime))
    
@dp.message(lambda message:message.text=="Cartoon")
async def show_anime(message:Message):
    await message.reply("This is good Cartoon "+random.choice(cartoon))
    
@dp.message(lambda message:message.text=="Game")
async def show_anime(message:Message):
    await message.reply("This is good Game "+random.choice(game))

@dp.message(Command("game"))
async def launch_game(message:Message):
    def run_game():
        try:
            subprocess.Popen(r"c:\Program Files\Google\Chrome\Application\chrome.exe") 
            return "Start game"
        except FileNotFoundError:
            return " No way for game"
        
    loop=asyncio.get_event_loop()
    response = await loop.run_in_executor(None, run_game)
    await message.reply(response)
    
@dp.message(Command("weather"))
async def start_command(message:Message):  
    await message.answer("Choose city for weather") 

@dp.message(F.text)
async def get_weather(message:types.Message) :
    city=message.text
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347"
        weather_data=requests.get(url).json()
        
        temperature=weather_data["main"]["temp"]
        temperature_feels=weather_data["main"]["feels_like"]
        wind_speed=weather_data["wind"]["speed"]
        cloud_cover=weather_data["weather"][0]["description"]
        humidity=weather_data["main"]["humidity"]
        
        await message.answer(f"Температура воздуха: {temperature}\n"
                             f"Ощущается как:{temperature_feels}\n"
                             f"Ветер:{wind_speed} м/с \n"
                             f"Облачность: {cloud_cover} \n"
                             f"Влажность: {humidity}%")
        pass
    except KeyError:
        await message.answer("Не удалось определить город")
        
engine=pyttsx3.init()

engine.setProperty("rate",150)
engine.setProperty("volume",0.5)

engine.say("Добро пожаловать Аружан")

engine.runAndWait()
   
async def main():
    await dp.start_polling(bot)
if __name__=="__main__":
    asyncio.run(main())
