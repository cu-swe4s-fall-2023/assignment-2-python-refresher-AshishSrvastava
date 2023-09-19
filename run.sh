# This works to get all types of fires
printf "This will print out the total emissions from all types of fires:\n"
python print_fires.py --country 'United States of America' --file_name 'Agrofood_co2_emission.csv' --all_fires True

# This will also work
printf "\nThis will also out the total emissions from all types of fires:\n"
python print_fires.py --country 'United States of America' --file_name 'Agrofood_co2_emission.csv' --savannah_fires_column --forest_fires_column --organic_soil_fires_column --humid_tropical_forest_fires_column

# This will also work
printf "\nThis will also out the total emissions from all types of fires, but now we're specifying specific columns:\n"
python print_fires.py --country 'United States of America' --file_name 'Agrofood_co2_emission.csv' --savannah_fires_column 2 --forest_fires_column 3 --organic_soil_fires_column 22 --humid_tropical_forest_fires_column 23

# This will work to get forest and savannah fires
printf "\nThis will print out the total emissions from forest and savannah fires:\n"
python print_fires.py --country 'United States of America' --file_name 'Agrofood_co2_emission.csv' --savannah_fires_column --forest_fires_column

# This will throw an error
printf "\nThis will throw an error:\n"
python print_fires.py --country 'United States of America' --file_name 'Agrofood_co2_emission2.csv'

# This will throw an error
printf "This will also give an error:\n"
python print_fires.py --country 'United States of America' --file_name 'Agrofood_co2_emission.csv'