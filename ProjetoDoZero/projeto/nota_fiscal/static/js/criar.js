// Quando o formulário for submetido, envia uma requisição AJAX
// para criar uma nova nota fiscal.
$('#nota-fiscal-form').submit(function(event) {
    // Impede o comportamento padrão de enviar o formulário.
    event.preventDefault();
  
    // Pega os dados do formulário.
    var data_emissao = $('#data_emissao').val();
    var valor_total = $('#valor_total').val();
  
    // Envia a requisição AJAX para criar uma nova nota fiscal.
    $.ajax({
      url: '{% url "criar_nota_fiscal" %}',
      method: 'POST',
      data: {
        'data_emissao': data_emissao,
        'valor_total': valor_total,
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
      },
      success: function(response) {
        // Redireciona para a página de detalhes da nova nota fiscal.
        window.location.href = '{% url "detalhes_nota_fiscal" response.nota_fiscal_id %}';
      },
      error: function(xhr, status, error) {
        // Exibe uma mensagem de erro.
        alert('Ocorreu um erro ao criar a nota fiscal: ' + error);
      }
    });
  });