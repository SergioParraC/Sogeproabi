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

admin.site.register(ToolsModel, MaterialsAdmin)
admin.site.register(ToolsFamilyModel, MaterialsFamilyAdmin)
admin.site.register(LabourModel, MaterialsAdmin)
admin.site.register(SubcontractJobModel, MaterialsAdmin)
admin.site.register(FreightModel, MaterialsAdmin)
admin.site.register(EquipmentModel, MaterialsAdmin)
admin.site.register(AuxEquipmentModel, MaterialsAdmin)

