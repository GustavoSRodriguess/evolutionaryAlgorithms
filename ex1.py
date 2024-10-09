import time

class Elevador:
    def __init__(self, andares=10):
        self.andar_atual = 0
        self.direcao = None  # subindo ou descendo
        self.chamadas_externas = []  # lista de tuplas andar, direcao
        self.chamadas_internas = []  # lista andar
        self.portas_abertas = False
        self.andares = andares
    
    def chamar_elevador(self, andar, direcao):
        #adc andar de fora
        if 0 <= andar < self.andares:
            self.chamadas_externas.append((andar, direcao))
            print(f"Chamado recebido para o andar {andar}, direção: {direcao}.")
        else:
            print("Andar inválido!")
    
    def selecionar_andar(self, andar):
        #adc andar de dentro
        if 0 <= andar < self.andares:
            self.chamadas_internas.append(andar)
            print(f"Andar {andar} selecionado dentro do elevador.")
        else:
            print("Andar inválido!")
    
    def abrir_portas(self):
        #abre porta
        self.portas_abertas = True
        print(f"Portas abertas no andar {self.andar_atual}.")
        time.sleep(2)  # simula tempo rpa entrar/sair
    
    def fechar_portas(self):
        #fecha portas
        self.portas_abertas = False
        print("Portas fechadas.")
    
    def mover(self):
        while self.chamadas_externas or self.chamadas_internas:
            # define direcao com base nas chamadas 
            if self.chamadas_externas:
                proximo_andar, direcao = self.chamadas_externas[0]
            else:
                proximo_andar = self.chamadas_internas[0]
                direcao = 'subindo' if proximo_andar > self.andar_atual else 'descendo'
            
            self.direcao = direcao
            
            # move o elevas
            if self.direcao == 'subindo' and self.andar_atual < proximo_andar:
                self.andar_atual += 1
                print(f"Elevador subindo para o andar {self.andar_atual}.")
            elif self.direcao == 'descendo' and self.andar_atual > proximo_andar:
                self.andar_atual -= 1
                print(f"Elevador descendo para o andar {self.andar_atual}.")
            
            time.sleep(2)  # so pra simular o tempo 
            
            # verifica se chego no andar
            if self.andar_atual == proximo_andar:
                self.abrir_portas()
                self.fechar_portas()
                
                if (proximo_andar, direcao) in self.chamadas_externas:
                    self.chamadas_externas.remove((proximo_andar, direcao))
                if proximo_andar in self.chamadas_internas:
                    self.chamadas_internas.remove(proximo_andar)
        
        print("Todas as chamadas atendidas.")

def interface_usuario(elevador):
    while True:
        print("\nEscolha uma ação:")
        print("1. Chamar elevador de um andar (externo)")
        print("2. Selecionar andar dentro do elevador (interno)")
        print("3. Mover o elevador")
        print("4. Sair")
        
        escolha = input("Digite o número da ação desejada: ")

        if escolha == '1':
            andar = int(input("Digite o andar de onde deseja chamar o elevador (0 a 9): "))
            direcao = input("Digite a direção (subindo/descendo): ")
            elevador.chamar_elevador(andar, direcao)
        elif escolha == '2':
            andar = int(input("Digite o andar que deseja selecionar dentro do elevador (0 a 9): "))
            elevador.selecionar_andar(andar)
        elif escolha == '3':
            elevador.mover()
        elif escolha == '4':
            print("Encerrando o simulador.")
            break
        else:
            print("Escolha inválida! Tente novamente.")

elevador = Elevador()
interface_usuario(elevador)
