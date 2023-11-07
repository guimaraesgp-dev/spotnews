from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Category
from news.forms import CategoryForms


# Create your views here.
def home(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context)


def news_details(request, new_id):
    new = get_object_or_404(News, id=new_id)
    ct = new.categories.all()
    return render(request, "news_details.html", {"new": new, "categories": ct})


def categories_form(request):
    form = CategoryForms()
    context_form = {"form": form}

    if request.method == "POST":
        name = request.POST.get("name")
        Category.objects.create(name=name)
        return redirect("home-page")

    return render(request, "categories_form.html", context_form)
