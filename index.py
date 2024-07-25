from flask import Flask
from src.routes.abbreviations import reductions

app = Flask(__name__)

app.register_blueprint(reductions)

if __name__ == '__main__':
    app.run(debug=False)