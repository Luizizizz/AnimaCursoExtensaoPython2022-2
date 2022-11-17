#1º passo: importar a biblioteca sqlite3
import sqlite3

#2º passo: estabelecer conexão com o banco
conn = sqlite3.connect("dc_universe.db")

#3º passo: criar um objeto do tipo cursor
cursor_ex = conn.cursor()

#4º passo: Comando SQL do banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#5º passo: Executar o camando do 4º passo no SQLlite(no cursor)
cursor_ex.execute(sql)

#6º passo: Exibir a consulta com todos os nomes de heróis e vilões do banco de dados
pessoas = cursor_ex.fetchall()
  
#for pessoa in pessoas:
# print(pessoa)

for pessoa in pessoas:
  print(f"Nome: {pessoa[1]} ({pessoa[2]})")