from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ListViewFactory(APIView):
    def __init__(self, serializer_class, model):
        self.serializer_class = serializer_class
        self.model = model

    def get(self, request, format=None):
        data = self.model.objects.all()
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemViewFactory(APIView):
    def __init__(self, serializer_class, model):
        self.serializer_class = serializer_class
        self.model = model

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = self.serializer_class(data)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = self.serializer_class(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
