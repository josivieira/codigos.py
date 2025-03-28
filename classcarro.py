class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano})"

def iniciar_jogo():
    carros = [
        Carro("Toyota", "Corolla", 2020),
        Carro("Ford", "Mustang", 1967),
        Carro("Chevrolet", "Camaro", 2015),
        Carro("Honda", "Civic", 2018),
        Carro("Volkswagen", "Golf", 2016)
    ]
    
    carro_escolhido = random.choice(carros)
    
    print("Adivinhe o carro!")
    tentativa = Carro(input("Marca: "), input("Modelo: "), int(input("Ano: ")))
    
    if (tentativa.marca.lower() == carro_escolhido.marca.lower() and
        tentativa.modelo.lower() == carro_escolhido.modelo.lower() and
        tentativa.ano == carro_escolhido.ano):
        print("Parabéns! Você acertou!")
    else:
        print(f"Errado! Era {carro_escolhido}.")

if __name__ == "__main__":
    iniciar_jogo()