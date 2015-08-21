from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.views.generic import CreateView

from .forms import NotesSearchForm, NeedsSearchForm, NotesForm, NeedsForm

from nx.models import Note, Need

def notes(request):
    form = NotesSearchForm(request.GET)
    notes = form.search()
    return render_to_response('notes.html', {'notes': notes})

def note(request, note_id=None):
    result = Note.objects.get(id=note_id)
    return render_to_response('note_detail.html', {'note': result})

def need(request, need_id=None):
    result = Need.objects.get(id=need_id)
    return render_to_response('need_detail.html', {'need': result})

def search_needs(request):
    form = NeedsSearchForm(request.GET)
    needs = form.search()
    return render_to_response('needs.html', {'needs': needs})

class NoteCreate(CreateView):
    """
    Link creation view - assigns the user to the new link, as well
    as setting Mezzanine's ``gen_description`` attribute to ``False``,
    so that we can provide our own descriptions.
    """

    form_class = NotesForm
    model = Note

    def get_success_url(self):
        return "/note/" + str(self.object.id)

class NeedCreate(CreateView):
    form_class = NeedsForm
    model = Need

    def get_success_url(self):
        return "/need/" + str(self.object.id)
