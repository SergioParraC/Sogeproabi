from django.contrib import admin
from apps.APUs.models import *
# Register your models here.

class APIsAdmin(admin.ModelAdmin):
    list_display = ('description',)

class MaterialRelationAdmin(admin.ModelAdmin):
    list_display = ('id_materials',)

admin.site.register(AnalysisOfUnitaryPricesModel, APIsAdmin)
admin.site.register(MaterialsRelationshipModel, MaterialRelationAdmin)