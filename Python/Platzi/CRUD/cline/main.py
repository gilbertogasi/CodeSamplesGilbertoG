import sys


clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software enginerr',
    },
    {
        'name': 'Ricardo',
        'company':'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data engineer',
    }
]


def create_client(client):
    global clients


    if client not in clients:
        clients.append(client)
    else:
        print('Client alredy is in the client\'s list')


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('what is the client {}? '.format(field_name))

    return field


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name? ')

        if client_name.lower() == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
                uid = idx,
                name = client['name'],
                company = client['company'],
                email = client['email'],
                position = client['position']))


def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_client_name
    else:
        print('Client is not in clients list')


def delete_client(index):
    global clients

    try:
        del clients[index]
    except IndexError:
        print('Client is not in clients list')


def search_client(client_name):
    for client in clients:
        if client != client_name:
            continue
        else:
            return True


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = {
                 'name': _get_client_field('name'),
                 'company': _get_client_field('company'),
                 'email': _get_client_field('email'),
                 'position': _get_client_field('position'),
                }
        #client_name = _get_client_name()
        create_client(client)
        list_clients()
    if command == 'L':
        list_clients()
    elif command == 'D':
        list_clients()
        print('')
        index = int(input('please, digit the id of client for delete: '))
        print('')
        #client_name = _get_client_name()
        delete_client(index)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name? ')
        update_client(client_name, updated_client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our clients list'.format(client_name))

        list_clients()
    else:
        print('Invalid command')

