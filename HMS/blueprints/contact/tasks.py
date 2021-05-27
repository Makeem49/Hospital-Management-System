from hms.app import create_celery_app
from hms.email import contact_me

celery = create_celery_app()

celery.task()
def contact_task(email, subject, template, data):
    """
    :param email: user email address
    :param type: string
    :param subject: user email subject
    :param type: string 
    :param template: email template
    :param type : path
    :param data: dictionary containing other info 
    :param type: dictionary
    """

    contact_me(email, subject, template, data)

    return None

