import configparser
import json
from mongoengine import connect, disconnect_all
from mongoengine.fields import ListField, StringField, ReferenceField
from pathlib import Path

config_ini = Path(__file__).parent.parent.joinpath("config.ini")

config = configparser.ConfigParser()
config.read(config_ini)

mongodb_pass = config.get("DB", "PASS")
mongo_user = config.get("DB", "user")
db_name = config.get("DB", "db_name")
domain = config.get("DB", "domain")

disconnect_all()
connection_url = f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority"
connect(host=connection_url, ssl=True)
