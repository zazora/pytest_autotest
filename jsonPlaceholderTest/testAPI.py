import requests
URL = "https://jsonplaceholder.typicode.com"

def test_create_post():
    payload = {
        "title":"greeting",
        "body":"hello everybody",
        "userId": 1	
        }
    response = requests.post(f"{URL}/posts",json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"]=="greeting"
    assert data["body"]=="hello everybody"
    assert data["userId"]==1
    assert "id" in data
	
def test_update_post():
    payload = {
        "title":"new greeting",
        "body":"hello",
        "userId":1
        }
    response = requests.put(f"{URL}/posts/1",json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "new greeting"
    assert data["body"] == "hello"
    	
def test_delete_post():
    response = requests.delete(f"{URL}/posts/1")
    assert response.status_code in [200,204]
    assert response.text in ('','{}')
	
	
