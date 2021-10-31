from flask import redirect,url_for
from blueprints import app
from blueprints import user 

@app.route('/')
def bienvenue():
    return redirect(url_for('user.home'))

if __name__ == '__main__':
    app.run(debug=True)
