from flask import Flask, request

import cpf_service

application = Flask(__name__)


@application.route('/cpf/validator/<string:cpf>', methods=['GET'])
def validate_cpf(cpf):
    return cpf_service.validate(cpf)


@application.route('/cpf/generate', methods=['POST'])
def generate_cpf():
    return cpf_service.generate_cpf()


@application.route('/cpf/generatelist', methods=['POST'])
def generate_list_cpf():
    return cpf_service.generate_list_cpfs(request.args.get('qtd', type=int))


if __name__ == '__main__':
    application.run()
