class Payment_jab:
    def pay_jab(self_jab):
        print("Processing payment")

class CashPayment_jab(Payment_jab):
    def pay_jab(self_jab):
        print("Payment made using cash")

class CardPayment_jab(Payment_jab):
    def pay_jab(self_jab):
        print("Payment made using credit card")

payments_jab = [CashPayment_jab(), CardPayment_jab()]
for p_jab in payments_jab:
    p_jab.pay_jab()