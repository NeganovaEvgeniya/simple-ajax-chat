from flask import Flask
from flask import render_template
from flask import request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Хранилище сообщений в оперативной памяти
data = []

@app.get("/")
def hello_world():
    return render_template('index.html')

# Маршрут для получения всех сообщений из памяти
@app.get("/messages")
def get_messages():
    result = json.dumps(data, ensure_ascii=False)
    # Очищаем список после отправки, чтобы избежать дублирования в интерфейсе
    data.clear()
    return result

# Маршрут для обработки новых сообщений от клиента
@app.post("/send_message")
def sent_message():
    message_data = {'author': request.form['author'], 'text': request.form['message']}
    data.append(message_data)
    return '{"status": "ok"}'

app.run()