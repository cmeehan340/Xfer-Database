'''
evaluation_view.py
Chris Meehan
4/30/2020
'''
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView,
                                  DetailView)
from ..models.model_evaluation import TransferEvaluation



class EvalListView(ListView):
    '''
    Generates the view for the Evaluations page
    '''
    model = TransferEvaluation
    template_name = 'evaluation/eval_home.html'

class EvalCreateView(CreateView):
    '''
    Generates a view to create courses
    '''
    model = TransferEvaluation
    template_name = 'evaluation/eval_new.html'
    fields = '__all__'
    success_url = reverse_lazy('evaluation_home')

class EvalDetailView(DetailView):
    '''
    Generates a view to show course details
    '''
    model = TransferEvaluation
    template_name = 'evaluation/eval_detail.html'


class EvalUpdateView(UpdateView):
    '''
    Generates a view to allow updating a course
    '''
    model = TransferEvaluation
    template_name = 'evaluation/eval_edit.html'
    success_url = reverse_lazy('evaluation_home')
    fields = '__all__'

class EvalDeleteView(DeleteView):
    '''
    Generates a view to allow deleting a course
    '''
    model = TransferEvaluation
    template_name = 'evaluation/eval_delete.html'
    success_url = reverse_lazy('evaluation_home')
