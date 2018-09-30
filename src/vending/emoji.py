from importlib.resources import open_text
import json
import random

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


def request_emoji(category):
    emoji = random.choice(categories[category]["emojis"])
    return emoji
