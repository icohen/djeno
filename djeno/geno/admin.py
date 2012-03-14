from django.contrib import admin
from geno import models

class OneToOneInline(admin.StackedInline):
    template = 'geno/admin/onetoonestacked.html'

class Inline(admin.StackedInline):
    template = 'geno/admin/stacked.html'


class BirthInline(OneToOneInline):
    model = models.Birth
    
class DeathInline(OneToOneInline):
    model = models.Death
    

class MarriageInline(Inline):
    model = models.Marriage.spouses.through
    # verbose names below are a hack otherwise these show up as Spouses instead of Marriages in the PersonAdmin
    verbose_name_plural = 'Marriages'
    verbose_name = 'Marriage'
    extra = 0

class SpouseInline(Inline):
    model = models.Spouse
    extra = 2

class PersonAdmin(admin.ModelAdmin):
    inlines = [BirthInline, DeathInline, MarriageInline]

class MotherAdmin(PersonAdmin):
    model = models.Mother

class FatherAdmin(PersonAdmin):
    model = models.Father

class MarriageAdmin(admin.ModelAdmin):
    model = models.Marriage
    inlines = [SpouseInline]



admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Marriage, MarriageAdmin)
admin.site.register(models.Mother, MotherAdmin)
admin.site.register(models.Father, FatherAdmin)


