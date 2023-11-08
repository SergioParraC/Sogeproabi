from django.contrib import admin
from apps.APUs.models import *
# Register your models here.

class APIsAdmin(admin.ModelAdmin):
    list_display = ('key_user_item','description')


class MaterialRelationAdmin(admin.ModelAdmin):
    list_display = ('get_key_item','id_materials')
    
    def get_key_item(self, obj):
        return obj.id_APU.key_user_item
    
class LabourRelarionshipAdmin(admin.ModelAdmin):
    list_display = ('get_key_item', 'id_labour')

    def get_key_item(self, obj):
        return obj.id_APU.key_user_item

admin.site.register(AnalysisOfUnitaryPricesModel, APIsAdmin)
admin.site.register(MaterialsRelationshipModel, MaterialRelationAdmin)
admin.site.register(LabourRelarionshipModel, LabourRelarionshipAdmin)
