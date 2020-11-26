from flask import Flask

from website import website_bp
from admin import admin_bp

app = Flask(__name__)

app.secret_key = 'Uma_Chave_bem_secreta'

app.register_blueprint(website_bp)

app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(
        debug=True
    )

