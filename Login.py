from flask import Flask, render_template, request, jsonify

app = Flask('myapp')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # TODO: Check if email and password are valid

    # Return JSON response indicating success or failure
    response = {'success': True, 'message': 'Login successful.'}
    return jsonify(response)

if 'myapp' == '__main__':
    app.run(debug=True)
