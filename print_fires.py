import argparse
import my_utils


# TODO : Add cla for country, country_column, fires_column, file_name

parser = argparse.ArgumentParser(
                description='Prints the total amount of CO2 emissions from savannah, forest, organic soil, and humid tropical fires in a given country from a given year to a given year',
                prog='print_fires.py')

parser.add_argument('--country',
                   type=str,
                   help='The country to collect the CO2 emissions from fires for',
                   required=True)

parser.add_argument('--country_column',
                     type=int,
                     help='The index of column holding the countries in the file',
                     required=True)

parser.add_argument('--fires_column',
                     type=int,
                     help='The index of column holding the CO2 emissions from a specific type of fire in the file',
                     required=True)

parser.add_argument('--file_name',
                     type=str,
                     help='The name of the file to read the data from',
                     required=True)

def main():
    country='United States of America'
    country_column = 0
    year_column = 1
    savannah_fires_column = 2
    forest_fires_column = 3
    organic_soil_fires_column = 22
    humid_tropical_forest_fires_column = 23
    
    file_name = 'Agrofood_co2_emission.csv'
    
    savannah_fires_strings_list = my_utils.get_column(file_name, 
                                                      country_column, 
                                                      country, 
                                                      result_column=savannah_fires_column)
    forest_fires_string_list = my_utils.get_column(file_name, 
                                                   country_column, 
                                                   country, 
                                                   result_column=forest_fires_column)
    organic_soil_fires_column = my_utils.get_column(file_name,
                                                    country_column,
                                                    country,
                                                    result_column=organic_soil_fires_column)
    humid_tropical_forest_fires_column = my_utils.get_column(file_name,
                                                            country_column,
                                                            country,
                                                            result_column=humid_tropical_forest_fires_column)
    
    savannah_fires = sum([float(fire) for fire in savannah_fires_strings_list])
    forest_fires = sum([float(fire) for fire in forest_fires_string_list])
    organic_soil_fires = sum([float(fire) for fire in organic_soil_fires_column])
    humid_tropical_forest_fires = sum([float(fire) for fire in humid_tropical_forest_fires_column])
    
    fires = savannah_fires + forest_fires + organic_soil_fires + humid_tropical_forest_fires
    
    years_with_fires_string_list = my_utils.get_column(file_name, 
                                                       country_column, 
                                                       country, 
                                                       result_column=year_column)
    years_with_fires_list = [int(year) for year in years_with_fires_string_list]
    
    minimum_year = min(years_with_fires_list)
    maximum_year = max(years_with_fires_list)
    
    print(f"There was a total of {fires} kilotons of CO2 emissions from savannah, forest, organic soil, and humid tropical fires in {country} from {minimum_year} to {maximum_year}")

if __name__ == '__main__':
    main()
