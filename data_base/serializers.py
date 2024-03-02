from rest_framework import serializers
from .models import Country, Manufacturer, Car, Comment
import requests


class CountrySerializer(serializers.ModelSerializer):
    manufacturers = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'name', 'manufacturers']


class CarSerializer(serializers.ModelSerializer):
    # manufacturer = serializers.StringRelatedField(read_only=True)
    manufacturer = serializers.SlugRelatedField(queryset=Manufacturer.objects.all(), slug_field='name')
    comments = serializers.StringRelatedField(many=True, read_only=True)
    # comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ['id', 'name', 'manufacturer', 'comments', 'comments_count']

    def get_comments_count(self, car):
        return car.comments.count()


class CarSerializerComment(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ['name', 'comments_count']

    def get_comments_count(self, car):
        return car.comments.count()


class ManufacturerSerializer(serializers.ModelSerializer):
    # country = serializers.StringRelatedField(read_only=True)
    country = serializers.SlugRelatedField(queryset=Country.objects.all(), slug_field='name')
    # cars = serializers.StringRelatedField(many=True, read_only=True)
    cars = CarSerializerComment(many=True, read_only=True)

    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'country', 'cars']


class CommentSerializer(serializers.ModelSerializer):
    car = serializers.SlugRelatedField(queryset=Car.objects.all(), slug_field='name')

    class Meta:
        model = Comment
        fields = ['id', 'e_mail', 'time_created', 'time_updated', 'comment', 'car']

    def validate_comment(self, comment):
        if comment == '':
            raise serializers.ValidationError('The field can\'t be empty')
        return comment

    def validate_e_mail(self, e_mail):
        if e_mail == '':
            raise serializers.ValidationError('The field can\'t be empty')
        return e_mail


