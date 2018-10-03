from importlib.resources import open_text
import json
import random
import time

import prometheus_client

from . import data


with open_text(data, 'emoji-test.json') as file:
    emojis = json.load(file)

categories = dict()
categories["cat1"] = {
    "name": "Caras",
    "icon": "😋",
    "emojis": emojis["face-positive"] + emojis["face-neutral"] + emojis["face-negative"]
}

categories["cat2"] = {
    "name": "Animales",
    "icon": "🐈",
    "emojis": emojis["animal-mammal"] + emojis["animal-bird"] + \
              emojis["animal-reptile"] + emojis["animal-marine"] + emojis["animal-bug"]
}

categories["cat3"] = {
    "name": "Vegetales",
    "icon": "🍅",
    "emojis": emojis["food-fruit"] + emojis["food-vegetable"]
}

categories["cat4"] = {
    "name": "Comida",
    "icon": "🍔",
    "emojis": emojis["food-prepared"] + emojis["food-asian"] + emojis["food-sweet"]
}

categories["cat5"] = {
    "name": "Transporte",
    "icon": "🚅",
    "emojis": emojis["transport-ground"] + emojis["transport-water"] + emojis["transport-air"]
}

categories["cat6"] = {
    "name": "Banderas",
    "icon": "🇪🇸",
    "emojis": emojis["country-flag"]
}


def get_random_category():
    return random.choice(list(categories.keys()))


vending_emoji_cooking_duration_hist = prometheus_client.Histogram(
    "vending_emoji_cooking_duration_seconds",
    "Emoji cooking time duration",
    [],
    buckets=[0.1, 0.3, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 8.0, float("inf")]
)


@vending_emoji_cooking_duration_hist.time()
def request_emoji(category):
    emojis = categories[category]["emojis"]

    time.sleep(random.lognormvariate(0.2, 1))

    emoji = random.choice(emojis)
    return emoji
