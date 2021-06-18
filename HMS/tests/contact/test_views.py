from flask import url_for
from hms.extensions import mail
from hms.email import contact_me


class TestContact():
    def test_contact_page(self, client):
        """
        Contact page should respond with status code 200
        """
        response = client.get(url_for('contact.index'))
        assert response.status_code == 200

    def test_contact_me(self, client):
        """
        Sending a fake data using client post 
        """
        form = {
            "email" : "admin@gmail.com",
            "name" : "Admin test",
            "message" : "This is very good test."
        }

        
        response = client.post(url_for('contact.index'), data=form, follow_redirects=True)
        
        assert b'Thank you ' in  response.data
        assert response.status_code == 200


    def test_send_fake(self, client):
        form = {
            "email" : "admin@gmail.com",
            "name" : "Admin test",
            "message" : "This is very good test.",
            "path" : '/contact/mail/index'
        }

        with mail.record_messages() as outbox:
            contact_me(form.get('email'), 'contact message' ,'/contact/mail/index', data=form)

        assert len(outbox) == 1


