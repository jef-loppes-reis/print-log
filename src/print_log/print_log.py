"""---"""
from rich.console import Console
from rich.panel import Panel

class PrintLog:
    """
    Classe para registrar e exibir logs formatados no console utilizando a biblioteca `rich`.
    
    Métodos
    -------
    log(texto: str, estilo: str, título: str = None)
        Exibe uma mensagem formatada no console com o estilo e título especificados.

    log_trace_back()
        Exibe o traceback completo de uma exceção, incluindo variáveis locais.
    
    Exemplos
    --------
    >>> Exemplo de uso da classe PrintLog
        log = PrintLog()
    
    >>> Log de erro
        log.log("Ocorreu um erro!", "error", title="Erro")

    >>> Log de sucesso
        log.log("A operação foi bem-sucedida!", "sucess", title="Sucesso")
    
    >>> Log de alerta
        log.log("Aviso: Algo pode estar errado!", "alert", title="Alerta")

    >>> Exibindo o traceback de uma exceção
        try:
            1 / 0  # Causa uma exceção de divisão por zero
        except ZeroDivisionError:
            log.log_trace_back()
    """

    styles: dict[str, str] = {
        'sucess': 'bold green',
        'error': 'red',
        'alert': 'yellow'
    }

    def __init__(self):
        """
        Inicializa uma instância da classe PrintLog.

        Cria um objeto `Console` que será usado para imprimir mensagens no console.
        """
        self.console: Console = Console()

    def log(self, text: str, style: str, title: str = None):
        """
        Exibe uma mensagem formatada no console com o estilo e título especificados.
        
        Parâmetros
        ----------
        text : str
            O texto da mensagem a ser exibido.
        
        style : str
            O estilo de exibição da mensagem. Pode ser um dos seguintes valores: 
            `sucess`, `error` ou `alert`.
        
        title : str, opcional
            O título que será exibido na parte superior do painel. O padrão é `None`.

        Retorna
        -------
        None
            A função não retorna nenhum valor. Ela apenas imprime a mensagem formatada no console.
        
        Exemplos
        --------
        >>> Exemplo de log de erro
        log.log("Ocorreu um erro!", "error", title="Erro")

        >>> Exemplo de log de sucesso
        log.log("A operação foi bem-sucedida!", "sucess", title="Sucesso")
        
        >>> Exemplo de log de alerta
        log.log("Aviso: Algo pode estar errado!", "alert", title="Alerta")
        """
        error_details: Panel = Panel(
            text,
            title=title,
            style=self.styles.get(style, None)
        )
        self.console.print(error_details)

    def log_trace_back(self):
        """
        Exibe o traceback completo de uma exceção, incluindo variáveis locais.
        
        Este método é útil para mostrar detalhes de exceções, como a pilha de chamadas 
        e as variáveis locais no momento do erro.

        Retorna
        -------
        None
            A função não retorna nenhum valor. Ela apenas imprime o traceback no console.
        
        Exemplos
        --------
        >>> Exemplo de uso do log_trace_back:
            try:
                1 / 0  # Causa uma exceção de divisão por zero
            except ZeroDivisionError:
                log.log_trace_back()
        """
        self.console.print_exception(show_locals=True)
