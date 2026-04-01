from mysite.database.models import (UserProfile, City, Review,
                                    Region, District, Property)
from sqladmin import ModelView


class UserProfileAdmin(ModelView, model=UserProfile):
    column_list = [UserProfile.first_name, UserProfile.username]


class CityAdmin(ModelView, model=City):
    column_list = [City.id, City.name]


class RegionAdmin(ModelView, model=Region):
    column_list = [Region.name]


class DistrictAdmin(ModelView, model=District):
    column_list = [District.name]


class PropertyAdmin(ModelView, model=Property):
    column_list = [Property.description]


class ReviewAdmin(ModelView, model=Review):
    column_list = [Review.id]