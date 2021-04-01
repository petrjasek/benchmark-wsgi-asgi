import random
import fastapi
import elasticsearch
import motor.motor_asyncio

from elasticapm.contrib.starlette import make_apm_client, ElasticAPM


apm = make_apm_client({
    "SERVICE_NAME": "asgi",
    "SECRET_TOKEN": "superdesk",
})

app = fastapi.FastAPI()
app.add_middleware(ElasticAPM, client=apm)

es = elasticsearch.AsyncElasticsearch("http://localhost:9201")
mongo = motor.motor_asyncio.AsyncIOMotorClient()


@app.get("/")
async def home():
    token = await mongo["superdesk"]["auth"].find_one()

    resp = await es.search(
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
