import db


def header():
    print('---Library App---')
    print('')


def show_log(data):

    if data:
        for idx, entry in enumerate(data):
            print(f'{idx+1}. {entry}')

        # TODO: picked_entry = input('Pick an entry (book name): ')

    else:
        print('No entries.')


def make_an_entry(data):
    entry = input('Write about the book, [x] to exit: \n')

    if entry == 'x':
        return

    db.add_entry(entry, data)
