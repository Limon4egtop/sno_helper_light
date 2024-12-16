from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_menu_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Журналы для публикации")
    kb.button(text="Гранты")
    kb.button(text="Афиша мероприятий")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)