from django.contrib import admin
from djeno.geno import models

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
    # verbose names below are a hack otherwise these show up as MarriageRelations instead of Marriages in the PersonAdmin
    verbose_name_plural = 'Marriages'
    verbose_name = 'Marriage'
    extra = 0

class MarriageRelationInline(Inline):
    model = models.MarriageRelation
    extra = 2

class PersonAdmin(admin.ModelAdmin):
    inlines = [BirthInline, DeathInline, MarriageInline]

class MarriageAdmin(admin.ModelAdmin):
    model = models.Marriage
    inlines = [MarriageRelationInline]



admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Marriage, MarriageAdmin)


