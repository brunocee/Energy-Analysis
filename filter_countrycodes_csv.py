import pandas as pd
import pycountry

def filter_csv_by_country_codes(input_file, output_file):
    country_codes = set(country.alpha_3 for country in pycountry.countries)

    df = pd.read_csv(input_file)
    filtered_df = df[df['Country Code'].isin(country_codes)]

    filtered_df.to_csv(output_file, index=False)

# Example usage
input_file = 'WorldBankDataGDP-modifiable.csv'
output_file = 'output.csv'
filter_csv_by_country_codes(input_file, output_file)
