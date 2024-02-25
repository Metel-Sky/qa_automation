import datetime
from datetime import datetime
import pytest
import requests

@pytest.fixture
def api_url():
    return "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

@pytest.fixture
def exchange_rates_data():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Не вдалося отримати дані: {e}")
        return None

@pytest.fixture
def exchange_rates_txt_file(exchange_rates_data):
    data = [f"{rate_data['cc']}: {rate_data['txt']} to UAH: {rate_data['rate']}" for rate_data in exchange_rates_data]

    file_path = f"exchange_rates_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(file_path, 'w', encoding='windows-1251') as file:
        file.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n\n".join(data))

    return file_path




