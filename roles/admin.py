from django.contrib import admin

from roles.models import ObjectPermission
admin.site.register(ObjectPermission)

from roles.models import Permission
admin.site.register(Permission)

from roles.models import Role
admin.site.register(Role)

from roles.models import PrincipalRoleRelation
admin.site.register(PrincipalRoleRelation)
