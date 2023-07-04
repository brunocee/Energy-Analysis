import pycountry

def get_alpha3_country_codes():
    countries = pycountry.countries
    print(pycountry.countries.get(alpha_3='USB'))
    alpha3_country_codes = [country.alpha_3 for country in countries]

    return alpha3_country_codes

# Example usage
alpha3_codes = get_alpha3_country_codes()

print(alpha3_codes)