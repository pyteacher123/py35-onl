class BankCard:
    def __init__(self, number, cvc, first_name, last_name):
        self.number = number
        self.cvc = cvc
        self.first_name = first_name
        self.last_name = last_name

    def _luhn_algorithm(self, value):
        card_sum = 0
        for index, digit in enumerate(value):
            digit = int(digit)
            if index % 2 == 0:
                digit *= 2
                if digit > 9:
                    digit -= 9

            card_sum += digit

        if card_sum % 10 != 0:
            raise ValueError("Invalid card number")

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if len(value) != 16:
            raise ValueError("Card number length must be 16.")

        if not value.isdigit():
            raise ValueError("Card number must contains only integers.")

        if value[0] not in ('4', '5'):
            raise ValueError("Unsupported payment gateway.")

        self._luhn_algorithm(value)

        self._number = value

    @property
    def cvc(self):
        return self._cvc

    @cvc.setter
    def cvc(self, value):
        if len(value) != 3:
            raise ValueError("Invalid cvc code")

        self._cvc = value


bc1 = BankCard("4561261212345467", '13', None, None)
print(bc1)
