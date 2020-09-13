#Faz a conexão com o MySQL

import mysql.connector #ao utilizar pela primeira vez: para importar tem q instalar a biblioteca C:\Users\miche\AppData\Local\Programs\Python\Python38-32\Scripts>pip install mysql-connector-python

class Conexao(object):

    def conectar(self):
        try:
            self._conexao = mysql.connector.connect(
                host = "localhost", 
                user = "root", 
                password = "2435136",
                #database = "db_my_sql_python" #esse comando só se usa quando eu já tenho o banco de dados criado lá pelo phpMyAdmin ou pelo MySQL, daí é só conectar a ele por esse comando e, nesse caso, nao preciso usar o comando: "USE db_my_sql_python" lá da linha 25
            )
        except Exception as e:
            print('Não foi possível realizar a conexão com o banco de dados')
            print(e)

        self._cursor = self._conexao.cursor()  #o self. deixa essa variável disponível para todos os métodos dessa classe
        
        #criar banco de dados
        try:
            self._cursor.execute("CREATE DATABASE IF NOT EXISTS db_my_sql_python")
        except Exception as e:
            print('Não foi possível criar o banco de dados')
            print(e)
        else:
            print('Banco de dados criado com sucesso')
        
        """
        #mostra os bancos de dados existentes
        cursor.execute("SHOW DATABASES")

        for i in cursor:
            print(i)
        """

        #informa que eu quero usar o banco de dados db_my_sql_python - esse comando é usado só para quando eu crio o banco de dados por aqui, se eu criar ele lá pelo phpMyAdmin ou pelo MySQL direto, nao precisa disso, é só fazer a conexão com o banco lá  na linha 9 
        self._cursor.execute("USE db_my_sql_python")
        
        #adicionar tabela ao banco de dados
        try:
            sql = "CREATE TABLE IF NOT EXISTS tabela_mysql (id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT, nome VARCHAR(50) NOT NULL, idade INT(3))"
            self._cursor.execute(sql)
        except Exception as e:
            print('Não foi possível criar a tabela')
            print(e)
        else:
            print('Tabela criada com sucesso')
    
    #fecha as conexões com o banco
    def desconectar(self):
        try:
            self._cursor.close()
            self._conexao.close()
        except Exception as e:
            print('Erro ao fechar conexão')
            print(e)

    #getters 
    def get_cursor(self):
        return self._cursor
    
    def get_conexao(self):
        return self._conexao
