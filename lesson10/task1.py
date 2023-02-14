import csv


def find_info_by_name(company_name):
    with open("sp500.csv") as db_file:
        data = csv.DictReader(db_file)
        result = []
        for row in data:
            if company_name.lower() in row.get("Name").lower():
                result.append({
                    "Symbol": row.get("Symbol"),
                    "Name": row.get("Name"),
                    "Sector": row.get("Sector"),
                    "Stock Price": row.get("Price")
                    }
                )
        return result


while True:
    user_choice = input("1 - Find info by name\n"
                        "6 - Exit\nYour choice: ")

    if user_choice == "6":
        print("GOODBYE!")
        break
    elif user_choice == "1":
        company_name = input("Enter search string: ")
        result = find_info_by_name(company_name=company_name)
        print(result)
