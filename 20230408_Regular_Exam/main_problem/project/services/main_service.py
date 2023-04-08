from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name, capacity=30):
        super().__init__(name, capacity)

    def details(self):
        result = [f"{self.name} Main Service:"]
        if not self.robots:
            result.append("Robots: none")
        else:
            result.append(f"Robots: {' '.join(robot.name for robot in self.robots)}")
        return '\n'.join(result)
