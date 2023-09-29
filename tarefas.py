# Uma lista de tarefas consiste em um dicionário python 'defaultdict(list)' em que
# as chaves (keys) são as 'categorias de tarefas' e os valores (values) são listas
# de objetos da classe de dados Tarefa.


from collections import defaultdict
# from categoria import incluir_categoria, obter_categoria_existente, categoria_existe
from tarefa import tarefa_to_string, eh_tarefa_pendente, eh_tarefa_concluida


# retorna um dicionário de listas
def criar_lista_de_tarefas():
    return defaultdict(list)


# retorna uma lista com as chaves (categorias) do dicionário ordenadas em ordem alfabética 
def obter_categorias(mapa_de_tarefas):   
    return sorted(mapa_de_tarefas.keys(), key=str.lower)


# retorna um valor lógico indicando se uma 'categoria procurada' existe no dicionário
# notar que a verificação é feita de forma case insensitive, ou seja, se eu procurar
# por uma categoria 'COMPRAR' e a chave já existente no dicionário for 'Comprar', a função
# retorna o valor True
def categoria_existe(mapa_de_tarefas, categoria_procurada):    
    # list comprehension
    return any(categoria.lower() == categoria_procurada.strip().lower() for categoria in mapa_de_tarefas)


# procura por uma 'categoria_procurada' entre as chaves do dicionário e retorna a 'categoria' 
# (chave) da forma que eventualmente já esteja armazenada no dicionário. No caso da 'categoria_procurada'
# não existir nas chaves do dicionário, a própria categoria_procurada é retornada pela função 
def obter_categoria_existente(mapa_de_tarefas, categoria_procurada):      
    if categoria_existe(mapa_de_tarefas, categoria_procurada):
        categoria_minuscula = categoria_procurada.lower()
        for categoria in mapa_de_tarefas.keys():
            if categoria.lower() == categoria_minuscula:
                return categoria
    
    return categoria_procurada


# inclui uma entrada sem tarefas no dicionário, isto é, cria uma categoria de tarefas para que
# as tarefas dessa categoria sejam incluídas posteriormente
# se a categoria já existe (case insensitive), não faz nada
# ao final, a função retorna o dicionário com a categoria_para_inclusao (seja porque 
# já existia ou porque foi incluída na função 
def incluir_categoria(mapa_de_tarefas, categoria_para_inclusao):
    if not isinstance(categoria_para_inclusao, str):
        return mapa_de_tarefas
    
    if categoria_para_inclusao.strip() == "":
        return mapa_de_tarefas

    if categoria_existe(mapa_de_tarefas, categoria_para_inclusao):
        return mapa_de_tarefas
    
    mapa_de_tarefas[categoria_para_inclusao] = []                      

    return mapa_de_tarefas 


# adiciona uma tarefa no dicionário associada à chave categoria da tarefa 
def adicionar_tarefa(mapa_de_tarefas, tarefa):
    mapa = mapa_de_tarefas
    categoria_para_incluir = tarefa.categoria
    mapa = incluir_categoria(mapa, categoria_para_incluir)
    categoria_salva = obter_categoria_existente(mapa, categoria_para_incluir)
    return mapa[categoria_salva].append(tarefa)  


# retorna a quantidade de tarefas associadas a determinada categoria
def contar_tarefas_da_categoria(mapa_de_tarefas, categoria_procurada):
    if categoria_existe(mapa_de_tarefas, categoria_procurada):
        categoria = obter_categoria_existente(mapa_de_tarefas, categoria_procurada)
        return len(mapa_de_tarefas[categoria])
    
    return 0            

 
# retorna a quantidade de tarefas em todo o dicionário
def contar_total_de_tarefas(mapa_de_tarefas):
    #list comprehension
    todas_as_tarefas = [item for lista in mapa_de_tarefas.values() for item in lista]    
    return len(todas_as_tarefas)


# imprime todas as tarefas de determinada categoria
def __imprimir_tarefas_da_categoria__(tarefas, categoria):
    return f"{categoria}\n" + "\n".join(f" ->  {tarefa_to_string(tarefa)}" for tarefa in tarefas)
    
        
# imprime todas as tarefas do dicionário        
def imprimir_tarefas(mapa_de_tarefas):
    categorias_ordenadas = sorted(mapa_de_tarefas.keys(), key=str.lower)
    tarefas_como_texto = map(lambda categoria: __imprimir_tarefas_da_categoria__(mapa_de_tarefas[categoria], categoria), categorias_ordenadas)
    return "\n".join(tarefas_como_texto)
  

# filtro que retorna todas as tarefas não concluídas (pendentes) do dicionário
def filtrar_tarefas_pendentes(mapa_de_tarefas):
    tarefas_pendentes_por_categoria = {}
        
    for categoria, tarefas in mapa_de_tarefas.items():
        tarefas_pendentes = list(filter(lambda tarefa: eh_tarefa_pendente(tarefa), tarefas))
        
        if tarefas_pendentes:
            tarefas_pendentes_por_categoria[categoria] = tarefas_pendentes
    
    return tarefas_pendentes_por_categoria


# filtro que retorna todas as tarefas concluídas do dicionário
def filtrar_tarefas_concluidas(mapa_de_tarefas):
    tarefas_concluidas_por_categoria = {}
        
    for categoria, tarefas in mapa_de_tarefas.items():
        tarefas_concluidas = list(filter(lambda tarefa: eh_tarefa_concluida(tarefa), tarefas))
        
        if tarefas_concluidas:
            tarefas_concluidas_por_categoria[categoria] = tarefas_concluidas
    
    return tarefas_concluidas_por_categoria


# função para excluir uma tarefa do dicionário
def excluir_tarefa(mapa_de_tarefas, tarefa_para_excluir):
    categoria = tarefa_para_excluir.categoria
    tarefas = mapa_de_tarefas[categoria]
    for tarefa in tarefas:
        if tarefa == tarefa_para_excluir:
            tarefas.remove(tarefa)
    return mapa_de_tarefas


# função para excluir uma determinada categoria do dicionário caso não existam tarefas associadas
def excluir_categoria(mapa_de_tarefas, categoria_para_exclusao):
    if not isinstance(categoria_para_exclusao, str):
        raise TypeError("Uma categoria deve ser um texto.")

    if not categoria_existe(mapa_de_tarefas, categoria_para_exclusao):
        return mapa_de_tarefas
        
    categoria_existente = obter_categoria_existente(mapa_de_tarefas, categoria_para_exclusao)        
    
    if not mapa_de_tarefas[categoria_existente]:
        del mapa_de_tarefas[categoria_existente]
        
    return mapa_de_tarefas   