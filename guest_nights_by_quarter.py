import pandas as pd
import plotly.express as px
from io import StringIO

# Your data
data = """
"contents" "2024M01" "2024M02" "2024M03" "2024M04" "2024M05" "2024M06" "2024M07" "2024M08" "2024M09" "2024M10" "2024M11" "2024M12"
"Guest nights" . 2251851 2527944 2182055 3123680 4653212 6773484 5270260 3244081 2527791 2274468 .
"""

# Load data into DataFrame
df = pd.read_csv(StringIO(data), sep=' ', quotechar='"').T
df.columns = df.iloc[0]
df = df[1:]
df.index.name = 'Month'
df['Guest nights'] = pd.to_numeric(df['Guest nights'], errors='coerce')

# Fill missing values
df['Guest nights'] = df['Guest nights'].interpolate().ffill().bfill()

# Convert index to datetime and extract quarter
df.index = pd.to_datetime(df.index.str.replace('M', '-') + '-01')
df['Quarter'] = df.index.quarter.map({1: 'Q1', 2: 'Q2', 3: 'Q3', 4: 'Q4'})

# Sum guest nights by quarter
quarterly_data = df.groupby('Quarter')['Guest nights'].sum().reset_index()

# Create pie chart
fig = px.pie(
    quarterly_data,
    names='Quarter',
    values='Guest nights',
    #title='Guest Nights by Quarter (2024)',
    color='Quarter',
    color_discrete_map={'Q1': 'lightcyan', 'Q2': 'cyan', 'Q3': 'royalblue', 'Q4': 'darkblue'},
    hole=0.3,
    labels={'Guest nights': 'Total Guest Nights'},
)

# Update layout
fig.update_traces(
    textinfo='value',
    pull=[0.1, 0, 0, 0],
)

fig.update_layout(
    font=dict(size=12),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
)

fig.write_html("guest_nights_by_quarter.html", full_html=True, include_plotlyjs='cdn', config={"responsive": True})