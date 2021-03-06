from config import HOST
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

@app.route('/<string:target>')
def goto(target):
    goto = get_url(target)
    if goto:
        if goto.find('http://') != 0 and goto.find('https://') != 0:
            goto = 'https://' + goto
        return redirect(goto)
    else:
        url = 'http://' + HOST + '/' + target
        return render_template('erro_nourl.html', url=url)

@app.route('/shortit', methods=['POST'])
def shortit():
    goto = request.form['url']
    target = add_url(goto)
    link = 'http://' + HOST + '/' + str(target)
    flash(goto + ' foi encurtada para <a href="' + link + '">' + link + '</a>', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
