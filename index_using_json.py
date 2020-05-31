from difflib import get_close_matches
import json
import os.path
import sys


def translate(data, word):
    low_word = word.lower()
    if low_word in data:
        return data[low_word]
    elif len(get_close_matches(low_word, data.keys())) > 0:
        user_confirm = input( 'Did you mean \'%s\' instead. [Y/N]' % get_close_matches(low_word, data.keys())[0])
        if user_confirm.lower() == 'y':
            return data[get_close_matches(low_word, data.keys())[0]]
        else:
            return 'Word not found'
    else:
        return 'Word does not exist.'


def open_json(filename):
    return json.load(open(filename))


def main():
    file = input('Enter the file name to be opened')
    if os.path.exists(file):
        data = open_json(file)
        while True:
            # print(data.keys())
            word = input("Enter word: ")
            result = translate(data, word)
            if type(result) == list:
                for line in result:
                    print(line)
            else:
                print(result)

            cont_option = input('Do you need to search other word [Y/N]:')
            if cont_option.lower() == 'y':
                continue
            else:
                sys.exit(0)
    else:
        print('Wrong filename')


if __name__ == '__main__':
    main()
