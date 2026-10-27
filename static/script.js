
const botaoAjuda = document.getElementById("ajuda");
const avisoAjuda = document.getElementById("aviso-ajuda");

botaoAjuda.addEventListener("click", function () {
    avisoAjuda.classList.toggle("aberto");

    if (avisoAjuda.classList.contains("aberto")) {
        botaoAjuda.textContent = "×";
        botaoAjuda.setAttribute("aria-label", "Fechar ajuda");
    } else {
        botaoAjuda.textContent = "?";
        botaoAjuda.setAttribute("aria-label", "Abrir ajuda");
    }
});

// Destaca visualmente a escolha feita antes de enviar ao Flask.
document.querySelectorAll(".escolhas").forEach(function (formulario) {
    formulario.addEventListener("submit", function (evento) {
        const botao = evento.submitter;

        if (!botao) return;

        botao.textContent = "Processando...";
        botao.disabled = true;
    });
});
