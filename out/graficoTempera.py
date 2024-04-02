import ast
import sys
import matplotlib.pyplot as plt

args = sys.argv

if len(sys.argv) < 2:
  print("Erro:  Nome do arquivo não informado")
  print("Uso:   python graficoAG.py <filename>")
  sys.exit(1)
  
filename = args[1]
  
with open(filename, "r") as arquivo:
  texto = arquivo.read()

# 1: descricao
# 2: cidades
# 3: distancias
# 4 - n: gerações

linhas = texto.split("\n")
qtd_cidades = linhas[0]
cidades = ast.literal_eval(linhas[1])
body = linhas[2:]

cidadesX = [cidade[0] for cidade in cidades]
cidadesY = [cidade[1] for cidade in cidades]

geracoes = []
melhorGeracao = []
melhorGlobal = []
estadosGlobal = []



for content in body:
  for index, item in enumerate(content.split("|")):
    if index == 0 and item.strip():
      geracoes.append(int(item.strip()))
    elif index == 1 and item.strip():
      melhorGlobal.append(float(item.strip()))
    elif index == 2 and item.strip():
      melhorGeracao.append(float(item.strip()))
    elif index == 3 and item.strip():
      estadosGlobal.append(ast.literal_eval(item.strip()))

x = geracoes

plt.figure() 
plt.plot(x, melhorGeracao, label="Melhor da geração")
plt.plot(x, melhorGlobal, label="Melhor global")
plt.legend()
plt.title(f"Tempura Simulada ")

plt.xlabel("Geração")
plt.ylabel("Custo")
plt.savefig(f"{filename}_adaptacao_do_AG.png")

primeiraConexao = estadosGlobal[0]
primeiraConexao.append(primeiraConexao[0])

ultimaConexao = estadosGlobal[-1]
ultimaConexao.append(ultimaConexao[0])


plt.figure() 
for i in range(len(primeiraConexao) - 1):
    idx1 = int(primeiraConexao[i])
    idx2 = int(primeiraConexao[i+1])
    plt.plot([cidadesX[idx1], cidadesX[idx2]], [cidadesY[idx1], cidadesY[idx2]], f'r-')
plt.legend(['Conexão'])
plt.scatter(cidadesX, cidadesY)
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.savefig(f"{filename}_primeira_conexao.png")
plt.title('Primeira conexao')

plt.figure() 
for i in range(len(ultimaConexao) - 1):
  plt.plot([cidadesX[ultimaConexao[i]], cidadesX[ultimaConexao[i+1]]],[cidadesY[ultimaConexao[i]], cidadesY[ultimaConexao[i+1]]], f'r-')
plt.legend(['Conexão'])
plt.scatter(cidadesX, cidadesY)
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('Melhor conexao')
plt.savefig(f"{filename}_melhor_conexao.png")
plt.show()
