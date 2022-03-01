from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import FileSystemStorage
from .forms import personalform, companyform, documentform
# from .storage.exceptions import NoFileStorageConfigured


def home(request):
    return render(request, 'multiform/home.html')


class multistepform(SessionWizardView):
    template_name = 'multiform/multiform.html'
    form_list = [personalform, companyform, documentform]
    file_storage = FileSystemStorage(location='media')

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]

        return render(self.request, 'multiform/test.html', {'data': form_data})
