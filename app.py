from flask import Flask, render_template, url_for, flash, request, redirect
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_pyfile('config.py')

    return app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shortit', methods=['POST'])
def shortit():
    flash(request.form['url'] + ' foi encurtada!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
