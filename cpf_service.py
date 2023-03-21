from validate_docbr import CPF
from flask import make_response, jsonify, abort

cpf = CPF()


def validate(cpf_):
    validated = cpf.validate(cpf_)

    if not validated: abort(404)

    if validated and int(cpf_[-1]) % 2 == 0:
        response = {'status': 'ABLE_TO_VOTE'}
    else:
        response = {'status': 'UNABLE_TO_VOTE'}

    return make_response(jsonify(response))


def generate_cpf():
    return make_response(jsonify(cpf.generate()))


def generate_list_cpfs(qtd):
    return make_response(jsonify(cpf.generate_list(qtd)))
