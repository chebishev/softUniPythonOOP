from project.clients.base_client import BaseClient


class Adult(BaseClient):
    PERCENTAGE = 2

    def __init__(self, name, client_id, income, interest=4.0):
        super().__init__(name, client_id, income, interest)

    def increase_clients_interest(self):
        self.interest += self.PERCENTAGE
        return self.interest
