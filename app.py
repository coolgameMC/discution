from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Définir une liste d'utilisateurs (en pratique, tu utiliseras une base de données)
users = {
    'alice': 'password1',
    'bob': 'password2'
}

@app.route('/')
def index():
    if 'username' in session:
        return f"Connecté en tant que {session['username']}"
    return "Non connecté"

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

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
