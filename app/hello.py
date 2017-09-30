from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<int:score>')
def hello_name(score):
	return render_template('hello.html', marks=score)

@app.route('/blog/<int:postID>')
def show_blog(postID):
	return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
	return 'Revision Number %.2f' % revNo

@app.route('/flask')
def hello_flask():
	return 'Hello Flask'

@app.route('/python/')
def hello_python():
	return 'Hello Python'

@app.route('/result')
def result():
    d = {'phy':50, 'che':60, 'maths':70}
    return render_template('result.html', result=d)

#app.add_url_rule('/', 'hello', hello_world)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)