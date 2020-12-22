import os


def load(name):
    """
    This method creates and loads database.

    :param name: This base name to load.
    :return: A new data structure to populate file data.
    """
    data = []
    filename = get_full_path(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, data):
    filename = get_full_path(name)
    print(f'... saving to: {filename}')

    with open(filename, 'w') as fout:
        for entry in data:
            fout.write(entry + '\n')


def get_full_path(name):
    filename = os.path.abspath(os.path.join('.', 'book_libs', name + '.blb'))
    return filename


def add_entry(entry, data):
    data.append(entry)
