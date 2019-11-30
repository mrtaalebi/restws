from django.shortcuts import redirect
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from restws.models import Charger
from restws.serializers import ChargerSerializer


class ChargerView(GenericAPIView):

    queryset = Charger.objects.all()
    serializer_class = ChargerSerializer

    def get(self, request):
        data = self.get_serializer(self.get_queryset(), many=True).data
        return Response(data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
