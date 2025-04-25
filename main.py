import asyncio
from aiogram import Bot,Dispatcher
from app.handlers import router

async def main():
    bot = Bot(token='7708914926:AAEepSv-HFqOXJ-qX4auuRpP2cCM4Yrkmyg')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    print ('Бот включен')
    try:
        asyncio.run(main())
    except KeyboardInterrupt:   
        print('Бот выключен')