from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Initialiser une liste d'utilisateurs (en pratique, tu utiliseras une base de données)
users = {
    'alice': 'password1',
    'bob': 'password2'
}

# Initialiser une liste de messages
messages = []

@app.route('/')
def index():
    if 'username' in session:
        return render_template('chat.html', username=session['username'], messages=messages)
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect('/')
        else:
            return "Identifiants incorrects"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users:
            users[username] = password  # Stocker le nouvel utilisateur (en pratique, tu utiliseras une base de données)
            return redirect('/login')
        else:
            return "Nom d'utilisateur déjà pris"
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

@app.route('/send_message', methods=['POST'])
def send_message():
    if 'username' in session:
        message = request.form['message']
        messages.append((session['username'], message))
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
