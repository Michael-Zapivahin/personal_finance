from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Создание экземпляра приложения
app = Flask(__name__, template_folder='app/templates')

# Конфигурация приложения
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Инициализация расширений
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# Импорт маршрутов
from app import routes

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)
