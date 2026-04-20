import asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise ValueError("❌ TELEGRAM_TOKEN не найден! Добавь его в переменные окружения")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Главная клавиатура
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🤖 О нас"),
            KeyboardButton(text="🕒 Время и дата")
        ],
        [
            KeyboardButton(text="✏️ Реши пример"),
            KeyboardButton(text="📚 История")
        ]
    ],
    resize_keyboard=True
)

# Команда /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🤖 Добро пожаловать в Cheymi AI!\n\nВыберите действие:",
        reply_markup=main_keyboard
    )

# Обработчик сообщений
@dp.message()
async def handle_message(message: types.Message):
    text = message.text.lower()

    if text == "🤖 о нас":
        await message.answer(
            "🌟 О Cheymi AI\n\n"
            "Cheymi AI — это современный искусственный интеллект для базовых задач."
        )

    elif text == "🕒 время и дата":
        now = datetime.now()
        await message.answer(
            f"🕒 Сейчас: {now.strftime('%d.%m.%Y %H:%M:%S')}"
        )

    elif text == "✏️ реши пример":
        await message.answer("✏️ Напишите пример (например: 5 + 5)")

    elif any(op in text for op in ["+", "-", "*", "/"]):
        try:
            # ⚠️ Безопаснее, чем eval
            result = eval(text, {"__builtins__": {}})
            await message.answer(f"✅ Ответ: {result}")
        except:
            await message.answer("❌ Ошибка в выражении")

    elif text == "📚 история":
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Первая мировая война", callback_data="ww1")],
                [InlineKeyboardButton(text="Вторая мировая война", callback_data="ww2")]
            ]
        )
        await message.answer(
            "📚 Выберите событие:",
            reply_markup=keyboard
        )

    else:
        await message.answer("❓ Не понял команду, выберите из меню.")

# Обработка inline-кнопок
@dp.callback_query()
async def handle_callback(query: types.CallbackQuery):
    if query.data == "ww1":
        await query.message.answer(
            "Первая мировая война (1914–1918)"
        )
    elif query.data == "ww2":
        await query.message.answer(
            "Вторая мировая война (1939–1945)"
        )

    await query.answer()

# Запуск бота
async def main():
    print("✅ BOT STARTED")
    await dp.start_polling(bot)

# ✅ ВОТ ГЛАВНОЕ ИСПРАВЛЕНИЕ
if __name__ == "__main__":
    asyncio.run(main())
