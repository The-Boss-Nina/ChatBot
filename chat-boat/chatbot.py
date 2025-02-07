from flask import Flask, request, jsonify, render_template
import random
import nltk
import string
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

perguntas_respostas = {
    1: "Como posso ajudar você neste belo dia?",
    2: "Estou bem, obrigada por perguntar. Espero que você também esteja bem.",
    3: "Meu nome é Hiro do sistema SystemTec.",
    4: "Fui criado para introduzir o estudo de Inteligência Artificial. Posso responder a perguntas simples para iniciar um diálogo com o usuário.",
    5: "Tchau! Muito obrigada por testar esse serviço! Tenha um bom dia!"
}

cumprimento = ["olá", "oi", "ai", "ola", "hey", "ei"]
gentileza = ["tudo bem", "como vai", "tudo certo", "bem"]
nome = ["qual é o seu nome", "como você se chama", "seu nome", "nome"]
funcao = ["função", "o que você pode fazer", "quais são suas habilidades", "funções", "o que você faz", "funcao", "qual é a sua função"]
despedida = ["adeus", "Bye", "até logo", "tchau"]
intencao_dia = ["que dia é hoje", "qual é a data", "qual o dia da semana"]
tempo = ["vai chover hoje", "como está o tempo", "está fazendo calor"]
atividade = ["o que posso fazer hoje", "qual é a melhor atividade para relaxar", "o que fazer no meu tempo livre"]

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

    if any(questao in tokens for questao in intencao_dia):
        hoje = datetime.now().strftime("%A, %d de %B de %Y")
        return f"Hoje é {hoje}"

    if any(questao in tokens for questao in tempo):
        return "Desculpe, eu não tenho informações sobre o tempo. Você pode verificar o clima no seu aplicativo favorito!"

    if any(questao in tokens for questao in atividade):
        return "Você pode tentar fazer uma caminhada, praticar um hobby ou até ler um livro para relaxar."

    if any(questao in tokens for questao in cumprimento):
        return perguntas_respostas.get(1)
    
    if any(questao in tokens for questao in gentileza):
        return perguntas_respostas.get(2)

    if any(questao in tokens for questao in nome):
        return perguntas_respostas.get(3)

    if any(questao in tokens for questao in funcao):
        return perguntas_respostas.get(4)

    if any(questao in tokens for questao in despedida):
        return perguntas_respostas.get(5)
    
    return "Desculpe, não entendi a pergunta."

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)