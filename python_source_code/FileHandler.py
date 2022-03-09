import FileLayout as fl


def Criar_Ficheiro():
    # Abre um ficheiro no formato txt para escrever e criar se não existir
    ficheiro = open(fl.Nome_Ficheiro()+".txt", "w+")

    ficheiro.write(fl.Cabecalho_Ficheiro()+"\n")
    ficheiro.write(fl.Remuneracao_Funcionario_Detalhe()+"\n")
    ficheiro.write(fl.Totalizador_Ficheiro())
