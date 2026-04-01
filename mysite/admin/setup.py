from .views import UserProfileAdmin, CityAdmin, RegionAdmin, DistrictAdmin, PropertyAdmin, ReviewAdmin
from fastapi import FastAPI
from sqladmin import Admin
from mysite.database.db import engine


def setup_admin(mysite: FastAPI):
    admin = Admin(mysite, engine)
    admin.add_view(UserProfileAdmin)
    admin.add_view(RegionAdmin)
    admin.add_view(DistrictAdmin)
    admin.add_view(CityAdmin)
    admin.add_view(PropertyAdmin)
    admin.add_view(ReviewAdmin)
