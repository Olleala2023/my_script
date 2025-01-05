# my_script.py
import os
import time
import requests
import logging
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from dotenv import load_dotenv

load_dotenv()  # Загрузит переменные из .env

FROM_ADDR = os.getenv("FROM_ADDR")
FROM_PASSWORD = os.getenv("FROM_PASSWORD")

# Настройка логирования
logging.basicConfig(
    filename='my_script.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    encoding='utf-8'  # Указываем кодировку UTF-8
)
def send_email_smtp(
    from_addr: str,
    password: str,
    to_addr: str,
    subject: str,
    body: str,
    smtp_server: str,
    smtp_port: int = 465
):
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = from_addr
    msg['To'] = to_addr

    try:
        if smtp_port == 465:
            server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        else:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()

        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        logging.info("Письмо успешно отправлено")
    except Exception as e:
        logging.error(f"Ошибка при отправке письма: {e}")
        print(f"Ошибка при отправке письма: {e}")       
    
def main():
    start_time = time.time()
    logging.info(f"Скрипт запущен с почтой: {FROM_ADDR}")
    print("Привет, это моя первая программа на Python! Обновлено.\n")

    try:
        response = requests.get("https://api.github.com")
        status_code = response.status_code
        logging.info(f"Статус ответа от GitHub API: {status_code}")
        print(f"Статус ответа от GitHub API: {status_code}")
        
        # Допустим, отправим письмо
        subject = "Результат скрипта"
        body = f"Статус ответа от GitHub API: {status_code}"
        send_email_smtp(
            from_addr=FROM_ADDR,      # Ваш email
            password=FROM_PASSWORD,     # Пароль/токен
            to_addr="sidorin19@list.ru", # Кому отправляем
            subject="Тестовое письмо",
            body=f"Статус ответа от GitHub API: {status_code}",
            smtp_server="smtp.mail.ru",           # Пример: Gmail
            smtp_port=465                           # Порт для TLS
        )
    
    except Exception as e:
        logging.error(f"Ошибка при выполнении запроса: {e}")
        print(f"Ошибка при выполнении запроса: {e}")

    end_time = time.time()
    execution_time = end_time - start_time
    logging.info(f"Время выполнения программы: {execution_time:.4f} секунд")
    print(f"Время выполнения программы: {execution_time:.4f} секунд")

if __name__ == "__main__":
    main()