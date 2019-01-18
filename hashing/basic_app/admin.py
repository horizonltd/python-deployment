from django.contrib import admin
from basic_app.models import UserProfileInfo

# Register your models here.


#Any model registered here you can be able to view
# it through the admin panel
admin.site.register(UserProfileInfo)