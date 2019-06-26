from django.contrib import admin
from conduit import models
# Register your models here.

admin.site.register([
    models.Article,
    models.Tag
])