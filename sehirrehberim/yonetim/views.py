# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import *
from django.http import *
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from yonetim.forms import *
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from yonetim.models import Kampanya
from yonetim.serializers import KampanyaSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view




# Create your views here.
@login_required        
def yonetim(request):
    return render_to_response('yonetim.html',locals())
    
def register(request):
    if request.method == 'POST':
        form=KullaniciKayitFormu(request.POST)
        if form.is_valid():
            form.save()
            kullanici=authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            if kullanici.is_authenticated():
                login(request,kullanici)
            return HttpResponseRedirect("/yonetim/")
    else:
        form=KullaniciKayitFormu()
    return render_to_response('registration/register.html',locals(),context_instance=RequestContext(request))
    
    
@login_required
def kampanya_listesi(request):
    kampanya_tumu=Kampanya.objects.all()
    arama_formu=AramaFormu()
    if request.GET.get('aranacak_kelime'):
        arama_formu=AramaFormu(request.GET)
        if arama_formu.is_valid():
            aranacak_kelime=arama_formu.cleaned_data['aranacak_kelime']
            kampanya_tumu=Kampanya.objects.filter(Q(icerik__contains=aranacak_kelime)
            | Q(baslik__contains=aranacak_kelime) | Q(firma__contains=aranacak_kelime)
            | Q(kategori__contains=aranacak_kelime))
        
    sayfa = request.GET.get('sayfa',1)
    kampanya_sayfalari=Paginator(kampanya_tumu,5)#5
    kampanya_verileri=kampanya_sayfalari.page(int(sayfa))
    return render_to_response("kampanya_listesi.html",locals())    
    
@login_required
def kampanya_ekleme(request):
    if request.method == 'POST':
        form=KampanyaFormu(request.POST)
        if form.is_valid():
            temiz_veri=form.cleaned_data
            kampanya=Kampanya(firma=temiz_veri['firma'], kategori=temiz_veri['kategori'],
                              enlem=temiz_veri['enlem'], boylam=temiz_veri['boylam'],
                              baslik=temiz_veri['baslik'], icerik=temiz_veri['icerik'],  )
            kampanya.save()
            return HttpResponseRedirect('/kampanya-listesi/')
    else:
        form=KampanyaFormu()
    return render_to_response('genel_form.html', {'form':form, 'baslik':'Kampanya Ekleme', 'ID':1},context_instance=RequestContext(request))
    
    

@api_view(['GET', 'POST'])
def kampanya_list(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        kampanyalar = Kampanya.objects.all()
        serializer = KampanyaSerializer(kampanyalar, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = KampanyaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def kampanya_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        kampanya = Kampanya.objects.get(pk=pk)
    except Kampanya.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = KampanyaSerializer(kampanya)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = KampanyaSerializer(kampanya, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        kampanya.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)