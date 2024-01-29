from django.shortcuts import render, HttpResponseRedirect, HttpResponse


class AllViews:
    def home(request):
        return render(request, 'index.html')

    def catalog(request):
        return render(request, 'catalog.html')

    def karkasson(request):
        return render(request, 'karkasson.html')

    def karkasson1(request):
        return render(request, 'karkasson1.html')

    def karkasson2(request):
        return render(request, 'karkasson2.html')

    def karkasson3(request):
        return render(request, 'karkasson3.html')

    def karkasson4(request):
        return render(request, 'karkasson4.html')

    def karkasson5(request):
        return render(request, 'karkasson5.html')

    def contact(request):
        return render(request, 'contacts.html')

