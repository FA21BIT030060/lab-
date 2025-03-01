from flask import Flask

app = Flask(__name__)  # Corrected version

@app.route("/")
def home():
    return "hello,MY name is Abdul Rafay, my name is Sharoon ali "

if _name_ == "_main_":
    app.run()
