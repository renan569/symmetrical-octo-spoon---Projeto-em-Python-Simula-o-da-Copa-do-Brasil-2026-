// Destaca visualmente a escolha feita antes de enviar ao Flask.
document.querySelectorAll(".escolhas").forEach(function (formulario) {
    formulario.addEventListener("submit", function (evento) {
        const botao = evento.submitter;

        if (!botao) return;

        botao.textContent = "Processando...";

        // Desativa só depois que o navegador já leu os dados do formulário
        setTimeout(function () {
            botao.disabled = true;
        }, 0);
    });
});
