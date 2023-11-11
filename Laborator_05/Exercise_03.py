'''
Create a base class Vehicle with attributes like make, model, and year, and then create subclasses
for specific types of vehicles like Car, Motorcycle, and Truck.
Add methods to calculate mileage or towing capacity based on the vehicle type.
'''
from datetime import datetime


class Vehicle: #considering that vehicles are gas powered, if not, we should add a new class ElectricVehicle, HybridVehicle
    existing_id = set()
    def __init__(self, id, make, model, year, colour, type_of_comustible, volume_of_fuel, current_fuel_level, itp_expiry_date, weight):
        if id in Vehicle.existing_id:
            raise ValueError(f"The id {id} is already used.")
        self.id = id
        Vehicle.existing_id.add(id)
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        self.type_of_comustible = type_of_comustible
        self.volume_of_fuel = volume_of_fuel
        self.current_fuel_level = current_fuel_level
        self.itp_expiry_date = itp_expiry_date
        self.weight = weight

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_make(self, make):
        self.make = make

    def get_make(self):
        return self.make

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_colour(self, colour):
        self.colour = colour

    def get_colour(self):
        return self.colour

    def set_type_of_car(self, type_of_car):
        self.type_of_car = type_of_car

    def get_type_of_car(self):
        return self.type_of_car

    def set_type_of_comustible(self, type_of_comustible):
        self.type_of_comustible = type_of_comustible

    def get_type_of_comustible(self):
        return self.type_of_comustible

    def set_volume_of_fuel(self, volume_of_fuel):
        self.volume_of_fuel = volume_of_fuel

    def get_volume_of_fuel(self):
        return self.volume_of_fuel

    def set_current_fuel_level(self, current_fuel_level):
        self.current_fuel_level = current_fuel_level

    def get_current_fuel_level(self):
        return self.current_fuel_level

    def set_itp_expiry_date(self, itp_expiry_date):
        self.itp_expiry_date = itp_expiry_date

    def get_itp_expiry_date(self):
        return self.itp_expiry_date

    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight

    def estimate_mileage(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def estimate_towing_capacity(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def check_itp_status(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def add_comustible(self, type_of_comustible, volume_of_fuel):
        if type_of_comustible != self.type_of_comustible:
            raise ValueError("Wrong type of comustible")
        if self.current_fuel_level + volume_of_fuel > self.volume_of_fuel:
            raise ValueError("Too much fuel")
        self.current_fuel_level += volume_of_fuel

    def fuel_efficiency_mileage(self, inital_fuel_level, final_full_level, distance_travelled):
        return (final_full_level - inital_fuel_level) / distance_travelled


class Car(Vehicle):
    def __init__(self, id, make, model, year, colour, type_of_comustible, volume_of_fuel, current_fuel_level, itp_expiry_date, weight, engine_power):
        super().__init__(id, make, model, year, colour, type_of_comustible, volume_of_fuel, current_fuel_level, itp_expiry_date, weight)
        self.engine_power = engine_power

    def estimate_mileage(self):
        current_year = datetime.now().year
        return 13000 * (current_year - self.year) # Assuming an average of 13,000 miles per year

    def estimate_towing_capacity(self):
        return min(self.engine_power * 2, self.weight * 1.5)

    def check_itp_status(self):
        if not self.itp_expiry_date:
            return "ITP status not applicable"

        expiry_date = datetime.strptime(self.itp_expiry_date, "%Y-%m-%d")
        today = datetime.now()

        if today > expiry_date:
            return "ITP expired. Maintenance checkups for cars would include engine health, oil levels, brake pads, tire condition, and suspension system."
        elif (expiry_date - today).days <= 30:
            return "ITP expiring soon"
        else:
            return "ITP valid"


class Motorcycle(Vehicle):
    def __init__(self, id, make, model, year, colour, type_of_comustible, volume_of_fuel, current_fuel_level, itp_expiry_date, weight):
        super().__init__(id, make, model, year, colour, type_of_comustible, volume_of_fuel, current_fuel_level, itp_expiry_date, weight)

    def estimate_mileage(self):
        current_year = datetime.now().year
        return 4000 * (current_year - self.year)  # Assuming an average of 4,000 miles per year

    def estimate_towing_capacity(self):
        return self.weight * 1.5

    def check_itp_status(self):
        if not self.itp_expiry_date:
            return "ITP status not applicable"

        expiry_date = datetime.strptime(self.itp_expiry_date, "%Y-%m-%d")
        today = datetime.now()

        if today > expiry_date:
            return "ITP expired. For motorcycles, maintenance focuses more on aspects like chain tension, tire pressure and tread, brake fluid levels, and engine oil."
        elif (expiry_date - today).days <= 30:
            return "ITP expiring soon"
        else:
            return "ITP valid"


class Truck(Vehicle):

    def __init__(self, id, make, model, year, colour, type_of_comustible, volume_of_fuel, current_fuel_level, itp_expiry_date, weight, engine_size):
        super().__init__(id, make, model, year, colour, type_of_comustible, volume_of_fuel, current_fuel_level, itp_expiry_date, weight)
        self.engine_size = engine_size

    def estimate_mileage(self):
        current_year = datetime.now().year
        return 6000 * (current_year - self.year)  # Assuming an average of 6,000 miles per year

    def estimate_towing_capacity(self):
        return min(self.engine_size * 5, self.weight * 1.5)

    def check_itp_status(self):
        if not self.itp_expiry_date:
            return "ITP status not applicable"

        expiry_date = datetime.strptime(self.itp_expiry_date, "%Y-%m-%d")
        today = datetime.now()

        if today > expiry_date:
            return "ITP expired.Truck maintenance involves checking the engine for heavy-duty performance, transmission systems, cargo-related components, and more robust brake systems."
        elif (expiry_date - today).days <= 30:
            return "ITP expiring soon"
        else:
            return "ITP valid"