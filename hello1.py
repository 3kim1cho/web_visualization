from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	title = 'Test'
	return render_template('index.html',title=title)

if __name__ == '__main__':
	app.debug = True
	app.run(host='133.130.110.36',port=5000)
