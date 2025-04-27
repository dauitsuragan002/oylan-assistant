# Мультитілдік хабарламалар (локализация)
HANDLER_MESSAGES = {
    "start_handler": {
        "kaz": "Сәлем! Мен {assistant_name} ботымын. {description}",
        "rus": "Привет! Я бот {assistant_name}. {description}",
        "eng": "Hello! I am {assistant_name} bot. {description}",
        "tur": "Merhaba! Ben {assistant_name} botuyum. {description}"
    },
    "info_handler": {
        "kaz": "Телеграм бот: {assistant_name}, {model} API және Soyle API қолданылып жасалған.",
        "rus": "Телеграм-бот: {assistant_name} создан с использованием {model} API и Soyle API.",
        "eng": "Telegram bot: {assistant_name} is built using {model} API and Soyle API.",
        "tur": "Telegram botu: {assistant_name}, {model} API ve Soyle API kullanılarak oluşturulmuştur."
    },
    "help_handler": {
        "kaz": "\n/lang - Жүйе тілін таңдау. \n/info - Бот туралы ақпарат. \n/more - Менің басқада бот достарым.\n",
        "rus": "\n/lang - Выбрать язык системы. \n/info - Информация о боте. \n/more - Другие мои боты.\n",
        "eng": "\n/lang - Choose system language. \n/info - About the bot. \n/more - My other bot friends.\n",
        "tur": "\n/lang - Sistem dilini seç. \n/info - Bot hakkında bilgi. \n/more - Diğer bot arkadaşlarım.\n"
    },
    "more_handler": {
        "kaz": "Таныс болыңыз!\n\n 1.Ағылшын тілін ЖИ мен бірге үйрену - @englishkaz_bot\n\n2.Мәтінді қазақша тегін сөйлету - @qaztts_bot",
        "rus": "Познакомьтесь!\n\n 1.Учите английский с ИИ - @englishkaz_bot\n\n2.Озвучьте текст на казахском бесплатно - @qaztts_bot",
        "eng": "Meet our friends!\n\n 1.Learn English with AI - @englishkaz_bot\n\n2.Text-to-speech in Kazakh for free - @qaztts_bot",
        "tur": "Tanışın!\n\n 1.Yapay zeka ile İngilizce öğrenin - @englishkaz_bot\n\n2.Kazakça metni ücretsiz seslendirin - @qaztts_bot"
    },
    "lang_handler": {
        "kaz": "Бот интерфейсінде қазақ тілі орнатылған 🇰🇿.\n\nЖүйе тілін ауыстыру үшін таңдаңыз. 👇",
        "rus": "Для смены системного языка выберите ниже. 👇",
        "eng": "To change the system language, choose below. 👇",
        "tur": "Sistem dilini değiştirmek için aşağıdan seçin. 👇"
    },
    
}

MESSAGES={
    "bot_response": {
        "kaz": "Сіз: {recognized_text}\n\n{assistant_name}: {bot_response}",
        "rus": "Вы: {recognized_text}\n\n{assistant_name}: {bot_response}",
        "eng": "You: {recognized_text}\n\n{assistant_name}: {bot_response}",
        "tur": "Siz: {recognized_text}\n\n{assistant_name}: {bot_response}"
    },
    "menu_text": {
        "kaz": "Төменде боттың мәзірі көрсетілген👇",
        "rus": "Ниже показано меню бота👇",
        "eng": "The bot menu is shown below👇",
        "tur": "Aşağıda bot menüsü gösterilmektedir👇"
    },
    "cmd_list": {     
        "kaz": "Ботта орналасқан командалар тізімі 👇",
        "rus": "Список команд, доступных в боте 👇",
        "eng": "List of commands available in the bot 👇",
        "tur": "Botta ayarlanmış komutlar tablosu 👇"
    },
    "cmd_button": {
        "kaz": "🧑‍💻 Командалар",
        "rus": "🧑‍💻 Команды",
        "eng": "🧑‍💻 Commands",
        "tur": "🧑‍💻 Komutlar"
    },
    "close_menu_button": {
        "kaz": "🔼 Мәзірді жабу",
        "rus": "🔼 Закрыть меню",
        "eng": "🔼 Close menu",
        "tur": "🔼 Menüyü kapat"
    },
    "open_menu_button": {
        "kaz": "🔽 Мәзір",
        "rus": "🔽 Меню",
        "eng": "🔽 Menu",
        "tur": "🔽 Menü"
    },
    "back_button": {
        "kaz": "« Артқа",
        "rus": "« Назад",
        "eng": "« Back",
        "tur": "« Geri"
    },
    "lang_button": {
        "kaz": "Жүйе тілі",
        "rus": "Язык системы",
        "eng": "System language",
        "tur": "Sistem dili"
    },
    "info_button": {
        "kaz": "ℹ️ Ақпарат",
        "rus": "ℹ️ Информация",
        "eng": "ℹ️ Info",
        "tur": "ℹ️ Bilgi"
    },
    "more_button": {
        "kaz": "Басқа",
        "rus": "Другие",
        "eng": "More",
        "tur": "Daha fazla"
    },
    "help_button": {
        "kaz": "➕ Көмек",
        "rus": "➕ Помощь",
        "eng": "➕ Help",
        "tur": "➕ Yardım"
    },
    "lang_button": {
        "kaz": "Жүйе тілі",
        "rus": "Язык системы",
        "eng": "System language",
        "tur": "Sistem dili"
    },
    "process_callback_1":{
        "kaz": "Сәлем! Мен {model} тілдік моделінің көмегімен жұмыс жасаймын.\n\nМаған орнатылған негізгі командалар осы белгі '/' арқылы немесе \"Меню\" батырмасы арқылы орындылады." + "\n\nТөменде боттың мәзірі көрсетілген👇",
        "rus": "Привет! Я работаю с языковой моделью {model}.\n\nОсновные команды, установленные для меня, доступны через этот значок '/' или через кнопку \"Меню\"." + "\n\nНиже показано меню бота👇",
        "eng": "Hello! I am working with the {model} language model.\n\nThe main commands installed for me are available through this icon '/' or through the \"Menu\" button." + "\n\nThe bot menu is shown below👇",
        "tur": "Merhaba! {model} dil modeli ile çalışıyorum.\n\nBenim için kurulu ana komutlar bu simge '/' veya \"Menü\" düğmesi aracılığıyla kullanılabilir." + "\n\nAşağıda bot menüsü gösterilmektedir👇",
        },
    "process_callback_2":{
        "kaz": 'Мен {model} тілдік моделінің көмегімен жұмыс жасаймын',
        "rus": 'Я работаю с языковой моделью {model}',
        "eng": 'I am working with the {model} language model',
        "tur": '{model} dil modeli ile çalışıyorum',
    },
}
    
ERROR_MSG = {
    "201": {
        "kaz":'Сәлем, бір қателік кетті( Қазір жөндеймін!',
        "rus":'Привет, произошла ошибка( Я сейчас исправлю!',
        "eng":'Hello, an error occurred( I will fix it now!',
        "tur":'Merhaba, bir hata oluştu( Şimdi düzelteceğim!',
    },
    "202": {
        "kaz":'Сәлем, мені кешіріңіз, мен жөндеймін!',
        "rus":'Привет, извините меня, я исправлюсь!',
        "eng":'Hello, forgive me, I will fix it!',
        "tur":'Merhaba, beni affet, düzelteceğim!'
    },
}