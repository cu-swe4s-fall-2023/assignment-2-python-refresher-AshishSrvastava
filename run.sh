# This works
printf "This will work:\n"
python print_fires.py --country 'United States of America' --file_name 'Agrofood_co2_emission.csv'

# This will throw an error
printf "\nThis will throw an error:\n"
python print_fires.py --country 'United States of America' --file_name 'Agrofood_co2_emission2.csv'