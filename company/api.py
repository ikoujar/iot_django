from rest_framework import generics
from company.serializers import CompanySerializer


class CompanyAPI(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = CompanySerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        return self.model.objects.all()


class CompanyListAPI(generics.ListCreateAPIView):

    serializer_class = CompanySerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        return self.model.objects.filter()


