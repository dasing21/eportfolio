import pandas as pd
import plotly.express as px
from io import StringIO

# Your data
csv_data = """
"14162: Guest nights, by type of accommodation, country of residence, contents and month"

"type of accommodation";"country of residence";"Guest nights 2024M01";"Guest nights 2024M02";"Guest nights 2024M03";"Guest nights 2024M04";"Guest nights 2024M05";"Guest nights 2024M06";"Guest nights 2024M07";"Guest nights 2024M08";"Guest nights 2024M09";"Guest nights 2024M10";"Guest nights 2024M11";"Guest nights 2024M12"
"Hotels and similar establishments";"Total";1534573;1808839;1952596;1735900;2111194;2828096;3526269;3210272;2389974;2103792;1970032;1562320
"Hotels and similar establishments";"Foreign national, total";365919;497382;519834;386408;550620;837929;1241279;1173660;659261;509886;411032;488427
"Hotels and similar establishments";"Norway";1168654;1311457;1432762;1349492;1560574;1990167;2284990;2036612;1730713;1593906;1559000;1073893
"Camping sites";"Total";.;.;.;.;724620;1416233;2640066;1527470;.;.;.;.
"Camping sites";"Foreign national, total";.;.;.;.;178626;577617;890264;692751;.;.;.;.
"Camping sites";"Norway";.;.;.;.;545994;838616;1749802;834719;.;.;.;.
"Holiday dwellings and youth hostels";"Total";.;.;.;.;287866;408883;607149;532518;.;.;.;.
"Holiday dwellings and youth hostels";"Foreign national, total";.;.;.;.;163544;232723;322373;310320;.;.;.;.
"Holiday dwellings and youth hostels";"Norway";.;.;.;.;124322;176160;284776;222198;.;.;.;.
"""

# Read data (skip the first 2 rows)
df = pd.read_csv(
    StringIO(csv_data),
    delimiter=";",
    skiprows=2,
    na_values=["."]
)

# Fill missing values with 0
df.fillna(0, inplace=True)

# Filter only "Total" rows (avoid double-counting)
df_totals = df[df["country of residence"] == "Total"].copy()  # Explicit copy to avoid warning

# Calculate total guest nights for 2024 (using .loc to avoid SettingWithCopyWarning)
df_totals.loc[:, "Total Guest Nights 2024"] = df_totals.iloc[:, 2:].sum(axis=1)

# Select relevant columns
accommodation_totals = df_totals[["type of accommodation", "Total Guest Nights 2024"]]

# Create pie chart using Plotly
fig = px.pie(
    accommodation_totals,
    names="type of accommodation",
    values="Total Guest Nights 2024",
    #title="Distribution of Guest Nights by Accommodation Type (2024)",
    color="type of accommodation",
    color_discrete_sequence=["#ff9999", "#66b3ff", "#99ff99"],
    hole=0.3  # Add a hole in the middle to create a donut chart effect if desired
)

# Save the figure as an HTML file
fig.write_html("top_accomodation_type.html", full_html=True, include_plotlyjs='cdn')