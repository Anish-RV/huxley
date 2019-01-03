#!/usr/bin/env python

# Copyright (c) 2011-2015 Berkeley Model United Nations. All rights reserved.
# Use of this source code is governed by a BSD License (see LICENSE).

from django.contrib import admin

from huxley.core.models import *

from .assignment import AssignmentAdmin
from .committee import CommitteeAdmin
from .committee_feedback import CommitteeFeedbackAdmin
from .country import CountryAdmin
from .delegate import DelegateAdmin
from .schools import SchoolAdmin
from .registration import RegistrationAdmin
from .position_paper import PositionPaperAdmin
'''
Add an import for your new models
'''

'''Your code here'''
'''Your code here'''
>>>>>>> 60e3ad96396eb5518a40a19bea73041f477d4563

admin.site.register(Conference)
admin.site.register(Country, CountryAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Committee, CommitteeAdmin)
admin.site.register(CommitteeFeedback, CommitteeFeedbackAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(CountryPreference)
admin.site.register(Delegate, DelegateAdmin)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Rubric)
admin.site.register(PositionPaper, PositionPaperAdmin)
'''
Register your models with the admin site.
'''

'''Your code here'''
'''Your code here'''
>>>>>>> 60e3ad96396eb5518a40a19bea73041f477d4563
