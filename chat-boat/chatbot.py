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
    5: "Tchau! Muito obrigado por testar esse serviço! Tenha um bom dia!",
    6: "Hoje é [data completa].",  # Resposta padrão para o dia
    7: "Desculpe, não tenho informações sobre o tempo.",
    8: "Você pode tentar fazer uma caminhada, praticar um hobby ou até ler um livro para relaxar.",
    9: "Eu sou Hiro, um chatbot criado para interagir com você! Eu posso responder perguntas sobre o tempo, atividades, data e outras questões simples."
}

cumprimento = ["olá", "oi", "ai", "ola", "hey", "ei"]
gentileza = ["tudo bem", "como vai", "tudo certo", "bem"]
nome = ["qual é o seu nome", "como você se chama", "seu nome", "nome", "qual o seu nome?"]
funcao = ["função", "qual a sua função", "o que você pode fazer", "quais são suas habilidades", "qual é a sua função?", "o que você faz", "quais perguntas você pode responder"]
despedida = ["adeus", "bye", "até logo", "tchau"]
intencao_dia = ["que dia é hoje", "qual é a data", "qual o dia da semana", "qual é o dia de hoje", "qual é a data de hoje?", "qual o dia?"]
tempo = ["vai chover hoje", "como está o tempo", "está fazendo calor"]
atividade = ["o que posso fazer hoje", "qual é a melhor atividade para relaxar", "o que fazer no meu tempo livre", "qual é a melhor forma de relaxar?"]
quem_e_voce = ["quem é você", "quem é o seu nome", "qual é o seu nome", "qual é o nome do chatbot", "quem é o bot", "quem é o seu criador?"]

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

    # Responder perguntas sobre o dia
    if any(questao in tokens for questao in intencao_dia):
        hoje = datetime.now().strftime("%A, %d de %B de %Y")  # Formato completo
        return f"Hoje é {hoje}"

    # Responder perguntas sobre o tempo
    if any(questao in tokens for questao in tempo):
        return perguntas_respostas[7]

    # Responder perguntas sobre atividades
    if any(questao in tokens for questao in atividade):
        return perguntas_respostas[8]

    # Responder perguntas sobre quem é o Hiro
    if any(questao in tokens for questao in quem_e_voce):
        return perguntas_respostas[9]
    
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