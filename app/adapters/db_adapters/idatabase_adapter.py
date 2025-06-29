from abc import ABC, abstractmethod


class IDatabaseAdapter(ABC):
    @abstractmethod
    def _connect(self, **kwargs):
        pass

    @abstractmethod
    def insert(self, **kwargs):
        pass

    @abstractmethod
    def fetch_all(self, **kwargs):
        pass

    @abstractmethod
    def close(self, **kwargs):
        pass