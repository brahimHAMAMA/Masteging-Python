from flask import Flask, render_template

skills_app = Flask(__name__)

skills_list = [('html', 80),('php', 45),('java', 55),('css', 90)]
@skills_app.route('/')
def homepage():
    return render_template('homepage.html', pagetitle="Home Page", coustm_css = "home.css")

@skills_app.route('/about')
def about():
    return render_template('about.html', pagetitle="About Page")

@skills_app.route('/add')
def add():
    return render_template('add.html', title="add Page", coustm_css = "add.css")

@skills_app.route('/skills')
def skills():
    return render_template('skills.html', title= "Skills Page", skills= skills_list, page_head="My Skills", description="This Is My Skills Page", coustm_css = "skills.css")

if __name__ == "__main__":
    skills_app.run(debug=True, port=3000)