from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def index():
    """ Return homepage. """
    return render_template("index.html")

@app.route("/application-form")
def show_application_form():
    """ Return application form. """

    open_positions = ["Software Engineer", "QA Engineer", "Product Manager"]

    return render_template("application-form.html", open_positions=open_positions)

@app.route("/application-response", methods=["POST"])
def show_application_response():
    """ Return application response. """

    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    salary = request.form.get("salary-req")
    position = request.form.get("position_choice")
    salary = float(salary)

    return render_template("application-response.html", first_name=first_name, 
                            last_name=last_name, salary=salary, position=position)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
