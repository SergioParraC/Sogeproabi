from django.contrib import admin
from apps.supplies.models import *

class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'unit')

class MaterialsFamilyAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

class LabourAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

admin.site.register(MaterialsFamilyModel, MaterialsFamilyAdmin)
admin.site.register(MaterialsModel, MaterialsAdmin)
admin.site.register(LabourModel, LabourAdmin)