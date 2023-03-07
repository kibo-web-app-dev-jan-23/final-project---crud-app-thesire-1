from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from .models import Category
from ..models import Assignment
from . import *
from .. import db
from datetime import datetime

# define the assignment tracker routes
@assignment_tracker_blueprint.route('/')
@login_required
def index():
    assignments = Assignment.query.filter_by(user_id=current_user.id).order_by(Assignment.due_date).all()
    return render_template('index.html', assignments=assignments)

@assignment_tracker_blueprint.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d')
        category = request.form['category']
        assignment = Assignment(title=title, description=description, due_date=due_date, user_id=current_user.id, category=category)
        db.session.add(assignment)
        db.session.commit()
        flash('Assignment created successfully.')
        return redirect(url_for('assignment_tracker.index'))

    return render_template('create.html')

@assignment_tracker_blueprint.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    assignment = Assignment.query.get(id)
    if request.method == 'POST':
        assignment.title = request.form['title']
        assignment.description = request.form['description']
        assignment.due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d')
        assignment.category = request.form['category']
        db.session.commit()
        flash('Assignment updated successfully.')
        return redirect(url_for('assignment_tracker.index'))

    return render_template('edit.html', assignment=assignment)

@assignment_tracker_blueprint.route('/<int:id>/delete', methods=['GET','POST'])
@login_required
def delete(id):
    assignment = Assignment.query.get(id)
    db.session.delete(assignment)
    db.session.commit()
    flash('Assignment deleted successfully.')
    return redirect(url_for('assignment_tracker.index'))

@assignment_tracker_blueprint.route('/<int:id>/show', methods=['GET'])
@login_required
def show(id):
    assignment = Assignment.query.get(id)
    if assignment:
        return render_template('show.html', assignment=assignment)
    else:
        flash(f"No assignment found with ID {id}", "error")
        return redirect(url_for('assignment_tracker.index'))