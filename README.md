# Personal Assistant Bot Framework with Oylan 2 API

This is a flexible framework for creating personalized Telegram bots that integrate with the **Oylan 2 API**. The framework allows you to create your own AI assistant with natural language capabilities in multiple languages. It also leverages **Soyle API** for advanced voice processing features.

## Features

- 🤖 **Custom Assistant Creation:** Create your own AI assistant using Oylan 2 API with customizable name, description, and behavior
- 🗣️ **Advanced Voice Processing:**
  - Voice Recognition with automatic language detection
  - Text-to-Speech synthesis
  - Transcription services
- 🌐 **Multilingual Support:** 
  - Supports Kazakh, Russian, English, and Turkish
  - Automatic language detection for voice inputs
  - Language-specific responses
- 📝 **Context Management:**
  - Add and manage context files
  - Support for multiple file types (docx, images)
  - Context-aware responses
- ⚙️ **Easy Configuration:** 
  - Environment-based setup
  - Modular architecture
  - Customizable settings

## Quick Start

### Prerequisites

- Python 3.9+
- Required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Setup

1. Create a `.env` file with your API keys:

```env
TOKEN=<Your Telegram Bot Token>
API_RESPONSE=<Your Oylan API Key>
API_SOYLE=<Your Soyle API Key>
API_MAIN_SOYLE=<Your Main Soyle API Key, get it in the browser 'dev tools' > https://mangisoz.nu.edu.kz/soyle> 
```
![How to get main Soyle API Key](temp/get_token.jpg)

2. Configure your assistant in `config.py`:
```python
ASSISTANT_ID = 'your_assistant_id'
```

### Creating Your Assistant

You can create and configure your assistant using the provided modules in `api_issai/assistant/`:

1. Create a new assistant using `create.py`:
```bash
py -m api_issai.assistant.create

```
2. Update assistant settings using `update.py`:
```bash
py -m api_issai.assistant.update

```
3. Get assistant information using `get_info.py`:
```bash
py -m api_issai.assistant.get_info
```

4. Add context files:
```bash
pyt -m api_issai.contexts.add_context
```

These modules allow you to fully customize your assistant's behavior, including:
- Name, id and description
- System instructions
- Context data

## Advanced Features

### Voice Processing
- Automatic language detection for voice messages
- High-quality text-to-speech synthesis
- Accurate transcription services

### Context Management
- Add multiple context files
- View and manage existing contexts
- Delete outdated contexts

### Language Support
- Automatic language detection
- Multilingual interface
- Language-specific responses

## To-Do List

- [x] Initialize Telegram bot with Aiogram
- [x] Set up environment variables for API keys
- [x] Integrate Oylan 2 API for responses
- [x] Add voice message handling with auto-detection
- [x] Implement multilingual support (KK, RU, EN, TR)
- [x] Add advanced TTS and transcription features
- [x] Implement file_prompt (image, audio) handling
- [ ] Implement file_prompt (video, docs) handling
- [ ] ISSAI API Python SDK

## License

This project is licensed under the MIT License.

## Contact

For questions or suggestions, please contact:

- https://t.me/david667s
- https://t.me/davidsuragan