from AbstractBase.AbstractTransCreator import *
from TransformStrategy.CustomDummifierTrans import *

class DummifierTransGenerator(AbstractTransCreator):
	
	
	def generateTrans(self):
		return CustomDummifierTrans()
		
	