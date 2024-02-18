from flask import Flask, render_template, request
from simplifier import simplify
import json

app = Flask(__name__)

def get_table_data():
    return request.form.get('json_data')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        table_data = get_table_data()
        table_data = json.loads(table_data)

        exp = simplify(convert_to_matrix(table_data))

        return render_template('index.html', table=table_data, matrix=exp)

    # Initial table configuration with one row and two columns
    initial_table = [['', '']]
    return render_template('index.html', table=initial_table)

def convert_to_matrix(table):
    matrix = []
    for row in table:
        matrix.append([int(cell) if cell else 0 for cell in row])
    return matrix

if __name__ == '__main__':
    app.run(debug=True)
