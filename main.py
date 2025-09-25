from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hellow2 from FastAPIdasdasdas3232"}
