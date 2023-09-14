import my_utils

def main():
    country='United States of America'
    country_column = 0
    year_column = 1
    savannah_fires_column = 2
    forest_fires_column = 3
    file_name = 'Agrofood_co2_emission.csv'
    
    savannah_fires_strings_list = my_utils.get_column(file_name, 
                                                      country_column, 
                                                      country, 
                                                      result_column=savannah_fires_column)
    savannah_fires = sum([float(fire) for fire in savannah_fires_strings_list])
    forest_fires_string_list = my_utils.get_column(file_name, 
                                                   country_column, 
                                                   country, 
                                                   forest_fires_column)
    forest_fires = sum([float(fire) for fire in forest_fires_string_list])
    fires = savannah_fires + forest_fires
    
    years_with_fires_string_list = my_utils.get_column(file_name, 
                                                       country_column, 
                                                       country, 
                                                       result_column=year_column)
    years_with_fires_list = [int(year) for year in years_with_fires_string_list]
    
    minimum_year = min(years_with_fires_list)
    maximum_year = max(years_with_fires_list)
    
    print(f"There were a total of {fires} savannah and forest fires in {country} from {minimum_year} to {maximum_year}")

if __name__ == '__main__':
    main()
