from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import DetailView,FormView,ListView

from brand.models import Brand
from userauth.models import Order

from .models import Car

from .forms import CommentForm

# Create your views here.
def homepage(request, brand_slug = None):
    brands = Brand.objects.all()
    cars = Car.objects.all()
    if brand_slug:
        brand = Brand.objects.get(slug=brand_slug)
        cars = Car.objects.filter(brand=brand)

    return render(request, 'car/home.html',{'brands': brands , 'cars' : cars})

@login_required
def buy_car(request, id):
    car = Car.objects.get(id=id)
    if car.quantity > 0:
        car.quantity -= 1
        car.save()
        Order.objects.create(user=request.user, car=car)
        
    else:
        messages.error(request, 'This car is out of stock')
        return redirect('car_detail',id=car.id)
    return redirect('home')

@method_decorator(login_required, name='dispatch')
class ProfileView(ListView):
    model = Car
    template_name = 'car/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.filter(user=self.request.user)
        cars = []
        for order in orders:
            cars.append(order.car)
        context['cars'] = cars
        return context


class CarDetailView(DetailView , FormView):
    model = Car
    template_name = 'car/car_detail.html'
    form_class = CommentForm
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.get_object()
        comments = car.comments.all()
        context['comments'] = comments
        return context
    
    def get_success_url(self):
        return reverse_lazy('car_detail',kwargs={'id':  self.get_object().id})

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.car = self.get_object()
        comment.save()
        return super().form_valid(form)
    


        


