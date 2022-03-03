from django.contrib import admin
from .models import JobApplication


class JobApplicationAdmin(admin.ModelAdmin):
    model = JobApplication
    list_display = ('created', 'first_name', 'last_name',
                    'company', 'vat', 'address_line', 'county',
                    'country', 'company_email', 'phone', 'proof_id', 'proof_business',
                    'password')
    readonly_fields = ('stage',)
    exclude = ('session_hash',)


admin.site.register(JobApplication, JobApplicationAdmin)
