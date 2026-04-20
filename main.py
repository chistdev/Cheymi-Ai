import asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
import os

# Загружаем переменные из .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🤖 Cheymi AI v1.0\n\n"
        "Выбери:\n"
        "1 - Реши пример\n"
        "2 - Время и дата\n"
        "3 - История"
    )

# Обработка сообщений
@dp.message()
async def handle_message(message: types.Message):
    text = message.text

    if text == "1":
        await message.answer("✏️ Напиши пример (например: 5 + 5)")

    elif any(op in text for op in ["+", "-", "*", "/"]):
        try:
            result = eval(text)
            await message.answer(f"✅ Ответ: {result}")
        except Exception as e:
            await message.answer(f"❌ Ошибка: {e}")

    elif text == "2":
        now = datetime.now()
        await message.answer(
            f"🕒 Сейчас: {now.strftime('%d.%m.%Y %H:%M:%S')}"
        )

    elif text == "3":
        await message.answer(
            "📚 История:\n"
            "1 - Первая мировая\n"
            "2 - Вторая мировая"
        )

    elif text.lower() in ["1 мировая", "первая мировая"]:
        await message.answer("Первая мировая война (1914–1918)")

    elif text.lower() in ["2 мировая", "вторая мировая"]:
        await message.answer("Вторая мировая война (1939–1945)")

    else:
        await message.answer("❓ Не понял команду")

# Запуск
async def main():
    await dp.start_polling(bot)

if name == "__main__":
    asyncio.run(main())
