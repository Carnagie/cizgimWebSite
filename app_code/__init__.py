from flask import Flask, render_template, request, session, redirect


app = Flask(__name__)

app.secret_key = 'super secret key'


@app.route('/', methods=["GET","POST"])
def index():

    return render_template('index.html')

@app.route('/danismanlik.html', methods=["GET","POST"])
def index2():

    return render_template('danismanlik.html')

@app.route('/arsiv.html', methods=["GET","POST"])
def index3():

    return render_template('arsiv.html')

@app.route('/insaat.html', methods=["GET","POST"])
def index4():

    return render_template('insaat.html')

@app.route('/mimarlik_muhendislik.html', methods=["GET","POST"])
def index5():

    return render_template('mimarlik_muhendislik.html')

@app.route('/google56eaba67fcb83997.html', methods=["GET","POST"])
def index6():

    return render_template('google56eaba67fcb83997.html')


if __name__ == "__main__":
    app.run(debug=True,port=8000)