class Appliance:
    MONTH = 30

    def __init__(self, cost):
        self.cost = cost

    def get_monthly_expense(self):
        return self.cost * self.MONTH
