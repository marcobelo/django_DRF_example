from rest_framework.response import Response


def list_view(model, serializer):
    list_heroes = model.objects.all()
    result = serializer(list_heroes, many=True)
    return Response(result.data)
