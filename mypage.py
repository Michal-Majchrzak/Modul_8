from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/mypage/me', methods=['GET'])
def me():
    return render_template("about-me.html")


@app.route('/mypage/contact', methods=['GET'])
def contact():
    return render_template("contact.html")


@app.route('/mypage/contact', methods=['POST'])
def send_message():
    message = request.form.get('message')
    if message is not None:
        print(f"Twoja wiadomość to : {message}")

    return redirect('/mypage/me')
