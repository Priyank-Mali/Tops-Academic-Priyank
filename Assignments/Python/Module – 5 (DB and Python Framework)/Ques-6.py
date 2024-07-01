# Mention what command line can be used to load data into Django?

"""
python manage.py loaddata <fixture_filename>

This command is typically used to load data from files into our database.
files can be --> JSON / XML format

example:
if you have a JSON file: initial_data.json

python manage.py loaddata initial_data.json

--> this command reads the data from the file and inserts it into the appropriate database tables
"""