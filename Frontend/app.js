// função para cadastrar um livro
function cadastrarLivro(livro) {
    fetch('/cadastrar_livro', {
      method: 'POST',
      body: JSON.stringify(livro),
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error(error))
  }
    
  // função para buscar um livro pelo ID
  function buscarLivro(id) {
    fetch(`/buscar_livro/${id}`)
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error(error))
  }
    
  // função para deletar um livro pelo ID
  function deletarLivro(id) {
    fetch(`/deletar_livro/${id}`, { method: 'DELETE' })
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error(error))
  }
  