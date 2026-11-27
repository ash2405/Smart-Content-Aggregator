
def test_without_token(client):
    response = client.get('/user/admin/dashboard')
    assert response.status_code == 401
    assert response.json() == {
         "detail": "Not authenticated"
    }

def test_invalid_token(client):

    headers = {
        "Authorization":"Bearer dsfa34fasfa"
    }
    response = client.get('/user/admin/dashboard',
                          headers=headers)

    assert response.status_code == 401
    assert response.json() == {
         "detail": "Invalid or expired token"
    }

def test_normal_user_access(client):
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZXhwIjoxNzk1NzgyMzY3fQ.FWaQ5z7cWzVXhRxrg2DdWe3dYjUFu9l1hT7JDkKmUik"
    }

    response = client.get(
        "/user/admin/dashboard",
        headers=headers
    )

    assert response.status_code == 403
    assert response.json() == {
        "detail": "You don't have permission to access this resource."
    }

def test_admin_access(client):
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzIiwiZXhwIjoxNzk1NzgzMzI5fQ.fF6aff45D5S8q5yRbftAporIe_re0g6LnCKJtaIkgZU"
    }

    response = client.get(
        "/user/admin/dashboard",
        headers=headers
    )

    assert response.status_code == 200
    assert response.json()["role"] == "admin"