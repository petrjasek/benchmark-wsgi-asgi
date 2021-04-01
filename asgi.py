import fastapi
import elasticsearch
import motor.motor_asyncio


app = fastapi.FastAPI()
es = elasticsearch.AsyncElasticsearch("http://localhost:9201")
mongo = motor.motor_asyncio.AsyncIOMotorClient()


@app.get("/")
async def home():
    token = await mongo["superdesk"]["auth"].find_one()

    resp = await es.search(
        index="superdesk_archive",
        body={"query": {"match_all": {}}},
        size=20,
    )

    return {
        "resp": resp,
        "token": str(token["_id"]),
    }
