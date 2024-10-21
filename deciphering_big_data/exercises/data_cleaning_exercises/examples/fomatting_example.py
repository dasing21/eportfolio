example_dict = {
    'float_number': 1324.321325493,
    'very_large_integer': 43890923148390284,
    'percentage': .324,
    }
string_to_print = "float: {float_number:.4f}\n" 
string_to_print += "integer: {very_large_integer:,}\n" 
string_to_print += "percentage: {percentage:.2%}"
print(string_to_print.format(**example_dict))