from django.contrib.auth.mixins import UserPassesTestMixin

class ArticulosMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.es_colaborador or self.request.user.is_superuser
    
class ComentariosMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()

        if hasattr(obj, 'texto'):
            return self.request.user.es_colaborador or self.request.user.is_superuser or self.request.user == obj.user