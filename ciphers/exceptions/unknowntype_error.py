class UnknownTypeError(Exception):
    def __init__(self, obj, message):
        self.obj = obj
        self.message = message

    def __str__(self):
        return self.message

