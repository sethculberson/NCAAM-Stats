import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

def getImage(path):
    # Read the image
    img = plt.imread(path)
    
    # Calculate the zoom to scale the image to 10x10 pixels
    zoom = 25 / max(img.shape[:2])
    
    return OffsetImage(img, zoom=zoom, alpha=1.0)

def generatePlot(x="", y=""):
    plt.rcParams["toolbar"] = "None"

    df = pd.read_csv("23-24seasondata.csv")
    dfx = df["3P%"]
    dfy = df["W"]

    img_paths = []
    for index, row in df.iterrows():
        r = row["School"]
        img_paths.append(f"logos/{r}.png")

    arrdfx = dfx.to_numpy()
    arrdfy = dfy.to_numpy()

    A = np.vstack([arrdfx,np.ones(len(arrdfx))]).T
    m, c = np.linalg.lstsq(A,arrdfy,rcond=None)[0]

    fig, ax = plt.subplots()
    fig.set_size_inches(15,8)
    plt.scatter(x=dfx,y=dfy,alpha=0.0)

    for x0, y0, path in zip(dfx, dfy, img_paths):
        ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
        ax.add_artist(ab)

    plt.plot(dfx, m*arrdfx + c, 'r', label='Fitted line')
    plt.text(x=5.3, y=37.5,s=f"{m:.2f} additional offensive rebounds per game are worth 1 win")
    plt.legend()
    plt.xlabel("Offensive Rebounds Per Game")
    plt.ylabel("Total Wins")
    plt.show()
generatePlot()