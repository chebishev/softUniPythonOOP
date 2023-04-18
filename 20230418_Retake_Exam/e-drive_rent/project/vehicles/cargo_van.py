from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180

    def __init__(self, brand, model, license_plate_number):
        super().__init__(brand, model, license_plate_number, self.get_max_mileage)

    @property
    def get_max_mileage(self):
        return self.MAX_MILEAGE

    def drive(self, mileage):
        percentage_to_reduce = round(mileage / self.get_max_mileage * 100)
        percentage_to_reduce += 5  # TODO 0.05 from the battery as alternative to 5%
        self.battery_level -= percentage_to_reduce
