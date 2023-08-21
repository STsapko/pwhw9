import part_1_mongo.connect
from part_1_mongo.models import Author, Quote
import json


def insert_to_mongodb():
    authors_json = "authors.json"
    quotes_json = "quotes.json"

    with open(authors_json, "r", encoding="utf-8") as fr:
        authors = json.load(fr)
    with open(quotes_json, "r", encoding="utf-8") as fr:
        quotes = json.load(fr)

    for author in authors:
        Author(
            fullname=author["fullname"],
            born_date=author["born_date"],
            born_location=author["born_location"],
            description=author["description"],
        ).save()

    for quote in quotes:
        author = Author.objects.get(fullname=quote["author"])
        Quote(tags=quote["tags"], author=author, quote=quote["quote"]).save()
