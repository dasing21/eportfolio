import pandas as pd
import io

csv_data = """
"14162: Guest nights, by country of residence, contents and month"

"country of residence";"Guest nights 2024M01";"Guest nights 2024M02";"Guest nights 2024M03";"Guest nights 2024M04";"Guest nights 2024M05";"Guest nights 2024M06";"Guest nights 2024M07";"Guest nights 2024M08";"Guest nights 2024M09";"Guest nights 2024M10";"Guest nights 2024M11";"Guest nights 2024M12"
"Total";.;2251851;2527944;2182055;3123680;4653212;6773484;5270260;3244081;2527791;2274468;.
"Foreign national, total";.;695497;711789;525217;892790;1648269;2453916;2176731;1006965;657840;511441;.
"Norway";.;1556354;1816155;1656838;2230890;3004943;4319568;3093529;2237116;1869951;1763027;.
"Denmark";.;150483;110167;30116;50646;64572;140688;81090;41882;31180;23858;.
"Finland";.;6948;12624;12047;17200;51377;104320;50388;26336;13410;9030;.
"Iceland";.;2405;2426;2282;2782;3280;3927;6400;2984;1914;1826;.
"Sweden";.;78606;78886;77160;88278;144630;272126;157495;87494;69517;54405;.
"Albania";.;166;237;285;389;374;529;991;563;986;522;.
"Andorra";.;85;118;91;123;129;161;313;77;78;37;.
"Belarus";.;120;182;138;392;464;497;690;238;329;250;.
"Belgium";.;8208;10217;9107;18514;30685;62113;45439;13807;8585;7223;.
"Bosnia-Herzegovina";.;678;308;211;153;266;159;344;198;154;134;.
"Bulgaria";.;590;990;1134;891;1255;2614;1979;2066;1061;645;.
"Estonia";.;2542;2127;2222;3385;5560;9729;7800;3381;2404;2431;.
"France";.;26910;27401;23077;44051;74496;114695;118423;37180;22857;19402;.
"Greece";.;1657;2062;1989;3738;3036;5394;10476;2415;2829;1982;.
"Ireland";.;3633;4804;4447;5809;6570;5950;5226;3616;3318;2847;.
"Italy";.;17814;21507;15346;14835;28120;52327;115146;20749;14972;15987;.
"Kosovo";.;88;84;12;13;38;130;1083;34;46;51;.
"Croatia";.;1012;812;902;1292;1447;1909;1749;1330;872;729;.
"Latvia";.;2333;2596;2448;3055;4532;8418;6166;2838;2614;1867;.
"Liechtenstein";.;105;222;53;369;200;547;334;159;156;99;.
"Lithuania";.;3921;5696;6430;8603;8873;13181;12004;5765;4926;4465;.
"Luxembourg";.;532;585;709;1182;1717;3294;4775;1683;721;300;.
"North Macedonia";.;68;75;131;63;50;129;165;258;156;123;.
"Malta";.;128;233;132;330;378;742;853;477;228;245;.
"Moldova";.;67;248;139;405;143;459;236;151;171;163;.
"Monaco";.;40;65;46;61;129;84;311;76;125;72;.
"Montenegro";.;292;382;108;62;650;81;64;301;69;29;.
"Netherlands";.;37161;29724;23769;64054;158640;230117;216220;52162;25426;19146;.
"Poland";.;25838;24527;26311;31850;51061;72084;61267;40220;28037;28212;.
"Portugal";.;3203;3357;4227;5139;8328;8583;10951;5552;3803;4731;.
"Romania";.;3703;3429;2910;2954;3990;9657;8027;4888;3695;3799;.
"Russia";.;563;517;705;778;1125;1510;1572;937;693;553;.
"San Marino";.;30;50;12;8;33;22;29;0;15;12;.
"Serbia";.;240;311;359;419;377;662;768;519;1111;335;.
"Slovakia";.;999;1287;2229;2908;3438;6489;5466;3344;1254;1171;.
"Slovenia";.;609;725;634;873;1428;3836;3143;1099;960;627;.
"United Kingdom";.;78055;62673;54125;54839;74615;82026;89721;56566;48158;49238;.
"Spain";.;12313;19153;14391;28208;36068;56779;85784;32234;18611;16419;.
"Switzerland";.;16521;16471;9489;22430;54614;97466;56437;27049;14142;9819;.
"Czech Republic";.;3038;4857;4921;13281;24366;39486;28695;12645;4108;2271;.
"T¸rkiye";.;1370;1639;2249;2171;4049;5410;5739;3743;2050;1761;.
"Germany";.;68668;97416;65157;193956;438905;575043;533379;207303;79949;42789;.
"Ukraine";.;891;901;847;3281;3843;7447;7054;3954;3172;3274;.
"Hungary";.;799;1548;2296;2124;2744;7877;6539;2242;1503;1112;.
"Austria";.;5853;8885;5310;10151;20280;32693;27810;11171;5934;4369;.
"Vatican City State";.;8;37;6;21;37;68;64;29;18;70;.
"The rest of Europe";.;.;.;.;.;.;.;.;.;.;.;.
"South Africa";.;636;822;499;919;1390;1233;1547;974;1217;941;.
"United Arab Emirates";.;1663;1757;2757;2775;4248;10736;10362;3972;3819;1839;.
"India";.;3972;6051;5208;7914;12389;9973;10132;8454;11761;9795;.
"Indonesia";.;702;699;2146;1117;967;990;683;1041;2702;1804;.
"Israel";.;626;677;363;1463;2517;5418;4069;1708;601;383;.
"Malaysia";.;1775;2030;913;1392;2050;1304;1239;3164;3751;2964;.
"Qatar";.;1143;1037;1153;995;1520;3259;3168;1483;768;829;.
"Singapore";.;3373;5577;2781;3618;4664;3091;3522;5162;7890;8921;.
"Taiwan";.;3678;3464;1846;4496;8173;8727;7572;8608;5736;3038;.
"Thailand";.;2437;4964;5029;2835;2481;5225;2600;4248;9576;6005;.
"Japan";.;2086;2023;1817;3620;5085;6959;7720;6929;3022;2081;.
"China";.;15262;8685;7346;10150;20027;30595;32702;24953;23980;13225;.
"South Korea";.;1478;1523;1967;9739;15456;20207;18712;8565;2723;1430;.
"Cyprus";.;416;364;362;353;519;968;1800;605;373;559;.
"Canada";.;2612;4200;3876;7548;11715;13565;14566;9649;5774;3535;.
"Mexico";.;1083;1695;852;1577;1829;3386;2795;2479;3043;2328;.
"United States";.;58762;75975;52053;82793;174607;213267;213615;144431;98886;80045;.
"Brazil";.;4543;3308;2391;4181;6373;6672;5327;5593;5641;4305;.
"Australia";.;7640;8922;5613;11218;14706;17071;15574;16261;12247;9510;.
"The rest of South America";.;2081;3958;3633;5374;7107;9807;8105;6116;6659;4231;.
"The rest of Oceania";.;1268;1739;1643;3889;5731;5014;4999;2247;2918;2071;.
"The rest of Asia";.;7068;7962;8445;15615;19084;30124;23745;15714;16430;11249;.
"The rest of Asia -2017";.;.;.;.;.;.;.;.;.;.;.;.
"The rest of Africa";.;1900;1796;1815;3143;4719;4867;3572;2894;2006;1923;.
"Unknown";.;.;.;.;.;.;.;.;.;.;.;.
"""

# Read the data correctly, skipping the first two lines which are headers
df = pd.read_csv(io.StringIO(csv_data), sep=";", skiprows=2)

# Rename the first column
df = df.rename(columns={df.columns[0]: "origin"})

# Convert all columns except first to numeric (turning '.' to NaN)
for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Now fill the missing values
# Fill first column NaNs with second column's values
df.iloc[:, 1] = df.iloc[:, 1].fillna(df.iloc[:, 2])

# Fill last column NaNs with second-to-last column's values
df.iloc[:, -1] = df.iloc[:, -1].fillna(df.iloc[:, -2])

# Create a new DataFrame with just the country names
df_total = df[['origin']].copy()

# Calculate the sum of all numeric columns (excluding the 'country' column)
df_total['total'] = df.select_dtypes(include='number').sum(axis=1)

import plotly.express as px

# Skip first two rows ("Total" and "Foreign national, total") and get top 5 countries
top_countries = df_total.iloc[3:].sort_values('total', ascending=False).head(5)

# Create the bar chart
fig = px.bar(top_countries,
             x='origin',
             y='total',
             #title='Top 5 Countries by Guest Nights',
             labels={'total': 'Total Guest Nights', 'origin': 'Origin'},
             color='origin')

# Customize the layout
fig.update_layout(
    xaxis_title='Origin',
    yaxis_title='Total Guest Nights',
    showlegend=False
)

# Show the plot
fig.write_html("top_origin_countries.html", full_html=True, include_plotlyjs='cdn', config={"responsive": True})