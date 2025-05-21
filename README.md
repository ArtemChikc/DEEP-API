# 🤖 DEEP-API
The Ultimate DeepSeek Chat Library for Python 🚀

Бесплатная и простая в использовании библиотека для интеграции DeepSeek Chat в ваши Python-проекты!

🔥 Преимущества DEEP-API
✅ Полностью бесплатный доступ к DeepSeek Chat через Python
✅ Автоматическая работа через браузер (без официального API)
✅ Поддержка длинных диалогов с возможностью очистки истории
✅ Гибкие настройки (think, search и другие параметры)
✅ Простота интеграции – всего несколько строк кода!

⚙️ Требования
Python 3.10+ 🐍
Google Chrome (последняя версия) 🌐
Установка зависимостей:
```pip install selenium undetected-chromedriver```

🚀 Быстрый старт
1️⃣ Импортируем библиотеку
```python
from deep_api import dpsk  # Импорт основного класса
```
2️⃣ Инициализируем чат
```python
chat = dpsk(
    user_token="ВАШ_USER_TOKEN",  # Как получить – см. ниже 👇
    prompt="Ты – умный AI-ассистент. Отвечай вежливо.",  # Системный промпт (опционально)
    inst_chrdriver=True  # Автоматическая установка ChromeDriver (если не установлен)
)
```
3️⃣ Отправляем запрос
```python
response = chat.chat("Привет! Как дела?")  # Получаем ответ от DeepSeek
print(response)
```
⚡ Доп. параметры:
think=True – включить глубокое мышление AI
search=True – включить поиск в интернете
4️⃣ Очистка истории (если нужно)
```python
chat.refresh()  # Сброс контекста диалога
```

🔑 Как получить userToken?
1) Откройте chat.deepseek.com в Chrome
2) Авторизуйтесь (если требуется)
3) Откройте DevTools (F12 или ПКМ → "Исследовать")
4) Перейдите во вкладку Application → Local Storage
5) Найдите ключ userToken и скопируйте его значение (value):
![image](https://github.com/user-attachments/assets/38e79a4a-0cce-4620-bd19-def1dcdda2b4)

6) Вставьте его в код при инициализации dpsk()

💡 Пример использования
```python
from deep_api import dpsk
# Инициализация
ai = dpsk("ваш_токен_здесь", prompt="Отвечай как Пушкин")
# Чат-бот в стиле Пушкина
poem = ai.chat("Напиши короткое стихотворение про Python")
print(poem)
# Очистка истории
ai.refresh()
# ИЛИ закрытие программы
ai.driver.quit()
```

DEEP-API – ваш ключ к бесплатному и мощному ИИ-ассистенту! 🎉
