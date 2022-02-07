# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/Welcome")
def read_name(name: str):
    return {'Welcome' : f'{name}'}

if __name__ == '__main__' :
    uvicorn.run(app, host='127.0.0.1', port=8000)
    



