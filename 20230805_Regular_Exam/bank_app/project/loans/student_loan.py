from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    PERCENTAGE = 0.2
    INTEREST_RATE = 1.5
    AMOUNT = 2000.0

    def __init__(self, interest_rate=INTEREST_RATE, amount=AMOUNT):
        super().__init__(interest_rate, amount)

    def increase_interest_rate(self):
        self.interest_rate += self.PERCENTAGE
        return self.interest_rate
