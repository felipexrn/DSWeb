from django.contrib import admin
from .models import Laboratorio, Computador

class ComputadorInline(admin.TabularInline):
    model = Computador
    extra = 1
    show_change_link = True
    list_display = ['patrimonio', 'identificador','ligado']
    list_filter = ['ligado']
    search_fields = ['patrimonio']
    
class LaboratorioAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['nome']})]
    inlines = [ComputadorInline]
admin.site.register(Laboratorio, LaboratorioAdmin)
