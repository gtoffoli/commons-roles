# commons-roles
Provides per-object permissions for Django on roles.

This Django app is an almost direct evolution of the *django-permissions* app by Kai Diefenbach: https://github.com/diefenbach/django-permissions.


Years ago I had to change its name, since in my project I wasn't able to overcome a name conflict in other ways.
Now, I have made it compatible with both Python 2 and Python 3, and with both Django 1.9 and Django 2.0.
In fact I'm using it in a project with Python 2.7 and Django 1.8 (*) and in another project with Python 3.5-3.6 and Django 2.0.
I need to test it better and to cleanse the code.

Some relevant changes:
- removed seemingly unused code from the __init__ module
- moved some code from functions in the utils module to methods of the models, to avoid some circularity in the app loading.

(*) For back-compatibility of the property versions of User.is_authenticated an User.is_anonymous, I had to patch Django 1.8 to include some copmatibility code that was there only in Django 1.9 and 1.10.
