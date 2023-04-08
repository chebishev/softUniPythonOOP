from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name, capacity=15):
        super().__init__(name, capacity)

    def details(self):
        # result = [f"{self.name} Secondary Service:"]
        # if not self.robots:
        #     result.append("Robots: none")
        # else:
        #     result.append(f"Robots: {' '.join(robot.name for robot in self.robots)}")
        # return '\n'.join(result)
        return f"{self.name} Secondary Service:\n" \
               f"Robots: {' '.join(robot.name for robot in self.robots) if self.robots else 'none'}"
