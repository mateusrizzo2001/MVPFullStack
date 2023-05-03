from flask import Flask, request
from flask_swagger import swagger 
import sqlite3

app = Flask(__name__)

banco = sqlite3.connect('mvp_livros.db')
cursor = banco.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS livros_registrados (titulo TEXT, autor TEXT, ano INTEGER)')

@app.route("/swagger")
def get_swagger():
    swag = swagger(app)
    swag['info']['title'] = "API de livros"
    swag['info']['version'] = "1.0"
    return swag

@app.route('/cadastrar_livro', methods=['POST'])
def cadastrar_livro():
    titulo = request.form['titulo']
    autor = request.form['autor']
    ano = request.form['ano']
    cursor.execute('INSERT INTO livros_registrados (titulo, autor, ano) VALUES (?, ?, ?)', (titulo, autor, ano))
    banco.commit()
    return 'Livro cadastrado com sucesso!'

@app.route('/buscar_livro', methods=['GET'])
def buscar_livro():
    id = request.args.get('id')
    cursor.execute('SELECT * FROM livros_registrados WHERE rowid = ?', (id,))
    livro = cursor.fetchone()
    if livro:
        return f'Livro encontrado: {livro}'
    else:
        return 'Livro não encontrado'

@app.route('/deletar_livro', methods=['POST'])
def deletar_livro():
    id = request.form['id']
    cursor.execute('DELETE FROM livros_registrados WHERE rowid = ?', (id,))
    banco.commit()
    return 'Livro deletado com sucesso!'

if __name__ == '__main__':
    app.run()
