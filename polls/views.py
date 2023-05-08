from django.shortcuts import render,get_list_or_404

from django.template import loader
from .models import Question
from django.http import HttpResponse


#this packages and modules for shortcut render

#Create your view   here

def index(request):
    latest_question_list = Question.objects.order_by("pub_date")[:5]
    #output = ", ".join([q.question_text for q in latest_question_list])
    """
    template = loader.get_template("polls/index.html")
    context={
        "latest_question_list":latest_question_list
    }
    return HttpResponse(template.render(context,request))
    """
    #we can use the shortcut:render()
    #By using the shortcut:render() we don;t need to import the loader and httpResponse
    context = {"latest_question_list":latest_question_list}
    return render(request,"polls/index.html",context)
    

def details(request, question_id):
 
    question = Question.objects.get(pk=question_id)
    return render(request,"polls/detail.html",{"question":question})
    #return HttpResponse("You're looking at questions %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question %s."% question_id)

