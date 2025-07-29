from flask import Flask, render_template , request , redirect , url_for , make_response

app = Flask(__name__) # app değişkeni oluşturup bunu flask nesnesi haline getirdik


@app.route('/')
def Definition():
    name  = request.cookies.get('name')
    print('name', name)
    response = make_response('<html><body><h1>Hello World!</h1></body></html>')
    response.set_cookie('name', 'Çağlar')
    return response

@app.route('/hello')
def Hello():
    return render_template('hello.html')

@app.route('/hello-admin')
def HelloAdmin():
    return render_template('helloadmin.html')

@app.route('/hello-user/<name>')
def HelloUser(name):
    return render_template("hellouser.html", username=name)

@app.route('/add/<number1>/<number2>')
def add(number1, number2):
    number1 = int(number1)
    number2 = int(number2)
    calculation_result = number1 + number2
    return render_template("add.html", number1=number1, number2=number2, calculation_result=calculation_result)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        return redirect(url_for('HelloUser', name=username))
    else:
        return render_template('login.html')

@app.route('/ogrenci', methods=['GET', 'POST'])
def ogrenci():
    if request.method == 'POST':
        name = request.form['name']
        fizik = request.form['fizik']
        matematik = request.form['matematik']
        kimya = request.form['kimya']
        return f"<h1>{name} adlı öğrencinin notları:<br>Fizik: {fizik}<br>Matematik: {matematik}<br>Kimya: {kimya}</h1>"
    return render_template('ogrenci.html')


@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    fizik = request.form['fizik']
    matematik = request.form['matematik']
    kimya = request.form['kimya']
    return render_template("student_result.html", name=name,
                           fizik = fizik,
                           matematik = matematik,
                           kimya = kimya)

