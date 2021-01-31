import random


def cinema(rows, seats):
    return [[random.random() < 0.5 for i in range(seats)] for j in range(rows)]


def free_seats(cinema, quantity):
    assert(quantity < 31)
    assert(quantity > 0)
    result = 0
    for ir, row in enumerate(cinema):
        seats = 0
        for ip, place in enumerate(row):
            if(place):
                seats += 1
            else:
                seats = 0
            if(quantity == seats):
                return (f"{ir+1}{ip-quantity+2:02}")
    return result


def print_cinema(cinema):
    for row in cinema:
        for seat in row:
            print(f"%s\t" % (seat), end='')
        print()


cine = cinema(10, 30)
print_cinema(cine)
print(free_seats(cine, 6))
