def main():
    f = None
    try:
        f = open('./test.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('文件不存在')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时编码错误')
    finally:
        if f:
            f.close()


if __name__ == '__main__':
    main()
