from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    valid_loans = {
        'StudentLoan': StudentLoan,
        'MortgageLoan': MortgageLoan
    }
    valid_clients = {
        'Student': Student,
        'Adult': Adult
    }
    valid_client_loan = {
        "StudentLoan": "Student",
        "MortgageLoan": "Adult"
    }
    GRANTED_LOANS = 0
    GRANTED_SUM = 0

    def __init__(self, capacity):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type):
        if loan_type not in self.valid_loans:
            raise Exception("Invalid loan type!")

        self.loans.append(self.valid_loans[loan_type]())
        return f"{loan_type} was successfully added."

    def add_client(self, client_type, client_name, client_id, income):
        if client_type not in self.valid_clients:
            raise Exception("Invalid client type!")
        if self.capacity == len(self.clients):
            raise Exception("Not enough bank capacity.")
        self.clients.append(self.valid_clients[client_type](client_name, client_id, income))
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type, client_id):
        loan = [loan for loan in self.loans if loan.__class__.__name__ == loan_type][0]
        client = [client for client in self.clients if client.client_id == client_id][0]
        for client_loan in self.valid_client_loan:
            if loan_type == client_loan and client.__class__.__name__ == self.valid_client_loan[client_loan]:
                self.loans.remove(loan)
                client.loans.append(loan)
                BankApp.GRANTED_LOANS += 1
                BankApp.GRANTED_SUM += loan.amount
                return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."
        else:
            raise Exception("Inappropriate loan type!")

    def remove_client(self, client_id):
        try:
            client = [client for client in self.clients if client.client_id == client_id][0]
        except IndexError:
            raise Exception("No such client!")

        if len(client.loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type):
        counter = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                counter += 1
                loan.increase_interest_rate()

        return f"Successfully changed {counter} loans."

    def increase_clients_interest(self, min_rate):
        counter = 0
        for client in self.clients:
            if client.interest < min_rate:
                counter += 1
                client.increase_clients_interest()
        return f"Number of clients affected: {counter}."

    def get_statistics(self):
        output = []
        active_clients = len(self.clients)
        output.append(f"Active Clients: {active_clients}")
        total_income = sum([client.income for client in self.clients])
        output.append(f"Total Income: {total_income:.2f}")
        output.append(f"Granted Loans: {BankApp.GRANTED_LOANS}, Total Sum: {BankApp.GRANTED_SUM:.2f}")
        output.append(f"Available Loans: {len(self.loans)}, Total Sum: {sum([loan.amount for loan in self.loans]):.2f}")
        try:
            average_client_interest_rate = sum(client.interest for client in self.clients) / active_clients
        except ZeroDivisionError:
            average_client_interest_rate = 0
        output.append(f"Average Client Interest Rate: {average_client_interest_rate:.2f}")

        return "\n".join(output)


# test inputs:

bank = BankApp(3)

print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))
print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))

print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
# print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))

print(bank.grant_loan('StudentLoan', '1234567891'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print(bank.grant_loan('MortgageLoan', '1234567000'))

print(bank.remove_client('1234567999'))

print(bank.increase_loan_interest('StudentLoan'))
print(bank.increase_loan_interest('MortgageLoan'))

print(bank.increase_clients_interest(1.2))
print(bank.increase_clients_interest(3.5))

print(bank.get_statistics())
