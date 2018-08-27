from django.contrib import admin
from .models import Protocol,Med,Lab,PreMed,PrnMed,Hydration, Condition,HomeMeds

# Register your models here.

class MedInstanceInline(admin.StackedInline):
    model = Med
    extra = 0

class LabInstanceInline(admin.TabularInline):
    model = Lab
    extra = 0

class PreMedInstanceInline(admin.StackedInline):
    model = PreMed
    extra = 0

class PrnMedInstanceInline(admin.StackedInline):
    model = PrnMed
    extra = 0

class HydrationInstanceInline(admin.StackedInline):
    model = Hydration
    extra = 0

class ConditionInstanceInline(admin.StackedInline):
    model = Condition
    extra = 0

class HomeMedsInstanceInline(admin.StackedInline):
    model = HomeMeds
    extra = 0


@admin.register(Protocol)
class ProtocolAdmin(admin.ModelAdmin):
    list_display = ('name', 'request', 'date_request',)
    fields = ['name', 'slug', 'request', 'date_request','priority','division','keyword','disease_state','number_of_cycles','duration_of_cycles','citation']
    prepopulated_fields = {"slug": ("name",)}
    inlines = [HomeMedsInstanceInline,ConditionInstanceInline,PreMedInstanceInline,PrnMedInstanceInline,HydrationInstanceInline,MedInstanceInline,LabInstanceInline]
