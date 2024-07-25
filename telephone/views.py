from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
import requests
from django.conf import settings
# views.py
import requests
from django.http import JsonResponse

class PhoneEditForm(generic.UpdateView):
    template_name = 'phones/edit.html'
    form_class = forms.PhoneForm
    success_url = reverse_lazy('phone_list')

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get('id')
        return get_object_or_404(models.Phone, id=phone_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(PhoneEditForm, self).form_valid(form=form)
class PhoneDeleteForm(generic.DeleteView):
    template_name = 'phones/confirm_delete.html'
    success_url = reverse_lazy('phone_list')

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get('id')
        return get_object_or_404(models.Phone, id=phone_id)
class PhoneCreateComment(generic.CreateView):
    template_name = 'phones/phone_list.html'
    form_class = forms.CommentForm
    success_url = reverse_lazy('phone_list')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(PhoneCreateComment, self).form_valid(form=form)
class PhoneCreateReview(generic.CreateView):
    template_name = 'phones/phone_detail.html'
    form_class = forms.ReviewForm
    success_url = reverse_lazy('phone_list')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(PhoneCreateReview, self).form_valid(form=form)
class PhoneCreateForm(generic.CreateView):
    template_name = 'phones/create_phone.html'
    form_class = forms.PhoneForm
    success_url = reverse_lazy('phone_list')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(PhoneCreateForm, self).form_valid(form=form)
class PhoneDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Phone
    template_name = 'phones/phone_detail.html'
    context_object_name = 'phone'

    def get_object(self, queryset=None):
        return get_object_or_404(models.Phone, id=self.kwargs.get('id'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        phone = self.get_object()
        context['reviews'] = models.Review.objects.filter(review_phone=phone).order_by('-created_at')
        context['review_form'] = forms.ReviewForm()
        return context

    def post(self, request, *args, **kwargs):
        phone = self.get_object()
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.review_phone = phone
            review.user = request.user
            review.save()
            return redirect('phone_detail', id=phone.id)
        else:
            context = self.get_context_data(object=phone)
            context['review_form'] = review_form
            return render(request, self.template_name, context)

class PhoneListView(generic.ListView):
    model = models.Phone
    template_name = 'phones/phone_list.html'
    context_object_name = 'phones'
    paginate_by = 5

    def get_queryset(self):
        return models.Phone.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = models.Comment.objects.all()
        context['comment_form'] = forms.CommentForm()

        # Fetch clothing data from new API
        try:
            clothes_response = requests.get('http://localhost:3000/clothes')
            if clothes_response.status_code == 200:
                context['clothes'] = clothes_response.json()
            else:
                context['clothes'] = []
        except requests.RequestException as e:
            context['clothes'] = []
            print(f"Error fetching clothes: {e}")

        return context

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.phone_id = request.POST.get('phone_id')  # Обратите внимание, как вы получаете phone_id
            comment.save()
            return redirect('phone_list')
        else:
            context = self.get_context_data()
            context['comment_form'] = comment_form
            return self.render_to_response(context)
class SearchPhoneView(generic.ListView):
    template_name = 'phones/phone_list.html'
    context_object_name = 'phones'
    paginate_by = 5

    def get_queryset(self):
        return models.Phone.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['q'] = self.request.GET.get('q')
        return contex
@csrf_exempt
def create_comment_ajax(request):
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return JsonResponse({'text': comment.text}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def create_review_ajax(request):
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return JsonResponse({'description': review.description}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
