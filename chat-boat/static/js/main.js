$(document).ready(function () {
    $("#perguntar").click(function () {
        var pergunta = $("#pergunta").val();
        console.log("Pergunta enviada:", pergunta);  // Log da pergunta enviada

        $.ajax({
            url: 'http://localhost:5000/chatbot',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ question: pergunta }),
            success: function (data) {
                console.log("Resposta recebida:", data);  // Log da resposta recebida
                if (data.response) {
                    $("#resposta").text(data.response);
                } else {
                    $("#resposta").text("Desculpe, não entendi a pergunta.");
                }
            },
            error: function (xhr, status, error) {
                console.log(xhr.responseText);
                $("#resposta").text("Erro ao processar a solicitação.");
            }
        });
    });
});