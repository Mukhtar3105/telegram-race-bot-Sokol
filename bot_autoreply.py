import requests
import time

BOT_TOKEN = '7986450530:AAEHTmcGHEyHdCvjU7HRYcqRf17hsQCgoN8'
URL = f'https://api.telegram.org/bot{BOT_TOKEN}'
WELCOME_MESSAGE = '🏁 Добро пожаловать! Вы будете получать уведомления о дрэг-заездах.'

last_update_id = None

def send_menu(chat_id):
    keyboard = {
        "keyboard": [
            [{"text": "🔍 Регистрация"}, {"text": "💨 Результаты"}],
            [{"text": "📊 Классы"}, {"text": "🔥 ТОП 10"}],
            [{"text": "💬 Чат"}, {"text": "🏁 Online"}]
        ],
        "resize_keyboard": True
    }

    data = {
        "chat_id": chat_id,
        "text": "Выберите действие из меню 👇",
        "reply_markup": keyboard
    }

    requests.post(f'{URL}/sendMessage', json=data)

while True:
    try:
        response = requests.get(f'{URL}/getUpdates', params={'offset': last_update_id, 'timeout': 10})
        data = response.json()

        for result in data.get('result', []):
            update_id = result['update_id']
            message = result.get('message', {})
            chat = message.get('chat', {})
            chat_id = chat.get('id')
            text = message.get('text', '')

            if last_update_id is None or update_id > last_update_id:
                print(f'📩 Новое сообщение от {chat_id}: {text}')

                if text == '/menu':
                    send_menu(chat_id)
                else:
                    # Отправка приветствия (если не /menu)
                    requests.post(f'{URL}/sendMessage', data={
                        'chat_id': chat_id,
                        'text': WELCOME_MESSAGE
                    })

                last_update_id = update_id + 1

        time.sleep(1)

    except Exception as e:
        print(f'Ошибка: {e}')
        time.sleep(2)
