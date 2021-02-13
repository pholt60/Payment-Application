from flask import Flask, render_template, redirect, url_for, request  # Import Flask Class
app = Flask(__name__) # Create an Instance

@app.route('/') # Route the Function
def main(): # Run the function
    return render_template('index.html') # Render the template

@app.route('/Search')
def search():
	return render_template 
	('search.html')

@app.route('/Register')
def register():
	return render_template
	('registration.html')



app.run(host='0.0.0.0', port=5000, debug=True) # Run the Application (in debug mode)


