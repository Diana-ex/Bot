@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'HEAD':
        return '', 200

    data = request.json

    if data['type'] == 'confirmation':
        return '1c6691de'

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
