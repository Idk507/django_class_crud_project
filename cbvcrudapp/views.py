from django.shortcuts import render
from django.views.generic import View,ListView,DetailView,CreateView,DeleteView,UpdateView
from cbvcrudapp.models import student
from django.urls import reverse_lazy
from django.http import HttpResponse

# Create your views here.
class greetingview(View):
    greetingmsg= "Hello here idk!!"
    def get(self,request):
        return HttpResponse(self.greetingmsg)
class studentlistview(ListView):
    model = student
   # def get(self,request):
        
       # return render(request,'studentlist.html',{'student':student})
    #default template_name is studentlist.html
    #default context_object_name is studentlist
class studentdetailview(DetailView):
    model = student
    #default template_name is student_detail.html
    #default context_object_name is studentdetail.detail
    
class studentcreate(CreateView):
    model = student
    fields = ('firstname','lastname','testscore1','testscore2','testscore3','testscore4','testscore5','testscore6')    
class studentupdate(UpdateView):
    model = student  
    fields=('firstname','lastname','testscore1','testscore2','testscore3','testscore4','testscore5','testscore6',) 
     
    
class studentdelete(DeleteView):
    model = student
    success_url = reverse_lazy('list')
    
      
  