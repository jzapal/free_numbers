import datetime

import fire
import yagmail

import requests
from pydantic import BaseSettings


class Settings(BaseSettings):
    email_user: str
    email_password: str
    send_to: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()


def search_for_numbers(number_of_days: int = 30):
    BASE_URL = 'https://udwola-rez.um.warszawa.pl/pol/queues/190/124'
    today = datetime.date.today()
    for i in range(number_of_days):
        date = (today + datetime.timedelta(days=i)).strftime('%Y-%m-%d')
        url = f'{BASE_URL}/{date}'
        res = requests.get(url)
        if res.status_code != 200:
            continue
        if not res.content.find(b'brak wolnych') > -1:
            send_notification(date)
            print(f'Znaleziono termin na {date}!')
            return
    print('Nie znaleziono wolnych numerków :(')


def send_notification(date):
    with yagmail.SMTP(settings.email_user, settings.email_password) as yag:
        yag.send(settings.send_to.split(','), "Wolny numerek",
                 f"Pojawił się wolny numerek na {date}")


if __name__ == '__main__':
    fire.Fire(search_for_numbers)

