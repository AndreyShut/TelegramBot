
from aiogram import F,Router
from aiogram.types import Message,CallbackQuery
from aiogram.filters import CommandStart,Command
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()

class Register(StatesGroup):
    login = State()
    password = State()

@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer('Hello!',reply_markup=kb.main)


@router.message(Command('help'))
async def cmd_help(message:Message):
    await message.answer('Help')

@router.message(F.text == "Расписание")
async def select(message:Message):
    await message.answer('Выберите Расписание',reply_markup=kb.select)

@router.callback_query(F.data == "today")
async def today(callback:CallbackQuery):
    await callback.message.answer('Вы выбрали расписание на сегодня')

@router.message(Command('register'))
async def register(message:Message,state:FSMContext):
    await state.set_state(Register.login)
    await message.answer('Введите ваш логин')

@router.message(Register.login)
async def register_login(message:Message, state:FSMContext):
    await state.update_data(login=message.text)
    await state.set_state(Register.password)
    await message.answer("Введите ваш пароль")

@router.message(Register.password)
async def register_password(message:Message, state:FSMContext):
    await state.update_data(password=message.text)
    await state.set_state(Register.password)
    data = await state.get_data()
    await message.answer(f'Ваш логин: {data["login"]}\nВаш пароль: {data["password"]}')
    await state.clear()
