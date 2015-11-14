from flask import Flask

app = Flask('shorty')


@app.route('/')
def index():
    return 'shorty'

if __name__ == '__main__':
    app.run(debug=True)
