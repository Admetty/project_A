import time
import db
import functionality as func


def main_loop():

    print('Welcome! What would you like to do?')

    name = 'default'
    data = db.load(name)

    while True:
        player_input = input('\nShow entries: 1, Make an entry: 2, Exit: 3.\n')

        if player_input == '1':
            func.show_log(data)
        elif player_input == '2':
            func.make_an_entry(data)
        elif player_input == '3':
            db.save(name, data)
            print('Exiting ~~')
            time.sleep(1)
            return
        else:
            print('Input invalid. Try again')


def main():
    func.header()
    main_loop()


if __name__ == '__main__':
    main()
