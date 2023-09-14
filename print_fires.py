import my_utils

def main():
    country='United States of America'
    country_column = 0
    savannah_fires_column = 2
    forest_fires_column = 3
    file_name = 'Agrofood_co2_emission.csv'
    savannah_fires_strings_list = my_utils.get_column(file_name, country_column, country, result_column=savannah_fires_column)
    savannah_fires = sum([float(fire) for fire in savannah_fires_strings_list])
    forest_fires_string_list = my_utils.get_column(file_name, country_column, country, forest_fires_column)
    forest_fires = sum([float(fire) for fire in forest_fires_string_list])
    fires = savannah_fires + forest_fires
    print(fires)

if __name__ == '__main__':
    main()
