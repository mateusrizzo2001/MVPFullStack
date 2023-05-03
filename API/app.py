from flask import Flask, request, render_template, make_response
from flask_swagger import swagger 
import sqlite3

app = Flask(__name__)

banco = sqlite3.connect('mvp_livros.db')
cursor = banco.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS livros_registrados (titulo TEXT, autor TEXT, ano INTEGER, id INTEGER PRIMARY KEY AUTOINCREMENT)')

@app.route("/swagger")
def get_swagger():
    swag = swagger(app, prefix='/v1')
    swag['info']['title'] = "API de livros"
    swag['info']['version'] = "1.0"
    return swag

@app.route('/v1/cadastrar_livro', methods=['POST'])
def cadastrar_livro():
    """
    Cadastra um novo livro no banco de dados.

    ---
    parameters:
      - name: titulo
        in: formData
        type: string
        required: true
      - name: autor
        in: formData
        type: string
        required: true
      - name: ano
        in: formData
        type: integer
        required: true
    responses:
      200:
        description: Livro cadastrado com sucesso.
    """
    titulo = request.form['titulo']
    autor = request.form['autor']
    ano = request.form['ano']
    cursor.execute('INSERT INTO livros_registrados (titulo, autor, ano) VALUES (?, ?, ?)', (titulo, autor, ano))
    banco.commit()
    return 'Livro cadastrado com sucesso!'

@app.route('/v1/buscar_livro', methods=['GET'])
def buscar_livro():
    """
    Busca um livro pelo ID.

    ---
    parameters:
      - name: id
        in: query
        type: integer
        required: true
    responses:
      200:
        description: Livro encontrado.
      404:
        description: Livro não encontrado.
    """
    id = request.args.get('id')
    cursor.execute('SELECT * FROM livros_registrados WHERE id = ?', (id,))
    livro = cursor.fetchone()
    if livro:
        return f'Livro encontrado: {livro}'
    else:
        return 'Livro não encontrado', 404

@app.route('/v1/deletar_livro', methods=['POST'])
def deletar_livro():
    """
    Deleta um livro pelo ID.

    ---
    parameters:
      - name: id
        in: formData
        type: integer
        required: true
    responses:
      200:
        description: Livro deletado com sucesso.
      404:
        description: Livro não encontrado.
    """
    id = request.form['id']
    cursor.execute('DELETE FROM livros_registrados WHERE id = ?', (id,))
    banco.commit()
    if cursor.rowcount > 0:
        return 'Livro deletado com sucesso!'
    else:
        return 'Livro não encontrado', 404

@app.route('/')
def home():
    cursor.execute('SELECT * FROM livros_registrados')
    livros = cursor.fetchall()
    response = make_response(render_template('index.html', livros=livros))
    response.headers['Cache-Control'] = 'no-cache'
    return response


if __name__ == '__main__':
    app.run(debug=True)

