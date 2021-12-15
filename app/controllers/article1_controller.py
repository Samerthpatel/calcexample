"""index controller"""

from flask import render_template
from app.controllers.controller import ControllerBase

    # pylint: disable=invalid-name
class article1controller(ControllerBase):
    """index controller"""

    @staticmethod
    def get():
        """index controller"""

        return render_template('article1.html')
