from dataclasses import dataclass
from datetime import date


@dataclass
class Tarefa:
    categoria: str  
    titulo: str
    data_vencimento: date
    concluida: bool = False


def criar_tarefa(categoria, titulo, data_vencimento):
    if not titulo:
        raise ValueError("É obrigatório informar um título para a tarefa.")
    return Tarefa(categoria, titulo, data_vencimento)


def eh_tarefa_concluida(tarefa):
    return tarefa.concluida


def eh_tarefa_pendente(tarefa):
    return not tarefa.concluida


def concluir_tarefa(tarefa):
    if not tarefa.concluida:
        return Tarefa(tarefa.categoria, tarefa.titulo, tarefa.data_vencimento, True)
    return tarefa


def boolean_como_sim_ou_nao(valor_logico):
    return "sim" if valor_logico else "não"


def tarefa_to_string(tarefa):    
    # return f"{tarefa.categoria} -  {tarefa.titulo} - {tarefa.descricao} - Concluída: {tarefa.concluida}"
    return f"{tarefa.titulo} - Vencimento: {tarefa.data_vencimento} - Concluída: {boolean_como_sim_ou_nao(tarefa.concluida)}"