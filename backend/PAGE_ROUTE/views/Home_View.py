from django.http import HttpRequest, JsonResponse

def HomeView(request : HttpRequest) -> JsonResponse:
    x : JsonResponse = {"message": "Hello Ome, this is from Django backend!"}
    return JsonResponse(x)