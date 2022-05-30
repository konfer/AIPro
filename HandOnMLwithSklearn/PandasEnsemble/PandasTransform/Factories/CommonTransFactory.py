from PandasEnsemble.PandasTransform.GenerateTranform.DummifierTransGenerator import *
from PandasEnsemble.PandasTransform.GenerateTranform.CategoryImputerGenerator import *
from PandasEnsemble.PandasTransform.GenerateTranform.CutterTransGenerator import *
from PandasEnsemble.PandasTransform.GenerateTranform.EncodingTransGenerator import *
from PandasEnsemble.PandasTransform.GenerateTranform.QuantitativeImputerTransGenerator import *


class CommonTransFactory:
	
	def __init__(self):
		pass
	
	
	def makeCustomCateoryTransform(self):
		
		return CategoryImputerGenerator().generateTrans()
		
		#return TransformStrategy.CustomQuantitativeImputerTrans(cols)
	
	def makeCustomCutterTrans(self):
		return CutterTransGenerator().generateTrans()
	
	def makeCustomDummifierTrans(self):
		
		return DummifierTransGenerator().generateTrans()
		#return TransformStrategy.CustomDummifierTrans(cols)
	
	def makeCustomEncodingTrans(self):
		return EncodingTransGenerator().generateTrans()
		
		
	def makeCustomQuantitativeImputerTrans(self):
		return  QuantitativeImputerTransGenerator().generateTrans()