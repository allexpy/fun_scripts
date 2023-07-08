file_name = 'path_to_file'
lines = (line for line in open(file_name))
list_lines = (s.rstrip().split(',') for s in lines)
cols = next(list_lines)
company_data = (dict(zip(cols, data)) for data in list_lines)
funding = (int(company_dict['raisedAmt']) for company_dict in company_data if company_dict['round'] == 'a')
total_series_a = sum(funding)
