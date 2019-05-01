# Import flask module
from flask import Flask, redirect, url_for, request

# Create a Flask app with name of current module as argument
app = Flask(__name__)

"""
Create a HTTP route
It is basically a decorator with binds the URL to a particular function
We can access the request and response arguments of the HTTP request
"""


@app.route("/")
# This function will be invoked when anyone accesses the / route on the server
def hello_world():
    # The response of the function will be rendered onto the screen
    return "Hello World"


# Another method to bind URL to a function
app.add_url_rule('/hello', 'hello', hello_world)


# Dynamic URL binding with variables
# Possible converters used as variables : int, float, path
@app.route("/hello/<name>")
def hello_name(name):
    return "Hello " + name


@app.route("/blog/<int:count>")
def blog_count(count):
    return "Totoal Blog posts: " + str(count)


@app.route('/hotel/<float:price>')
def hotel_cost(price):
    return "Your total charges are " + str(price)


"""
If you create you route as /route it will not be accessible through URL pattern of /route/
So to be safe keep route patterns of the following format always : /route/
"""


@app.route("/route/")
def route():
    return "Route accessed"


# Use for url_for method

# Route for admin users
@app.route('/admin')
def hello_admin():
    return "Hello admin"


# Route for guest users
@app.route('/guest')
def hello_guest():
    return "Hello guest"


# Depending on name variable redirect user
# url_for generates a url for given endpoint with the corresponding method
@app.route("/user/<name>")
def hello_user(name):
    # redirect user to admin/guest page depending on name value. Import redirect and url_for
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest'))


"""
HTTP methods:
GET : Sends data through URL rewriting in unencrypted format
POST : USed to send data to Server through request body. Secure
HEAD : Same as GET but without response body
PUT : Replace current resource at the URl with the sent one
DELETE : Delete resources at the specified URL 
"""


# Example of form submission from login.html and POST/GET requests

# show the HTML page on the /loginPage route
@app.route("/loginPage")
def login_page():
    file = open('login.html', 'r')
    html = file.read()
    file.close()
    return html


# This route is invoked on form submission
@app.route("/login", methods=['POST', 'GET'])
def login():
    # access request parameters. Import request module
    if request.method == 'POST':
        # Access form variable
        name = request.form["name"]
        return redirect(url_for('success', name=name))
    else:
        # Access URL arguments
        name = request.args.get('name')
        return redirect(url_for('success', name=name))


# Invoked after /login route to welcome user
@app.route('/success/<name>')
def success(name):
    return "welcome " + name


# This will just make the Flask app run on the server if current module is the main one
if __name__ == '__main__':
    """
    App.run can take following params:
    Host : The server machine on which it will run (127.0.0.1)
    Port : The port on the server machine to be used for handling HTTP requests by Flask (5000
    Option : To be forwarded to underlying server
    debug : Set it to True to begin Flask app in Debug mode where basically the server will reload itself 
            if code changes along with some debugging features
    """
    app.run(debug=True)
