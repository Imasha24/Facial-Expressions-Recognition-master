from flask import Flask, render_template, request, jsonify
import requests

app = Flask('myapp')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        # Make API call to sign up user
        api_url = 'https://yourapi.com/signup'
        api_data = {'username': username, 'email': email, 'password': password, 'confirm_password': confirm_password}
        api_response = requests.post(api_url, data=api_data)

        if api_response.status_code == 200:
            return render_template('success.html')
        else:
            return render_template('error.html')
    else:
        return render_template('signup.html')

if 'myapp' == '__main__':
    app.run(debug=True)
