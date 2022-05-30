from sklearn.base import TransformerMixin

class CustomCategoryImputerTrans(TransformerMixin):
	
	def __init__(self, cols = None):
		self.cols = cols
		
	def setCols(self,cols):
		self.cols = cols
	
	def transform(self, df):
		X = df.copy()
		for col in self.cols:
			X.loc[:, col].fillna(X.loc[:, col].value_counts().index[0], inplace = True)
		return X
	
	def fit(self, *_):
		return self