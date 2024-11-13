import asyncio

from aiogram.methods import DeleteWebhook
from aiogram.types import BotCommand
from aiogram import Bot, Dispatcher

from bot.handlers.handlers import router

import config as conf


async def main() -> None:

    bot = Bot(token=conf.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    bot_commands = [
                BotCommand(command="/start", description="Get start")]

    await bot.set_my_commands(bot_commands)
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        print("on")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("off")