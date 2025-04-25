from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup,InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='1')],
                                     [KeyboardButton(text='2')],
                                     [KeyboardButton(text='3.1'),
                                      KeyboardButton(text='3.2')]],
                                      resize_keyboard=True,
                                      input_field_placeholder='Выберите пункт меню...')


select = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='1.1')],
                                               [InlineKeyboardButton(text='2.1')],
                                               [InlineKeyboardButton(text='3.1.1'),
                                               InlineKeyboardButton(text='3.1.2')],])
