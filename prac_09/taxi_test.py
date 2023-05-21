from prac_09.taxi import Taxi


def main():
    """The main function of the script that demonstrates the functionality of the Taxi class"""
    my_taxi = Taxi("Prius 1", 100, 1.23)
    my_taxi.drive(40)
    print(my_taxi)
    print("Current fare: $" + str(my_taxi.get_fare()))
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print("Current fare: $" + str(my_taxi.get_fare()))


main()

