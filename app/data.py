from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    def __init__(self):
        load_dotenv()
        self.client = MongoClient(getenv("MONGO_URI"), tlsCAFile=where())
        self.db = self.client[getenv("MONGO_DB")]
        self.collection = self.db[getenv("MONGO_COLLECTION")]
    
    #turns monster data into dictionaries and then multiplies them (by amount given)
    def seed(self, amount):
        monsters = [Monster().to_dict() for _ in range(amount)]
        self.collection.insert_many(monsters)
    #in case of bad or currpt data
    def reset(self):
        self.collection.delete_many({})

    def count(self) -> int:
        return self.collection.count_documents({})
    #grab the data and turns in into a 2D list for readablitiy by pandas
    def dataframe(self) -> DataFrame:
        documents = list(self.collection.find({}, {'_id': 0}))
        if not documents:
            return DataFrame()

        return DataFrame(documents)
    #converts to HTML for the website
    def html_table(self) -> str:
        df = self.dataframe()
        if df.empty:
            return None
        return df.to_html(index=False, escape=False)


if __name__ == "__main__":
    db = Database()
    db.seed(1000)