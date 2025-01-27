class RunTimeException(Exception):
    """
    Base exception for Interpreter
    """

    def __init__(self, message: str):
        self.message = message
