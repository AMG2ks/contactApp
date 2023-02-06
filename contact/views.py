from django.shortcuts import render
from django.views.generic import DeleteView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.parsers import FormParser, MultiPartParser

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from contact.models import Contact
from contact.serializers import ContactSerializer, ContactDetailsSerializer


# Create your views here.
class ContactListAPIView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Contact.objects.all()
    serializer_class = ContactDetailsSerializer
    lookup_field = 'pk'


class ContactCreateAPIView(CreateAPIView):
    parser_classes = (FormParser, MultiPartParser)
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'pk'


class ContactDetailsAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Contact.objects.all()
    serializer_class = ContactDetailsSerializer
    lookup_field = 'pk'


class ContactDeleteAPIView(DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'pk'
