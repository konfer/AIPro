from PandasEnsemble.PandasTransform.AbstractBase.AbstractTransCreator import *
from PandasEnsemble.PandasTransform.TransformStrategy.CustomCutterTrans import *

class CutterTransGenerator(AbstractTransCreator):
	
	def generateTrans(self):
		return CustomCutterTrans()
		
	
		
	