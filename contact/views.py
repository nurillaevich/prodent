from django.shortcuts import render
from rest_framework import generics
from .models import Contact, ContactInfo
from .serializers import ContactSerializer, ContactInfoSerializer


class ContactView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactInfoView(generics.ListAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
