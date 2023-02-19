
def format_text_field(name, field_size):
    # Truncate the name if it is longer than the field size
    if len(name) > field_size:
        name = name[:field_size]
    # Add spaces to the end of the name until it is the desired field size
    name += ' ' * (field_size - len(name))
    return name


def format_date_field(name, field_size):
    pass

def format_numeric_field(name, field_size):
    pass