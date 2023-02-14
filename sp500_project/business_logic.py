from data_access import get_all_records


def find_info_by_name(company_name):
    data = get_all_records()
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
