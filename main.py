from fastapi import FastAPI
import os
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "This is an API developed by Hexaorzo to fetch bank details from IFSC code"}

@app.get("/{ifsc}")
async def read_item(ifsc):
    if len(ifsc) > 4:
        bank = ifsc[:4]
        if os.path.isfile("bank/" + bank + ".json"):
            with open("bank/" + bank + ".json", "r") as f:
                data = json.load(f)
                if ifsc in data:
                    return data[ifsc]
                else:
                    return {"error": "IFSC not found"}
        else:
            return {"error": "Bank not found"}
    else:
        return {"error": "Invalid IFSC"}