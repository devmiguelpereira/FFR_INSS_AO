from datetime import date

def reference_date():
    
    data = date.today()

    day = data.day
    month = data.month
    year = data.year

    if (month <= 9 or day <= 9):
        return "0{}0{}{}".format(day, month, year)

    else:
        return "{}{}{}".format(day, month, year)

"""
Type of fields

N - Numeric Values
D - Date
C - Alfanumeric values

"""
general_settings = {

    'paysheet_type': 0, # 0 by default (Normal PaySheet) and If payslip is complementary then the value is 1 

    'company_info' : {

                        'company_inss_number': 256, # N - Numeric Field
                        'new_company_inss_number': 256, # N - Numeric Field
                        
                        'company_fiscal_number': "5510126032" + " " * 10, # C - Alfanumeric Field
                        'company_name': "ORGANIZACOES KILAMBAL LDA" + " " * 42, # C - Alfanumeric Field
                        'suburb_code': " " * 5,  # N - Numeric Field
    },

    'header_configuration': {

                        'registration_type': "00", # N - Numeric Field 
                        'reference_date': reference_date(), # D - Date Field
                        'file_type': "N", # C - Alfanumeric Field
                        
                        'blank_spaces': " " * 45 # C - Alfanumeric Field

    },

    'employee_record_configuration': {
                        'registration_type': "10",
                        'employee_inss_number': "005004879",
                        'new_employee_inss_number': "                    ",
                        'employee_name':"ANDRE JORGE CAMPOS                                                    ",
                        'professional_category_code': "     ",
                        'base_salary': "00000025865580",
                        'other_compensation': "00000005276966",
                        'start_of_employment': "        ",
                        'end_of_employment': "        ",
                        'blank_spaces': " " * 30


    },

    'file_totalizer': {
                        'registration_type': "99",
                        'total_registration_type':"0000000000",
                        'fill_with_zeros': "0000000000",
                        'base_salary_total': "00000000000000",
                        'other_compensation_total': "00000000000000",
                        'responsible_for_generating_the_file': "FFR_INSS_AO                             ",
                        'email_of_the_responsible_for_generating_the_file': "ffr@ffr_inss_ao.com                                ",
                        'blank_spaces': " " * 40


    }

        
    
    

}



