'''
approver_view.py
Chris Meehan
4/19/2020
'''
from django.views.generic import(ListView,
                                    CreateView,
                                    DeleteView,
                                    UpdateView,
                                    DetailView)
from ..models.model_approver import Approver
from django.urls import reverse_lazy



class ApproverListView(ListView):
    model = Approver
    template_name = 'approver_home.html'

class ApproverDetailView(DetailView):
    model = Approver
    template_name = 'approver_detail.html'

class ApproverCreateView(CreateView):
    model = Approver
    template_name = 'approver_new.html'
    fields = ['approver_name']
    success_url = reverse_lazy('home')
    fields = '__all__'

class ApproverDeleteView(DeleteView):
    model = Approver
    template_name = 'approver_delete.html'
    success_url = reverse_lazy('home')

class ApproverUpdateView(UpdateView):
    model = Approver
    template_name = 'approver_edit.html'
    success_url = reverse_lazy('home')
    fields = '__all__'
