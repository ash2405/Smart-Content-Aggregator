from unittest.mock import AsyncMock,patch

from fastapi.testclient import TestClient
from app.main import app
from uuid import uuid4

unique_url = f"https://example.com/articles/{uuid4()}"

# Tests for Create Article
def test_create_article(client, mock_article):

    with patch("app.routes.article.create_article_service",
               new_callable= AsyncMock) as mock_create_article:
        mock_create_article.return_value = mock_article
        
        response = client.post("/articles/", json=mock_article)
        mock_create_article.assert_awaited_once()    
    assert response.status_code == 201

    data = response.json()

    assert data["title"] == mock_article["title"]
    assert data["url"] == mock_article["url"]


# Tests for Get Articles
def test_get_article(client,mock_article_list):

    with patch(
        "app.routes.article.get_articles_service",
        new_callable=AsyncMock) as mock_list_articles:
        mock_list_articles.return_value = mock_article_list
        response = client.get("/articles/")
        mock_list_articles.assert_awaited_once()
        assert response.status_code == 200

        print("Response Data: ", response.json())
        


def test_get_article_by_id(client,mock_article):

    with patch(
        "app.routes.article.get_article_by_id_service",
        new_callable=AsyncMock
    ) as get_article_by_id_service:

        get_article_by_id_service.return_value = mock_article

        response = client.get("/articles/1")
        get_article_by_id_service.assert_awaited_once()

        response_data = response.json()

        print("Response Data:", response_data['title'])

        assert response_data["title"] == mock_article["title"]


def test_delete_article(client, mock_article):

    # Create an article to delete
    with patch(
        "app.routes.article.create_article_service",
        new_callable=AsyncMock
    ) as create_article_service:

        create_article_service.return_value = mock_article

        response = client.post("/articles/", json=mock_article)
        create_article_service.assert_awaited_once()

        assert response.status_code == 201

        create_response = response.json()
        
        with patch(
            "app.routes.article.delete_article_service",
            new_callable=AsyncMock
        ) as delete_article_service:

            delete_article_service.return_value = None

            delete_response = client.delete(f"/articles/{create_response['id']}")

            delete_article_service.assert_awaited_once()

            print("Delete Response Status Code:", delete_response.status_code)

            assert delete_response.status_code == 204


def update_article(client, mock_article):
    # Create an article to update
    with patch(
        "app.routes.article.create_article_service",
        new_callable=AsyncMock
    ) as create_article_service:

        create_article_service.return_value = mock_article

        response = client.post("/articles/", json=mock_article)
        create_article_service.assert_awaited_once()

        assert response.status_code == 201

        create_response = response.json()

        # Update the article
        updated_data = {
            "title": "Updated Article Title",
            "url": "https://example.com/updated-article",
            "content": "Updated content.",
            "source_id": 2,
            "status": "Draft",
            "category": "Technology"
        }

        with patch(
            "app.routes.article.update_article_service",
            new_callable=AsyncMock
        ) as update_article_service:

            update_article_service.return_value = {**create_response, **updated_data}

            update_response = client.put(f"/articles/{create_response['id']}", json=updated_data)

            update_article_service.assert_awaited_once()

            print("Update Response Status Code:", update_response.status_code)
            print("Update Response Data:", update_response.json())

            assert update_response.status_code == 200

            updated_response_data = update_response.json()

            assert updated_response_data["title"] == updated_data["title"]


