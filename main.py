from vehicle import Vehicle, Car
    
old_vehicle = Vehicle(year=2021, color='Silver', wheel_count=4)
print(old_vehicle)

new_car = Car('Nissan', 'Versa', 'Red', odometer=15)
print(new_car)

print(new_car.get_color())

# method resolution order
print(Car.__mro__)
