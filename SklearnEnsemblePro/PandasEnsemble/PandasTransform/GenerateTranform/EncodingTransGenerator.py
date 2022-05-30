from AbstractBase.AbstractTransCreator import *
from TransformStrategy.CustomEncodingTrans import *

class EncodingTransGenerator(AbstractTransCreator):
	
	
	def generateTrans(self):
		return CustomEncodingTrans()
		
	