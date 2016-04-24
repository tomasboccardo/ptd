from abc import abstractmethod


class PtdBaseCommand(object):
    @abstractmethod
    def execute(*args):
        pass
