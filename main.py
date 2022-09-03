import requests
from flask import Flask, render_template

# set up Flask
app = Flask(__name__)


# set up the main page
@app.route('/')
def welcome():
    return "welcome"


# set up the guess page
@app.route('/guess')
def guess():
    return "Write your name in the URL."


# get the information using route parameter <userID>
@app.route('/guess/<userID>')
def hello_world(userID):
    response = requests.get(f"https://api.agify.io?name={userID}")
    response2 = requests.get(f"https://api.genderize.io?name={userID}")
    name = userID
    age = response.json()["age"]
    gender = response2.json()["gender"]
    return render_template("index.html", num=age, gen=gender, nam=name)


# rendering the json data from the api
@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/1ceebdb9e9eea5f51c01"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)
