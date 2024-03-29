import os
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('test_page.html')
    # return 'Hello World!'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

