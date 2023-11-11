from flask import Flask, render_template, request, redirect, url_for
from database import update_medicamento, add_medicamento
from medicamentos import get_medicamento_by_id, get_medicamentos
from precios import get_precios

app = Flask(__name__)

@app.route('/')
def index():
    medicamentos = get_medicamentos()
    precios = get_precios()

    medicamentos_precios = zip(medicamentos, precios)
    
    return render_template('index.html', medicamentos_precios=medicamentos_precios)

@app.route('/editar/<int:medicamento_id>', methods=['GET', 'POST'])
def editar(medicamento_id):
    medicamento = get_medicamento_by_id(medicamento_id)
    if request.method == 'POST':
        cantidad = request.form['cantidad']
        precio = request.form['precio']
        update_medicamento(medicamento_id, cantidad, precio)
        return redirect(url_for('index'))
    else:
        medicamento = get_medicamento_by_id(medicamento_id)
        return render_template('editar.html', medicamento=medicamento)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        medicamento = request.form['medicamento']
        cantidad = request.form['cantidad']
        precio = request.form['precio']
        presentacion = request.form['presentacion']

        add_medicamento(medicamento, cantidad, precio, presentacion)
        return redirect(url_for('index'))
    else:
        return render_template('agregar.html')

if __name__ == '__main__':
    app.run(debug=True)
