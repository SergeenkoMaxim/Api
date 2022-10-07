# from crypt import methods
# from curses import meta
from math import remainder
import flask
from flask import request, jsonify, render_template
import jyserver.Flask as jsf
from laba_1 import Generator
from laba_1 import GeneratorWithId
# from symbol import pass_stmt

t = Generator()
g = GeneratorWithId()

app = flask.Flask(__name__, template_folder='Templates')
app.config["DEBUG"] = True

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template("index.html")
        
    if request.method == "POST":
        if request.form['send_user_id'] is not None:
            g.UsersIdentifier = request.form["send_user_id"]
            g.Clear_Password()
            g.get_password_policy()
            g.create_password()
            password_with_id = g.Answer
            print(g.UsersIdentifier)
            return render_template("index.html", data=password_with_id)

@app.route('/home', methods=['POST', 'GET'])
def index():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
            t.clear_password()
            t.generate()
            password = t.password
            return render_template("index.html", password_without_id = password)

    if request.method == "POST" and request.form["send_user_id"]:
        g.UsersIdentifier = request.form["send_user_id"]
        g.Clear_Password()
        g.get_password_policy()
        g.create_password()
        password_with_id = g.Answer
        print(g.UsersIdentifier)
        return render_template("index.html", data=password_with_id)
    

    # if request.method == "POST":
        # if request.form['generate_password'] in None:
        #     t.generate()
        #     password = t.password
        #     return render_template("index.html", password_without_id = password)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)

# поменять id всех кнопок на уникальные, чтобы не было путаницы и из их названия было понятно, что они делают

# поменять айди всех кнопок в местах вызовов функций

# прописать логику для каждой кнопки, как мы это сделали для кнопки Submit

# переименовать все классы и их методы в питоническом стиле: классы с большой буквы в камел кейсе, функции и переменные
# с маленькой буквы и слова разделены нижними подчеркиваниями

# дать методам и функциям понятные названия, как get_user_id

# удалить ненужные аттрибуты из класса. т.е те, которые дублируются или не используются

# переместить символы в отдельный файлик с константами и удалить эти символы из классов. в методах вызывать рандом из
# файла с константами
