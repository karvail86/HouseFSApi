from fastapi import FastAPI
import uvicorn

from mysite.api import users, regions, cities, district, property, property_image, property_doc, reviews, auth
from mysite.admin.setup import setup_admin

house_app = FastAPI(title="Karvajl_87")

house_app.include_router(users.user_router)
house_app.include_router(regions.region_router)
house_app.include_router(cities.city_router)
house_app.include_router(district.district_router)
house_app.include_router(property.property_router)
house_app.include_router(property_image.property_image_router)
house_app.include_router(property_doc.property_doc_router)
house_app.include_router(reviews.review_router)
house_app.include_router(auth.auth_router)

setup_admin(house_app)

if __name__ == '__main__':
    uvicorn.run(house_app, host='127.0.0.1', port=8005)
