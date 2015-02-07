# done by SM on 04.02.2015.
import StringIO
import PIL
import PIL.Image
from django.http import HttpResponse
from matplotlib import pylab as pl
from Gumbo.models import Question

def index(request):

    qs_list = Question.objects.order_by('-pub_date')[:5]

    output = '<br/>'.join([p.question_text for p in qs_list])
    return HttpResponse(output)

def graph(request):
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [1, 4, 9, 16, 25, 36, 49]
    pl.plot(x, y, linewidth=2)
    pl.xlabel("x axis")
    pl.ylabel("y axis")
    pl.grid(False)
    pl.title("Sample graph")
    # pl.show()

    buff = StringIO.StringIO()
    canvas = pl.get_current_fig_manager().canvas
    canvas.draw()
    graphIMG = PIL.Image.frombytes('RGB', canvas.get_width_height(), canvas.tostring_rgb())
    graphIMG.save(buff, "PNG")
    pl.close()

    return HttpResponse(buff.getvalue(), mimetype="image/png")