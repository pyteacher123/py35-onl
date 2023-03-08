# first_name, last_name - проверять, что начинаются с большой буквы и длина
# от 5 до 15 символов email - содержит один символ @, что втора часть
# будет равна gmail.com phone - начинается с знака +, длина 12 символов
# telegram - начинается с @, длина от 5 до 25 символов

class Field:
    def __init__(self, f_type):
        self.validator_obj = f_type()

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validator_obj(value)
        setattr(instance, self.name, value)


class Name:
    def __call__(self, value):
        if not value[0].isupper():
            raise ValueError("Name should start from capital letter.")

        if len(value) not in range(5, 16):
            raise ValueError("Name length must be in range (5, 15).")


class Email:
    def __call__(self, value):
        email_split = value.split('@')
        if len(email_split) != 2:
            raise ValueError("Email must contains only one @.")

        if email_split[1] != "gmail.com":
            raise ValueError("Unsupported email provider.")


class Phone:
    def __call__(self, value):
        if value[0] != "+":
            raise ValueError("Phone must starts from +.")

        if len(value) != 13:
            raise ValueError("Phone length must be 13.")


class Telegram:
    def __call__(self, value):
        if value[0] != "@":
            raise ValueError("Telegram username must starts from @.")

        if len(value) not in range(5, 26):
            raise ValueError("Telegram username length must be in range"
                             "(5, 25).")


class User:
    first_name = Field(Name)
    last_name = Field(Name)

    def __init__(self, first_name, last_name, contact):
        self.first_name = first_name
        self.last_name = last_name
        self.contact = contact


class Contact:
    email = Field(Email)
    phone = Field(Phone)
    telegram = Field(Telegram)

    def __init__(self, email, phone, telegram):
        self.email = email
        self.phone = phone
        self.telegram = telegram


class NewClass:
    email = Field(Email)

    def __init__(self, email):
        self.email = email


contact1 = Contact("max@gmail.com", "+375447364848", "@fhehfjwh")
user1 = User("Maksim", "Perkovskiy", contact1)
print(user1.first_name)
print(user1.contact.email)
