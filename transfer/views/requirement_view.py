'''
major_req_view.py
Chris Meehan
4/21/2020
'''
from django.views.generic import(ListView,
                                    CreateView,
                                    DeleteView,
                                    UpdateView,
                                    DetailView)
from ..models.model_requirement import MajorRequirement
from django.urls import reverse_lazy



class RequirementListView(ListView):
    model = MajorRequirement
    template_name = 'requirement/major_req_home.html'

class RequirementDetailView(DetailView):
    model = MajorRequirement
    template_name = 'requirement/major_req_detail.html'

class RequirementCreateView(CreateView):
    model = MajorRequirement
    template_name = 'requirement/major_req_new.html'
    fields = ['approver_name']
    success_url = reverse_lazy('home')
    fields = '__all__'

class RequirementDeleteView(DeleteView):
    model = MajorRequirement
    template_name = 'requirement/major_req_delete.html'
    success_url = reverse_lazy('home')

class RequirementUpdateView(UpdateView):
    model = MajorRequirement
    template_name = 'requirement/major_req_edit.html'
    success_url = reverse_lazy('home')
    fields = '__all__'
