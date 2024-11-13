import logging
import config as conf

from aiogram import F, Router, types

from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
from bot.keyboards import keyboards as kb


logging.basicConfig(level=logging.INFO)
router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("текст текст текст", reply_markup=kb.info_about_bot)


@router.callback_query(F.data == "info_for_admins")
async def students(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text("инфа для админов", reply_markup=kb.admin_panel)



@router.callback_query(F.data == "ученики")
async def students(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text("инфа об учениках", reply_markup=kb.back_to_admin_panel)


@router.callback_query(F.data == "успеваемость")
async def progress(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text("инфа об успеваемости", reply_markup=kb.back_to_admin_panel)


@router.callback_query(F.data == "разработчики")
async def developers(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text("инфа о разработчиках", reply_markup=kb.back_to_admin_panel)


@router.callback_query(F.data == "темы")
async def terms(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text("инфа о темах", reply_markup=kb.back_to_admin_panel)


@router.callback_query(F.data == "back_to_main")
async def back_to_main(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text("текст текст текст", reply_markup=kb.info_about_bot)


@router.callback_query(F.data == "back_to_admin_panel")
async def back_to_main(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.edit_text("текст текст текст", reply_markup=kb.admin_panel)