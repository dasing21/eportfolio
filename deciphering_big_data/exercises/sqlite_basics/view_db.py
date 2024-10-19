import dataset

db = dataset.connect("sqlite:///data_wrangling.db")
sources = db["data_sources"].all()
for row in sources:
  print(row)