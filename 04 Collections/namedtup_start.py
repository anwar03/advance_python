# Demonstrate the usage of namdtuple objects

import collections


def main():
    # TODO: create a Point namedtuple
    point = collections.namedtuple("Points", "x y")
    # TODO: use _replace to create a new instance
    p1 = point(10, 20)
    p2 = point(20, 30)

    print(p1, p2)
    print(p1.x, p2.x)

if __name__ == "__main__":
    main()
