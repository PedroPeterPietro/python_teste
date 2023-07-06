# Dicionario é um conjunto não-ordenado de pares chave:valor , onde as chaves são únicas em umda dada instância 
alunos = {
    "aluno1": {"Nome": "Pedro", "idade": "23"},
    "aluno2": {"Nome": "Maria", "idade": "20"},
    "aluno3": {"Nome": "João", "idade": "25"}
}

alunos_testes = alunos.copy()
pessoa = {"Nome": "Pedro", "idade": "3"}

pessoa_outro_modo = dict(nome="Pedro", idade = 23)
pessoa["registro"] = "Municipal"
print(pessoa_outro_modo)
teste = pessoa_outro_modo.fromkeys(["Endereço:"])


print(pessoa["Nome"].upper())
print(teste)

for aluno in alunos:
      for item in aluno:
         print(item)

for aluno in alunos_testes:
     print(aluno)

teste_iterar: list = alunos["aluno1"].keys()

print(teste_iterar)

print(pessoa.keys())

resultado = "aluno1" in alunos
print(resultado)