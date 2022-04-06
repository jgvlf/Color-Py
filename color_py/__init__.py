class Colors:
    def __init__(self):

        '''
        Classe para modificar as propriedades do texto no console, para
        utilizar deve-se instanciar a classe Colors e, colocar a variável
        instanciada com o caracter "." e depois a propriedade requisitada
        EXEMPLO:
        c = Colors()
        Vermelho:
        c.red
        Azul com negrito:
        c.blue c.bold
        Verde com fundo Cyano:
        c.green c.self.cyan_background
        '''

        self.bold = '\033[1m'
        self.underline = '\033[4m'
        self.negative = '\033[7m'
        self.white = '\033[30'
        self.red = '\033[31m'
        self.green = '\033[32m'
        self.yellow = '\033[33m'
        self.blue = '\033[34m'
        self.purple = '\033[35m'
        self.cyan = '\033[36m'
        self.gray = '\033[37m'
        self.white_background = '\033[30'
        self.red_background = '\033[31m'
        self.green_background = '\033[32m'
        self.yellow_background = '\033[33m'
        self.blue_background = '\033[34m'
        self.purple_background = '\033[35m'
        self.cyan_background = '\033[46m'
        self.gray_background = '\033[37m'
        self.clean = '\033[m'