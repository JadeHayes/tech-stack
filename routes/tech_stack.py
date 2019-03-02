from flask import Blueprint, render_template

tech_stack_blueprint = Blueprint('tech_stack', __name__,  template_folder='../templates')


@tech_stack_blueprint.route('/')
def tech_stack_render():
    return render_template('tech_stack.html')
