import json
import os

MEMORY_FILE = "memory.json"

def load_memory():

    if os.path.exists(MEMORY_FILE):

        with open(MEMORY_FILE, "r") as f:
            return json.load(f)

    return {}

def save_memory(data):

    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f)

def remember(key, value):

    data = load_memory()

    data[key] = value

    save_memory(data)

def recall(key):

    data = load_memory()

    return data.get(key, None)