from rest_framework.response import Response


def list_view(model, serializer):
    data_list = model.objects.all()
    result = serializer(data_list, many=True)
    return Response(result.data)
