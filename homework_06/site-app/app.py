from os import getenv

from flask import Flask, render_template
from flask_migrate import Migrate


from models.database import db
from veiws.about import about_app
from veiws.users import users_app


app = Flask(__name__)

config_name = "config.%s" % getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(config_name)

app.register_blueprint(about_app, url_prefix="/about")
app.register_blueprint(users_app, url_prefix="/users")

db.init_app(app)
migrate = Migrate(app, db, compare_type=True)
with app.app_context():
    db.create_all()



@app.route("/")
def index():
    return  render_template("index.html")



if __name__ == "__main__":
    app.run(port=5000)