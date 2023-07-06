#!/usr/bin/python3
"""
Feed DB with dummy data
*To Run*
```bash
VIT_ENV=dev VIT_MYSQL_USER=vit_dev VIT_MYSQL_PWD=vit_dev_pwd\
VIT_MYSQL_DB=vit_db VIT_MYSQL_HOST=localhost python3 feed_db.py
```
"""
from os import path
import json
from models import storage
from models.brand import Brand
from models.detail_point import DetailPoint
from models.work import Work

with open("dummy_data.json", "r") as file:
    list_json = json.load(file)

for data in list_json:
    brand = Brand(**data)
    brand.save()
    for item in data["detail_points"]:
        point = DetailPoint(content=item["content"], brand_id=brand.id)
        point.save()
    for item in data["works"]:
        work = Work(**item)
        work.brand_id = brand.id
        work.save()

storage.close()
