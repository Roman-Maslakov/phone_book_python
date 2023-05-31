phone_book: list[dict[str, str]] = []
path = 'phone_book/book.txt'

def open_pb():
    global phone_book, path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for contact in data:
            contact = contact.strip().split(':')
            phone_book.append({'name':contact[0], 'phone':contact[1], 'comment':contact[2]})

def save_pb():
    global phone_book, path
    data = []
    for contact in phone_book:
        contact = ':'.join([value for value in contact.values()])
        data.append(contact)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(data))

def get_pb() -> list[dict[str, str]]:
    global phone_book
    return phone_book

def add_contact(contact: dict[str, str]):
    global phone_book
    phone_book.append(contact)
    name = contact.get('name')
    return name

def delete_contact(index: int):
    global phone_book
    return phone_book.pop(index-1).get('name')

def change_contact(index: int, changes: dict):
    global phone_book
    name = phone_book.pop(index-1).get('name')
    phone_book.insert(index-1, changes)
    return name

def search_contact(search: str):
    global phone_book
    search_result = []
    for contact in phone_book:
        search_data = ' '.join(contact.values())
        if search in search_data:
            search_result.append(contact)
    return search_result