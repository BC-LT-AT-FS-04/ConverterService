#
# @app.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia. # <add direccion de jala la paz>
# All rights reserved. #
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from flask import Flask
from models import db
from os import environ

from routes.metadata_routes import metadata_blueprint
from routes.audio_routes import audio_blueprint
from routes.image_routes import image_blueprint
from routes.video_routes import video_blueprint
from routes.download_routes import download_blueprint
from routes.login_routes import login_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(metadata_blueprint, url_prefix='/api')
app.register_blueprint(audio_blueprint, url_prefix='/api')
app.register_blueprint(image_blueprint, url_prefix='/api')
app.register_blueprint(video_blueprint, url_prefix='/api')
app.register_blueprint(download_blueprint, url_prefix='/api')
app.register_blueprint(login_blueprint, url_prefix='/api')


@app.route("/")
def home():
    return "Welcome to the API Converter Service v1!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090, debug=True)
