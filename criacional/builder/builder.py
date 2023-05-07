"""
Builder é um padrão de criação que tem a intenção
de separar a construção de um objeto complexo
da sua representação, de modo que o mesmo processo
de construção possa criar diferentes representações.

Builder te da a possibilidade de criar objetos passo-a-passo
e isso já é possível no Python sem este padrão.

Geralmente o builder aceita o encadeamento de métodos
(method chaining).
"""
from abc import ABC, abstractmethod


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__


class User(StringReprMixin):

    def __init__(self) -> None:
        self.firstname = None
        self.lastname = None
        self.age = None
        self.phone_numbers = []
        self.addresses = []


class IUserBuilder(ABC):
    
    @property
    @abstractmethod
    def result(self): pass

    @abstractmethod
    def add_firstname(self, firstname): pass

    @abstractmethod
    def add_lastname(self, lastname): pass

    @abstractmethod
    def add_age(self, age): pass

    @abstractmethod
    def add_phone(self, phone): pass
    
    @abstractmethod
    def add_address(self, address): pass


class UserBuilder(IUserBuilder):
    
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self.__result = User()

    @property
    def result(self):
        return_data = self.__result
        self.reset()
        return return_data

    def add_firstname(self, firstname):
        self.__result.firstname = firstname
        return self

    def add_lastname(self, lastname):
        self.__result.lastname = lastname
        return self

    def add_age(self, age):
        self.__result.age = age
        return self

    def add_phone(self, phone):
        self.__result.phone_numbers.append(phone)
        return self
    
    def add_address(self, address):
        self.__result.addresses.append(address)
        return self


class UserDirector:

    def __init__(self, builder: UserBuilder) -> None:
        self.__builder = builder

    def with_age(self, firstname, lastname, age):
        return self.__builder.add_firstname(firstname)\
                            .add_lastname(lastname)\
                            .add_age(age)\
                            .result

    def with_address(self, firstname, lastname, address):
        return self.__builder.add_firstname(firstname)\
                            .add_lastname(lastname)\
                            .add_address(address)\
                            .result


if __name__ == '__main__':
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)

    user_1 = user_director.with_age('Pedro', 'Henrique', 22)
    print(user_1)

    user_2 = user_director.with_address('José', 'Silva', 'Rua Azul')
    print(user_2)
