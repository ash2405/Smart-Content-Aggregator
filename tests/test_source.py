from unittest.mock import AsyncMock,patch


#Get source list
def test_get_source_list(client, mock_source_list):
    with patch(
        "app.routes.source.get_sources_service",
        new_callable=AsyncMock
    ) as mock_get_sources_service:
        mock_get_sources_service.return_value = mock_source_list

        response = client.get("/sources/")
        mock_get_sources_service.assert_awaited_once()

        assert response.status_code == 200

#Get source by id
def test_get_source_by_id(client, mock_source):
    with patch(
        "app.routes.source.get_source_by_id_service",
        new_callable=AsyncMock
    ) as mock_get_source_by_id_service:
        mock_get_source_by_id_service.return_value = mock_source

        response = client.get("/sources/1")
        mock_get_source_by_id_service.assert_awaited_once()

        assert response.status_code == 200

# Create source
def test_create_source(client, mock_source):
    with patch(
        "app.routes.source.source_create",
        new_callable=AsyncMock
    ) as mock_source_create:
        mock_source_create.return_value = mock_source

        response = client.post("/sources/", json=mock_source)
        mock_source_create.assert_awaited_once()

        assert response.status_code == 201

# Update source
def test_update_source(client, mock_source):

    with patch(
        "app.routes.source.source_create",
        new_callable=AsyncMock
    ) as mock_source_create:

        mock_source_create.return_value = mock_source

        create_response = client.post("/sources/", json=mock_source)
        mock_source_create.assert_awaited_once()

        assert create_response.status_code == 201

        with patch(
            "app.routes.source.update_source_service",
            new_callable=AsyncMock
        ) as mock_update_source_service:

            update_source_data = {
                "name": "Updated Source Name",
                "url": "https://updatedsource.com"
            }
            mock_update_source_service.return_value = {**create_response.json(), **update_source_data}

            update_response = client.put("/sources/1", json=update_source_data)
            mock_update_source_service.assert_awaited_once()

            assert update_response.status_code == 200

# Delete source
def test_delete_source(client, mock_source):

    with patch(
        "app.routes.source.source_create",
        new_callable=AsyncMock
    ) as mock_source_create:

        mock_source_create.return_value = mock_source

        create_response = client.post("/sources/", json=mock_source)
        mock_source_create.assert_awaited_once()

        assert create_response.status_code == 201

        with patch(
            "app.routes.source.source_delete_service",
            new_callable=AsyncMock
        ) as delete_source_service:

            delete_source_service.return_value = None

            delete_response = client.delete(f"/sources/{create_response.json()['id']}")
            delete_source_service.assert_awaited_once()

            assert delete_response.status_code == 204