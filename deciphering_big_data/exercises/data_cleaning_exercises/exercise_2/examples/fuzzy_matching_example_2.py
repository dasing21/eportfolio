from fuzzywuzzy import fuzz

# Use token_sort_ratio method to match strings despite order of words
my_records = [
    {
        "favorite_food": "cheeseburgers with bacon",
        "favorite_drink": "wine, beer, and tequila",
        "favorite_dessert": "cheese or cake",
    },
    {
        "favorite_food": "burgers with cheese and bacon",
        "favorite_drink": "beer, wine, and tequila",
        "favorite_dessert": "cheese cake",
    },
]
print(
    fuzz.token_sort_ratio(
        my_records[0].get("favorite_food"), my_records[1].get("favorite_food")
    )
)
print(
    fuzz.token_sort_ratio(
        my_records[0].get("favorite_drink"), my_records[1].get("favorite_drink")
    )
)
print(
    fuzz.token_sort_ratio(
        my_records[0].get("favorite_dessert"), my_records[1].get("favorite_dessert")
    )
)

# Use extract method to compare possible matches and extractOne to get best match
from fuzzywuzzy import process

choices = ["Yes", "No", "Maybe", "N/A"]
print(process.extract("ya", choices, limit=2))
print(process.extractOne("ya", choices))
print(process.extract("nope", choices, limit=2))
print(process.extractOne("nope", choices))
