$(document).ready(function () {
    $("#perguntar").click(function () {
        var pergunta = $("#pergunta").val();

        if (pergunta.trim() === "") {
            return;
        }

        // Adiciona a pergunta ao histórico
        $("#chat-history").append(`<div class="question"><strong>Você:</strong> ${pergunta}</div>`);

        // Limpa o campo de pergunta
        $("#pergunta").val("");

        $.ajax({
            url: 'http://localhost:5000/chatbot',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ question: pergunta }),
            success: function (data) {
                if (data.response) {
                    // Adiciona a resposta ao histórico
                    $("#chat-history").append(`<div class="response"><strong>Bot:</strong> ${data.response}</div>`);
                } else {
                    $("#chat-history").append(`<div class="response"><strong>Bot:</strong> Desculpe, não entendi a pergunta.</div>`);
                }

                // Scroll para o final do histórico
                $('#chat-history').scrollTop($('#chat-history')[0].scrollHeight);
            },
            error: function (xhr, status, error) {
                console.log(xhr.responseText);
                $("#chat-history").append(`<div class="response"><strong>Bot:</strong> Erro ao processar a solicitação.</div>`);
            }
        });
    });

    // Permitir que o usuário envie a pergunta também ao pressionar 'Enter'
    $("#pergunta").keypress(function (e) {
        if (e.which === 13) { // 13 é o código da tecla 'Enter'
            $("#perguntar").click();
        }
    });
});