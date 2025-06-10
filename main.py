from flask import Flask, request
import vk_api
import os

app = Flask(__name__)

GROUP_TOKEN = os.getenv("GROUP_TOKEN")
vk_session = vk_api.VkApi(token=GROUP_TOKEN)
vk = vk_session.get_api()

@app.route('/', methods=['GET', 'POST'])
def main():
    data = request.json

    if data['type'] == 'confirmation':
        return '1c6691de'  # Строка, которую должен вернуть сервер

    elif data['type'] == 'message_new':
        try:
            user_id = data['object']['peer_id']
            message_text = data['object']['text']

            # Отправляем ответ пользователю
            vk.messages.send(
                peer_id=user_id,
                message=f"Вы написали: {message_text}",
                random_id=0
            )
        except KeyError as e:
            print(f"Ошибка при обработке данных: {e}")
            return "Ошибка при обработке данных", 400

    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 5000)))
    
