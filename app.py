from flask import Flask
from flask_injector import FlaskInjector
from controllers.account_controller import account_bp
from services.account_service import AccountService
from repositories.account_repository import AccountRepository
from injector import Binder
from utils.exceptions import InsufficientFundsError, AccountNotFoundError, DuplicateAccountError, handle_api_error

def configure(binder: Binder):
    binder.bind(AccountService, to=AccountService(AccountRepository()), scope=None)

app = Flask(__name__)
app.register_blueprint(account_bp)

# Register error handlers
app.register_error_handler(InsufficientFundsError, handle_api_error)
app.register_error_handler(AccountNotFoundError, handle_api_error)
app.register_error_handler(DuplicateAccountError, handle_api_error)

FlaskInjector(app=app, modules=[configure])

if __name__ == '__main__':
    app.run(debug=True)
