$(document).ready(function () {
    $("#perguntar").click(function () {
        var pergunta = $("#pergunta").val();

        if (pergunta.trim() === "") {
            return;
        }

        // Adiciona a pergunta ao histórico com balão do usuário
        $("#chat-history").append(`<div class="message user-message"><span class="message-text">Você: ${pergunta}</span></div>`);

        // Limpa o campo de pergunta
        $("#pergunta").val("");

        $.ajax({
            url: 'http://localhost:5000/chatbot',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ question: pergunta }),
            success: function (data) {
                if (data.response) {
                    // Adiciona a resposta ao histórico com balão do bot
                    $("#chat-history").append(`<div class="message bot-message"><span class="message-text">Hiro: ${data.response}</span></div>`);
                } else {
                    $("#chat-history").append(`<div class="message bot-message"><span class="message-text">Hiro: Desculpe, não entendi a pergunta.</span></div>`);
                }

                // Scroll para o final do histórico
                $('#chat-history').scrollTop($('#chat-history')[0].scrollHeight);
            },
            error: function (xhr, status, error) {
                console.log(xhr.responseText);
                $("#chat-history").append(`<div class="message bot-message"><span class="message-text">Hiro: Erro ao processar a solicitação.</span></div>`);
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