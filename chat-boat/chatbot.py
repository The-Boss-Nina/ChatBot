from flask import Flask, request, jsonify, render_template
import random
import string
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Pares de perguntas e respostas
perguntas_respostas = {
    1: "Como posso ajudar você neste belo dia?",
    2: "Estou bem, obrigado por perguntar. Espero que você também esteja bem.",
    3: "Meu nome é Hiro do sistema SystemTec.",
    4: "Fui criado para introduzir o estudo de Inteligência Artificial. Posso responder a perguntas simples para iniciar um diálogo com o usuário.",
    5: "Tchau! Muito obrigado por testar esse serviço! Tenha um bom dia!"
}

cumprimento = ["olá", "oi", "hello"]
gentileza = ["tudo bem"]
nome = ["qual é o seu nome", "seu nome", "nome", "qual o seu nome?"]
funcao = ["função", "qual a sua função", "qual é a sua função?"]
despedida = ["adeus", "bye", "tchau"]

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        data = request.json
        user_question = data['question']
        resposta = responder_pergunta(user_question)
        return jsonify({'response': resposta})
    except Exception as e:
        return jsonify({'response': 'Desculpe, houve um erro ao processar sua pergunta.'})

def responder_pergunta(pergunta):
    tokens = [word.strip(string.punctuation) for word in pergunta.lower().split()]
    
    # Responder perguntas relacionadas a saudações
    if any(questao in tokens for questao in cumprimento):
        return perguntas_respostas[1]
    
    # Responder perguntas relacionadas a gentileza
    if any(questao in tokens for questao in gentileza):
        return perguntas_respostas[2]

    # Responder perguntas sobre o nome
    if any(questao in tokens for questao in nome):
        return perguntas_respostas[3]

    # Responder perguntas sobre a função
    if any(questao in tokens for questao in funcao):
        return perguntas_respostas[4]

    # Responder perguntas relacionadas a despedida
    if any(questao in tokens for questao in despedida):
        return perguntas_respostas[5]
    
    return "Desculpe, não entendi a pergunta."

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)