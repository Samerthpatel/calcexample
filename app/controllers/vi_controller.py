"""index controller"""

from flask import render_template
from app.controllers.controller import ControllerBase

    # pylint: disable=invalid-name
class ViController(ControllerBase):
    """index controller"""

    @staticmethod
    def get():
        """index controller"""

        return render_template('vi.html')