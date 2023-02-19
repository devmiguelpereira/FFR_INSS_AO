import file_standard_format as fsf
import file_settings as fs



def generate_file_name(company_inss_number: int, paysheet_type: int, year: int, month: int) -> str:
    # If payslip is complementary then the value is 1 else it is 0 for a normal payslip
    paysheet_type = "1" if paysheet_type == 1 else "0"
    return f"{company_inss_number}{year}{month:02d}{paysheet_type}.txt"


def header(file_type: str, company_inss_number: str):


    # field in this function
    """
    registration_type           - size 2
    reference_date              - size 8
    file_type                   - size 1
    company_inss_number         - size 9
    new_company_inss_number     - size 20
    company_fiscal_number       - size 20 
    company_name                - size 70
    suburb_code                 - size 5
    blank_spaces                - size 45

    """

    field_sizes = {
        'registration_type': 2,
        'reference_date': 8,
        'file_type': 1,
        'company_inss_number': 9,
        'new_company_inss_number': 20,
        'company_fiscal_number': 20,
        'company_name': 70,
        'suburb_code': 5,
        'blank_spaces': 45
    }

    field_data = {

        'registration_type':fs.general_configuration['registration_type'],
        'reference_date': fs.reference_date(),
        'file_type': fs.general_configuration['file_type'],

        'company_inss_number': fs.company_info['company_inss_number'],
        'new_company_inss_number': fs.company_info['new_company_inss_number'],

        'company_fiscal_number': fsf.format_text(fs.company_info['company_fiscal_number'], field_sizes['company_fiscal_number']),
        'company_name': fsf.format_text(fs.company_info['company_name'],field_sizes['company_name']),
        'suburb_code': fsf.format_text(fs.company_info['suburb_code'],field_sizes['suburb_code']),
        'blank_spaces': fsf.format_text(fs.general_configuration['blank_spaces'], field_sizes['blank_spaces'])

        
    }

    return "{}{}{}{}{}{}{}{}{}".format(
    field_data['registration_type'], 
    field_data['reference_date'], 
    field_data['file_type'], 
    field_data['company_inss_number'],
    field_data['new_company_inss_number'], 
    field_data['company_fiscal_number'], 
    field_data['company_name'], 
    field_data['suburb_code'],
    field_data['blank_spaces']
    )


def employee_compensation_record():
    pass


def file_totalizer():
    pass
