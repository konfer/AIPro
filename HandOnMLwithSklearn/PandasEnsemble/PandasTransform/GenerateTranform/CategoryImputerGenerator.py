from PandasEnsemble.PandasTransform.AbstractBase.AbstractTransCreator import *
from PandasEnsemble.PandasTransform.TransformStrategy.CustomCategoryImputerTrans import *

class CategoryImputerGenerator(AbstractTransCreator):
	
	
	def generateTrans(self):
		return CustomCategoryImputerTrans()
	
	