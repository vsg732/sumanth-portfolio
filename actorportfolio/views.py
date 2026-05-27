from django.shortcuts import render, redirect

from .models import (
    PortfolioData,
    Filmography,
    Gallery
)


# ================= HOME PAGE =================

def portfolio(request):

    data = PortfolioData.objects.last()

    return render(
        request,
        'index.html',
        {'data': data}
    )


# ================= ADMIN PAGE =================

def admin_page(request):

    if request.method == "POST":

        # ================= SAVE PORTFOLIO =================

        data = PortfolioData.objects.create(

            actor_name=request.POST.get('actor_name'),

            email=request.POST.get('email'),

            phone=request.POST.get('phone'),

            instagram=request.POST.get('instagram'),

            facebook=request.POST.get('facebook'),

            twitter=request.POST.get('twitter'),

            youtube=request.POST.get('youtube'),

            background=request.FILES.get('background'),

            about_image=request.FILES.get('about_image'),

            about_description=request.POST.get(
                'about_description'
            )

        )

        # ================= FILMOGRAPHY =================

        titles = request.POST.getlist(
            'film_title[]'
        )

        roles = request.POST.getlist(
            'film_role[]'
        )

        years = request.POST.getlist(
            'film_year[]'
        )

        trailers = request.POST.getlist(
            'film_trailer[]'
        )

        posters = request.FILES.getlist(
            'film_poster[]'
        )

        for i in range(len(titles)):

            # EMPTY TITLE SKIP

            if titles[i]:

                poster = None

                if i < len(posters):

                    poster = posters[i]

                Filmography.objects.create(

                    portfolio=data,

                    title=titles[i],

                    role=roles[i],

                    year=years[i],

                    trailer=trailers[i],

                    poster=poster

                )

        # ================= GALLERY =================

        gallery_names = request.POST.getlist(
            'gallery_name[]'
        )

        gallery_images = request.FILES.getlist(
            'gallery_image[]'
        )

        for i in range(len(gallery_images)):

            image_name = ""

            if i < len(gallery_names):

                image_name = gallery_names[i]

            Gallery.objects.create(

                portfolio=data,

                image=gallery_images[i],

                image_name=image_name

            )

        return redirect('portfolio')

    return render(request, 'admin.html')