# Mission to Mars - scraping application
import scrape_mars
from flask import Flask, jsonify, render_template, redirect
from flask_pymongo import PyMongo

# Initialize Flask
app = Flask(__name__)

# Initialize MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Query MongoDB document and pass its data into an HTML template to display data
@app.route("/")
def index():
    mars_portal_info = mongo.db.mars_db.find_one()
    return render_template("index.html", portal_info=mars_portal_info)

# Call scraped values function, and insert them into MongoDB document in 'mars_db' database
@app.route("/scrape")
def scrape():
    # Grab dictionary of scraped values from function
    marsportal_scraped_values = scrape_mars.scrape()   

    # Declare the database
    mars_db = mongo.db.mars_db

    # Insert (or update) the document containing our dictionary into the database
    mars_db.update(
        {},
        marsportal_scraped_values,
        upsert=True
    )
    # Redirect to the home page to pass MongoDB values into our HTML template
    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)