import pandas as pd

from sklearn.base import TransformerMixin

class CustomCutterTrans(TransformerMixin):
	
	def __init__(self, col = None, labels = False):
		self.col = col
		self.labels = labels
		
	def setCol(self, col):
		self.col = col
		
	def setBins(self, bins):
		self.bins = bins
		
	def setLabels(self, labels):
		self.labels = labels
		
	
	def transform(self, df):
		X = df.copy()
		X.loc[:, self.col] = pd.cut(X.loc[:, self.col], bins = self.bins, labels = self.labels)
		return X
	
	def fit(self, *_):
		return self