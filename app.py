from flask import Flask, request

import cpf_service

app = Flask(__name__)


@app.route('/validator/<string:cpf>', methods=['GET'])
def validate_cpf(cpf):
    return cpf_service.validate(cpf)


@app.route('/validator/generate', methods=['POST'])
def generate_cpf():
    return cpf_service.generate_cpf()


@app.route('/validator/generatelist', methods=['POST'])
def generate_list_cpf():
    return cpf_service.generate_list_cpfs(request.args.get('qtd', type=int))


if __name__ == '__main__':
    app.run()
