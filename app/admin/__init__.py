from flask.ext.admin import Admin

from app.database import db
from app.main.models import User, Tag
from app.admin.views import UserAdmin, TagAdmin


def create_admin(app):
    # Create admin interface
    admin = Admin(app, name="Admin", url="/admin", template_mode="bootstrap3")

    # Add views
    admin.add_view(UserAdmin(User, db))
    admin.add_view(TagAdmin(Tag, db))
    
    if admin.app is None:
        admin.init_app(app)
    
    return admin

