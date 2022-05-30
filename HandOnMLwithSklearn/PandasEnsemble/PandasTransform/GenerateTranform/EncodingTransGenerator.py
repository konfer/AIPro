from PandasEnsemble.PandasTransform.AbstractBase.AbstractTransCreator import *
from PandasEnsemble.PandasTransform.TransformStrategy.CustomEncodingTrans import *

class EncodingTransGenerator(AbstractTransCreator):
	
	
	def generateTrans(self):
		return CustomEncodingTrans()
		
	