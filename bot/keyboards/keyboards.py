from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


admin_panel = InlineKeyboardMarkup(inline_keyboard=[
                            [InlineKeyboardButton(text="ученики", callback_data="ученики")],
                            [InlineKeyboardButton(text="успеваемость", callback_data="успеваемость")],
                            [InlineKeyboardButton(text="разработчики", callback_data="разработчики")],
                            [InlineKeyboardButton(text="темы", callback_data="темы")],
                            [InlineKeyboardButton(text="назад", callback_data="back_to_main")]])


info_about_bot = InlineKeyboardMarkup(inline_keyboard=[
                            [InlineKeyboardButton(text="что в боте(для админов)", callback_data="info_for_admins")]])


back_to_main = InlineKeyboardMarkup(inline_keyboard=[
                            [InlineKeyboardButton(text="На главную", callback_data="back_to_main")]])


back_to_admin_panel = InlineKeyboardMarkup(inline_keyboard=[
                            [InlineKeyboardButton(text="назад", callback_data="back_to_admin_panel")]])

