import peewee
import ccdb

for p in ccdb.PredictDb.select():
    print p.result, p.input_url, p.predict_url, p.model, p.predict_date

query = ccdb.PredictDb.select().where(ccdb.PredictDb.model == 'a_b_pu_model_v1')
for a in query:
    print a.model, a.predict_date
