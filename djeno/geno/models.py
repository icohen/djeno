from django.db import models

class Person(models.Model):
    name     = models.CharField(max_length=64)
    children = models.ManyToManyField('self', 
                                     symmetrical=False,
                                     related_name='parents',
                                     blank=True, null=True)

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='People'

class Event(models.Model):
    date = models.DateField()
    
    def __unicode__(self):
        return self.date.isoformat()

class Birth(Event):
    baby = models.OneToOneField(Person)
    
    def __unicode__(self):
        return 'Birth of {0}'.format(self.baby.name)

class Death(Event):
    deceased = models.OneToOneField(Person)
    
    def __unicode__(self):
        return 'Death of {0}'.format(self.deceased.name)

class MarriageRelation(models.Model):
    person = models.ForeignKey(Person)
    marriage = models.ForeignKey('Marriage')

class Marriage(Event):
    spouses = models.ManyToManyField(Person, through=MarriageRelation)
    end_date = models.DateField(blank=True, null=True)
    
    @property
    def start_date(self):
        return self.date        
    
    def __unicode__(self):
        spouse_names_list = self.spouses.values('name', flat=True)
        formatted_spouses = ' and '.join(spouse_names_list)
        return 'Marriage between {0}'.format(formatted_spouses)
    