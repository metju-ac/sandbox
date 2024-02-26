import sys

def main(a, b, c, d, params):
    params = eval(params)
    print(params)
    print(a)
    print(b)
    print(c)
    print(d)

    with open(a) as f:
        print(f.readlines())


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])