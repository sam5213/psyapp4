from flask import Flask, request, jsonify
import telegram
from datetime import datetime

# Настройки Telegram бота
bot_token = 'YOUR_BOT_TOKEN'
chat_id = 'YOUR_CHAT_ID'  # ID чата, где будут приходить уведомления

app = Flask(__name__)
bot = telegram.Bot(token=bot_token)

@app.route('/', methods=['GET'])
def index():
    return '<h1>Привет! Это API для записи на консультации.</h1>'

@app.route('/book', methods=['POST'])
def book_consultation():
    data = request.form.to_dict()
    name = data['name']
    date_str = data['date']
    try:
        date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M')
    except ValueError:
        return jsonify({'error': 'Неверный формат даты'}), 400
    
    message = f'{name} записался(лась) на консультацию на {date.strftime("%d.%m.%Y %H:%M")}.'
    bot.send_message(chat_id=chat_id, text=message)
    
    return jsonify({'success': True}), 201

@app.route('/cancel/<consultation_id>', methods=['DELETE'])  # Примем консультацию по ID
def cancel_consultation(consultation_id):
    # Логика удаления консультации по ID
    message = f'Консультация с ID {consultation_id} была отменена.'
    bot.send_message(chat_id=chat_id, text=message)
    
    return jsonify({'success': True}), 204

if __name__ == '__main__':
    app.run(debug=True)
