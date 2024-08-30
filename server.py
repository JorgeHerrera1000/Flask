from flask import Flask, render_template


app = Flask(__name__)








@app.route('/loteria')
@app.route('/loteria/<int:cols>')
@app.route('/loteria/<int:rows>/<int:cols>')
def index(rows=4, cols=4):
    return render_template("index.html", row=rows, col=cols, color_one="#dda8c4", color_two="#287fe4", color_three="#eadb00")














if __name__ =="__main__":
    app.run(debug=True)