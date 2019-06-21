from flask import jsonify


def login():
    res = {"type":"+ok","msg":"Login Successful"}
    return jsonify(res)