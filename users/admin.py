from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm
from .models import User
 
class UserAdmin(UserAdmin):
   add_form = UserCreationForm
 
   # define fields to be used in displaying the User model.
  
   list_display = ('email', 'is_admin')
   list_filter = ('is_admin',)
   fieldsets = (
       (None, {'fields': ('email', 'password')}),
       ('Permissions', {'fields': ('is_admin',)}),
   )
   add_fieldsets = (
       (None, {
           'classes': ('wide',),
           'fields': ('email','password1', 'password2'),
       }),)
   ordering = ('email',)
   filter_horizontal=()

# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)