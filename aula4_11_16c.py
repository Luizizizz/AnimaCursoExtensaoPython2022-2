#1º passo: importar a biblioteca sqlite3
import sqlite3

#PASSOS 2 e 3 VIRARÃO função conectar()
def conectar():
  #2º passo: estabelecer conexão com o     banco
  conn = sqlite3.connect("dc_universe.db")
 
  #3º passo: criar um objeto do tipo cursor
  cursor_ex = conn.cursor()

  return conn, cursor_ex

