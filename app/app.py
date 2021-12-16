"""A simple flask web app"""
from flask import Flask
from werkzeug.debug import DebuggedApplication

from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.article1_controller import article1controller
from app.controllers.article2_controller import article2controller
from app.controllers.article3_controller import article3controller
from app.controllers.article4_controller import article4controller
from app.controllers.git_controller import GitController
from app.controllers.docker_controller import DockerController
from app.controllers.terminal_controller import TerminalController
from app.controllers.vi_controller import ViController
from app.controllers.history_controller import HistoryController
from app.controllers.result_controller import ResultController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# pylint: disable=undefined-variable
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

@app.route("/", methods=['GET'])
def index_get():
    """A simple flask web app"""

    return IndexController.get()

@app.route("/article1", methods=['GET'])
def article1_get():
    """A simple flask web app"""

    return article1controller.get()

@app.route("/article2", methods=['GET'])
def article2_get():
    """A simple flask web app"""

    return article2controller.get()

@app.route("/article3", methods=['GET'])
def article3_get():
    """A simple flask web app"""

    return article3controller.get()

@app.route("/article4", methods=['GET'])
def article4_get():
    """A simple flask web app"""

    return article4controller.get()

@app.route("/git", methods=['GET'])
def git_get():
    """A simple flask web app"""

    return GitController.get()

@app.route("/docker", methods=['GET'])
def docker_get():
    """A simple flask web app"""

    return DockerController.get()

@app.route("/terminal", methods=['GET'])
def terminal_get():
    """A simple flask web app"""

    return TerminalController.get()

@app.route("/vi", methods=['GET'])
def vi_get():
    """A simple flask web app"""

    return ViController.get()

@app.route("/history", methods=['GET'])
def history_get():
    """A simple flask web app"""

    return HistoryController.get()

@app.route("/result", methods=['GET'])
def result_get():
    """A simple flask web app"""

    return ResultController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    """A simple flask web app"""

    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    """A simple flask web app"""

    return CalculatorController.post()
