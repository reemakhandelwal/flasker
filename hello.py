from flask import Flask, render_template


#Create a flask instance
app = Flask(__name__)

#Create a route decorator
@app.route('/')

# def index():
#     return "<h1>Hello World!</h1>"
# """
# safe
# capitalize
# lower
# upper
# title
# trim
#  striptags

# """
def index():
    first_name = "Kavya"
    favourite_pizza=['Pepperoni',"Cheese","Mushrooms",41]
    return render_template("index.html",first_name=first_name,favourite_pizza=favourite_pizza)

#localhost:5000/user/Reema
@app.route('/user/<name>')

def user(name):
    return render_template("user.html",user_name=name)
    # def user(name):
#     return "<h1>Hello {}!</h1>".format(name)

#create custom error pages
#invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
    