import json


def main():
    mydict = {
        'name': 'kirintang',
        'age': 27,
        'friend': ['张三', '李四'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_spedd': 280},
            {'brand': 'BMW', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 300}
        ]
    }
    try:
        with open('profile.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('success')


if __name__ == '__main__':
    main()
