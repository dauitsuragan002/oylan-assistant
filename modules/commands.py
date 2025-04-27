from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import *
from modules.functions import *
from modules.bot import *

# Command /start
async def start_handler(message: types.Message):
    try:
        if message.chat.type == 'private':
            builder = InlineKeyboardBuilder()
            lang = get_user_lang(message.from_user.id)
            wlc_msg = HANDLER_MESSAGES['start_handler'][lang].format(assistant_name=assistant_name, description=description)
            if ASSISTANT_ID:
                builder.row(InlineKeyboardButton(text=MESSAGES['open_menu_button'][lang], callback_data='menu'))
                await message.answer(text=wlc_msg,
                    reply_markup=builder.as_markup(),
                    parse_mode='Markdown')
            else:
                await message.reply("Қате: ассистент табылмады және жасалмады.")
    except Exception as e:
        print("Error in start_handler:", e)

# Command /info
async def info_handler(message: types.Message):
    if message.chat.type == 'private':
        lang = get_user_lang(message.from_user.id)
        info_text = HANDLER_MESSAGES['info_handler'][lang].format(assistant_name=assistant_name, model=model)
        await message.answer(info_text)
    else:
        print("Not PRIVATE CHAT:", message.chat.type)

# Command /help
async def help_handler(message: types.Message):
    if message.chat.type == 'private':
        lang = get_user_lang(message.from_user.id)
        help_text = HANDLER_MESSAGES['help_handler'][lang]
        await message.answer(help_text)
    else:
        print("Not a private chat")

# Command /more
async def more_handler(message: types.Message):
    if message.chat.type == 'private':
        builder = InlineKeyboardBuilder()
        lang = get_user_lang(message.from_user.id)
        builder.row(InlineKeyboardButton(text=MESSAGES['back_button'][lang], callback_data='cmd'))
        more_text = HANDLER_MESSAGES['more_handler'][lang]
        await message.answer(more_text, reply_markup=builder.as_markup())

# Command /lang
async def lang_handler(message: types.Message):
    try:
        user_id = message.from_user.id
        
        if message.chat.type == 'private':
            
            builder = InlineKeyboardBuilder()
            check_mark = "✅"
            lang = get_user_lang(user_id)
            text = HANDLER_MESSAGES['lang_handler'][lang]

            change_user_languages = config.user_languages.get(user_id, ('kaz', 'Қазақ тілі'))

            if change_user_languages:
                language_code, user_language = change_user_languages
            
            builder.row(InlineKeyboardButton(text=f"Қазақ тілі {check_mark if language_code == 'kaz' else ''}",callback_data="kaz"),)
            builder.row(InlineKeyboardButton(text=f"Русский {check_mark if language_code == 'rus' else ''}", callback_data="rus"),)
            builder.row(InlineKeyboardButton(text=f"English {check_mark if language_code == 'eng' else ''}", callback_data="eng"))
            builder.row(InlineKeyboardButton(text=f"Türkçe {check_mark if language_code == 'tur' else ''}", callback_data="tur"))
            builder.row(InlineKeyboardButton(text=MESSAGES['back_button'][language_code], callback_data='menu'),)
            config.first_time_users[user_id] = True  
            await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=builder.as_markup())
          
    except Exception as e:
        print("Problem in lang_handler:", e)

def get_keyboard_markup_lang(selected_language: str) -> InlineKeyboardMarkup:
    check_mark = "✅"

    if selected_language:
        language_code, user_language = selected_language
    else:
        language_code = 'kaz'
        user_language = 'Қазақ тілі'

    buttons = [
        InlineKeyboardButton(text="Қазақ тілі", callback_data="kaz"),
        InlineKeyboardButton(text="Русский", callback_data="rus"),
        InlineKeyboardButton(text="English", callback_data="eng"),
        InlineKeyboardButton(text="Türkçe", callback_data="tur"),
        InlineKeyboardButton(text=MESSAGES['back_button'][language_code], callback_data='menu')
    ]
    
    for button in buttons:
        if button.callback_data == language_code:
            button.text = f"{user_language} {check_mark}"
    keyboard = InlineKeyboardMarkup(inline_keyboard=[buttons[i:i + 1] for i in range(0, len(buttons), 1)])
    return keyboard