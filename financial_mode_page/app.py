# With global_variables_1 and functions_1

from flask import Flask, render_template, request, jsonify
from plotly.graph_objs import Figure, Scatter, Layout
from functions import *
import global_variables as gv

app = Flask(__name__)


@app.route('/')
def home():
    # Generar un gráfico por defecto al cargar la página
    fig = generate_plot(gv.model_months, gv.get_monthly_interest_rate())
    graph_json = fig.to_json()
    return render_template('index_plotly_dynamic.html', graph_json=graph_json, 
                           default_months=gv.model_months,
                           default_interest=gv.annual_interest_rate, 
                           default_betha=gv.betha, 
                           default_cost_prompt_gpt4_cop=gv.get_cost_prompt_gpt4_cop())


@app.route('/update_plot', methods=['POST'])
def update_plot():
    # Obtener los datos del formulario
    months_range = int(request.form['months_range'])
    discount_rate = float(request.form['discount_rate'])
    betha = float(request.form['betha'])

    print(months_range, discount_rate)

    # Actualizar las variables globales con los valores recibidos del formulario
    gv.model_months = months_range
    gv.annual_interest_rate = discount_rate
    gv.betha = betha

    # Calcular el nuevo costo actualizado
    updated_cost = gv.get_cost_prompt_gpt4_cop()

    # Generar el gráfico actualizado
    fig = generate_plot(gv.model_months, gv.get_monthly_interest_rate())

    # Devolver el gráfico y el costo en formato JSON
    graph_json = fig.to_json()
    
    return jsonify({
        'graph_json': graph_json,       # Graph data
        'updated_cost': updated_cost    # Updated cost data
    }) # Esto entra como 'data' al código de Javascript


if __name__ == '__main__':
    app.run(debug=True)
