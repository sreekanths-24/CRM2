from django.shortcuts import render, redirect
from .models import FeedbackTable
from django.contrib import messages

# Create your views here.
def sendfeedback(request):
	if request.method == "POST":
		name = request.POST["yourname"]
		email = request.POST["youremail"]
		feedback = request.POST["userfeedbacktake"]
		print(f'name = {name} email = {email} feedback = {feedback}')
		obj = FeedbackTable(name=name, email=email, feedback=feedback)
		obj.save()
		messages.success(request, "feedback submitted sucessfully")
		return redirect('store')
	return render(request, 'give_feedback.html')

def viewfeedback(request):
    feedback_list = FeedbackTable.objects.order_by('-created_at')
    return render(request, 'see_feedback.html', {'feedback_list': feedback_list})
    