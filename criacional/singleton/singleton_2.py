def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]

    return get_class


@singleton
class AppSettings:
    def __init__(self) -> None:
        ''' Problema: o init será chamado todas as vezes que a classe for instanciada,
            sendo assim, os atributos serão reescritos sempre. '''
        print('OI')
        self.tema = 'Escuro'
        self.font = '18px'


if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'Tema Claro'
    print(as1.tema)

    as2 = AppSettings()
    print(as2.tema)
