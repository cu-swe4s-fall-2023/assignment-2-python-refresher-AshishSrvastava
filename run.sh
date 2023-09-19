# This works to get all types of fires
python print_fires.py --country 'United States of America' --file_name 'Agrofood_co2_emission.csv' --all_fires True

# This will work to get forest and savannah fires
python print_fires.py --country 'United States of America' --file_name 'Agrofood_co2_emission.csv' --savannah_fires_column --forest_fires_column

# This will throw an error
printf "\nThis will throw an error:\n"
python print_fires.py --country 'United States of America' --file_name 'Agrofood_co2_emission2.csv'

# This will throw an error
printf "This will give an error:\n"
python print_fires.py --country 'United States of America' --file_name 'Agrofood_co2_emission.csv'