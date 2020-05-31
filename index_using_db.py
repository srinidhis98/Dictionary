from difflib import get_close_matches
import mysql.connector
import sys


def copy_contents_to_file(new_dict):
    with open('data_dic.txt', 'w') as file:
        sys.stdout = file
        for key, item in new_dict.items():
            print(f'{key}: {item}')
        sys.stdout = sys.__stdout__


def translate(data, word):
    low_word = word.lower()
    for key, value in data.items():
        if low_word == key.lower():
            return data[key]

        else:
            continue

    else:
        if len(get_close_matches(low_word, data.keys())) > 0:
            user_confirm = input('Did you mean \'%s\' instead. [Y/N]' % get_close_matches(low_word, data.keys())[0])
            if user_confirm.lower() == 'y':
                return data[get_close_matches(low_word, data.keys())[0]]
            else:
                return 'Word not found'


def server_connect():
    connection = mysql.connector.connect(
        user='ardit700_student',
        password='ardit700_student',
        host='108.167.140.122',
        database='ardit700_pm1database'
    )

    cursor = connection.cursor()
    disp_all = cursor.execute('SELECT * FROM Dictionary')
    full_dictionary = cursor.fetchall()
    return full_dictionary


def main():
    full_dict = server_connect()
    new_dict = dict(full_dict)
    while True:
        choice = input(f'1. Copy the contents of db to file\n2. Translate Word\n3. Exit')
        if choice == '1':
            copy_contents_to_file(new_dict)
            continue
        elif choice == '2':
            word = input('Enter word: ')
            result = translate(new_dict, word)
            print(result)
            continue
        elif choice == '3':
            sys.exit(0)


if __name__ == '__main__':
    main()
