from rest_framework import serializers

from contact.models import Contact
from django.contrib.auth import get_user_model


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name']


class ContactDetailsSerializer(serializers.ModelSerializer):
    owner = ContactOwnerSerializer()

    class Meta:
        model = Contact
        fields = ('name', 'phone', 'owner')
