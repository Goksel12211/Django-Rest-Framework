from django.contrib import admin

# Register your models here.
from .models import WatchList,StreamPlatform
admin.site.register(WatchList)
admin.site.register(StreamPlatform) 