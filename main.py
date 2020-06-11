from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

cep = '08310420'
url = str(f'https://viacep.com.br/ws/{cep}/json/')
data = requests.get(url).text
inst = json.loads(data)

@app.route('/')
def index():
    return render_template("index.html",cep=inst.get('cep'),logradouro=inst.get('logradouro'),bairro=inst.get('bairro'),complemento=inst.get('complemento'),localidade=inst.get('localidade'),uf=inst.get('uf'))


if __name__=="__main__":
    app.run(debug=True)
    