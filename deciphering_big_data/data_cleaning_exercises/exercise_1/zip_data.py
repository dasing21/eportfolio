from csv import reader

data_rdr = reader(open("data/unicef/mn.csv", "r"))

header_rdr = reader(open("data/unicef/mn_headers_updated.csv", "r"))

data_rows = [d for d in data_rdr]
header_rows = [h for h in header_rdr if h[0] in data_rows[0]]

all_short_headers = [h[0] for h in header_rows]

skip_index = []
final_header_rows = []

for header in data_rows[0]:
    if header not in all_short_headers:
        index = data_rows[0].index(header)
        skip_index.append(index)
    else:
        for head in header_rows:
            if head[0] == header:
                final_header_rows.append(head)
                break

new_data = []

for row in data_rows[1:]:
    new_row = []
    for i, d in enumerate(row):
        if i not in skip_index:
            new_row.append(d)
    new_data.append(new_row)

zipped_data = []

for drow in new_data:
    zipped_data.append(list(zip(final_header_rows, drow)))

## Print question and answer
# for x in zipped_data[0]:
#     print("Question: {[1]}\nAnswer: {}".format(x[0], x[1]))

# # Print data entries
# for x in enumerate(zipped_data[0][:20]):
#     print(x)

# Print start time
# from datetime import datetime

# start_string = "{}/{}/{} {}:{}".format(
#     zipped_data[0][8][1],
#     zipped_data[0][7][1],
#     zipped_data[0][9][1],
#     zipped_data[0][13][1],
#     zipped_data[0][14][1],
# )
# print("Start string is ", start_string)
# start_time = datetime.strptime(start_string, "%m/%d/%Y %H:%M")
# print("Start time is ", start_time)

# Print end time
# end_time = datetime(
#     int(zipped_data[0][9][1]),
#     int(zipped_data[0][8][1]),
#     int(zipped_data[0][7][1]),
#     int(zipped_data[0][15][1]),
#     int(zipped_data[0][16][1]),
# )
# print('End time is ', end_time)

# # Print duration of first interview
# duration = end_time - start_time
# print('Duration is ', duration)
# print('Duration in days', duration.days)
# print('Duration in seconds: ', duration.total_seconds())
# minutes = duration.total_seconds() / 60
# print('Duration in minutes: ', minutes)

# Convert datatime object into different formatted strings
# print('strftime format: ', end_time.strftime('%m/%d/%Y %H:%M:%S'))
# print('ctime format: ', start_time.ctime())
# print('PHP format: ', start_time.strftime('%Y-%m-%dT%H:%M:%S'))

# # Try to locate missing data
# for row in zipped_data:
#     for answer in row:
#         if answer[1] is None:
#             print(answer)

# # Try to locate NA answers
# na_count = {}

# for row in zipped_data:
#     for resp in row:
#         question = resp[0][1]
#         answer = resp[1]
#         if answer == 'NA':
#             if question in na_count.keys():
#                 na_count[question] += 1
#             else:
#                 na_count[question] = 1
# print(na_count)

# # Fint the datatypes of the responses
# datatypes = {}
# start_dict = {
#     "digit": 0,
#     "boolean": 0,
#     "empty": 0,
#     "time_related": 0,
#     "text": 0,
#     "unknown": 0,
# }
# for row in zipped_data:
#      for resp in row:
#         question = resp[0][1]
#         answer = resp[1]
#         key = 'unknown'
#         if answer.isdigit():
#             key = 'digit'
#         elif answer in ['Yes', 'No', 'True', 'False']:
#             key = 'boolean'
#         elif answer.isspace():
#             key = 'empty'
#         elif answer.find('/') > 0 or answer.find(':') > 0:
#             key = 'time_related'
#         elif answer.isalpha():
#             key = 'text'
#         if question not in datatypes.keys():
#             datatypes[question] = start_dict.copy()
#             datatypes[question][key] += 1
# print(datatypes)

# Write a function to create a unique set
# for x in enumerate(zipped_data[0]):
#     print(x)

# # Find out if each row is a unique entry
# set_of_keys = set(["%s-%s-%s" % (x[0][1], x[1][1], x[2][1]) for x in zipped_data])
# uniques = [
#     x
#     for x in zipped_data
#     if not set_of_keys.remove("%s-%s-%s" % (x[0][1], x[1][1], x[2][1]))
# ]
# print(len(set_of_keys))
