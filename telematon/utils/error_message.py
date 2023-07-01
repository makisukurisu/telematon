class ErrorMessage:
    def __init__(self, message: str, *args):
        self.message = message
        self.args = args

    def __str__(self) -> str:
        return " ".join([self.message, str(self.args)])
