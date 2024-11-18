from flask import Flask, render_template

app = Flask("__name__")


@app.route("/")
def home():
    return render_template("main.html")


@app.route("/api/v1/<word>/")
def about(word):
    print(type(word))
    return {"definition": word.upper(),
            "word": word}
    
    
if __name__ == "__main__":
    app.run(debug=True)
