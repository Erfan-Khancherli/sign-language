from rest_framework import serializers

from .models import Packages , UserPackage
from word.models import Category
from word.serializers import Categoryserializer , Categorypackageserializer

class PackageSerializer(serializers.ModelSerializer):
    included_categories = Categoryserializer(many=True, read_only=True, source='get_categories')
    categories = serializers.PrimaryKeyRelatedField(required = True,
        many=True, queryset=Category.objects.all()
    )

    class Meta:
        model = Packages
        fields = [
            "id", "name", "description", "price", "duration_days","categories",
            "created_at","created_by","updated_at", "included_categories"
        ]

    def get_categories(self, obj):
        return Category.objects.filter(packagecategory__package=obj)


class PackagelistSerializer(serializers.ModelSerializer):
    included_categories = Categoryserializer(many=True, read_only=True, source='get_categories')
    categories = Categorypackageserializer(many=True, read_only=True)

    class Meta:
        model = Packages
        fields = [
            "id", "name", "description", "price", "duration_days","categories",
            "created_at","created_by","updated_at", "included_categories"
        ]

    def get_categories(self, obj):
        return Category.objects.filter(packagecategory__package=obj)
class UserPackageSerializer(serializers.ModelSerializer):
    package = PackageSerializer(read_only=True)   # nested package info
    package_id = serializers.IntegerField(write_only=True)  # used for input

    class Meta:
        model = UserPackage
        fields = [
            "id",
            "package",       # full package details (nested)
            "package_id",    # for creating purchases
            "start_date",
            "end_date",
            "is_active",
            "payment_id",
        ]