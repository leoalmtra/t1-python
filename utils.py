def leap_year(year:int):
    """
    Calculate a leap year.

    Args:
        year(Int): A integer year.
    
    Return: 
        Boolean: True if the year is a leap year or false if not.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True

def validation(rule_data, rule_list:list):
    """
    Validate a data.

    Args:
        validate_data: A modular data
    
    Return:
        String: A modular error message.
    """
    for rule, message in rule_list:
        if not rule(rule_data):
            print(f"Failed to validate:{message}")
            return False
    return True