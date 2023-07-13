from django.contrib import admin
from .models import Laboratorio, Computador, Mac

class MacInline(admin.TabularInline):
    model = Mac
    extra = 1
    list_display = ['computador','mac']
    list_filter = ['mac']
    search_fields = ['mac']

class ComputadorAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['patrimonio'], 'fields': ['ligado'],})]
    inlines = [MacInline]
admin.site.register(Computador, ComputadorAdmin)

class ComputadorInline(admin.TabularInline):
    model = Computador
    extra = 1
    show_change_link = True
    list_display = ['patrimonio', 'ligado']
    list_filter = ['ligado']
    search_fields = ['patrimonio']
    
class LaboratorioAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['nome']})]
    inlines = [ComputadorInline]
admin.site.register(Laboratorio, LaboratorioAdmin)
