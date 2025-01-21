from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/set_color", methods=["POST"])
def set_color():
    selected_color = request.form.get('color', '#ffffff')
    return render_template('result.html', color=selected_color)

if __name__ == "__main__":
    app.run(debug=True)
