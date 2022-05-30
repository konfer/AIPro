import pandas as pd


from sklearn.base import TransformerMixin

class CustomDummifierTrans(TransformerMixin):
	
	def __init__(self, cols = None, prefix_sep = '_'):
		self.cols = cols
		self.prefix_sep = prefix_sep
		
	def getCols(self, cols):
		self.cols = cols
		
	def getPrefixSep(self, prefix_sep):
		self.prefix_sep = self.prefix_sep
	
	def transform(self, X):
		return pd.get_dummies(X, columns = self.cols, prefix_sep = self.prefix_sep)
	
	def fit(self, *_):
		return self