from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup,InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Расписание')],
                                     [KeyboardButton(text='Задолжности')],
                                     [KeyboardButton(text='Новости'),
                                      KeyboardButton(text='Обновления')]],
                                      resize_keyboard=True,
                                      input_field_placeholder='Выберите пункт меню...')


select = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сегодня',callback_data='today')],
    [InlineKeyboardButton(text='Завтра',callback_data='tomorrow')],
    [InlineKeyboardButton(text='На 3 дня',callback_data='ThreeDay'),
    InlineKeyboardButton(text='На неделю',callback_data='Week')],])
