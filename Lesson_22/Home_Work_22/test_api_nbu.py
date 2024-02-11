import requests

def test_api_response_status(api_url):
    response = requests.get(api_url)
    assert response.status_code == 200


def test_api_response_content(api_url):
    response = requests.get(api_url)
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    assert len(response.json()) > 0


def test_api_response_structure(api_url,exchange_rates_txt_file):
    response = requests.get(api_url)
    data = response.json()
    assert data








