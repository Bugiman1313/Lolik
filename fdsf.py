import requests

def test_get_request():
    # Выполняем GET-запрос к публичному API
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    
    # Проверяем, что статус код 200 (успешный запрос)
    assert response.status_code == 200
    
    # Проверяем, что ответ содержит ключ 'title'
    data = response.json()
    assert 'title' in data