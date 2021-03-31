import flask
import elasticsearch


app = flask.Flask(__name__)
es = elasticsearch.Elasticsearch("http://localhost:9201")


@app.route('/')
def home():
    resp = es.search(
        index="superdesk_archive",
        body={"query": {"match_all": {}}},
        size=20,
    )

    return {"resp": resp}
