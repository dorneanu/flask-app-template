from flask import current_app 
from flask.ext import admin
from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib import sqla

from app.database import db
from app.main.models import User, Tag


class UserAdmin(sqla.ModelView):
    column_display_pk = False


class TagAdmin(sqla.ModelView):
    column_display_pl = False


# Create admin interface
# admin = Admin(current_app, name="Admin", url="/admin", template_mode="bootstrap3")

# Add models views
# admin.add_view(UserAdmin(User, db))
# admin.add_view(TagAdmin(Tag, db))
