# Banking Transactions API

## Overview

This project is a simple banking transactions API that allows users to create accounts, transfer funds between accounts, and retrieve transaction histories. The API is built using Python and Flask and follows a three-layer architecture consisting of Controllers, Services, and Repositories. Dependency Injection is used to manage the service and repository layers.

## Requirements

- Python 3.9.6
- Flask
- Flask-Injector

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ChengangSun/banking-api.git
cd banking-api
python app.py
```

## Endpoints

1. **Create a New Account**
    - `POST /accounts`
    - Body: `{ "account_id": "123", "initial_balance": 1000.0 }`
    - Response: `{ "message": "Account created successfully" }`

2. **Transfer Funds**
    - `POST /accounts/transfer`
    - Body: `{ "from_account_id": "123", "to_account_id": "456", "amount": 100.0 }`
    - Response: `{ "message": "Transfer successful" }`

3. **Get Transaction History**
    - `GET /accounts/{account_id}/transactions`
    - Response: `[ { "from_account_id": "123", "to_account_id": "456", "amount": 100.0 }, ... ]`

##  Using cURL to Test the API

1. **Create a New Account**

```bash
curl -X POST http://127.0.0.1:5000/accounts -H "Content-Type: application/json" -d '{"account_id": "123", "initial_balance": 1000.0}'
```

2. **Transfer Funds**

First, create a second account:

```bash
curl -X POST http://127.0.0.1:5000/accounts -H "Content-Type: application/json" -d '{"account_id": "456", "initial_balance": 500.0}'
```

Then, transfer funds between the two accounts:

```bash
curl -X POST http://127.0.0.1:5000/accounts/transfer -H "Content-Type: application/json" -d '{"from_account_id": "123", "to_account_id": "456", "amount": 100.0}'
```

3. **Get Transaction History**

```bash
curl http://127.0.0.1:5000/accounts/123/transactions
```

4. **Error Handling Test**

```bash
curl -X POST http://127.0.0.1:5000/accounts/transfer -H "Content-Type: application/json" -d '{"from_account_id": "123", "to_account_id": "456", "amount": 10000.0}'
```

```bash
curl -X POST http://127.0.0.1:5000/accounts -H "Content-Type: application/json" -d '{"account_id": "456", "initial_balance": 500.0}'
```

```bash
curl http://127.0.0.1:5000/accounts/789/transactions
```

# Assumptions Made During Implementation

1. In-Memory Storage: The app uses in-memory storage (a simple Python dictionary) to store account and transaction data. This means that all data will be lost when the application is stopped. 

2. Unique Account IDs: It is assumed that account IDs are unique across the system. 

3. No Authentication: The API does not include any authentication or authorization mechanisms.

4. Simplified Error Handling: The API includes basic error handling for insufficient funds and invalid account IDs. Additional error cases (e.g., malformed requests) should be handled more robustly in a production environment.

# Future Improvements

1. Persistent Storage: Replace the in-memory storage with a persistent database.
2. Authentication: Add authentication and authorization to secure the API endpoints.
3. Improved Error Handling: Implement more robust error handling and input validation.
4. Testing: Add unit and integration tests to ensure the reliability of the application.


