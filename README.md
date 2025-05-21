# DEEP-API
the free api library of deepseek

Эта библиотека даст вам доступ к deepseek с помощью Python абсолютно бесплатно!
Библиотека очень пригодится тем людям которые хотят использовать текстовые ИИ в своих проектах.
Requirements:
Python 3.x
Chrome новейшей версии
pip install selenium undetected-chromedriver

Использование:
1) Импорт
   from deep-api import *
2) Инициирование deepseek
   chat = dpsk("Ваш юзер токен (о нём позже)", prompt="Ты обычный deepseek, делай что хочешь", inst_chrdriver=True)
3) Запрос
   chat.chat("Привет дипсик!", think=False, search=False)+"\n")
4) Очищение истории (если нужно)
   chat.refresh()

Как получить userToken?
1) Закодим на chat.deepseek.com
2) Если просит войти в аккаунт входим
3) Далее открываем devtools нажав 
