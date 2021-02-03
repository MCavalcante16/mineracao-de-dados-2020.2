from sklearn.preprocessing import Normalizer

def normalize(df):  
    scaler = Normalizer()
    scaler.fit(df)
    return scaler.transform(df)

def standardize(df):
    return (df-df.mean())/df.std()

def minmaxer(df):
    return (df - df.min())/(df.max() - df.min()) + 1