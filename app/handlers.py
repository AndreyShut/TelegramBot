
from aiogram import F,Router
from aiogram.types import Message
from aiogram.filters import CommandStart,Command
import app.keyboards as kb
router = Router()

@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer('Hello!',reply_markup=kb.main)


@router.message(Command('help'))
async def cmd_help(message:Message):
    await message.answer('Help')


