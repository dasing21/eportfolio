# pip install fuzzywuzzy
from fuzzywuzzy import fuzz

my_records = [
    {
        "favorite_book": "Grapes of Wrath",
        "favorite_movie": "Free Willie",
        "favorite_show": "Two Broke Girls",
    },
    {
        "favorite_book": "The Grapes of Wrath",
        "favorite_movie": "Free Willy",
        "favorite_show": "2 Broke Girls",
    },
]
# Find ratio of fuzziness
print(
    fuzz.ratio(my_records[0].get("favorite_book"), my_records[1].get("favorite_book"))
)
print(
    fuzz.ratio(my_records[0].get("favorite_movie"), my_records[1].get("favorite_movie"))
)
print(
    fuzz.ratio(my_records[0].get("favorite_show"), my_records[1].get("favorite_show"))
)

# Compare two strings based on similarity
print(
    fuzz.partial_ratio(
        my_records[0].get("favorite_book"), my_records[1].get("favorite_book")
    )
)
print(
    fuzz.partial_ratio(
        my_records[0].get("favorite_movie"), my_records[1].get("favorite_movie")
    )
)
print(
    fuzz.partial_ratio(
        my_records[0].get("favorite_show"), my_records[1].get("favorite_show")
    )
)
