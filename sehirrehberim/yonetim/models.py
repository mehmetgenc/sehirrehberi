from django.db import models

# Create your models here.

class Kampanya(models.Model):
    olusturulma = models.DateTimeField(auto_now_add=True)
    firma = models.CharField(max_length=200)
    kategori = models.CharField(max_length=100)
    enlem = models.CharField(max_length=50)
    boylam = models.CharField(max_length=50)
    baslik = models.CharField(max_length=200, blank=True, default='')
    icerik = models.TextField()
    onay = models.BooleanField(default=False)
    def __unicode__(self):
        return u'%s, %s' %(self.firma, self.baslik)
    class Meta:
        ordering=('olusturulma',)