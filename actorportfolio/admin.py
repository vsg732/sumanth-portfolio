from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PortfolioData, Filmography

class FilmographyInline(admin.TabularInline):
    model = Filmography
    extra = 1

class PortfolioAdmin(admin.ModelAdmin):
    inlines = [FilmographyInline]

admin.site.register(PortfolioData, PortfolioAdmin)