from business_logic import find_info_by_name
from validators import validate_user_choice
from errors import IncorrectUserInputError


while True:
    user_choice = input("1 - Find info by name\n"
                        "6 - Exit\nYour choice: ")

    try:
        validate_user_choice(user_choice=user_choice)
    except IncorrectUserInputError as err:
        print(err)
        continue

    if user_choice == "6":
        print("GOODBYE!")
        break
    elif user_choice == "1":
        company_name = input("Enter search string: ")
        result = find_info_by_name(company_name=company_name)
        print(result)
