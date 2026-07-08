import requests
import pandas as pd

scheme_codes = {
    "HDFC":125497,
    "SBI":119551,
    "ICICI":120503,
    "NIPPON":118632,
    "AXIS":119092,
    "KOTAK":120841
}

for name, code in scheme_codes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    nav_data = pd.DataFrame(data["data"])

    filename = f"data/raw/{name}.csv"

    nav_data.to_csv(filename, index=False)

    print(f"Saved {filename}")
