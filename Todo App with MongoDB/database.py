from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb+srv://hamzaaftab992:hamzakhan@cluster0.cm5lq.mongodb.net"
DATABASE_NAME = "todo_db"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]

def get_database():
    return db