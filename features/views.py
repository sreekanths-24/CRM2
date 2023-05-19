from django.shortcuts import render, redirect
from .models import FeedbackTable
from django.contrib import messages
from mainpart.models import Record
from store.models import NewShippingAdress, OrderItem
from django.db.models import Q
# Create your views here.
def sendfeedback(request):
	if request.method == "POST":
		name = request.POST["yourname"]
		email = request.POST["youremail"]
		feedback = request.POST["userfeedbacktake"]
		#print(f'name = {name} email = {email} feedback = {feedback}')
		obj = FeedbackTable(name=name, email=email, feedback=feedback)
		obj.save()
		messages.success(request, "feedback submitted sucessfully")
		return redirect('store')
	return render(request, 'give_feedback.html')

def viewfeedback(request):
    feedback_list = FeedbackTable.objects.order_by('-created_at')
    return render(request, 'see_feedback.html', {'feedback_list': feedback_list})
    
def searchdata(request):
	if request.method == "POST":
		searcheddata = request.POST['searcheddata']
		# recordresults = Record.objects.filter(first_name__icontains=searcheddata)
		multi_q = Q(Q(first_name__icontains=searcheddata) | Q(last_name__icontains=searcheddata)| Q(email__icontains=searcheddata)| Q(phone__icontains=searcheddata)| Q(address__icontains=searcheddata)| Q(city__icontains=searcheddata)| Q(state__icontains=searcheddata)| Q(zipcode__icontains=searcheddata)| Q(product__icontains=searcheddata))
		recordresults = Record.objects.filter(multi_q)
		return render(request, 'searchdata.html', {'searcheddata':searcheddata, 'recordresults':recordresults})
	else:
		return render(request, 'searchdata.html', {})
	
def ecommdata(request):
	ecommshippingdata = NewShippingAdress.objects.order_by('-date_added')
	return render(request, 'ecommdata.html', {'ecommshippingdata':ecommshippingdata})

def ecommorderdata(request):
	ecommorders = OrderItem.objects.order_by('-date_added')
	return render(request, 'ecommorder.html', {'ecommorders':ecommorders})