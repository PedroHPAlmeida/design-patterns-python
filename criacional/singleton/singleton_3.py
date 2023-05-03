class Singleton(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self) -> None:
        ''' Problema: o init será chamado todas as vezes que a classe for instanciada,
            sendo assim, os atributos serão reescritos sempre. '''
        self.tema = 'Escuro'
        self.font = '18px'


if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'Tema Claro'
    print(as1.tema)
    
    as2 = AppSettings()
    print(as2.tema)
    
    as3 = AppSettings()
    print(as3.tema)

    print(as1 == as2 == as3)
