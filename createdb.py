import peewee
import datetime

db2 = peewee.SqliteDatabase("data.db")

class BaseModel(peewee.Model):
    class Meta:
        database = db2

class PredictDb(BaseModel):
    result = peewee.TextField()
    input_url = peewee.TextField(unique=True)
    predict_url = peewee.TextField()
    predict_date = peewee.DateTimeField()

def createTable():
    try:
        PredictDb.create_table()
    except Exception as e:
        print "create table error is "+str(e)
        pass

if __name__ == "__main__":
    createTable()
