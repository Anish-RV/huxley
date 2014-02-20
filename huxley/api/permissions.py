# Copyright (c) 2011-2013 Kunal Mehta. All rights reserved.
# Use of this source code is governed by a BSD License found in README.md.

from rest_framework import permissions

class IsUserOrSuperuser(permissions.BasePermission):
    '''Accept only the users themselves or superusers.'''

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user == obj
