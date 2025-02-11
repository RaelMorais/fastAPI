from fastapi import FastAPI
from fastapi.responses import JSONResponse
app = FastAPI()

lista_tarefas = [
    {"id": 1, "nome": "Lavar o carro" , "data_vencimento" : "20/12/2025", "status": "Pendente", "categoria": "prioridades"},
    {"id": 2, "nome": "Lavar o carro" , "data_vencimento" : "20/12/2025", "status": "Pendente", "categoria": "prioridades"},
    {"id": 2, "nome": "Lavar o carro" , "data_vencimento" : "20/12/2025", "status": "Pendente", "categoria": "prioridades"},
]

@app.get("/tarefas")
def ler_tarefas():
    return lista_tarefas

@app.get("/tarefas/{id}")
def ler_tarefa_especifica(id: int):
    for tarefa in lista_tarefas:
        if tarefa['id'] == id:
            return tarefa
    else:
            return JSONResponse(status_code=404)
@app.get("/tarefas/nome/{nome}")
def ler_tarefa_por_nome(nome: str):
    tarefas_encontradas = [tarefa for tarefa in lista_tarefas if nome.lower() in tarefa['nome'].lower()]
    if tarefas_encontradas:
        return tarefas_encontradas
    return {"erro": "Tarefa não encontrada"}

@app.get("/tarefas/status/{status}")
def ler_tarefas_por_status(status: str):
    tarefas_encontradas = [tarefa for tarefa in lista_tarefas if tarefa['status'].lower() == status.lower()]
    if tarefas_encontradas:
        return tarefas_encontradas
    return JSONResponse(status_code=404, content={"erro": "Nenhuma tarefa encontrada"})
    