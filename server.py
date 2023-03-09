from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", num=3, color="blue", page="1")

@app.route('/play')
def play():
    return render_template("playground.html", num=3, color="blue", page="1")

@app.route('/play/<int:num>')
def play2(num):
    return render_template("playground.html",num=num,color="blue", page="2")

@app.route('/play/<int:num>/<color>')
def play3(num, color):
    return render_template("playground.html",num=num, color=color, page="3")

if __name__=="__main__":
    app.run(debug=True)