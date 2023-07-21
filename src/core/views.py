from django.views import generic

class HomeView(generic.TemplateView):
    template_name = 'blog/home.html'

    def get(self, request, *args, **kwargs):
        return super(HomeView, self).get(request, **kwargs)