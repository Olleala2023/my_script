# my_script.py
import time
import requests
import logging

# Настройка логирования
logging.basicConfig(
    filename='my_script.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    encoding='utf-8'  # Указываем кодировку UTF-8
)

def main():
    start_time = time.time()
    logging.info("Программа запущена")
    print("Привет, это моя первая программа на Python! Обновлено. Делаем обновление второй раз.`Делаем обновление третий раз.")

    try:
        response = requests.get("https://api.github.com")
        status_code = response.status_code
        logging.info(f"Статус ответа от GitHub API: {status_code}")
        print(f"Статус ответа от GitHub API: {status_code}")
    except Exception as e:
        logging.error(f"Ошибка при выполнении запроса: {e}")
        print(f"Ошибка при выполнении запроса: {e}")

    end_time = time.time()
    execution_time = end_time - start_time
    logging.info(f"Время выполнения программы: {execution_time:.4f} секунд")
    print(f"Время выполнения программы: {execution_time:.4f} секунд")

if __name__ == "__main__":
    main()