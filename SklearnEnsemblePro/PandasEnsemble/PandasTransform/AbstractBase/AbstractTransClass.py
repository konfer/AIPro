from abc import ABCMeta,abstractmethod


class AbstractTransClass(metaclass=ABCMeta):
	
	@abstractmethod
	def get(self, df = None):
		pass

