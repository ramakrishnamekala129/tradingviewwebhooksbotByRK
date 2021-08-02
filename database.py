from pymongo import MongoClient

client=MongoClient('localhost',27017)
# Create Flask object called app.


db=client.bot_database
dbnse=client.nse_data
collection=db.bot_collections