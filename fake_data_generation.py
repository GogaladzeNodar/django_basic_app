import json
from faker import Faker
import random
from datetime import datetime
import pytz


utc_timezone = pytz.timezone("UTC")

fake = Faker()

CategoryNumber = 100
ProductNumber = 500

Categories = []
Products = []

for i in range(1, CategoryNumber):
    ParentId = (
        random.randint(1, i - 1)
        if i > 1 and random.choice([True, False])
        else None  # aq i > 1-ze pirobis gareShe reinjidan amovarda da daerorda pirveli cdisas
    )
    Categories.append(
        {
            "model": "store.category",
            "pk": i,
            "fields": {
                "name": fake.word(),
                "parent": ParentId,  # ,
                "description": fake.text(),
                "is_active": random.choice([True, False]),
                "created_at": fake.date_time_between(
                    start_date=datetime(2000, 1, 1),
                    end_date=datetime(2019, 12, 31),
                )
                .astimezone(utc_timezone)
                .isoformat(),
                "updated_at": fake.date_time_between(
                    start_date=datetime(2020, 1, 1),
                    end_date=datetime.today(),
                )
                .astimezone(utc_timezone)
                .isoformat(),
            },
        }
    )

with open("fixtures/categories.json", "w") as f:
    json.dump(Categories, f, indent=4)


for i in range(1, ProductNumber):
    RandCategories = random.sample(range(1, CategoryNumber), random.randint(1, 4))
    Products.append(
        {
            "model": "store.product",
            "pk": i,
            "fields": {
                "name": fake.word(),
                "categories": RandCategories,
                "description": fake.text(),
                "price": round(random.uniform(1, 5000), 2),
                "image": "media/images/products/29051711_1.jpg",
                "stock": random.randint(1, 500),
                "created_at": fake.date_time_between(
                    start_date=datetime(2000, 1, 1),
                    end_date=datetime(2019, 12, 31),
                )
                .astimezone(utc_timezone)
                .isoformat(),
                "updated_at": fake.date_time_between(
                    start_date=datetime(2020, 1, 1),
                    end_date=datetime.today(),
                )
                .astimezone(utc_timezone)
                .isoformat(),
            },
        }
    )

with open("fixtures/products.json", "w") as f:
    json.dump(Products, f, indent=4)

with open("fixtures/categories.json", "w") as f:
    json.dump(Categories, f, indent=4)


# problemebi rac unda wavikitxo paralelurad
# romeli drois formatebi ar ikasteba JSON-ad
# timezonis gareshe ratom ar mushaobs
