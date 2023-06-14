import random
import json
import uuid
import sys
from num_random import generate_number

with open("currencies_list.json") as jsonfile:
    currencies_list = json.load(jsonfile)


def generate_client_list(length):
    client_list = []

    for i in range(length):
        _uuid = uuid.uuid4()
        client_id = str(_uuid)  # User IDs start from '1'
        num_tokens_accounts = random.randint(1, 10)  # Generate a random number between 1 and 10

        accounts = []

        for j in range(num_tokens_accounts):
            random_token = random.randint(0, len(currencies_list)-1)
            token_list = currencies_list[random_token]
            token_name = token_list[0]
            account_tokens = generate_number(token_list[1], token_list[2], currency=token_name)  # Generate a random number between 1e-9 and 1e9

            accounts.append((token_name, account_tokens))

        client_data = {
            client_id: accounts,
        }

        client_list.append(client_data)

    return client_list

def run ():
    # Check if an argument is provided
    if len(sys.argv) > 1:
        # Get the value from the command-line argument
        arg = sys.argv[1]

        # Call the function with the argument
        client_list = generate_client_list(int(arg))
    else:
        client_list = generate_client_list(10000)

    with open("client_list.json", "w") as jsonfile:
        json.dump(client_list, jsonfile)
    return client_list
run()