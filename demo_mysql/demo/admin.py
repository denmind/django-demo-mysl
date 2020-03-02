from django.contrib import admin
from django.db import models
from django.forms import TextInput
from .models import Person

"""
Person
"""


class PersonAdmin(admin.ModelAdmin):
    # Set 'autocomplete' to 'off' for all text inputs
    formfield_overrides = {
        models.CharField: {
            'widget': TextInput(
                attrs={
                    'autocomplete': 'off'
                }
            )
        }
    }

    # Display headers for viewing all records
    list_display = (
        'person_name',
        'person_gender',
        'show_person_dob',
        'calc_person_age',
        'show_person_register'
    )

    # Add filter for viewing
    list_filter = [
        'person_gender',
        'person_register',
    ]

    # Search this fields
    search_fields = [
        'person_name',
    ]

    # Results per page / pagination
    list_per_page = 15

    # Grouping of fields during adding and editing
    fieldsets = [
        (
            # Group name
            'Personal Information',
            {
                # Group contents
                'fields':
                    [
                        'person_name',
                        'person_gender',
                        'person_dob',
                    ]
            },
        ),
    ]


admin.site.register(Person, PersonAdmin)