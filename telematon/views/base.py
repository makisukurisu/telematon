import logging

from flask import request
from flask.views import View

from telematon.utils import ErrorMessage


class BaseJSONView(View):
    json_data: object = None

    def _check_json(self):
        self.json_data = request.get_json(force=True, silent=True)

    def process_data(self):
        raise NotImplementedError("process_data method must be implemented in subclass")

    def dispatch_request(self):
        self._check_json()
        if not self.json_data:
            logging.warning(ErrorMessage("No JSON provided, or is empty", request))
            return {
                "message": "No JSON provided, or is empty",
                "status": "error",
            }, 400
        return self.process_data()
