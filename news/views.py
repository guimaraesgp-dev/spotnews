from django.shortcuts import render, get_object_or_404
from news.models import News


# Create your views here.
def home(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context)


def news_details(request, new_id):
    new = get_object_or_404(News, id=new_id)
    categ = new.categories.all()
    return render(
        request, "news_details.html", {"new": new, "categories": categ}
    )
