import sqlite3


class livrosDB:

    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS livros ('
                            'livroID INTEGER PRIMARY KEY AUTOINCREMENT,'
                            'titulo TEXT NOT NULL,'
                            'autor TEXT NOT NULL,'
                            'genero TEXT NOT NULL,'
                            'anoLancamento TEXT NOT NULL'
                            ')')
        self.conn.commit()

    def inserir(self, titulo, autor, genero, anoLancamento):
        consulta = 'INSERT OR IGNORE INTO livros (titulo, autor, genero, anoLancamento) VALUES (?, ?, ?, ?)'
        self.cursor.execute(consulta, (titulo, autor, genero, anoLancamento))
        self.conn.commit()

    def editar(self, livroID, titulo, autor, genero, anoLancamento):
        consulta = 'UPDATE livros SET titulo=?, autor=?, genero=?, anoLancamento=? where livroID=?'
        self.cursor.execute(consulta, (livroID, titulo, autor, genero, anoLancamento))
        self.conn.commit()

    def excluir(self, livroID):
        consulta = 'DELETE FROM livros WHERE livroID=?'
        self.cursor.execute(consulta, (livroID,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM livros')
        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()

    def buscar(self, valor):
        consulta = 'SELECT * FROM livros where titulo LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))
        for linha in self.cursor.fetchall():
            print(linha)


class alugueresDB:

    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS alugueres ('
                            'aluguelID INTEGER PRIMARY KEY AUTOINCREMENT,'
                            'livroID TEXT NOT NULL,'
                            'cpf TEXT NOT NULL,'
                            'dataAluguel TEXT NOT NULL,'
                            'dataDevol TEXT NOT NULL'
                            ')')
        self.conn.commit()

    def inserir(self, livroID, cpf, dataAluguel, dataDevol):
        consulta = 'INSERT OR IGNORE INTO alugueres (livroID, cpf, dataAluguel, dataDevol) VALUES (?, ?, ?, ?)'
        self.cursor.execute(consulta, (livroID, cpf, dataAluguel, dataDevol))
        self.conn.commit()

    def editar(self, aluguelID, livroID, cpf, dataAluguel, dataDevol):
        consulta = 'UPDATE alugueres SET livroID=?, cpf=?, dataAluguel=?, dataDevol=? where aluguelID=?'
        self.cursor.execute(consulta, (aluguelID, livroID, cpf, dataAluguel, dataDevol))
        self.conn.commit()

    def excluir(self, aluguelID):
        consulta = 'DELETE FROM alugueres WHERE aluguelID=?'
        self.cursor.execute(consulta, (aluguelID,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM alugueres')
        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()

    def buscar(self, valor):
        consulta = 'SELECT * FROM alugueres where cpf LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))
        for linha in self.cursor.fetchall():
            print(linha)


class usuariosDB:

    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS usuarios ('
                            'usuerID INTEGER PRIMARY KEY AUTOINCREMENT,'
                            'nome TEXT NOT NULL,'
                            'cpf TEXT NOT NULL,'
                            'telefone TEXT NOT NULL,'
                            'email TEXT NOT NULL'
                            ')')
        self.conn.commit()

    def inserir(self, nome, cpf, telefone, email):
        consulta = 'INSERT OR IGNORE INTO usuarios (nome, cpf, telefone, email) VALUES (?, ?, ?, ?)'
        self.cursor.execute(consulta, (nome, cpf, telefone, email))
        self.conn.commit()

    def editar(self, userID, nome, cpf, telefone, email):
        consulta = 'UPDATE usuarios SET nome=?, cpf=?, telefone=?, email=? where userID=?'
        self.cursor.execute(consulta, (userID, nome, cpf, telefone, email))
        self.conn.commit()

    def excluir(self, userID):
        consulta = 'DELETE FROM usuarios WHERE userID=?'
        self.cursor.execute(consulta, (userID,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM usuarios')
        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()

    def buscar(self, valor):
        consulta = 'SELECT * FROM usuarios where cpf LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))
        for linha in self.cursor.fetchall():
            print(linha)

if __name__ == '__main__':
    livros = livrosDB('thrustorys.db')
    livros.inserir('harry potter e a pedra filosofal', 'J.K. Rollan', 'fantasia','1997')
    livros.inserir('anne de green gables', 'L. M. Montgomery', 'romance', '1908')
    alugueres = alugueresDB('thrustorys.db')
    alugueres.inserir('1', '111.111.111-11', '02/05/24', '06/05/24')
    alugueres.inserir('2', '222.222.222-22', '01/05/24', '05/05/24')
    usuarios = usuariosDB('thrustorys.db')
    usuarios.inserir('gabriel pereira andrade', '111.111.111-11', '(74)91111-1111', 'g@gmail.com')
    usuarios.inserir('maria clara pereira andrade', '222.222.222-22', '(74)92222-2222', 'm@gmail.com')