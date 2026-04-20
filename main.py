import asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import os

# Берём токен из переменной окружения
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Проверка (чтобы сразу видеть ошибку в логах)
if not TOKEN:
    raise ValueError("❌ TELEGRAM_TOKEN не найден! Добавь его в переменные окружения")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🤖 Cheymi AI\n\n"
        "Выбери:\n"
        "1 - Реши пример\n"
        "2 - Время и дата\n"
        "3 - История"
    )

# Основной обработчик
@dp.message()
async def handler(message: Message):
    text = message.text

    if text == "1":
        await message.answer("✏️ Напиши пример (например: 5 + 5)")

    elif any(op in text for op in ["+", "-", "*", "/"]):
        try:
            result = eval(text)
            await message.answer(f"✅ Ответ: {result}")
        except:
            await message.answer("❌ Ошибка в выражении")

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

    elif text.lower() in ["первая мировая", "1 мировая"]:
        await message.answer("Первая мировая война (1914–1918)")

    elif text.lower() in ["вторая мировая", "2 мировая"]:
        await message.answer("Вторая мировая война (1939–1945)")

    else:
        await message.answer("❓ Не понял команду")

# запуск
async def main():
    print("✅ BOT STARTED")  # чтобы видеть в логах
    await dp.start_polling(bot)

if name == "__main__":
    asyncio.run(main())
