from AbstractBase.AbstractTransCreator import *
from TransformStrategy.CustomCategoryImputerTrans import *

class CategoryImputerGenerator(AbstractTransCreator):
	
	
	def generateTrans(self):
		return CustomCategoryImputerTrans()
	
	