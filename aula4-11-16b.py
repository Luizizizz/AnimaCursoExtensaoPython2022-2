#1º passo: importar a biblioteca sqlite3
import sqlite3

#2º passo: estabelecer conexão com o banco
conn = sqlite3.connect("dc_universe.db")

#3º passo: criar um objeto do tipo cursor
cursor_ex = conn.cursor()

#4º passo: comando para inserir um herói/vilão
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES(12, 'The Flash', 'Barry Allen', 'Herói(na)')"
#5º passo: Executar o comando SQL
print(cursor_ex.execute(sql))

#6º passo: Faz o commit e fecha o banco
conn.commit()
conn.close()