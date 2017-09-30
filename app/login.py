from flask import Flask, session, flash, redirect, abort, url_for, request, make_response, render_template

app = Flask(__name__)
app.secret_key = '1a22f2yfy2y2t2yg2gu2guihnfjfo'

@app.route('/')
def index():
	#if 'username' in session:
	#	username = session['username']
	#	return 'Logged in as ' + username + '<br>' + \
	#	"<b><a href='/logout'>Click here to log out</a></b>"
	#return "You are not logged in <br>" + \
	#"<b><a href='/login'>Click here to log in</a></b>"
	
	return render_template('index.html')

@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
	if request.method == 'POST':
		user = request.form['name']
		resp = make_response(render_template('readcookie.html'))
		resp.set_cookie('userID', user)
		return resp

@app.route('/getcookie')
def getcookie():
	name = request.cookies.get('userID')
	return '<h1>Welcome %s</h1>' % name

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None

	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid username or password. Please try again!'
		else:
			flash('You were successfully logged in')
			return redirect(url_for('index'))
	return render_template('index_login.html', error=error)

	#if request.method == 'POST':
	#    if request.form['username'] == 'admin':
	#    	return redirect(url_for('success'))
	#    else:
	#    	abort(401)
	#else:
	#	return redirect(url_for('index'))

	#if request.method == 'POST':
	#	session['username'] = request.form['username']
	#	return redirect(url_for('index'))
	#return '''
	#<form action='' method='post'>
    #  <p><input type='text' name='username'/></p>
    #  <p><input type='submit' value='Login'></p>
	#</form>
	#'''
	
	#if request.method == 'POST':
	#	user = request.form['name']
	#	return redirect(url_for('success', name=user))
	#else:
	#	user = request.args.get('name')
	#	return redirect(url_for('success', name=user))

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))

@app.route('/success')
def success():
	return 'Logged in successfully'

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)