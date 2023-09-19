import argparse
import my_utils


parser = argparse.ArgumentParser(
                description='Prints the total amount of CO2 emissions from savannah, forest, organic soil, and humid tropical fires in a given country from a given year to a given year',
                prog='print_fires.py')

parser.add_argument('--file_name',
                     type=str,
                     help='The name of the file to read the data from',
                     required=True)

parser.add_argument('--country',
                   type=str,
                   help='The country to collect the CO2 emissions from fires for',
                   required=True)

parser.add_argument('--country_column',
                     type=int,
                     help='The index of column holding the countries in the file',
                     nargs='?',
                     default=0,
                     required=False)

parser.add_argument('--year_column',
                    type=int,
                    help='The index of column holding the years in the file',
                    nargs='?',
                    default=1,
                    required=False)

parser.add_argument('--all_fires',
                    type=bool,
                    help='To include all fire sources (savannah, forest, organic soil, humid tropical forest) in the total CO2 emissions from fires',
                    nargs='?',
                    const=True,
                    )

parser.add_argument('--savannah_fires_column',
                     type=int,
                     help='The index of column holding the CO2 emissions from savannah fires in the file (defaults to 2)',
                     nargs='?',
                     const=2,
                     required=False)

parser.add_argument('--forest_fires_column',
                     type=int,
                     help='The index of column holding the CO2 emissions from forest fires in the file (defaults to 3)',
                     nargs='?',
                     const=3,
                     required=False)

parser.add_argument('--organic_soil_fires_column',
                     type=int,
                     help='The index of column holding the CO2 emissions from organic soil fires in the file (defaults to 22)',
                     nargs='?',
                     const=22,
                     required=False)

parser.add_argument('--humid_tropical_forest_fires_column',
                     type=int,
                     help='The index of column holding the CO2 emissions from humid tropical forest fires in the file (defaults to 23)',
                     nargs='?',
                     const=23,
                     required=False)

args = parser.parse_args()


def main():
    country = args.country
    country_column = args.country_column
    year_column = args.year_column
    savannah_fires_column = args.savannah_fires_column
    forest_fires_column = args.forest_fires_column
    organic_soil_fires_column = args.organic_soil_fires_column
    humid_tropical_forest_fires_column = args.humid_tropical_forest_fires_column
    file_name = args.file_name
    all_fires = args.all_fires 
    if all_fires:
        if savannah_fires_column is None:
            savannah_fires_column = 2
        if forest_fires_column is None:
            forest_fires_column = 3
        if organic_soil_fires_column is None:
            organic_soil_fires_column = 22
        if humid_tropical_forest_fires_column is None:
            humid_tropical_forest_fires_column = 23
    
    total_fires = 0
    fire_sources = []
    
 
    
    # Get the time range for when fires ocurred
    years_with_fires_list = my_utils.get_column(file_name, 
                                                    country_column, 
                                                    country, 
                                                    result_column=year_column)
    minimum_year = min(years_with_fires_list)
    maximum_year = max(years_with_fires_list)
    
    # Check for which fires to include
    if savannah_fires_column != None or all_fires == True:
        savannah_fires_list = my_utils.get_column(file_name, 
                                                        country_column, 
                                                        country, 
                                                        result_column=savannah_fires_column)
        total_fires += sum(savannah_fires_list)
        fire_sources.append("savannah")
    
    if forest_fires_column != None or all_fires == True:
        forest_fires_list = my_utils.get_column(file_name, 
                                                   country_column, 
                                                   country, 
                                                   result_column=forest_fires_column)
        total_fires += sum(forest_fires_list)
        fire_sources.append("forest")

    if organic_soil_fires_column != None or all_fires == True:
        organic_soil_fires_list = my_utils.get_column(file_name, 
                                                           country_column, 
                                                           country, 
                                                           result_column=organic_soil_fires_column)
        total_fires += sum(organic_soil_fires_list)
        fire_sources.append("organic soil")
        
    if humid_tropical_forest_fires_column != None or all_fires == True:
        humid_tropical_forest_fires_list = my_utils.get_column(file_name, 
                                                                   country_column, 
                                                                   country, 
                                                                   result_column=humid_tropical_forest_fires_column)
        total_fires += sum(humid_tropical_forest_fires_list)
        fire_sources.append("humid tropical forest")
        
    
    try:
        fire_sources_string = ", ".join(fire_sources[:-1]) + " and " + fire_sources[-1]
    except IndexError:
        print("Error: No fire sources specified for the given country Please specify source(s) or use the --all_fires flag")
        raise
    finally:
        print(f"There was a total of {total_fires} kilotons of CO2 emissions from {fire_sources_string} fires in {country} from {minimum_year} to {maximum_year}")

if __name__ == '__main__':
    main()
