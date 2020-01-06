from django.conf import settings

def index(request):
    print(settings.DATABASE["default"]["NAME"])


index()