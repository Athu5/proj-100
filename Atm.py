class Atm:

    def __init__(self, cardNumber, pinNumber):
        self.atmCardNumber = cardNumber
        self.pinNumber = pinNumber

    def CashWithdrawl(self):
        print("CashWithDrawl")

    def Balance_enquiry(self):
        print("BalanceEnquiry")

def main():
     
     atmpin = Atm("321", "123" )

     atmpin.CashWithdrawl()
     atmpin.Balance_enquiry()

main()
