from django.contrib.auth.mixins import UserPassesTestMixin

class ArticulosMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.es_colaborador or self.request.user.is_superuser