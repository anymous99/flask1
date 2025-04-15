from flask import Flask
from config import Config
from database import db
from speakingtestroutes import routes_bp as speakingtest_bp
from userroutes import routes_bp as userroute_bp

import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


app.register_blueprint(speakingtest_bp)
app.register_blueprint(userroute_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
