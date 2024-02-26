import requests
from datetime import datetime

def get_exchange_rates():
    api_url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        exchange_data = response.json()
        return exchange_data
    except requests.exceptions.RequestException as e:
        print(f"Не вдалося отримати дані: {e}")
        return None

def save_to_file(exchange_data, file_path):
    if not exchange_data:
        print("Дані не доступні. Вихід.")
        return

    data = [f"{rate_data['cc']}: {rate_data['txt']} to UAH: {rate_data['rate']}" for rate_data in exchange_data]

    with open(file_path, 'w', encoding='windows-1251') as file:
        file.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n\n")
        file.write("\n\n".join(data))

def main():
    file_path = "exchange_rates.txt"

    exchange_data = get_exchange_rates()
    save_to_file(exchange_data, file_path)

if __name__ == "__main__":
    main()

