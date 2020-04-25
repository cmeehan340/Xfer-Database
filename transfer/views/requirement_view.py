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
    '''
    This generates the view for major requirements
    '''
    model = MajorRequirement
    template_name = 'requirement/major_req_home.html'

class RequirementDetailView(DetailView):
    '''
    This generates the view for each major requirement
    '''
    model = MajorRequirement
    template_name = 'requirement/major_req_detail.html'

class RequirementCreateView(CreateView):
    '''
    This generates the view to create a major requirement
    '''
    model = MajorRequirement
    template_name = 'requirement/major_req_new.html'
    fields = ['approver_name']
    success_url = reverse_lazy('requirement_home')
    fields = '__all__'

class RequirementDeleteView(DeleteView):
    '''
    This generates the view to delete a major requirement
    '''
    model = MajorRequirement
    template_name = 'requirement/major_req_delete.html'
    success_url = reverse_lazy('requirement_home')

class RequirementUpdateView(UpdateView):
    '''
    This generates the view to update a major requirement
    '''
    model = MajorRequirement
    template_name = 'requirement/major_req_edit.html'
    success_url = reverse_lazy('requirement_home')
    fields = '__all__'
