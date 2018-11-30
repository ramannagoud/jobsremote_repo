from django.contrib import admin
from testapp.models import Jobs

# Register your models here.
class JobsAdmin(admin.ModelAdmin):
    list_display=['date','companyname','title','eligibility','address','email','phoneno']

admin.site.register(Jobs,JobsAdmin)
