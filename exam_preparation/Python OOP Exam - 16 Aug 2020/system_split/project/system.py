from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def get_hardware(name):
        return [h for h in System._hardware if h.name == name][0]

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        if not [h for h in System._hardware if h.name == hardware_name]:
            return "Hardware does not exist"

        hardware = System.get_hardware(hardware_name)
        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(express_software)
        System._software.append(express_software)

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        if not [h for h in System._hardware if h.name == hardware_name]:
            return "Hardware does not exist"

        hardware = System.get_hardware(hardware_name)
        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(light_software)
        System._software.append(light_software)

    @staticmethod
    def release_software_component(hardware_name, software_name):
        try:
            hardware = System.get_hardware(hardware_name)
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {sum([s.memory_consumption for s in System._software])} " \
               f"/ {sum([h.memory for h in System._hardware])}\n" \
               f"Total Capacity Taken: {sum([s.capacity_consumption for s in System._software])} " \
               f"/ {sum([h.capacity for h in System._hardware])}"

    @staticmethod
    def system_split():
        output = []
        for hardware_component in System._hardware:
            express_software = [s for s in hardware_component.software_components if s.software_type == "Express"]
            light_software = [s for s in hardware_component.software_components if s.software_type == "Light"]
            software_memory_usage = sum([s.memory_consumption for s in hardware_component.software_components])
            software_capacity_usage = sum([s.capacity_consumption for s in hardware_component.software_components])
            if hardware_component.software_components:
                software_components = ', '.join([s.name for s in hardware_component.software_components])
            else:
                software_components = 'None'
            output.append(f"Hardware Component - {hardware_component.name}\n"
                          f"Express Software Components: {len(express_software)}\n"
                          f"Light Software Components: {len(light_software)}\n"
                          f"Memory Usage: {software_memory_usage} / {hardware_component.memory}\n"
                          f"Capacity Usage: {software_capacity_usage} / {hardware_component.capacity}\n"
                          f"Type: {hardware_component.hardware_type}\n"
                          f"Software Components: {software_components}")
        return "\n".join(output)


System.register_power_hardware("HDD", 200, 200)
System.register_heavy_hardware("SSD", 400, 400)
print(System.analyze())
System.register_light_software("HDD", "Test", 0, 10)
System.register_express_software("HDD", "Test3", 50, 100)
System.register_light_software("SSD", "Windows", 20, 50)
System.register_express_software("SSD", "Linux", 50, 100)
System.register_light_software("SSD", "Unix", 20, 50)
print(System.analyze())
System.release_software_component("SSD", "Linux")
print(System.system_split())
