'''
approver_view.py
Chris Meehan
4/19/2020
'''
from django.urls import reverse_lazy
from django.views.generic import(ListView,
                                 CreateView,
                                 DeleteView,
                                 UpdateView,
                                 DetailView)
from ..models.model_approver import Approver

class ApproverListView(ListView):
    '''
    Lists all of the Approver Models
    '''
    model = Approver
    template_name = 'approver/approver_home.html'

class ApproverDetailView(DetailView):
    '''
    Details individual Approver model
    '''
    model = Approver
    template_name = 'approver/approver_detail.html'

class ApproverCreateView(CreateView):
    '''
    Creates a new Approver model
    '''
    model = Approver
    template_name = 'approver/approver_new.html'
    fields = ['approver_name']
    success_url = reverse_lazy('approver_home')
    fields = '__all__'

class ApproverDeleteView(DeleteView):
    '''
    Deletes a specific Approver model
    '''
    model = Approver
    template_name = 'approver/approver_delete.html'
    success_url = reverse_lazy('approver')

class ApproverUpdateView(UpdateView):
    '''
    Updates a specific approver model
    '''
    model = Approver
    template_name = 'approver/approver_edit.html'
    success_url = reverse_lazy('approver')
    fields = '__all__'
