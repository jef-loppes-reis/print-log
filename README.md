# Print Logs

Este código define uma classe PrintLog que ajuda a registrar mensagens de forma formatada utilizando a biblioteca rich para Python. Ele permite imprimir mensagens com 
estilos diferentes no console (por exemplo, sucesso, error, alerta) e, opcionalmente, incluir um título no painel da mensagem.

## Explicação do código

- **Dicionário `styles`:** Mapeia nomes de estilos como `'sucesso'`, `'error'` e `'alerta'` para strings de estilo específicas do rich (exemplo: _'bold green'_, _'red'_, _'yellow'_).
- **Método `__init__()`:** Inicializa uma instância de Console, que será usada para imprimir as mensagens.
- **Método `log()`:** Recebe texto, estilo e um título opcional. Ele envolve o texto em um Panel (uma caixa ao redor da mensagem no terminal) com o estilo especificado no dicionário styles e imprime no console.
- **Método `log_trace_back()`:** Imprime o traceback completo de um erro, incluindo as variáveis locais no rastreamento de erros.

## Como usar

```python
# Instancia a classe PrintLog
log = PrintLog()

# Registra uma mensagem de erro
log.log("Ocorreu um erro!", "erro", title="Error")

# Registra uma mensagem de sucesso
log.log("A operação foi bem-sucedida!", "sucesso", title="Sucesso")

# Registra uma mensagem de alerta
log.log("Aviso: Algo pode estar errado!", "alerta", title="Alerta")

# Imprime o traceback de uma exceção
log.log_trace_back()  # Normalmente utilizado dentro de um bloco de tratamento de exceção
```

**Exemplo de saída:**

```css
[Erro] Ocorreu um erro! [red]
```

A saída será estilizada com base no estilo escolhido e a mensagem aparecerá em um painel com o título opcional.
