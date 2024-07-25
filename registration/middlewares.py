from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class YearsExperienceSalaryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/workregister/' and request.method == 'POST':
            years_of_experience = int(request.POST.get('years_of_experience', 0))
            age = int(request.POST.get('age', 0))
            if years_of_experience <= 1 or age <= 18:
                return HttpResponseBadRequest('Ваш опыт или возвраст слишком мал для регистрации')
            elif years_of_experience == 2 or years_of_experience == 3:
                request.salary = 1000
            elif years_of_experience == 5 or years_of_experience == 6:
                request.salary = 2000
            elif years_of_experience > 5:
                request.salary = 3000
            else:
                request.salary = 0