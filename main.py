from flask import Flask, jsonify, redirect

# Import routes
from src.home.home             import home
from src.portfolium.portfolium import portfolium
from src.geral.geral           import geral

app = Flask(
    import_name     ="api-invest",
    static_folder   ="static",
    template_folder ="templates"
)
with app.app_context():
    home(app)
    geral(app)
    portfolium(app)


@app.route('/')
def home():
    return redirect('/invest/home')

if __name__ == "__main__":
    app.run(debug=True)