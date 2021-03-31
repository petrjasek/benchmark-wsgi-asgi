import fastapi
import elasticsearch


app = fastapi.FastAPI()
es = elasticsearch.AsyncElasticsearch("http://localhost:9201")


@app.get("/")
async def home():
    resp = await es.search(
        index="superdesk_archive",
        body={"query": {"match_all": {}}},
        size=20,
    )

    return {"resp": resp}
