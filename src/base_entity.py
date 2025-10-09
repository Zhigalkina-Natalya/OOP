from abc import ABC, abstractmethod


class BaseEntity(ABC):
    """
    Минимальный абстрактный класс с общими свойствами name и description. Требует реализации to_dict() у потомков.
    """

    name: str
    description: str

    def __init__(self, name: str, description: str) -> None:
        self.name = str(name)
        self.description = str(description)

    @abstractmethod
    def to_dict(self) -> dict:
        """Преобразование основных полей — должен реализовать потомок."""
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.description})"
