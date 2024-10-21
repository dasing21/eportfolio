import re

# Using words
word = '\w+'
sentence = 'Here is my sentence.'
find_all_words = re.findall(word, sentence)
search_result = re.search(word, sentence)
search_result.group()
match_result = re.match(word, sentence)
print('All words in sentence: ', find_all_words)
print('Match of object type word: ', search_result)
print('Matched string: ', search_result.group())
print('First matched word: ', match_result)

# Using numbers and capitalized words
number = '\d+'
capitalized_word = '[A-Z]\w+'
sentence = 'I have 2 pets: Bear and Bunny.'
search_number = re.search(number, sentence)
search_number.group()
match_number = re.match(number, sentence)
#match_number.group()
search_capital = re.search(capitalized_word, sentence)
search_capital.group()
match_capital = re.match(capitalized_word, sentence)
#match_capital.group()
print(search_number)
print(search_number.group())
print(match_number)
#print(match_number.group())
print(search_capital)
print(search_capital.group())
print(match_capital)
#print(match_capital.group())

# Using names
name_regex = '([A-Z]\w+) ([A-Z]\w+)'
names = "Barack Obama, Ronald Reagan, Nancy Drew"
name_match = re.match(name_regex, names)
name_match.group()
name_match.groups()
name_regex = '(?P<first_name>[A-Z]\w+) (?P<last_name>[A-Z]\w+)'
for name in re.finditer(name_regex, names):
    print('Meet {}!'.format(name.group('first_name')))