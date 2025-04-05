import pandas as pd
import plotly.graph_objects as go
from io import StringIO

# Load the data
csv_data = """
"region";"industry (SIC2007)";"Turnover (NOK million) 2020";"Turnover (NOK million) 2021";"Turnover (NOK million) 2022"
"30 Viken (2020-2023)";"Secondary industries and service activities";1212650.2;1354434.5;1532052.0
"03 Oslo";"Secondary industries and service activities";1045169.1;1254569.8;1542503.7
"34 Innlandet";"Secondary industries and service activities";225590.4;312498.7;348054.4
"38 Vestfold og Telemark (2020-2023)";"Secondary industries and service activities";319385.4;381000.0;445102.9
"42 Agder";"Secondary industries and service activities";216668.6;264536.2;313269.3
"11 Rogaland";"Secondary industries and service activities";492525.9;572644.6;666654.1
"46 Vestland";"Secondary industries and service activities";581345.3;709815.2;887130.3
"15 M¯re og Romsdal";"Secondary industries and service activities";244371.3;288116.3;333570.2
"50 Tr¯ndelag - Trˆˆndelage";"Secondary industries and service activities";340769.9;405009.8;457492.7
"18 Nordland - Nordl·nnda";"Secondary industries and service activities";162955.6;205904.3;238073.9
"54 Troms og Finnmark - Romsa ja Finnm·rku (2020-2023)";"Secondary industries and service activities";153434.3;180306.2;209773.2
"21 Svalbard";"Secondary industries and service activities";2890.8;3319.4;4928.0
"""

# Read data
df = pd.read_csv(StringIO(csv_data), sep=';')

# Define mapping from messy to clean region names
region_mapping = {
    "30 Viken": "Viken",
    "03 Oslo": "Oslo",
    "34 Innlandet": "Innlandet",
    "38 Vestfold og Telemark": "Vestfold og Telemark",
    "42 Agder": "Agder",
    "11 Rogaland": "Rogaland",
    "46 Vestland": "Vestland",
    "15 M¯re og Romsdal": "Møre og Romsdal",
    "50 Tr¯ndelag - Trˆˆndelage": "Trøndelag",
    "18 Nordland - Nordl·nnda": "Nordland",
    "54 Troms og Finnmark - Romsa ja Finnm·rku": "Troms og Finnmark",
    "21 Svalbard": "Svalbard"
}

# Clean region names
df['region'] = df['region'].str.replace(r'\(.*\)', '', regex=True).str.strip()
df['region'] = df['region'].map(region_mapping)

# Melt to long format
df_melted = df.melt(
    id_vars=["region", "industry (SIC2007)"],
    var_name="Year",
    value_name="Turnover (NOK million)"
)
df_melted["Year"] = df_melted["Year"].str.extract(r'(\d{4})')[0]

# Create figure
fig = go.Figure()

# Add traces for all regions
regions = sorted(df['region'].unique())
for region in regions:
    region_df = df_melted[df_melted['region'] == region]
    fig.add_trace(
        go.Scatter(
            x=region_df["Year"],
            y=region_df["Turnover (NOK million)"],
            name=region,
            visible=True,
            mode='lines+markers',
            hovertemplate="<b>%{x}</b><br>%{y:,.0f} NOK million",
            line=dict(width=2)
        )
    )

# Create dropdown buttons
buttons = [dict(
    label="All regions",
    method="update",
    args=[{"visible": [True]*len(regions)},
          {"title": {"text": "Turnover by Region (2020-2022)", "y": 0.92}}]
)]

for i, region in enumerate(regions):
    visibility = [False]*len(regions)
    visibility[i] = True
    buttons.append(dict(
        label=region,
        method="update",
        args=[{"visible": visibility},
              {"title": {"text": f"Turnover: {region} (2020-2022)", "y": 0.92}}]
    ))

# Determine common axis range
x_range = df_melted["Year"].unique()
y_range = [df_melted["Turnover (NOK million)"].min(), df_melted["Turnover (NOK million)"].max()]

# Update layout for responsiveness and spacing
fig.update_layout(
    autosize=True,
    title={
        'text': "Turnover by Region (2020-2022)",
        'y': 0.93,  # Adjusted to give more space above
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 16}
    },
    xaxis_title="Year",
    yaxis_title="Turnover (NOK million)",
    margin=dict(t=150, l=50, r=50, b=80),
    paper_bgcolor='white',
    plot_bgcolor='rgba(173, 216, 230, 0.3)',
    updatemenus=[dict(
        buttons=buttons,
        direction="down",
        pad={"r": 10, "t": 10, "b": 10},
        showactive=True,
        x=0.1,
        xanchor="left",
        y=1.12,  # Adjusted to give space above dropdown menu
        yanchor="top",
        bgcolor='white'
    )],
    annotations=[dict(
        text="Select region:",
        x=0,
        xref="paper",
        y=1.18,  # Further moved up to avoid overlap
        yref="paper",
        align="left",
        showarrow=False,
        font=dict(size=12)
    )],
    legend=dict(
        bgcolor='white'
    ),
    xaxis=dict(
        tickvals=[2020, 2021, 2022],  # Ensure we only show the years 2020-2022
    ),
    yaxis=dict(
        range=y_range,  # Fix y-axis range to the turnover values
    )
)

# Style axes
fig.update_xaxes(
    tickangle=-45,
    gridcolor='rgba(255,255,255,0.5)',
    linecolor='black'
)
fig.update_yaxes(
    gridcolor='rgba(255,255,255,0.5)',
    linecolor='black'
)

# Save as responsive HTML
fig.write_html("revenue_plot.html", full_html=True, include_plotlyjs='cdn', config={"responsive": True})