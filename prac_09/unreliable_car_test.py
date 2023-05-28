from prac_09.unreliable_car import UnreliableCar


def main():
    """The main function of the script. """
    my_car = UnreliableCar("UnreliableCar", 100, 50)

    driven = my_car.drive(50)
    print(f"The car drove {driven} km.")
    print(my_car)

    driven = my_car.drive(50)
    print(f"The car drove {driven} km.")

    print(my_car)


main()
