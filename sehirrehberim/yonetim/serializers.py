__author__ = 'mehmetgenc'
# -*- coding: utf-8 -*-
from django.forms import widgets
from rest_framework import serializers
from yonetim.models import Kampanya

class KampanyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kampanya
        fields = ('id','olusturulma','kategori','firma', 'baslik', 'icerik','enlem','boylam', 'onay',)

