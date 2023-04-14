from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService
    }
    SERVICE_NAMES = []

    VALID_ROBOTS = {
        "FemaleRobot": FemaleRobot,
        "MaleRobot": MaleRobot
    }
    ROBOTS_NAMES = []

    def __init__(self):
        self.robots = []
        self.services = []

    def get_service_by_name(self, name):
        return [s for s in self.services if s.name == name][0]

    def add_service(self, service_type, name):
        if service_type not in self.VALID_SERVICES:
            raise Exception("Invalid service type!")

        if name not in self.SERVICE_NAMES:
            service = self.VALID_SERVICES[service_type](name)
            self.services.append(service)
            self.SERVICE_NAMES.append(name)
            return f"{service_type} is successfully added."

    def add_robot(self, robot_type, name, kind, price):
        if robot_type not in self.VALID_ROBOTS:
            raise Exception("Invalid robot type!")

        if name not in self.ROBOTS_NAMES:
            robot = self.VALID_ROBOTS[robot_type](name, kind, price)
            self.robots.append(robot)
            self.ROBOTS_NAMES.append(name)
            return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name, service_name):
        robot = [r for r in self.robots if r.name == robot_name][0]
        service = self.get_service_by_name(service_name)
        if not robot.__class__.__name__ == "FemaleRobot" and service.__class__.__name__ == "SecondaryService" or \
                not robot.__class__.__name__ == "MaleRobot" and service.__class__.__name__ == "MainService":
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        service.robots.append(robot)
        self.robots.remove(robot)
        self.ROBOTS_NAMES.remove(robot_name)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name, service_name):
        service = self.get_service_by_name(service_name)
        for robot in service.robots:
            if robot.name == robot_name:
                self.add_robot(robot.__class__.__name__, robot.name, robot.kind, robot.price)
                service.robots.remove(robot)
                return f"Successfully removed {robot_name} from {service_name}."
        else:
            raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name):
        service = self.get_service_by_name(service_name)
        for robot in service.robots:
            robot.eating()
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name):
        service = self.get_service_by_name(service_name)
        total_price = 0
        for robot in service.robots:
            total_price += robot.price
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        return '\n'.join(s.details() for s in self.services)