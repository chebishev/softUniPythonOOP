class EthernetConnector:
    def connect_device_via_ethernet_cable(self, device):
        pass


class PowerConnector:
    def connect_device_to_power_outlet(self):
        pass


class HDMIConnector:
    def connect_device_to_hdmi_outlet(self, device):
        pass


class RCAConnector:
    def connect_device_to_rca_outlet(self, device):
        pass


class InternetEnabled(EthernetConnector):
    def connect_device_via_ethernet_cable(self, device):
        self.connect_device_via_ethernet_cable(device)


class EntertainmentDevice(PowerConnector):
    def plug_in_power(self):
        self.connect_device_to_power_outlet()


class DVDPlayer(EntertainmentDevice, RCAConnector):

    def connect_to_tv(self, television):
        self.connect_device_to_rca_outlet(television)


class Router(EntertainmentDevice, InternetEnabled, EthernetConnector):
    def connect_to_tv(self, television):
        self.connect_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_device_via_ethernet_cable(game_console)


class Television(EntertainmentDevice, InternetEnabled, HDMIConnector, EthernetConnector, RCAConnector):
    def connect_to_dvd(self, dvd_player):
        self.connect_device_to_rca_outlet(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_device_to_hdmi_outlet(game_console)


class GameConsole(EntertainmentDevice, InternetEnabled, HDMIConnector):
    def connect_to_tv(self, television):
        self.connect_device_to_hdmi_outlet(television)

