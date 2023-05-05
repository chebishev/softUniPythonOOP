class System:
    def __init__(self):
        self._hardware = []
        self._software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        ...

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        ...

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        ...

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        ...

    @staticmethod
    def release_software_component(hardware_name, software_name):
        ...

    @staticmethod
    def analyze():
        ...

    @staticmethod
    def system_split():
        ...
