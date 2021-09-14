from django.shortcuts import render
import pickle

# Create your views here.
def index(request):
     return render(request, 'index1.html')

def result(request):
    model = pickle.load(open('model.pkl','rb'))
    lis = []
    lis.append(float(request.POST['v']))
    lis.append(float(request.POST['s']))
    lis.append(float(request.POST['c']))
    lis.append(float(request.POST['e']))

    ans = model.predict([lis])
    if ans[0]==0:
        res = "not"
    if ans[0]==1:
        res = ""

    return render(request, 'index2.html',{"variable":res})
