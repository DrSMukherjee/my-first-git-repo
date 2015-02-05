# done by SM on 04.02.2015.
from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Gumbo says: Bark! Bark! hello world!")

# redfining view to see question database  1st by importing the question class 
from Gumbo.models import Question
def index(request):

    qs_list = Question.objects.order_by('-pub_date')[:5]

    output = '<br/>'.join([p.question_text for p in qs_list])
    return HttpResponse(output)
