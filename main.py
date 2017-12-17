from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form method="POST">
            <label for="rotate-by">Rotate by:<label>
            <input id="rotate-by" type="text" name="rot">
            <textarea name="text">
            </textarea>
            <input type="submit" value="submit">
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    plaintext = request.form['text']
    return """
        <h1>
            {}
        </h1>
        """.format(rotate_string(plaintext, rot))


app.run()