#realiza o CRUD do cliente

from conexaoMySQL import Conexao

class Crud(object):

    def __init__(self):
            try:
                self.con = Conexao()
                self.con.conectar()
                self.cursor = self.con.get_cursor() 
                self.conexao = self.con.get_conexao()
            except Exception as e:
                print('Erro ao fazer a conexão pelo crud')
                print(e)


    #adicionar dados no banco
    def adicionarNovoUsuario(self,usuario):
        try:
            self.cursor.execute("INSERT INTO tabela_mysql (nome,idade) VALUES (%s,%s)", (usuario.get_nome(), usuario.get_idade(), )) #isso é p evitar SQL Injection (NUNCA USAR OS CARACTERES + E % NOS PARÂMETROS QUE SERÃO USADO NA QUERY SQL PARA EVITAR SQL INJECTION,É IMPORTANTE PRIMEIRO CONVERTER OS DADOS QUE SERÃO USADOS NA QUERY SQL EM STRING E NÃO PASSAR O DADO NO FORMATO DIGITADO PELO USUÁRIO)
            self.conexao.commit()     
        except Exception as e:
            print('\nErro! Não foi possível inserir usuário')
            print(e)
        else:
            print('\n..usuario adicionado com sucesso..')
        finally:
            self.con.desconectar()

    
    #atualizar dados do banco
    def atualizarDados(self):
        print('\n...:: ATUALIZAR CLIENTE ::...')
        id_usu = input('\nInsira o ID do usuário: ')

        try:
            self.cursor.execute("SELECT * FROM tabela_mysql WHERE id = %s", (id_usu, ))

            print()
            for i in self.cursor:
                print(f'Id: {i[0]}\nNome: {i[1]}\nIdade: {i[2]}')
        except Exception as e:
            print("\nNão foi possível localizar usuário")
            print(e)
        else:
            novo_nome = input('\nInsira o novo nome: ')

            try:
                self.cursor.execute("UPDATE tabela_mysql SET nome = %s WHERE id = %s limit 1", (novo_nome, id_usu, )) #limit 1 pra que seja alterado somente 1 linha, caso existam outros id's iguais na tabela, esses nao serao mudados
                self.conexao.commit()
            except Exception as e:
                print("\nNão foi possível atualizar dados do usuário")
                print(e)
            else:
                print('\nDados atualizados com sucesso')
            finally:
                self.con.desconectar()

    
    #deletar dados do banco
    def excluirUsuario(self):
        id_usu = input('\nInsira o ID do usuário a ser excluído: ')
        opcao = input('\nTem certeza que deseja escluir usuário? (s/n)\n')

        try:
            if opcao == 's':
                self.cursor.execute("DELETE FROM tabela_mysql WHERE id = %s", (id_usu, ))
                self.conexao.commit()              
            else:
                print('\noperação cancelada\n')
                exit()
        except Exception as e:
            print('\nErro ao realizar operação\n')
            print(e)
        else:
            print('\n..Usuario excluído com sucesso..')
        finally:
            self.con.desconectar()
    
