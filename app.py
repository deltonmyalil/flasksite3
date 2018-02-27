from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)
'''
#These are static, just to get to knkow routing
@app.route('/')
def hello():
	return 'Hello World'

@app.route('/new')
def new():
	return 'new page'
	
@app.route('/demo')
def demo():
	return 'This is the demo'
'''
'''
@app.route('/profile/<name>')  # Specify variables as <var_name>
def profile(name):  # Pass the argument name
	return 'This profile belongs to %s' % name  # %s for string arg, give the %var_name
'''
'''
# If you wanted to pass an integer, do this:
@app.route('/profileId/<int:id>')
def profileId(id):
	return 'This profile belongs to the person with profile ID %d' % id
'''
'''
# Demo for dynamic url, redirecting
@app.route('/admin')
def hello_admin():
	return 'Hello Admin'
	
@app.route('/guest/<guest>')
def hello_guest(guest):
	return 'Hello guest %s' % guest
	
@app.route('/user/<name>')
def hello_user(name):
	if name == 'admin':
		return redirect(url_for('hello_admin'))  # import redirect and url_for from flask
	else:
		return redirect(url_for('hello_guest', guest= name))  # Since the function hello_guest has an argument which is name
'''

'''
# Showing how to use a login using http get and post
@app.route('/success/<name>')
def success(name):
    return "Welcome %s" % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['nm']
        return redirect(url_for('success', name=username))
    else:
        username = request.args.get('nm')
        return redirect(url_for('success', name=username))
'''

@app.route('/')
def student():
	return render_template('student.html')

@app.route('/result', methods= ['POST','GET'])
def result():
    if request.method == 'POST':
        result= request.form
        return render_template('result.html',result= result)

if __name__ == '__main__':
    app.run()
