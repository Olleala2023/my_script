# my_script.py
import time
import requests

def main():
    start_time = time.time()  # Засекаем время начала выполнения
    print("Привет, это моя первая программа на Python!")

    # Выполняем HTTP-запрос
    response = requests.get("https://api.github.com")
    print(f"Статус ответа от GitHub API: {response.status_code}")

    end_time = time.time()    # Засекаем время окончания выполнения
    execution_time = end_time - start_time  # Вычисляем время выполнения
    print(f"Время выполнения программы: {execution_time:.4f} секунд")

if __name__ == "__main__":
    main()