from django.http import HttpResponse


def test(request):
    return HttpResponse('ok', status=200)
