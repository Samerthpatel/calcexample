"""index controller"""

from flask import render_template
from app.controllers.controller import ControllerBase

class IndexController(ControllerBase):
    """index controller"""

    @staticmethod
    def get():
        """index controller"""

        return render_template('index.html')
