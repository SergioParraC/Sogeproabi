from django.contrib import admin
from apps.supplies.models import *
# Register your models here.

class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'unit')

class MaterialsFamilyAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

admin.site.register(MaterialsFamilyModel, MaterialsFamilyAdmin)
admin.site.register(MaterialsModel, MaterialsAdmin)
admin.site.register(ToolsModel, MaterialsAdmin)
admin.site.register(ToolsFamilyModel, MaterialsFamilyAdmin)
admin.site.register(LabourModel, MaterialsAdmin)