from flask.templating import render_template
from hms.blueprints.user import user

@user.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('page/register.html')
