import file_generator as fg
import file_settings as fs
import file_standard_format as fsf

def header(company_dict) -> str:


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
        

        'registration_type':fs.general_settings['header_configuration']['registration_type'],
        
        'reference_date': fsf.format_date(fg.split_date(company_dict['Data'], str_output=True), field_sizes['reference_date']),
        'file_type': "C" if company_dict['Tipo_Folha'] == "Complementar" else "N",

        'company_inss_number':fsf.format_numeric_field(str(company_dict['Numero_Contribuinte']), field_sizes['company_inss_number']),
        'new_company_inss_number':fsf.format_numeric_field(str(company_dict['Numero_Contribuinte']), field_sizes['new_company_inss_number']),

        'company_fiscal_number': fsf.format_text_field(str(company_dict['NIF_da_Empresa']), field_sizes['company_fiscal_number']),
        'company_name': fsf.format_text_field(str(company_dict['Nome_da_Empresa']),field_sizes['company_name']),
        
        
        'suburb_code': fsf.format_text_field(fs.general_settings['company_info']['suburb_code'],field_sizes['suburb_code']),
        'blank_spaces': fsf.format_text_field(fs.general_settings['header_configuration']['blank_spaces'], field_sizes['blank_spaces'])

        
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

def employee_record(employee_inss_number,employee_name,base_salary,other_compensation) -> str:
        # field in this function
    """
    'registration_type':                - size 2         
    'employee_inss_number':             - size 9
    'new_employee_inss_number':         - size 20
    'employee_name':                    - size 70
    'professional_category_code':       - size 5
    'base_salary':                      - size 14
    'other_compensation':               - size 14
    'start_of_employment':              - size 8
    'end_of_employment':                - size 8
    'blank_spaces':                     - size 30

    """

    field_sizes = {
        'registration_type': 2,
        'employee_inss_number': 9,
        'new_employee_inss_number': 20,
        'employee_name': 70,
        'professional_category_code': 5,
        'base_salary': 14,
        'other_compensation': 14,
        'start_of_employment': 8,
        'end_of_employment': 8,
        'blank_spaces': 30
    }

    field_data = {
        

        'registration_type':fs.general_settings['employee_record_configuration']['registration_type'],
        'employee_inss_number': fsf.format_numeric_field(str(employee_inss_number), field_sizes['employee_inss_number']),
        'new_employee_inss_number': fsf.format_numeric_field(str(employee_inss_number), field_sizes['new_employee_inss_number']),
        'employee_name': fsf.format_text_field(str(employee_name), field_sizes['employee_name']),
        'professional_category_code': fs.general_settings['employee_record_configuration']['professional_category_code'],
        'base_salary': fsf.format_salary_field(base_salary, field_sizes['base_salary']),
        'other_compensation': fsf.format_salary_field(other_compensation, field_sizes['other_compensation']),
        'start_of_employment': fs.general_settings['employee_record_configuration']['start_of_employment'],
        'end_of_employment': fs.general_settings['employee_record_configuration']['end_of_employment'],
        'blank_spaces': fs.general_settings['employee_record_configuration']['blank_spaces']

        
    }

    return "{}{}{}{}{}{}{}{}{}{}".format(
    field_data['registration_type'], 
    field_data['employee_inss_number'], 
    field_data['new_employee_inss_number'], 
    field_data['employee_name'],
    field_data['professional_category_code'], 
    field_data['base_salary'], 
    field_data['other_compensation'], 
    field_data['start_of_employment'],
    field_data['end_of_employment'],
    field_data['blank_spaces']
    )


def file_totalizer(responsible_dict):

    # field in this function
    """
    'registration_type':                                    - size 2
    'total_registration_type':                              - size 10
    'fill_with_zeros':                                      - size 10
    'base_salary_total':                                    - size 14
    'other_compensation_total':                             - size 14
    'responsible_for_generating_the_file':                  - size 40
    'email_of_the_responsible_for_generating_the_file':     - size 50
    'blank_spaces':                                         - size 40
    """

    field_sizes = {

        'registration_type': 2,
        'total_registration_type':10,
        'fill_with_zeros': 10,
        'base_salary_total': 14,
        'other_compensation_total': 14,
        'responsible_for_generating_the_file': 40,
        'email_of_the_responsible_for_generating_the_file': 50,
        'blank_spaces': 40
    }

    
    field_data = {

        'registration_type':fs.general_settings['file_totalizer']['registration_type'],
        'total_registration_type':fs.general_settings['file_totalizer']['total_registration_type'],
        'fill_with_zeros': fs.general_settings['file_totalizer']['fill_with_zeros'],
        'base_salary_total': fsf.format_salary_field(str(responsible_dict['Total_Salario_Base']), field_sizes['base_salary_total']),
        'other_compensation_total': fsf.format_salary_field(str(responsible_dict['Total_Outras_Remuneracoes']), field_sizes['other_compensation_total']),
        'responsible_for_generating_the_file': fsf.format_text_field(str(responsible_dict['Responsavel_do_Ficheiro']), field_sizes['responsible_for_generating_the_file']),
        'email_of_the_responsible_for_generating_the_file': fsf.format_text_field(str(responsible_dict['Email_do_Responsavel']), field_sizes['email_of_the_responsible_for_generating_the_file']),
        'blank_spaces': fs.general_settings['file_totalizer']['blank_spaces']

        
    }

    return "{}{}{}{}{}{}{}{}".format(
        field_data['registration_type'], 
        field_data['total_registration_type'], 
        field_data['fill_with_zeros'], 
        field_data['base_salary_total'],
        field_data['other_compensation_total'], 
        field_data['responsible_for_generating_the_file'], 
        field_data['email_of_the_responsible_for_generating_the_file'], 
        field_data['blank_spaces']
        )

