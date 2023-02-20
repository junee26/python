import fastapi
app = fastapi.FastAPI()

@app.get("/")
def hello():
    print("hellow world")
