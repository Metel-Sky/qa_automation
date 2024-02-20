import datetime
import pytest
from datetime import datetime
import requests


@pytest.fixture
def api_url():
    return "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"


@pytest.fixture
def exchange_rates_data(api_url):
    url = api_url
    try:
        response = requests.get(url)
        response.raise_for_status()  # Викинути виняток, якщо статус відповіді не 2xx
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        # Обробка помилок під час отримання даних
        print(f"Не вдалося отримати дані: {e}")
        return None

@pytest.fixture
def exchange_rates_txt_file(exchange_rates_data):
    data = []

    for rate_data in exchange_rates_data:
        #if rate_data == "USD":
            entry = (f"{rate_data['cc']}: {rate_data['txt']} to UAH: {rate_data['rate']}")

            data.append(entry)


    file_path = f"exchange_rates_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(file_path, 'w') as file:
        file.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
        file.write("\n\n")
        file.write("\n\n".join(data))

    return file_path

