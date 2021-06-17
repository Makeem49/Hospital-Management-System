from flask import url_for

class TestPage():
    def test_home_page(self, client):
        response = client.get(url_for("page.home"))
        assert response.status_code == 200

    def test_doctor_page(self, client):
        response = client.get(url_for("page.doctor"))
        assert response.status_code == 200

    def test_department_page(self, client):
        response = client.get(url_for("page.department"))
        assert response.status_code == 200

    def test_about_page(self, client):
        response = client.get(url_for("page.about"))
        assert response.status_code == 200
        
    