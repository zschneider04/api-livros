import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Essa é a homepage do site'

@app.route('/pegarvendas')
def pegarvendas():
    tabela = pd.read_csv('advertisement.csv')
    total_vendas = tabela['Vendas'].sum()
    resposta = {'total_vendas': total_vendas}
    return jsonify(resposta)
    

app.run('')

