import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor, VotingRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
import joblib

df = pd.read_csv("processed.csv", index_col=0)

X = df[['Green','RedEdge','NDVI','GNDVI','NDRE','EVI','SAVI','DVI','MSAVI','Altitude','Slope','Aspect','Relief','SOS']]
y = df['SOC']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

xgb = XGBRegressor(n_estimators=1200, learning_rate=0.03, max_depth=6, subsample=0.8, colsample_bytree=0.8, random_state=42, n_jobs=-1)
gbr = GradientBoostingRegressor(n_estimators=1200, learning_rate=0.03, max_depth=5, random_state=42)
lgbm = LGBMRegressor(n_estimators=1200, learning_rate=0.03, max_depth=-1, num_leaves=31, subsample=0.8, colsample_bytree=0.8, random_state=42, n_jobs=-1)
cat = CatBoostRegressor(iterations=1200, learning_rate=0.03, depth=6, loss_function='RMSE', verbose=0, random_state=42)

voting = VotingRegressor(estimators=[('xgb', xgb), ('gbr', gbr), ('lgbm', lgbm), ('cat', cat)], weights=[3, 1, 3, 2])
voting.fit(X_train, y_train)

joblib.dump(voting, "model.sav")
print("Model retrained and saved successfully!")
