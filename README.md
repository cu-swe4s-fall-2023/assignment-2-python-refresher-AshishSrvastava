[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# python-refresher
My submission for the Python Refresher Assignment (Assignment 2)

The goal was to use good practices to create a project that would calculate the total $CO_2$ emissions from fires in the US (which could be extended to any other statistic in the dataset for any other country)

## Installation and Usage
Clone the GitHub Repository and run the following command in the terminal:
```bash
$ bash run.sh
```
This will print the total emissions from forest fires in the US for the range of data provided in the data source. The bash script has 4 working commands, and 2 commands that should throw an error to test the error handling.

## Usage of `print_fires.py`
The data source provided can be passed in several ways - unique fire sources can be specified, or all types of fires (savannah, forest, organic soil and humid tropical forest fires).

`print_fires.py` can be called in the following format
```
usage: print_fires.py --country COUNTRY --file_name FILE_NAME 

Calculate CO2 emissions from fires in a country

optional arguments (at least one source must be specified)
--all_fires                                 Calculate emissions from all fire sources
--savannah_fires_column                     Column number for savannah fires (default 2)
--forest_fires_column                       Column number for forest fires (default 3)
--organic_soil_fires_column                 Column number for organic soil fires (default 22)
--humid_tropical_forest_fires_column        Column number for humid tropical forest fires (default 23)
```

### All fire types
```bash
python print_fires.py --country 'United States of America' --file_name 'Agrofood_co2_emission.csv' --all_fires True
```

### All fire types, naming specific sources, and indicating specific columns
```bash
python print_fires.py --country 'United States of America' --file_name 'Agrofood_co2_emission.csv' --savannah_fires_column 2 --forest_fires_column 3 --organic_soil_fires_column 22 --humid_tropical_forest_fires_column 23
```

### Specifying only two fire sources
```bash
python print_fires.py --country 'United States of America' --file_name 'Agrofood_co2_emission.csv' --savannah_fires_column --forest_fires_column
```


## Data Source
The data source was the provided `Agrofood_co2_emission.csv` file. This datafile provides information on Carbon Dioxide emissions by country and year. The level of $CO_2$ emissions are given in units of [kilotons]