from flaskr import login_manager
from flaskr import db
from .models import User


@login_manager.user_loader
def load_user(user_id):
    result = db.session.execute(db.select(User).where(User.id == user_id)).first()
    if result is not None:
        return result[0]

    return None
                                    