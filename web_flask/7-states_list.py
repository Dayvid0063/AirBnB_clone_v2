#!/usr/bin/python3
"""starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays states list sorted by name"""
    states = storage.all("State").values()
    sorted_state = sorted_state(states, key=lambda state: state.name)
    return render_template("7-states_list.html", sorted_state=sorted_state)


@app.teardown_appcontext
def teardown(exception):
    """Closes the session after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
