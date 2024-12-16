from aiogram import Router, F
from aiogram.enums import ChatAction, ParseMode
from aiogram.filters import Command
from aiogram.types import Message

from database.services.database_send_message_text import get_message_by_id
from keyboards import get_menu_kb
from database.services import database_users as db_service

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    try:
        message_1 = await get_message_by_id(1)  # Добавлен await
        message_2 = await get_message_by_id(2)  # Добавлен await
        hello_text = f"{message_1.text} <b>{message.from_user.first_name}</b>\n{message_2.text}"  # Формируем текст
    except Exception as e:
        # В случае ошибки сообщение fallback
        message_2 = await get_message_by_id(2)  # Добавлен await
        hello_text = f"Привет\n{message_2.text}"
    finally:
        # Отправляем сообщение
        await message.answer(
            text=hello_text,
            parse_mode=ParseMode.HTML,
            reply_markup=get_menu_kb(),
            disable_web_page_preview=True
        )
    if not await db_service.check_existing_user(message.from_user.id):
        try:
            await db_service.add_user(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)
        except Exception as e:
            await db_service.add_user(message.from_user.id)


@router.message(F.text.lower() == "меню")
async def menu(message: Message):
    await message.answer("Меню", reply_markup=get_menu_kb())


@router.message(F.text.lower() == "журналы для публикации")
async def journals_for_publication(message: Message):
    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    send_text = await get_message_by_id(3)
    await message.answer(send_text.text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


@router.message(F.text.lower() == "гранты")
async def grants(message: Message):
    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    send_text = await get_message_by_id(4)
    await message.answer(send_text.text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


@router.message(F.text.lower() == "афиша мероприятий")
async def events_schedule(message: Message):
    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    send_text = await get_message_by_id(5)
    await message.answer(send_text.text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


@router.message(Command("user_data"))
async def user_data(message: Message):
    await message.answer(text=str(message))