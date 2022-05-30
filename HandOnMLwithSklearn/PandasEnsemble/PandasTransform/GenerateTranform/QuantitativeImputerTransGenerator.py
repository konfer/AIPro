from PandasEnsemble.PandasTransform.AbstractBase.AbstractTransCreator import *
from PandasEnsemble.PandasTransform.TransformStrategy.CustomQuantitativeImputerTrans import *


class QuantitativeImputerTransGenerator(AbstractTransCreator):
	
	
	def generateTrans(self):
		return CustomQuantitativeImputerTrans()
	

		
