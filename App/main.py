from conexao import criar_conexao, fechar_conexao

def insere_usuario(con, nome, email, senha):
    cursor = con.cursor()
    sql = "INSERT INTO usuario (nome, email, senha) values (%s, %s, %s)"
    valores = (nome, email, senha)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

def select_todos_usuarios(con):
    cursor = con.cursor()
    sql = "SELECT id, nome, email FROM usuario"
    cursor.execute(sql)

    for (id, nome, email) in cursor:
        print(id, nome, email)
    
    cursor.close()


def main():
    con = criar_conexao("localhost", "root", "", "db")

    insere_usuario(con, "Ola Mundo", "ola@mundo.com.br", "olamundo")
    select_todos_usuarios(con)

    fechar_conexao(con)


if __name__ == "__main__":
    main()
