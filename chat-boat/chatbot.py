from flask import Flask, request, jsonify, render_template
import random
import nltk
import string  # Para remover a pontuação
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Pares de perguntas e respostas
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

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        data = request.json
        user_question = data['question']
        print(f"Pergunta recebida: {user_question}")  # Log da pergunta recebida
        resposta = responder_pergunta(user_question)
        print(f"Resposta gerada: {resposta}")  # Log da resposta gerada
        return jsonify({'response': resposta})
    except Exception as e:
        print(f"Erro ao processar a pergunta: {e}")  # Log de erro
        return jsonify({'response': 'Desculpe, houve um erro ao processar sua pergunta.'})

def responder_pergunta(pergunta):
    # Tokenização usando método simples, sem 'punkt' e removendo pontuação
    tokens = [word.strip(string.punctuation) for word in pergunta.lower().split()]  # Removendo a pontuação
    print(f"Tokens processados: {tokens}")  # Log dos tokens processados

    if len(tokens) > 0:
        for token in tokens:
            if token in cumprimento:
                return perguntas_respostas.get(1)
            
            elif token in gentileza:
                return perguntas_respostas.get(2)
            
            elif token in nome:
                return perguntas_respostas.get(3)
            
            elif token in funcao:
                return perguntas_respostas.get(4)
            
            elif token in despedida:
                return perguntas_respostas.get(5)
    
    return "Desculpe, não entendi a pergunta."

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)