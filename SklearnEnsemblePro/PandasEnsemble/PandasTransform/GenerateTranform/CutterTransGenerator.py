from AbstractBase.AbstractTransCreator import *
from TransformStrategy.CustomCutterTrans import *

class CutterTransGenerator(AbstractTransCreator):
	
	def generateTrans(self):
		return CustomCutterTrans()
		
	
		
	