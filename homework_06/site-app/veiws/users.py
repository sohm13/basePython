from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError, DatabaseError
from werkzeug.exceptions import NotFound, InternalServerError

from models.database import db
from models.models import User, Post
from veiws.forms.users import UserForm 

users_app = Blueprint("users_app", __name__)



@users_app.route('/')
def users_list():
    users = User.query.all()
    return render_template('users/users.html', users=users)


@users_app.route('/<int:user_id>/', endpoint="detail")
def detail(user_id: int):
    user = User.query.get(user_id)
    posts = Post.query.filter(user_id == user_id).all()
    details = {
        'user': user,
        'posts': posts,
        'user_id': user_id,
    }
    return render_template('users/detail.html', details=details)




@users_app.route("/add-user/", methods=["GET", "POST"], endpoint="add_user")
def add_user():
    form = UserForm()

    if request.method == 'GET':
        return render_template("users/add-user.html", form=form)
    name = form.name.data
    username = form.username.data
    email = form.email.data
    is_new = form.is_new.data
    
    user = User(name=name, username=username, email=email)

    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError:
        error_text = f"Could not save user {username!r}, user field is not unique!"
        print(error_text)
        form.form_errors.append(error_text)
        return render_template("users/users.html", form=form), 400

    except DatabaseError:
        raise InternalServerError(f"could not save product {username!r}")

    flash(f"Created new User: {user.name}", "success")
    url = url_for("users_app.detail", user_id=user.id)
    return redirect(url)



@users_app.route("/<int:user_id>/add-post/", methods=["POST", 'GET'], endpoint='add_post')
def add_post(user_id: int):
    
    if request.method == "GET":
        return render_template("users/add-post.html", user_id=user_id)

    title = request.form['title']
    content = request.form['content']

    user = User.query.filter(user_id == user_id).first()
    post = Post(user_id=user_id, title=title, body=content, user=user)

    db.session.add(post)
    db.session.commit()

    url = url_for("users_app.detail", user_id=user_id)
    return redirect(url)
    

