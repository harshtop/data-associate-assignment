import requests
import pandas as pd

def fetch_wb_data(indicator_code, indicator_name):
    url = f"https://api.worldbank.org/v2/country/all/indicator/{indicator_code}"
    params = {
        "format": "json",
        "per_page": 20000
    }

    response = requests.get(url, params=params)
    data = response.json()[1]

    df = pd.DataFrame(data)

    df = df[[
        "countryiso3code",
        "country",
        "date",
        "value"
    ]]

    df.columns = ["country_code", "country", "year", indicator_name]
    
    return df

# World Bank Indicators
mmr = fetch_wb_data("SH.STA.MMRT", "maternal_mortality")
health_exp = fetch_wb_data("SH.XPD.CHEX.PC.CD", "health_expenditure")
skilled_birth = fetch_wb_data("SH.STA.BRTC.ZS", "skilled_birth_rate")

wb_merged = mmr.merge(health_exp, on=["country_code", "country", "year"], how="inner")
wb_merged = wb_merged.merge(skilled_birth, on=["country_code", "country", "year"], how="inner")

# Our World in Data - GDP
gdp_url = "https://ourworldindata.org/grapher/gdp-per-capita-worldbank.csv"
gdp = pd.read_csv(gdp_url)

gdp = gdp.rename(columns={
    "Code": "country_code",
    "Year": "year",
    "GDP per capita (constant 2015 US$)": "gdp_per_capita"
})

gdp = gdp[["country_code", "year", "gdp_per_capita"]]

wb_merged["year"] = pd.to_numeric(wb_merged["year"], errors="coerce")
gdp["year"] = pd.to_numeric(gdp["year"], errors="coerce")

final_df = wb_merged.merge(gdp, on=["country_code", "year"], how="inner")

final_df = final_df[final_df["year"] >= 2010]
final_df = final_df.dropna()
final_df = final_df.drop_duplicates()

final_df.to_csv("processed_health_data.csv", index=False)

print("Data pipeline completed successfully.")
