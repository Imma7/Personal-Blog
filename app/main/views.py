from flask import render_template,request,redirect,url_for,flash,abort
from . import main
from .. import db
from .forms import PostForm, CommentForm, SubscriptionForm
from ..models import User,Writer,Post,Comment,Subscription
from flask_login import login_required,current_user
from app import login_manager

@login_manager.user_loader
def load_user(user_id):
    '''
    @login_manager.user_loader Passes in a writer_id to this function
    Function queries the database and gets a user's id as a response
    '''
    return User.query.get(user_id)

#Views
@main.route('/')
def index():
    
    # if post.validate_on_submit():
    # title = post.title.data,
    # body = post.body.data

    posts=Post.query.all()

    # return redirect(url_for('main.index'))
    return render_template('index.html', posts=posts)

@main.route('/post', methods=['GET','POST'])
def post():
    '''
    Post page
    '''
    post_form = PostForm()
    if post_form.validate_on_submit():
        title = post_form.title.data
        body = post_form.body.data
        time_posted = post_form.time_posted.data
        new_post = Post(title=title, body=body, time_posted=time_posted)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('post.html', post_form=post_form)

def new_post():
    '''
    New Post Page
    '''
    post_form = PostForm

    if post_form.validate_on_submit():
        title = post_form.title.data
        body = post_form.body.data


        # updated review instance
        new_post = Post(title=title,body = body,user_id=current_user.id)

        #save review method
        new_post.save_post()
        return redirect(url_for('.index'))

    title = f'{Post.title}'
    return render_template('posts.html',title= title, body=body )


@main.route('/comments/<int:id>', methods=['GET', 'POST'])
@login_required
def comments(id):
    comment_form = CommentForm()
    comment = Comment.query.order_by('-id').all()

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data()
        new_comment = Comment(comment=comment,users=current_user.username)
        new_comment.save_comment()
        return redirect(url_for('main.comments',id = post.id))
    return render_template('comments.html')

@main.route('/delete/<int:id>')
@login_required
def delete(id):
    del_comment = Comment.query.get(id)
    db.session.delete(del_comment)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/subscription',methods = ["GET","POST"])
def subscriber():

    form= SubscriptionForm()


    if form.validate_on_submit():
        email = form.email.data
        date = form.date.data


        # updated review instance
        new_subscriber = Subscription(email=email,date = date,user_id=current_user.id)

        #save review method
        new_subscriber.save_subscriber()
        return redirect(url_for('subscriber'))


    return render_template('index.html',email= email, subscribe_form=form )