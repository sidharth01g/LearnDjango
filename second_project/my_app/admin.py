from django.contrib import admin
from .models import Topic, AccessRecord, WebPage

# Register your models here.
admin.site.register(Topic)
admin.site.register(AccessRecord)
admin.site.register(WebPage)
