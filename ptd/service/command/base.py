from abc import abstractmethod


class PtdBaseCommand(object):
    def __init__(self, ptd_app):
        self.ptd_app = ptd_app

    @abstractmethod
    def execute(self, **kwargs):
        pass
