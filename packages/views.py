from django.shortcuts import render
from .serializers import PackageSerializer , UserPackageSerializer , PackagelistSerializer
from .models import Packages ,PackageCategory , UserPackage
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from word.models import Category
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from datetime import date, timedelta
from django.shortcuts import get_object_or_404




# class PackagesListView(ListAPIView):
#     permission_classes = (AllowAny,)
#     serializer_class = PackageSerializer
#     queryset = Packages.objects.all()

class PackageAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        category_ids = request.data["categories"]
        if len(category_ids)==0:
            return Response({"category list can not be empty."},status=status.HTTP_400_BAD_REQUEST)
        serializer = PackageSerializer(data=request.data)
        if serializer.is_valid():
            package = serializer.save(created_by = request.user)

            # Create PackageCategory rows
            for cat_id in category_ids:
                category = Category.objects.get(id=cat_id)
                PackageCategory.objects.create(packages=package, category=category , created_by = request.user)

            return Response(PackageSerializer(package).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, pk=None):
        if pk:
            package = get_object_or_404(Package, pk=pk)
            serializer = PackagelistSerializer(package)
            return Response(serializer.data)
        
        packages = Packages.objects.all()
        serializer = PackagelistSerializer(packages, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        package = get_object_or_404(Packages, pk=pk)
        data = request.data.copy()
        if "categories" in request.data:
            category_ids = request.data["categories"]

            serializer = PackageSerializer(package, data=data, partial=True)
            if serializer.is_valid():
                package = serializer.save(created_by = request.user)

                # reset categories
                PackageCategory.objects.filter(packages=package).delete()
                for cat_id in category_ids:
                    if Category.objects.filter(id=cat_id).exists():
                        PackageCategory.objects.create(packages=package, category_id=cat_id , created_by = request.user)

                return Response(PackageSerializer(package).data)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else : 
            print(request.data)
            serializer = PackageSerializer(package, data=data, partial=True)
            if serializer.is_valid():
                package = serializer.save(created_by = request.user)
                return Response(PackageSerializer(package).data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        package = get_object_or_404(Packages, pk=pk)

        # Optional: delete related PackageCategory rows
        PackageCategory.objects.filter(packages=package).delete()

        # Delete the package itself
        package.delete()

        return Response({"detail": "Package deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class UserPackageAPIView(APIView):

    permission_classes = [IsAuthenticated]
    def get(self, request):
        """List all packages owned by the current user"""
        user_packages = UserPackage.objects.filter(created_by=request.user)
        serializer = UserPackageSerializer(user_packages, many=True)
        return Response(serializer.data)
    def post(self, request):
        user = request.user
        purchases = request.data.get("purchases")  # expects a list of packages
        print(purchases)
        if not purchases or not isinstance(purchases, list):
            return Response({"purchases": "Provide a list of packages to buy."}, status=400)

        created_packages = []

        for item in purchases:
            package_id = item.get("package_id")
            payment_id = item.get("payment_id")
            if not package_id or not payment_id:
                continue  # skip invalid items

            try:
                package = Packages.objects.get(id=package_id)
            except Packages.DoesNotExist:
                continue  # skip invalid package

            user_package = UserPackage.objects.create(
                package=package,
                payment_id=payment_id,
                is_active=True,
                created_by = request.user
            )
            created_packages.append(user_package)

        serializer = UserPackageSerializer(created_packages, many=True)
        return Response(serializer.data, status=201)