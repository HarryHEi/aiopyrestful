class ValidationError(BaseException):
    def __init__(self, detail=''):
        self.detail = detail
