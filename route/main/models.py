from django.db import models

class Stations(models.Model):
    title = models.TextField('Станция')
    num_of_line = models.IntegerField('Номер линии')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'
