from main import bot,dp
from aiogram.types import Message
from config import my_id
async def send_to_admin(dp):
    await bot.send_message(chat_id=my_id,text="Salem!"
                                              "\nQaidan bolasyn?")
@dp.message_handler()
async def echo(message: Message):
    if message.text == 'merke':
        text = f"Salem, sen tochno  {message.text}  osyny jazgyn keldi ma?"
        await bot.send_message(chat_id=message.from_user.id, text=text)


    if message.text=="ia":
        text = f"Ooo tema, tema"
        await bot.send_message(chat_id=message.from_user.id, text=text)
    elif message.text == "jok":
        madi = f"Onda qaittan jaza alasyn,biraq durystap jaz"
        await bot.send_message(chat_id=message.from_user.id, text=madi)

