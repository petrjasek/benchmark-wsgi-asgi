import flask
import random
import pymongo
import elasticsearch


app = flask.Flask(__name__)
es = elasticsearch.Elasticsearch("http://localhost:9201")
mongo = pymongo.MongoClient()


@app.route('/')
def home():
    token = mongo["superdesk"]["auth"].find_one()

    resp = es.search(
        index="superdesk_archive",
        body={"query": {"bool": {
            "must": {"term": {"urgency": random.choice([2, 3, 4, 5, 6])}}
        }}},
        size=20,
    )

    return {
        "resp": resp,
        "token": str(token["_id"]),
    }
