from behave import when


@when(u'I close the account with ID "{accountNumber:d}"')
def close_account(context, accountNumber):
    response = context.web_client.put(
        f'/accounts/close',
        json={'accountNumber': accountNumber})

    assert response.status_code == 200, response.status_code
