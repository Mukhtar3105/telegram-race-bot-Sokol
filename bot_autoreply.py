import requests
import time

BOT_TOKEN = '7986450530:AAEHTmcGHEyHdCvjU7HRYcqRf17hsQCgoN8'
URL = f'https://api.telegram.org/bot{BOT_TOKEN}'
WELCOME_MESSAGE = '🏁 Добро пожаловать! Вы будете получать уведомления о дрэг-заездах.'

last_update_id = None

while True:
    try:
        response = requests.get(f'{URL}/getUpdates', params={'offset': last_update_id, 'timeout': 10})
        data = response.json()

        for result in data.get('result', []):
            update_id = result['update_id']
            message = result.get('message')
            if not message:
                continue

            chat_id = message['chat']['id']
            text = message.get('text', '')

            # Отвечаем только на новые сообщения
            if last_update_id is None or update_id > last_update_id:
                print(f'📩 Новое сообщение от {chat_id}: {text}')

                # Отправка приветствия
                requests.post(f'{URL}/sendMessage', data={
                    'chat_id': chat_id,
                    'text': WELCOME_MESSAGE
                })

                last_update_id = update_id + 1

        time.sleep(1)

    except Exception as e:
        print(f'❗ Ошибка: {e}')
        time.sleep(2)
