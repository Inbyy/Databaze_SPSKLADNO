from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/1')
def home():
    return "Ahoj, světe od učitele!"

@app.route('/2')
def pozdrav_ze_souboru():
    return render_template("index2.html")

@app.route('/3')
def pozdrav_ze_souboru_CSS():
    return render_template("index3.html")

@app.route('/4')
def pozdrav_z_promenny():
    text = "caucau"
    return render_template("index4.html", message = text)

@app.route('/5')
def obrazek():
    image_url = url_for('static', filename='styles/kostka.png')
    return render_template('index5.html', image_url=image_url)

@app.route('/6', methods=['GET', 'POST'])
def prvniFormularCislo():
    result = None
    if request.method == 'POST':
        number = request.form.get('number', type=int)
        if number is not None:
            result = number + 1
    return render_template('index6.html', result=result)

if __name__ == '__main__':
    app.run()