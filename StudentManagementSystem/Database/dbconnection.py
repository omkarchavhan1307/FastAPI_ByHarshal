from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("MongoDbUrl")

connectionstring = MongoClient(url)
# connectionstring = MongoClient("mongodb+srv://harshghorpade4150_db_user:Ki7xyv8qmiU6rEiP@cluster0.kdm1efq.mongodb.net/?appName=Cluster0")

DatabaseName = connectionstring["StudentDb"]

collectionName = DatabaseName["studentList"]