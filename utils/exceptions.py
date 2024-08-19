from flask import jsonify

class APIError(Exception):
    """Base class for all API exceptions."""
    status_code = 400
    default_message = 'A server error occurred.'

    def __init__(self, message=None, status_code=None):
        super().__init__(message)
        if status_code is not None:
            self.status_code = status_code
        self.message = message or self.default_message

    def to_dict(self):
        return {'error': self.message}

class InsufficientFundsError(APIError):
    status_code = 400
    default_message = 'Insufficient funds.'

class AccountNotFoundError(APIError):
    status_code = 404
    default_message = 'Account not found.'

class DuplicateAccountError(APIError):
    status_code = 400
    default_message = 'Account with the given ID already exists.'


def handle_api_error(e):
    response = jsonify(e.to_dict())
    response.status_code = e.status_code
    return response
