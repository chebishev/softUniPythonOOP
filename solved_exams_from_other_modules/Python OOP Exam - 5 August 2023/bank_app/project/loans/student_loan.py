from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    PERCENTAGE = 0.2
    INTEREST_RATE = 1.5
    AMOUNT = 2000.0

    def __init__(self):
        super().__init__(interest_rate=self.INTEREST_RATE, amount=self.AMOUNT)
