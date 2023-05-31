import view, model, text

def start():
    view.print_message(text.welcome)
    while True:
        choice = view.main_menu()
        match choice:
            case 1 :
                model.open_pb()
                view.print_message(text.loading_successful)
            case 2 :
                model.save_pb()
                view.print_message(text.save_successful)
            case 3 :
                pb = model.get_pb()
                view.print_contact(pb, text.load_error)
            case 4 :
                contact = view.input_contact(text.new_contact, text.cancel_input)
                name = model.add_contact(contact)
                view.print_message(text.new_contact_succeed(name))
            case 5 :
                pb = model.get_pb()
                index = view.input_index(text.index_del_contact, pb, text.load_error)
                name = model.delete_contact(index)
                view.print_message(text.del_contact(name))
            case 6 :
                search_request = view.search(text.search)
                search_result = model.search_contact(search_request)
                view.print_contact(search_result, text.search_error)
            case 7 :
                pb = model.get_pb()
                index = view.input_index(text.index_del_contact, pb, text.load_error)
                changes = view.input_contact(text.change_contact, text.load_error)
                name = model.change_contact(index, changes)
                view.print_message(text.changes_succeed(name))
            case 8 :
                view.print_message(text.goodbye)
                break