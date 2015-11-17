from flask import Flask, render_template, url_for, flash, request, redirect
from flask_bootstrap import Bootstrap
from models import add_url, get_url

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_pyfile('config.py')

    return app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:target>')
def goto(target):
    goto = get_url(target)
    if goto:
        if goto.find('http://') != 0 and goto.find('https://') != 0:
            goto = 'https://' + goto
        return redirect(goto)

@app.route('/shortit', methods=['POST'])
def shortit():
    goto = request.form['url']
    target = add_url(goto)
    flash(goto + ' foi encurtada para shorty/' + str(target), 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
