class Loan:
    def __init__(self, acc, name, existing_loan, cibil):
        self.acc = acc
        self.name = name
        self.existing_loan = existing_loan
        self.cibil = cibil
    def status(self):
        print(f"The account holder {self.name} with account number {self.acc}")
        print(f"He is loan status ={self.existing_loan} and cibil score is {self.cibil}")