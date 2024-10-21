from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/index")
@app.route("/")  # Обработчик
def index():
    print( url_for("index") ) # url_запрос
    return render_template("index.html")

@app.route("/restourant")
def restourant():
    print( url_for("restourant") ) # url_запрос
    return render_template("restourant.html")

if __name__ == "__main__":  # Запуск на локальном устройстве
    app.run(debug=True)  # Отображение ошибок
