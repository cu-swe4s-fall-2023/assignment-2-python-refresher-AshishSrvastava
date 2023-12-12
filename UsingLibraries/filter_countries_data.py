import pandas as pd


def filter_emissions_data_countries(input_file, output_file, countries):
    # Read emissions data from CSV
    all_countries_emissions_df = pd.read_csv(input_file)

    # Filter for specified countries
    filtered_countries_emissions_df = all_countries_emissions_df[
        all_countries_emissions_df["Area"].isin(countries)
    ]

    # Save the filtered data
    filtered_countries_emissions_df.to_csv(output_file, index=False)


def filter_gdp_data_countries(input_file, output_file, countries):
    # Read GDP data from CSV
    all_countries_gdp_df = pd.read_csv(input_file)

    # Transform GDP data to long format and convert year to integer
    all_countries_gdp_df = all_countries_gdp_df.melt(
        id_vars="Country", var_name="Year", value_name="GDP"
    )
    all_countries_gdp_df["Year"] = all_countries_gdp_df["Year"].astype(int)

    # Convert GDP from string to float, handling non-numeric characters like commas
    all_countries_gdp_df["GDP"] = pd.to_numeric(
        all_countries_gdp_df["GDP"].str.replace(",", ""), errors="coerce"
    )

    # Filter for specified countries
    filtered_countries_gdp_df = all_countries_gdp_df[
        all_countries_gdp_df["Country"].isin(countries)
    ]

    # Standardize country name for United States to match with Agrofood_co2_emission.csv
    filtered_countries_gdp_df["Country"] = filtered_countries_gdp_df[
        "Country"
    ].replace("United States", "United States of America")

    # Save the filtered GDP data
    filtered_countries_gdp_df.to_csv(output_file, index=False)


def merge_emissions_and_gdp(emissions_file, gdp_file, output_file):
    # Load emissions and GDP data
    emissions_data = pd.read_csv(emissions_file)
    gdp_data = pd.read_csv(gdp_file)

    # Merge datasets on 'Area'/'Country' and 'Year'
    merged_data = pd.merge(
        emissions_data,
        gdp_data,
        left_on=["Area", "Year"],
        right_on=["Country", "Year"],
    )

    # Save the merged data
    merged_data.to_csv(output_file, index=False)


if __name__ == "__main__":
    # File paths for input and output data
    input_emissions_csv = "Agrofood_co2_emission.csv"
    output_emissions_csv = "filtered_emissions_data.csv"

    input_gdp_csv = "IMF_GDP.csv"
    output_gdp_csv = "filtered_gdp_data.csv"
    output_merged_csv = "merged_data.csv"

    # List of North American countries for filtering
    north_american_countries = [
        "United States of America",
        "United States",
        "Mexico",
        "Canada",
        "Guatemala",
    ]

    # Process and filter emissions and GDP data
    filter_emissions_data_countries(
        input_emissions_csv, output_emissions_csv, north_american_countries
    )
    filter_gdp_data_countries(
        input_gdp_csv, output_gdp_csv, north_american_countries
    )

    # Merge the filtered emissions and GDP data
    merge_emissions_and_gdp(
        output_emissions_csv, output_gdp_csv, output_merged_csv
    )
