from russian_names import RussianNames


def print_names():
    count = int(input("Введите количество имен для вывода: "))
    for i in range(count):
        print(f'[{i+1}] ' + RussianNames().get_person())


if __name__ == '__main__':
    print_names()
