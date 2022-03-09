from datetime import date
"""
Tipos de Campos
As informações contidas nos campos do 
ficheiro podem ser dos tipos (N, D ou C):
N - Numérico
D - Data - informadas no formato DDMMAAAA
C - Alfanumérico(Texto)
"""

data = date.today()

dia = data.day
mes = data.month
ano = data.year
tipo_folha = 0


# Referencia será usado para fornecer o ano, mes e o tipo de ficheiro em referencia
# Nota: o tipo de folha recebe apenas dois valores padrão (0 - Normal & 1 - primeira Complementar)
def _Referencia(ano=ano, mes=mes, tipo_folha=tipo_folha):

    if (mes <= 9):
        return "{}0{}{}".format(ano, mes, tipo_folha)
        # Verificar uma forma de eliminar o zero do string
    else:
        return "{}{}{}".format(ano, mes, tipo_folha)


def _Referencia(dia=dia, mes=mes, ano=ano):

    if (mes <= 9 or dia <= 9):
        return "0{}0{}{}".format(dia, mes, ano)

    else:
        return "{}{}{}".format(dia, mes, ano)


# Nome do Ficheiro
# O nome do ficheiro para o INSS - Folha de Remunerações obedece a seguinte estrutura
# Número de Inscrição no INSS (Antigo)
# Ano de Referência da Folha de Remunerações
# Mês de Referência da Folha de Remunerações
# Indicador de Tipo de Folha de Remunerações (0 - Normal / 1 - primeira Complementar)
def Nome_Ficheiro(n_contribuinte=256):

    return "{}{}".format(n_contribuinte, _Referencia())

# tipo_ficheiro
# Indica o tipo de ficheiro da Folha de Remunerações e deve informar:
# N (normal) para Ficheiro incial com a Folha de Remunerações ou
# C (complementar) para Ficheiro com informações complementares ao ficheiro Normal

# numero_inscricao_empresa_inss
# Número de Inscrição da Empresa no INSS
# Este é o número de Inscrição fornecido no acto do cadastro da empresa junto
# ao Instituto de Segurança Social


def Cabecalho_Ficheiro(tipo_ficheiro="N",
                       numero_inscricao_empresa_inss="000000256"):

    # Estrutura e Tamanho
    # Tipo de Registro -                                Obrigatório: Sim                size: 002
    # Data de Referência -                              Obrigatório: Sim                size: 008
    # Tipo do Ficheiro -                                Obrigatório: Sim                size: 001
    # Número de Inscrição da Empresa no INSS -          Obrigatório: Sim                size: 009
    # Número de Inscrição da Empresa no INSS (Novo) -       size: 020
    # Número do Contribuinte no Ministério das Finanças -   size: 020
    # Nome da empresa -                                     size: 070
    # Código do Município -                                 size: 005
    # Espaços em Branco -                                   size: 045

    # Neste Tipo de Registro, o conteudo sempre deve ser "00", pois
    # indica que é a primeira linha do ficheiro.
    tipo_registro = "00"

    # Indica qual é a Referência da Folha de Remunerações no formato (DDMMAAAA)
    data_referencia = _Referencia(dia, mes, ano)  # size 008

    # Novo Número de Inscrição do INSS
    numero_inscricao_empresa_inss_nova = "                    "

    # Número do Contribuinte Junto ao Ministério das Finanças(NIF)
    nif = "5510126032          "

    # Nome da Empresa (Razão Social)
    nome_da_empresa = "ORGANIZACOES KILAMBAL LDA                                             "

    # Código do Município de Endereço da Empresa, conforme relação
    # de municípios disponibilizados no Anexo I - Relação de Municípios
    codigo_do_municipio = "     "

    # Neste campo devem estar informados apenas espaços em branco
    espacos_em_branco = "                                             "

    # retornando a as variaveis em conformidade com o formato da estrutura do Cabeçalho
    return "{}{}{}{}{}{}{}{}{}".format(tipo_registro, data_referencia, tipo_ficheiro,
                                       numero_inscricao_empresa_inss,
                                       numero_inscricao_empresa_inss_nova,
                                       nif,
                                       nome_da_empresa,
                                       codigo_do_municipio,
                                       espacos_em_branco)

#  Tipo de Registo onde serão informadas as remunerações dos funcionários da Empresa
# (Contribuinte), bem como actualizações de Categoria Profissional e Vinculo Laboral


def Remuneracao_Funcionario_Detalhe():

    # Indicador do Tipo de Registro -                   Obrigatório: Sim   size: 002
    # Número de Inscrição do Segurado no INSS -         Obrigatório: Sim   Size: 009
    # Número de Inscrição do Segurado no INSS (Novo) -  Size: 020
    # Nome do Funcionário (Segurado)                    Obrigatório: Sim   Size: 070
    # Código da Categoria Profissional -                Size: 005
    # Valor do Salário Base -                           Obrigatório: Sim   Size: 014
    # Valor Outras Remunerações Adicionais -            Obrigatório: Sim   Size: 014
    # Inicio do Vinculo -                               size: 008
    # Fim do Vinculo   -                                size: 008
    # Espaços em Branco -                               size: 030

    # Neste Tipo de Registro, o conteúdo sempre deve ser 10
    # pois indica que a linha é de Remunerações do Funcionário auferida no Mês e Ano de Referencia
    tipo_registro = "10"

    # Número de Inscrição do INSS consta no Cartão do Segurado
    numero_inscricao_segurado_inss = "005004879"
    numero_inscricao_segurado_inss_novo = "                    "

    # Nome do Funcionário (Segurado) conforme cadastrado na Empresa
    nome_funcionario_segurado = "ANDRE JORGE CAMPOS                                                    "

    # Código da Categoria Profissional
    cod_categoria_profissional = "     "

    # Valor do Salário Base
    valor_salario_base = "00000025865580"

    # Valor Outras Remunerações Adicionais
    valor_remuneracoes_adicionais = "00000005276966"

    # Inicio do Vinculo
    inicio_vinculo = "        "

    # Fim do Vinculo
    fim_vinculo = "        "

    # Espaços em Branco
    espacos_em_branco = "                              "

    return "{}{}{}{}{}{}{}{}{}{}".format(tipo_registro, numero_inscricao_segurado_inss,
                                         numero_inscricao_segurado_inss_novo,
                                         nome_funcionario_segurado, cod_categoria_profissional,
                                         valor_salario_base, valor_remuneracoes_adicionais,
                                         inicio_vinculo, fim_vinculo, espacos_em_branco)


# Tipo de Registo de finalização das informações do Ficheiro, onde deve conter Resumo de
# Registros e Valor Total de Remunerações contidas no ficheiro
def Totalizador_Ficheiro():

    # Indicador do Tipo de Registo -        Obrigatório: Sim    Size: 002
    # Número Total de Registros do Tipo 10                 - Size: 010
    # Preencher com zeros                                  - Size: 010
    # Soma do Campo "Valor do Salário Base"                - Size: 014
    # Soma do Campo "Valor Outras Remunerações Adicionais" - Size: 014
    # Nome Do Responsável Pela Geração Do Ficheiro         - Size: 040
    # E-Mail Do Responsável Pela Geração Do Ficheiro       - Size: 050
    # Espaços em Branco                                    - Size: 040

    # Neste Tipo de Registro, o conteúdo sempre deve ser "99", pois indica que a linha
    # é de Finalização do Ficheiro
    tipo_registro = "99"

    # Destina a informar a quantidade de Registos do Tipo 10 que  estão contidos no ficheiro
    total_registo_tipo_10 = "0000000000"

    # Preencher com zeros
    zeros = "0000000000"

    # Soma do Campo "Valor do Salário Base"
    total_valor_salario_base = "00000000000000"

    # Soma do Campo "Valor Outras Remunerações Adicionais"
    total_remuneracoes_adicionais = "00000000000000"

    # Nome Do Responsável Pela Geração Do Ficheiro
    responsavel_pela_geracao_do_ficheiro = "FFR_INSS_AO                             "

    # E-Mail Do Responsável Pela Geração Do Ficheiro
    email_responsavel_pela_geracao_do_ficheiro = "ffr@ffr_inss_ao.com                                "

    # Espaços em Branco
    espacos_em_branco = "                                        "

    return "{}{}{}{}{}{}{}{}".format(tipo_registro, total_registo_tipo_10, zeros, total_valor_salario_base,
                                     total_remuneracoes_adicionais, responsavel_pela_geracao_do_ficheiro,
                                     email_responsavel_pela_geracao_do_ficheiro, espacos_em_branco)
