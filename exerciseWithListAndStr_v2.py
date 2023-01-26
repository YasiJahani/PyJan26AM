import pandas as pd
import numpy as np

# DataFrame

df=pd.read_csv("data.txt", sep='[;:]', names=["t1", "x1", "t2", "x2"], engine="python")

print(df)

df=df[["x1","x2"]]

print(df)

print(df.describe())

df["y1"]=np.cos(df["x1"])
df["y2"]=np.sin(df["x2"])

print(df)

ax=df.plot(x="x1", y="y1")
df.plot(x="x2", y="y2", ax=ax)


