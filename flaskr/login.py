from flaskr import login_manager
from flaskr import db
from .models import User


@login_manager.user_loader
def load_user(user_email):
    row_proxy = db.session.execute(db.select(User)
                                   .where(User.email==user_email)
                                  ).first()
    if row_proxy is None:
        return None
    else:
        return row_proxy[0]
                                    