import logging

from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import *  # Import all configurations
from modules.commands import *  # Import all commands
from modules.functions import *  # Import all functions

# Callback handler for specific commands
@dp.callback_query(lambda query: query.data in ["info_cmd", "help_cmd", "more_cmd"])
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    data = callback_query.data
    message = callback_query.message
    builder = InlineKeyboardBuilder()
    lang = get_user_lang(user_id)
    text = ERROR_MSG['201'][lang]
    builder.row(InlineKeyboardButton(text=MESSAGES['back_button'][lang], callback_data='cmd'))
    if data == "help_cmd":
        text = HANDLER_MESSAGES['help_handler'][lang]
    elif data == "info_cmd":
        text = HANDLER_MESSAGES['info_handler'][lang].format(assistant_name=assistant_name, model=model)
    elif data == "more_cmd":
        text = HANDLER_MESSAGES['more_handler'][lang]
    await bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=text, reply_markup=builder.as_markup())

# Callback handler for menu-related commands
@dp.callback_query(lambda query: query.data in ["menu", "lang_cmd", "close_menu", 'cmd'])
async def process_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    data = callback_query.data
    builder = InlineKeyboardBuilder()
    lang = get_user_lang(user_id)
    
    message = callback_query.message
    if data == "menu":
        buttons = [
            [InlineKeyboardButton(text=MESSAGES['cmd_button'][lang], callback_data='cmd')],
            [InlineKeyboardButton(text=MESSAGES['close_menu_button'][lang], callback_data='close_menu')]
        ]
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        text = MESSAGES['process_callback_1'][lang].format(model=model)
        await bot.edit_message_text(
            chat_id=callback_query.message.chat.id, 
            message_id=callback_query.message.message_id,  
            text=text,
            reply_markup=keyboard,
            parse_mode='Markdown')
    elif data == "close_menu":
        builder.row(InlineKeyboardButton(text=MESSAGES['open_menu_button'][lang], callback_data='menu'))
        text = HANDLER_MESSAGES['start_handler'][lang].format(assistant_name=assistant_name, description=description)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text=text, reply_markup=builder.as_markup())
    elif data == "lang_cmd":
        text = HANDLER_MESSAGES['lang_handler'][lang]
        change_user_languages = config.user_languages.get(user_id, ('kaz', 'Қазақ тілі'))
        # print("change_user_languages", change_user_languages)
        
        language_code, user_language = change_user_languages
        user_id = message.from_user.id
        check_mark = "✅"
        # Батырмаларды әрқашан таңдалған тілге сай құру
        builder.row(InlineKeyboardButton(text=f"Қазақ тілі {check_mark if language_code == 'kaz' else ''}", callback_data="kaz"))
        builder.row(InlineKeyboardButton(text=f"Русский {check_mark if language_code == 'rus' else ''}", callback_data="rus"))
        builder.row(InlineKeyboardButton(text=f"English {check_mark if language_code == 'eng' else ''}", callback_data="eng"))
        builder.row(InlineKeyboardButton(text=f"Türkçe {check_mark if language_code == 'tur' else ''}", callback_data="tur"))
        builder.row(InlineKeyboardButton(text=MESSAGES['back_button'][lang], callback_data='menu'))
        config.first_time_users[user_id] = True
        keyboard = get_keyboard_markup_lang(config.user_languages.get(user_id, ""))
        await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text=text, reply_markup=builder.as_markup())
        
    elif data == "cmd":
        text = MESSAGES['cmd_list'][lang]
        builder.row(InlineKeyboardButton(text=MESSAGES['lang_button'][lang], callback_data='lang_cmd'))
        builder.row(InlineKeyboardButton(text=MESSAGES['info_button'][lang], callback_data="info_cmd"),
                    InlineKeyboardButton(text=MESSAGES['more_button'][lang], callback_data="more_cmd"),)
        builder.row(
            InlineKeyboardButton(text=MESSAGES['help_button'][lang], callback_data="help_cmd"),)
        builder.row(InlineKeyboardButton(text=MESSAGES['open_menu_button'][lang], callback_data='menu'))
        await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text=text, reply_markup=builder.as_markup())

# Callback handler for language selection
@dp.callback_query(lambda query: query.data in ["kaz", "rus", "eng", "tur"])
async def handle_language_callback(callback_query: types.CallbackQuery):
    callback_data = callback_query.data
    check_mark = "✅"
    language_code = "kaz"
    user_language = "Қазақ тілі"

    if callback_data == "kaz":
        await callback_query.answer(f"{check_mark} Қазақ тілі орнатылды.")
        language_code = "kaz"
        user_language = "Қазақ тілі"
    elif callback_data == "rus":
        await callback_query.answer(f"{check_mark} Язык установлен на русский.")
        language_code = "rus"
        user_language = "Русский"
    elif callback_data == "eng":
        await callback_query.answer(f"{check_mark} The language has been set to English.")
        language_code = "eng"
        user_language = "English"
    elif callback_data == "tur":
        await callback_query.answer(f"{check_mark} Türkçe diline geçildi")
        language_code = "tur"
        user_language = "Türkçe"

    user_id = callback_query.from_user.id
    save_language = (language_code, user_language)
    config.user_languages[user_id] = save_language
    config.first_time_users[user_id] = True

    # Жаңартылған тілді бірден қолдану
    lang = language_code
    keyboard = get_keyboard_markup_lang(config.user_languages.get(user_id, ""))
    text = HANDLER_MESSAGES['lang_handler'][lang]
    await callback_query.message.edit_text(
        text=text,
        reply_markup=keyboard,
    )