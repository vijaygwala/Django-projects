from django.shortcuts import render,redirect
from accounts.models import *
from accounts.forms import OrderForm, CreateUserForm,CustomerForm
from django.forms import inlineformset_factory
from accounts.filter import OrderFilter
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from accounts.decoraters import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.
@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + user)

			return redirect('Login')
			

	context = {'form':form}
	return render(request, 'pages/register.html', context)


@unauthenticated_user
def Login(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')

		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('Dash')
		else:
			messages.info(request,'username or password is Incorrect')

	context = {}
	return render(request, 'pages/login.html', context)


def Logout(request):
	logout(request)
	return redirect('Login')

	
@login_required(login_url='Login')
@allowed_users(allowed_roles=['Customers'])
def UserHome(request):
	orders=request.user.customer.order_set.all()
	total_orders=orders.count()

	deliverd=orders.filter(status='Deliverd').count()
	pending=orders.filter(status='Pending').count()
	context={'orders':orders,'total_orders':total_orders,'deliverd':deliverd,'pending':pending}
	

	return render(request,'pages/User.html',context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['Admins'])
def Products(request):
	products=Product.objects.all()
	return render(request,'pages/Product.html',{'products':products})

@login_required(login_url='Login')
@allowed_users(allowed_roles=['Admins'])
def Customers(request,pk):
	customers=Customer.objects.get(id=pk)
	orders=customers.order_set.all()
	total_orders=orders.count()
	myFilter=OrderFilter(request.GET,queryset=orders)
	orders=myFilter.qs
	context={'customers':customers,'orders':orders,'total_orders':total_orders,'myFilter':myFilter}
	return render(request,'pages/Customer.html',context)

@login_required(login_url='Login')
def Status(request):
	return render(request,'pages/status.html')


@login_required(login_url='Login')
@allowed_users(allowed_roles=['Customers'])
def AccountProfile(request):
	customer=request.user.customer
	form=CustomerForm(instance=customer)
	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES,instance=customer)
		if form.is_valid():
			form.save()
	context={'form':form}
	return render(request,'pages/profile.html',context)

@login_required(login_url='Login')
@admin_only
def Dash(request):
	customers=Customer.objects.all()
	orders=Order.objects.all()
	total_customer=customers.count()
	total_orders=orders.count()

	deliverd=orders.filter(status='Deliverd').count()
	pending=orders.filter(status='Pending').count()
	context={'customers':customers,'orders':orders,'total_customer':total_customer,'total_orders':total_orders,'deliverd':deliverd,'pending':pending}
	return render(request,'pages/dashboard.html',context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['Admins'])
def createOrder(request,pk):
	OrderFormSet=inlineformset_factory(Customer,Order,fields=('products','status'),extra=5)
	customer=Customer.objects.get(id=pk)

	formset=OrderFormSet(instance=customer)
	if request.method=='POST':
		formset=OrderFormSet(request.POST,instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('Dash')
	context={'form':formset}
	return render(request,'pages/order_form.html',context)


@login_required(login_url='Login')
@allowed_users(allowed_roles=['Admins'])
def updateOrder(request,pk):
	order=Order.objects.get(id=pk)
	form=OrderForm(instance=order)
	if request.method=='POST':
		form=OrderForm(request.POST,instance=order)
		if form.is_valid():
			form.save()
			return redirect('Dash')
	context={'form':form}
	return render(request,'pages/order_form.html',context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['Admins'])


def deleteOrder(request,pk):
	order=Order.objects.get(id=pk)
	if request.method=='POST':
		order.delete()
		return redirect('Dash')
	context={'item':order}
	return render(request,'pages/delete.html',context)



