print("""
          ░░░░▒▓▓▓▓▓▓▓▓▓▓▒░░░░░         
       ░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░       
      ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░     
    ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░   
 ░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░   
 ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░ 
░░▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░▒▓▓▓▓▒░▓▓▓▓▓▓▓▓▓▓▓░░
░▓▓▓▓▓▓▒░░░░░      ░▓▓▓▓▓▒ ░░▒▓▓▒▒░░▓▓▓░
░▓▓▓▓▓░░░░          ░░▒▓▓▓░░ ░░░  ░▒▓▓▓▒
▒▓▓▓▓░░░░             ░░▒▓▓░░░ ░░░▓▓▓▓▓▓
▓▓▓▓░░░▒▒▒░░░░      ░░░░░░▒▒░░░▓▓▓▓▓▓▓▓▓
▓▓▓▓░░▒▓▓▓▓▓▓▓░░    ░░▓▒░░░ ░░░▓▓▓▓▓▓▓▓▓
▒▓▓▓░░░▓▓▓▓▓▓▓▓▓░░  ░░▒▓▓░  ░░▒▓▓▓▓▓▓▓▓▓
▒▓▓▓▒░░▒▓▓▓▓▓▓▓▓▓▒░░░ ░░░░  ░░▓▓▓▓▓▓▓▓▓▒
░▓▓▓▓░░░▒▓▓▓▓▓▓▓▓▓▓░░      ░░▓▓▓▓▓▓▓▓▓▓░
░░▓▓▓▓░░░░▓▓▓▓░░▒▓▓▓░░░  ░░▒▓▓▓▓▓▓▓▓▓▓░░
░░░▓▓▓▓▒░░░░▒▓▓░░░░▓▓▓░░ ░░░▒▓▓▓▓▓▓▓▓░░░
  ░░▓▓▓▓▓▒░░░░░░    ░░░▒▒░░░░▓▓▓▓▓▓▓░░░ 
   ░░▒▓▓▓▓▓▓▓▒░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░  
     ░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░   
        ░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░      
          ░░░░▒▓▓▓▓▓▓▓▓▓▓▒░░░░░░

░█▀▀▄ ░█▀▀▀ ░█▀▀▀ ░█▀▀█ ── ─█▀▀█ ░█▀▀█ ▀█▀ 
░█─░█ ░█▀▀▀ ░█▀▀▀ ░█▄▄█ ▀▀ ░█▄▄█ ░█▄▄█ ░█─ 
░█▄▄▀ ░█▄▄▄ ░█▄▄▄ ░█─── ── ░█─░█ ░█─── ▄█▄
    the free api library of deepseek
            ｂｙ ｂ１ｔ０ｎｅ
        tg: https://t.me/u53rnm3
    github: https://github.com/ArtemChikc
""")

from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import sys
import requests
import zipfile
import json
import psutil

def close_processes(process_names):
    for proc in psutil.process_iter():
        for name in process_names:
            if name.lower() in proc.name().lower():
                proc.kill()
                print(f"Process {proc.pid} ({proc.name()}) has been terminated.")

# команда для закрытия всех процессов связанных с chrome
#желательно использовать при импорте библиотеки если ваша программа часто перезапускается
def close_chromedrivers():
    process_names = ["chrome.exe", "chromedriver.exe"]
    close_processes(process_names)


# Скачивание chromedriver
def chromedriver(install=False):
    # Определяем последнюю стабильную версию Chrome
    latest_release_url = "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json"
    response = requests.get(latest_release_url)
    data = response.json()

    version = data['channels']['Stable']['version']
    chromedriver_path = os.path.join(os.path.dirname(__file__), "program_files/chromedriver.exe")

    if install:
        if install!=True:
            path = os.path.join(os.path.dirname(__file__), install)
        else:
            path = ""
        if not os.path.exists(chromedriver_path):
            # Выбираем URL для текущей ОС
            if sys.platform == 'win32':
                url = next(item['url'] for item in data['channels']['Stable']['downloads']['chromedriver'] 
                        if item['platform'] == 'win32')
            if sys.platform == 'win64':
                url = next(item['url'] for item in data['channels']['Stable']['downloads']['chromedriver'] 
                        if item['platform'] == 'win64')
            elif sys.platform == 'linux':
                url = next(item['url'] for item in data['channels']['Stable']['downloads']['chromedriver']
                        if item['platform'] == 'linux64')
            elif sys.platform == 'darwin':
                url = next(item['url'] for item in data['channels']['Stable']['downloads']['chromedriver']
                        if item['platform'] == 'mac-x64')
            # Скачиваем архив
            print(f"Installing chromedriver {version}...")
            zip_path = os.path.join(path, "chromedriver.zip")
            with open(zip_path, 'wb') as f:
                f.write(requests.get(url).content)
            # Распаковываем
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(path)
            # Удаляем архив
            os.remove(zip_path)
            # Переименовываем файл (для Windows)
            if sys.platform.startswith('win'):
                if sys.platform == 'win32':
                    old_path = os.path.join(os.path.dirname(__file__), "chromedriver-win32", "chromedriver.exe")
                elif sys.platform == 'win64':
                    old_path = os.path.join(os.path.dirname(__file__), "chromedriver-win64", "chromedriver.exe")
                if os.path.exists(chromedriver_path):
                    os.remove(chromedriver_path)
                os.rename(old_path, chromedriver_path)
            print("Chromedriver is installed successfully!")

    return chromedriver_path, int(version.split(".")[0])



class UserTokenError(Exception):
    def __init__(self, message="Invalid userToken", code=400):
        self.code = code
        super().__init__(f"{message} (code: {code})")



class dpsk:
    # Инициирование deepseek, получает на вход 3 аргумента максимум
    #- ваш userToken на сайте дипсик (важно), промпт дипсику,
    #а так же скачивать ли chromedriver, можно ввести папку установки
    #(иначе при каждом запуске будет качаться заново)
    def __init__(self, userToken, prompt=None, install_chromedriver=False):
        print("Chrome initialization...")
        chromedriver_path, version = chromedriver(install_chromedriver)
        self.driver = Chrome(version_main=version, driver_executable_path=chromedriver_path, headless=False)

        self.count_msgs = 0
        self.prompt = prompt

        print("Starting DeepSeek...")
        self.driver.get("https://chat.deepseek.com")

        local_storage = self.driver.execute_script("return window.localStorage;")
        local_storage['userToken'] = json.dumps({"value": userToken, "__version": "0"})
        self.driver.execute_script("window.localStorage.clear();")
        for key, value in local_storage.items():
            self.driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")

        self.driver.get("https://chat.deepseek.com")
        self.del_history(prompt=prompt)

    # Команда для запроса нейронке, на вход подаётся текст и параметры - глубокое размышление и поиск
    def chat(self, text, think=False, search=False):        
        buttons = self.driver.find_elements(By.CSS_SELECTOR, ".ds-button.ds-button--primary.ds-button--filled")
        if think:
            buttons[0].click()
        if search:
            buttons[1].click()

        chat_input = self.driver.find_element("id", "chat-input")
        text_chunks = [text[i:i+50] for i in range(0, len(text), 50)]
        while not chat_input.get_attribute('value'):
            for chunk in text_chunks:
                if "\n" in chunk:
                    parts = chunk.split("\n")
                    for i, part in enumerate(parts):
                        if part:
                            chat_input.send_keys(part)
                        if i != len(parts)-1:
                            chat_input.send_keys(Keys.SHIFT + Keys.ENTER)
                else:
                    chat_input.send_keys(chunk)
        chat_input.send_keys(Keys.ENTER)

        result = None
        while not result:
            try:
                markdown_blocks = self.driver.find_elements(By.CSS_SELECTOR, 'div.ds-markdown.ds-markdown--block')
                if self.count_msgs+1==len(markdown_blocks):
                    target_markdown = markdown_blocks[self.count_msgs]
                    if target_markdown.find_element(By.XPATH, './following-sibling::div[contains(@class, "ds-flex")][1]'):
                        result = target_markdown.text
            except: pass
            try:
                busy_server = self.driver.find_element(
                    By.XPATH, "//span[text()='Server busy, please try again later.']")
                if busy_server:
                    result = None
                    break
            except: pass
            try:
                busy_server = self.driver.find_element(
                    By.XPATH, "//span[text()='Check network and retry.']")
                if busy_server:
                    result = None
                    break
            except: pass
        self.count_msgs += 1

        if think:
            buttons[0].click()
        if search:
            buttons[1].click()

        if not result:
            self.count_msgs -= 1
            self.driver.refresh()
        return result

    # Команда для очистки истории (практически просто создаёт новый чат), можно задать промпт
    def del_history(self, prompt=None):
        self.count_msgs = 0
        self.driver.get("https://chat.deepseek.com")

        if not self.driver.current_url=="https://chat.deepseek.com/sign_in":
            print("DeepSeek started!\n\n")
        else:
            self.driver.quit()
            raise UserTokenError("invalid userToken")
        
        if prompt or self.prompt:
            if prompt:
                self.prompt = prompt
            self.chat(self.prompt)


# Простой пример использования api
if __name__=="__main__":
    userToken = "your userToken"
    prompt = "Ты обычный DeepSeek."
    chat = dpsk(userToken, prompt=prompt, install_chromedriver=True)

    try:
        while True:
            inpt = input("Message DeepSeek: ")
            if inpt=="exit":
                chat.driver.quit()
                exit()
            elif inpt=="refresh":
                chat.refresh()
                continue
            think = False
            search = False
            if "#THINK" in inpt:
                think = True
            if "#SEARCH" in inpt:
                search = True
            print("DeepSeek:", chat.chat(inpt, think=think, search=search)+"\n")

    except KeyboardInterrupt:
        chat.driver.quit()
        exit()
