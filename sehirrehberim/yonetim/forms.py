from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from yonetim.models import *
from django.db.models.signals import post_save
from django import forms

class KullaniciKayitFormu(UserCreationForm):
    class Meta:
        model=User
        fields=('first_name','last_name','username','email')
        
    def clean_email(self):
        if not self.cleaned_data['email']:
            raise forms.ValidationError(u'E-posta adresi girmelisiniz')
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(
                u'''Bu e-posta adresine sahip kullanici mevcut.
                Baska bir e-posta adresi kullanin''')
        return self.cleaned_data['email']
        
class AramaFormu(forms.Form):
    aranacak_kelime=forms.CharField()
    
    def clean_aranacak_kelime(self):
        kelime=self.cleaned_data['aranacak_kelime']
        if len(kelime) < 3:
            raise forms.ValidationError('Aranacak kelime 3 harften az olamaz!')
        return kelime
        

class KampanyaFormu(forms.Form):
    firma=forms.CharField(widget=forms.TextInput(attrs={'size':53}))
    kategori=forms.CharField(widget=forms.TextInput(attrs={'size':53}))
    enlem=forms.CharField(widget=forms.TextInput(attrs={'size':53}))
    boylam=forms.CharField(widget=forms.TextInput(attrs={'size':53}))
    baslik=forms.CharField(widget=forms.TextInput(attrs={'size':53}))
    icerik = forms.CharField(widget=forms.Textarea(attrs={'rows':8, 'cols':50}))