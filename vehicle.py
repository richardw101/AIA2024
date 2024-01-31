class Vehicle:
    """
    Vehicle: a thing used for transporting people or goods, especially on land
    """
    def __init__(self, year=2022, color='Red', wheel_count=2):
        self.__year = year
        self.__color = color
        self.__wheel_count = wheel_count
        return
    
    def __str__(self):
        return f'{self.__year} {self.__color} {self.__wheel_count} wheel Vehicle'

    def get_color(self):
        return self.__color
    
class Car(Vehicle):
    """
    A special vehicle.
    """
    def __init__(self, make, model, color, odometer=0, year=2022):
        super().__init__(year=year, color=color, wheel_count=4)
        self.__make = make
        self.__model = model
        self.__odometer = odometer
        return

    def __str__(self):
        base = super().__str__()
        sub = f'{self.__make} {self.__model} Car with {self.__odometer} miles'
        result = f'{sub} which is also a {base}'
        return result
    
    def __increment_odometer(self, miles):
        self.__odometer += miles
        return self.__odometer
    
    def get_odometer(self):
        return self.__odometer

    def drive(self, miles):
        self.__increment_odometer(miles)
        return