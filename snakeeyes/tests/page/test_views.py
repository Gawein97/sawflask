from flask import url_for


class TestPage:
    """Test class for pages blueprint in views"""
    def test_home_page(self, client):
        """Home page view test: should response 200"""
        response = client.get(url_for("page.home"))
        assert response.status_code == 200

    def test_terms_page(self, client):
        """Home terms view test: should response 200"""
        response = client.get(url_for("page.terms"))
        assert response.status_code == 200

    def test_privacy_page(self, client):
        """Home privacy view test: should response 200"""
        response = client.get(url_for("page.privacy"))
        assert response.status_code == 200
