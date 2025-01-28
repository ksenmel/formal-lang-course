class InterpreterException(Exception):
    def __init__(self, msg: str):
        self.msg = msg


class VariableNotFoundException(InterpreterException):
    """
    Raises if variable is not found in the scope
    """

    def __init__(self, name: str):
        self.msg = f"Variable name '{name}' is not defined in the scope"


class VariableAlreadyExists(InterpreterException):
    """
    Raises if variable is already exists in the scope
    """

    def __init__(self, name: str):
        self.msg = f"Variable '{name}' already exists"


class InvalidType(InterpreterException):
    """
    Raises if type in not in Types
    """

    def __init__(self, typ: str):
        self.msg = f"Type '{typ}' doesn't exist"


class TypeMismatch(InterpreterException):
    """
    Raises types are not equal
    """

    def __init__(self, expected, actual):
        self.msg = f"Type mismatch: expected {expected}, got {actual}"


class UnsupportedOperation(InterpreterException):
    """
    Raises when this operation is not supported
    """

    def __init__(self):
        self.msg = "Unsupported operation"


class UnsupportedConstruction(InterpreterException):
    """
    Raises when this construction is not supported
    """

    def __init__(self, name):
        self.msg = f"Unsupported construction {name}"
