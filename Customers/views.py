from django.shortcuts import render
from django.views.generic import TemplateView,UpdateView
from .forms import CustomerForm, CustomerUserForm
from .models import Customer

# Create your views here.

class CustomerView(UpdateView):
    login_url = '/login/'
    redirect_field_name = '/'
    form_class =  (CustomerUserForm)
    model = Customer

def myCustomer(request):
    if request.method == 'POST':
        customer_user = CustomerUserForm(data=request.POST)
        customer_detail = CustomerForm(data=request.POST)

        if customer_user.is_valid() and customer_detail.is_valid():
            user = customer_user.save()
            user.set_password(user.password)
            user.save(commit=True)
            detail = customer_detail.save()
            detail.save()
        else:
            print(customer_user.errors, customer_detail.errors)
    else:
        customer_user = CustomerUserForm()
        customer_detail = CustomerForm()
    return render(request, 'Customers/customer_form.html', {'customer_user':customer_user,
                                                            'customer_detail':customer_detail})