
import file_settings as fs

def format_text_field(name, field_size):
    # Truncate the name if it is longer than the field size
    if len(name) > field_size:
        name = name[:field_size]
    # Add spaces to the end of the name until it is the desired field size
    name += ' ' * (field_size - len(name))
    return name

def format_date(date_str, optional=False):
    if not date_str:
        if optional:
            return " " * 8
        else:
            raise ValueError("Date field is required")

    if not date_str.isdigit():
        raise ValueError("Date field must contain only numbers")

    if len(date_str) != 8:
        raise ValueError("Date field must have size of 8 characters")

    day = date_str[:2]
    month = date_str[2:4]
    year = date_str[4:]

    formatted_date = "{}{}{}".format(day, month, year)

    return formatted_date

def format_numeric_field(field_value: str, field_size: int) -> str:
    # Remove any non-numeric characters
    numeric_value = ''.join(c for c in field_value if c.isdigit())

    # Pad with leading zeros until the desired length is reached
    formatted_value = numeric_value.rjust(field_size, '0')

    return formatted_value # Output: "0000012345"

def format_base_salary_value(salary: float) -> str:
    # Round the salary to 2 decimal places
    salary = round(salary, 2)

    # Convert the salary to a string without the decimal point or thousands separator
    salary_str = str(int(salary * 100)).zfill(14)

    return salary_str

#format_base_salary_value(456123.78)
#'00000045612378'