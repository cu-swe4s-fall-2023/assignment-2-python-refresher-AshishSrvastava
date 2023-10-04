test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run all_fires python ../../src/print_fires.py --country 'United States of America' --file_name 'test_Agrofood_co2_emission.csv' --all_fires True
assert_in_stdout "There was a total of 103213 kilotons of CO2 emissions from savannah, forest, organic soil and humid tropical forest fires in United States of America from 1990 to 2020"
assert_exit_code 0

run all_fires_specified python ../../src/print_fires.py --country 'United States of America' --file_name 'test_Agrofood_co2_emission.csv' --savannah_fires_column --forest_fires_column --organic_soil_fires_column --humid_tropical_forest_fires_colum
assert_in_stdout "There was a total of 103213 kilotons of CO2 emissions from savannah, forest, organic soil and humid tropical forest fires in United States of America from 1990 to 2020"
assert_exit_code 0

run all_fires_columns python ../../src/print_fires.py --country 'United States of America' --file_name 'test_Agrofood_co2_emission.csv' --savannah_fires_column 2 --forest_fires_column 3 --organic_soil_fires_column 22 --humid_tropical_forest_fires_column 23
assert_in_stdout "There was a total of 103213 kilotons of CO2 emissions from savannah, forest, organic soil and humid tropical forest fires in United States of America from 1990 to 2020"
assert_exit_code 0

run no_iceland_forest_fires python ../../src/print_fires.py --country 'Iceland' --file_name 'test_Agrofood_co2_emission.csv' --forest_fires_column
assert_in_stdout "There was a total of 0 kilotons of CO2 emissions from forest fires in Iceland from 1990 to 2020"
assert_exit_code 0

run multiple_fires_specified python ../../src/print_fires.py --country 'Australia' --file_name 'test_Agrofood_co2_emission.csv' --savannah_fires_column --forest_fires_column
assert_in_stdout "There was a total of 1845669 kilotons of CO2 emissions from savannah and forest fires in Australia from 1990 to 2020"
assert_exit_code 0

run file_does_not_exist python ../../src/print_fires.py --country 'United States of America' --file_name 'DNE_Agrofood_co2_emission2.csv'
assert_exit_code 1

run no_sources_specified python ../../src/print_fires.py --country 'United States of America' --file_name 'test_Agrofood_co2_emission.csv'
assert_exit_code 1

run array_mean python array_operations.py mean 1,2,3,4,5
assert_in_stdout 3.0
assert_exit_code 0

run array_median python array_operations.py median 1,2,3,4,5
assert_in_stdout 3.0
assert_exit_code 0

run array_stdev python array_operations.py stdev 1,2,3,4,5
assert_in_stdout 1.4142135623730951
assert_exit_code 0