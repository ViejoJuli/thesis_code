# With global_variables_1 and functions_1

from flask import Flask, render_template, request, jsonify
from plotly.graph_objs import Figure, Scatter, Layout
from functions_2 import *
import global_variables_2 as gv

app = Flask(__name__)


@app.route('/')
def home():
    # Generar un gráfico por defecto al cargar la página
    fig = generate_plot(gv.model_months, gv.get_monthly_interest_rate())
    graph_json = fig.to_json()
    return render_template('index_plotly_dynamic.html', graph_json=graph_json, default_months=gv.model_months,
                           default_interest=annual_interest_rate)


@ app.route('/update_plot', methods=['POST'])
def update_plot():
    # Obtener los datos del formulario
    months_range = int(request.form['months_range'])
    discount_rate = float(request.form['discount_rate'])

    print(months_range, discount_rate)

    # Actualizar las variables globales con los valores recibidos del formulario
    gv.model_months = months_range
    gv.annual_interest_rate = discount_rate

    # Generar el gráfico actualizado
    # Ajusta con tus variables
    fig = generate_plot(gv.model_months, gv.get_monthly_interest_rate())

    # Devolver el gráfico en formato JSON
    graph_json = fig.to_json()
    return jsonify(graph_json)


if __name__ == '__main__':
    app.run(debug=True)
