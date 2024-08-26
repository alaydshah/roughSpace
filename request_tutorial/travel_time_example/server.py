from fastapi import FastAPI, HTTPException

app = FastAPI()

# Dummy data for place IDs and travel times
PLACE_IDS = {
    "Start": "place_id_1",
    "Resort A": "place_id_2",
    "Resort B": "place_id_3",
    "Resort C": "place_id_4",
    "Resort D": "place_id_5"
}

TRAVEL_TIMES = {
    ("place_id_1", "place_id_2"): 10,
    ("place_id_1", "place_id_3"): 15,
    ("place_id_1", "place_id_4"): 20,
    ("place_id_1", "place_id_5"): 25,
    ("place_id_2", "place_id_3"): 30,
    ("place_id_2", "place_id_4"): 35,
    ("place_id_2", "place_id_5"): 40,
    ("place_id_3", "place_id_4"): 45,
    ("place_id_3", "place_id_5"): 50,
    ("place_id_4", "place_id_5"): 55,
    # Reverse routes
    ("place_id_2", "place_id_1"): 10,
    ("place_id_3", "place_id_1"): 15,
    ("place_id_4", "place_id_1"): 20,
    ("place_id_5", "place_id_1"): 25,
    ("place_id_3", "place_id_2"): 30,
    ("place_id_4", "place_id_2"): 35,
    ("place_id_5", "place_id_2"): 40,
    ("place_id_4", "place_id_3"): 45,
    ("place_id_5", "place_id_3"): 50,
    ("place_id_5", "place_id_4"): 55,
}


@app.get("/get_place_id")
async def get_place_id(place_name: str):
    place_id = PLACE_IDS.get(place_name, None)
    if not place_id:
        raise HTTPException(status_code=400, detail="Invalid place name")
    return {"place_id": place_id}


@app.get("/get_travel_time")
async def get_travel_time(place_id1: str, place_id2: str):
    travel_time = TRAVEL_TIMES.get((place_id1, place_id2), None)
    if not travel_time:
        raise HTTPException(status_code=400, detail="Invalid place IDs or no travel time available")
    return {"travel_time": travel_time}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)