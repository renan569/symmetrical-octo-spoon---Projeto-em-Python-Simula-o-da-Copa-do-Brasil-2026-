
import os
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "chave-so-para-desenvolvimento")


class Campeonato:
    def __init__(self):
        self.times = [
            "Cruzeiro", "Palmeiras", "Santos", "Grêmio",
            "Vitória", "Atlético-MG", "Vasco", "Internacional"
        ]

        self.eliminados = [
            "Flamengo", "Corinthians", "Botafogo", "Fluminense",
            "Chapecoense", "Ceará", "Bahia", "Sport"
        ]

        self.duelos = [
            ("Cruzeiro", "Atlético-MG"),
            ("Palmeiras", "Santos"),
            ("Grêmio", "Internacional"),
            ("Vasco", "Vitória")
        ]

    def times_eliminados(self):
        return self.eliminados


campeonato = Campeonato()


def montar_chave(resultados):
    # Quartas de final
    quartas = [
        {"id": f"q{i}", "times": duelo}
        for i, duelo in enumerate(campeonato.duelos)
    ]

    # Semifinais: 1º contra 4º; 2º contra 3º
    semifinais = []
    if all(f"q{i}" in resultados for i in range(4)):
        semifinais = [
            {"id": "s0", "times": (resultados["q0"], resultados["q3"])},
            {"id": "s1", "times": (resultados["q1"], resultados["q2"])}
        ]

    # Final
    final = []
    if "s0" in resultados and "s1" in resultados:
        final = [
            {"id": "f0", "times": (resultados["s0"], resultados["s1"])}
        ]

    fases = [
        {"nome": "Quartas de final", "id": "quartas", "jogos": quartas},
        {"nome": "Semifinais", "id": "semifinais", "jogos": semifinais},
        {"nome": "Grande final", "id": "final", "jogos": final}
    ]

    # Acrescenta o vencedor escolhido a cada jogo
    for fase in fases:
        for jogo in fase["jogos"]:
            jogo["vencedor"] = resultados.get(jogo["id"])

    return fases


@app.route("/")
@app.route("/pagina")
def pagina():
    resultados = session.get("resultados", {})
    fases = montar_chave(resultados)

    # Descobre os times eliminados durante a simulação
    eliminados_jogos = []
    for fase in fases:
        for jogo in fase["jogos"]:
            vencedor = jogo["vencedor"]
            if vencedor:
                perdedor = next(
                    time for time in jogo["times"] if time != vencedor
                )
                eliminados_jogos.append(perdedor)

    campeao = resultados.get("f0")

    return render_template(
        "pagina.html",
        fases=fases,
        eliminados=campeonato.times_eliminados(),
        eliminados_jogos=eliminados_jogos,
        campeao=campeao
    )


@app.route("/escolher", methods=["POST"])
def escolher():
    resultados = session.get("resultados", {})
    jogo_id = request.form.get("jogo_id")
    vencedor = request.form.get("vencedor")

    fases = montar_chave(resultados)
    jogo_encontrado = None

    for fase in fases:
        for jogo in fase["jogos"]:
            if jogo["id"] == jogo_id:
                jogo_encontrado = jogo
                break

    if jogo_encontrado and vencedor in jogo_encontrado["times"]:
        resultados[jogo_id] = vencedor

        if jogo_id.startswith("q"):
            for chave in ("s0", "s1", "f0"):
                resultados.pop(chave, None)
        elif jogo_id.startswith("s"):
            resultados.pop("f0", None)

        session["resultados"] = resultados  # sem esta linha nada é salvo

    return redirect(url_for("pagina"))

@app.route("/reiniciar", methods=["POST"])
def reiniciar():
    session.pop("resultados", None)
    return redirect(url_for("pagina"))


if __name__ == "__main__":
    app.run()