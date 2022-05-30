from PandasEnsemble.PandasTransform.AbstractBase.AbstractTransCreator import *
from PandasEnsemble.PandasTransform.TransformStrategy.CustomDummifierTrans import *

class DummifierTransGenerator(AbstractTransCreator):
	
	
	def generateTrans(self):
		return CustomDummifierTrans()
		
	