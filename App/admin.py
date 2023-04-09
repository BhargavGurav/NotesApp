from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "टिप्पणीपुस्तिका | administration"

admin.site.register(Created)
admin.site.register(Uploaded)

