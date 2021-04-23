from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
from pprint import pprint

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

@app.route("/")
def index():
    data = mongo.db.collection.find_one()
    print(data)
    return render_template("index.html", data=data)


@app.route("/scrape")
def run_scrape():
    scraped_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, scraped_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
