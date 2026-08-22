class Campeonato:
    def __init__(self):
            self.times = ["Cruzeiro", "Palmeiras", "Santos", "Grêmio", "Vitória", "Atlético-MG","Vasco", "Internacional"]
            self.eliminados = ["Flamengo", "Corinthians", "Botafogo", "Fluminense", "Chapecoense", "Ceará", "Bahia", "Sport"]
            self.duelos = {("Cruzeiro", "Atlético-MG"), ("Palmeiras", "Santos"), ("Grêmio", "Internacional"), ("Vasco", "Vitória")}
            
            
            print("Os times que foram eliminados são 👇")
    def times_eliminados(self):
                self.eliminados = ["Flamengo", "Corinthians", "Botafogo", "Fluminense", "Chapecoense", "Ceará", "Bahia", "Sport"]
                return self.eliminados
        
                
times = Campeonato()
print(times.eliminados)

def duelos():
    duelos = {("Cruzeiro", "Atlético-MG"), ("Palmeiras", "Santos"), ("Grêmio", "Internacional"), ("Vasco", "Vitória")}
    return duelos

duelos = duelos()
print("Os duelos da próxima fase são 👇")
print(duelos)

if ("Cruzeiro", "Atlético-MG") in duelos:
    print("Cruzeiro venceu o duelo contra Atlético-MG e está classificado para a próxima fase")
    
if ("Palmeiras", "Santos") in duelos:
    print("Palmeiras venceu o duelo contra Santos e está classificado para a próxima fase")

if ("Grêmio", "Internacional") in duelos:
    print("Grêmio venceu o duelo contra Internacional e está classificado para a próxima fase")

if ("Vasco", "Vitória") in duelos:
    print("Vasco venceu o duelo contra Vitória e está classificado para a próxima fase")
    

def times_classificados():
    times_classificados = ["Cruzeiro", "Palmeiras", "Grêmio", "Vasco"]
    return times_classificados

classificados = times_classificados()
print("Os times classificados para a próxima fase são 👇")
print(classificados)

def duelos_das_semifinais():
    duelos_das_semifinais = {("Cruzeiro", "Vasco"), ("Palmeiras", "Grêmio")}
    return duelos_das_semifinais

if ("Cruzeiro", "Vasco") in duelos_das_semifinais():
    print("Cruzeiro venceu o duelo contra Vasco e está classificado para a final")

if ("Palmeiras", "Grêmio") in duelos_das_semifinais():
    print("Palmeiras venceu o duelo contra Grêmio e está classificado para a final")

semifinais = duelos_das_semifinais()
print("Os duelos das semifinais são 👇")
print(semifinais)


def final_da_copa_do_brasil():
    final_da_copa_do_brasil = {("Cruzeiro", "Palmeiras")}
    return final_da_copa_do_brasil

if ("Cruzeiro", "Palmeiras") in final_da_copa_do_brasil():
    print("Cruzeiro venceu o duelo contra Palmeiras e é o campeão da Copa do Brasil 2026")
    print("Parabéns ao time do Cruzeiro 🏆")