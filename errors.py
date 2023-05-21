class InvalidModeException(Exception):
    def __init__(self):
        self.message = "This mode is invalid. Please input correct mode ('l' or 'w')"
        super().__init__(self.message)


class InvalidNumbersException(Exception):
    def __init__(self):
        self.message = "Given numbers are invalid. Please input correct numbers"
        super().__init__(self.message)