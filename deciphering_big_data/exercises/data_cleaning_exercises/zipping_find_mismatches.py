from csv import reader

data_rdr = reader(open('data/unicef/mn.csv', 'r'))
header_rdr = reader(open('data/unicef/mn_headers.csv', 'r'))

data_rows = [d for d in data_rdr]
header_rows = [h for h in header_rdr]

# print(len(data_rows[0]))
# print(len(header_rows))
# print(data_rows[0])
# print('-'*124)
# print(header_rows[:2])

bad_rows = []

for h in header_rows:
    if h[0] not in data_rows[0]:
        bad_rows.append(h)

for h in bad_rows:
    header_rows.remove(h)

# print(len(header_rows))

all_short_headers = [h[0] for h in header_rows]

for header in data_rows[0]:
    if header not in all_short_headers:
        print('mismatch!', header)