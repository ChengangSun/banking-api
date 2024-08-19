from flask import Blueprint, request, jsonify
from injector import inject
from models.dto import CreateAccountDTO, TransferFundsDTO
from services.account_service import AccountService
from utils.exceptions import InsufficientFundsError, AccountNotFoundError
from marshmallow import ValidationError, Schema, fields

account_bp = Blueprint('account', __name__)

# Define input schemas using Marshmallow
class CreateAccountSchema(Schema):
    account_id = fields.Str(required=True)
    initial_balance = fields.Float(required=True, validate=lambda x: x >= 0)

class TransferFundsSchema(Schema):
    from_account_id = fields.Str(required=True)
    to_account_id = fields.Str(required=True)
    amount = fields.Float(required=True, validate=lambda x: x > 0)

@inject
@account_bp.route('/accounts', methods=['POST'])
def create_account(account_service: AccountService):
    schema = CreateAccountSchema()
    try:
        data = schema.load(request.get_json())
        dto = CreateAccountDTO(**data)
        account_service.create_account(dto.account_id, dto.initial_balance)
        return jsonify({'message': 'Account created successfully'}), 201
    except ValidationError as e:
        return jsonify({'error': e.messages}), 400

@inject
@account_bp.route('/accounts/transfer', methods=['POST'])
def transfer_funds(account_service: AccountService):
    schema = TransferFundsSchema()
    try:
        data = schema.load(request.get_json())
        dto = TransferFundsDTO(**data)
        account_service.transfer_funds(dto.from_account_id, dto.to_account_id, dto.amount)
        return jsonify({'message': 'Transfer successful'}), 200
    except ValidationError as e:
        return jsonify({'error': e.messages}), 400
    except (InsufficientFundsError, AccountNotFoundError) as e:
        return jsonify({'error': str(e)}), 400

@inject
@account_bp.route('/accounts/<account_id>/transactions', methods=['GET'])
def get_transaction_history(account_id, account_service: AccountService):
    transactions = account_service.get_transaction_history(account_id)
    return jsonify([transaction.__dict__ for transaction in transactions]), 200
