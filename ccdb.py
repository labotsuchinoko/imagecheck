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
    model = peewee.TextField()
    predict_date = peewee.DateTimeField()

def createTable():
    try:
        PredictDb.create_table()
    except Exception as e:
        print "create table error is "+str(e)
        pass

class InsertDB:

    def __init__(self, url, predict_url, result, model):
        self.url = url
        self.predict_url = predict_url
        self.result = result
        self.model = model

    def insertData(self):
        try:
            PredictDb.create(result = self.result,
                            input_url = self.url,
                            predict_url = self.predict_url,
                            model = self.model,
                            predict_date = datetime.datetime.now())

        except Exception as e:
            print "insertdata error is "+str(e)
            pass

#print len(ccdb.PredictDb.select())
