#Richard Wang
#Period 9
#9/20/16

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hi():
    return __name__ + "\thi"

@app.route("/help")
def help():
    return "Help Aqui"

@app.route("/secret")
def secret():
    return "Wow, much secret"

@app.route("/fin")
def end():
    return "El Fin"

if __name__ == '__main__':
    app.run()
