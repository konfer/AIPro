from AbstractBase.AbstractTransCreator import *
from TransformStrategy.CustomQuantitativeImputerTrans import *


class QuantitativeImputerTransGenerator(AbstractTransCreator):
	
	
	def generateTrans(self):
		return CustomQuantitativeImputerTrans()
	

		
