from flask import Flask, render_template, request,redirect

app = Flask(__name__)
items = list()

@app.route('/')
def index():
    nomeLista = "Lista de coisas a fazer"
    listaPronta = True

    return render_template('index.html', nomeLista=nomeLista,
    items=items
    )


@app.route('/new', methods=['POST', 'GET'])
def new():
    if request.method == 'POST':
        item = request.form['item']
        items.append(item)
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)