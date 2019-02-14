from account_service.domain.errors import CustomerNotFound


def get_account(account_number, account_repository):
    return account_repository.fetch_by_account_number(account_number)


def create_account(account, account_repository, customer_client):
    if not customer_client.has_customer_with_id(account.customer_id):
        raise CustomerNotFound()

    account_repository.store(account)


def close_account(account_number, account_repository):
    account = account_repository.fetch_by_account_number(account_number)
    account.account_status = 'closed'
    account_repository.store(account)
