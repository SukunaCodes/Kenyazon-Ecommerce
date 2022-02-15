from .models import Subcategory


def menu_link(request):
    link = Subcategory.objects.all()
    return dict(link=link)
