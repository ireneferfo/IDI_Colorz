from collections import Counter
from sklearn.cluster import KMeans
import cv2

sizeX = 600
sizeY = 400

def preprocess(raw):
    image = cv2.resize(raw, (sizeX, sizeY), interpolation = cv2.INTER_AREA)                                          
    image = image.reshape(image.shape[0]*image.shape[1], 3)
    return image

    
def rgb_to_hex(rgb_color):
    hex_color = "#"
    for i in rgb_color:
        hex_color += ("{:02x}".format(int(i)))
    return hex_color


def analyze(img, n_colors):
    clf = KMeans(n_clusters = n_colors, random_state = 0)
    color_labels = clf.fit_predict(img)
    center_colors = clf.cluster_centers_ # in RGB

    counts =  Counter(color_labels)
    ordered_colors = [rgb_to_hex(center_colors[i]) for i in counts.keys()]

    d = {}
    for i in range(len(ordered_colors)):
        d[ordered_colors[i]] = list(counts.values())[i]/(sizeX*sizeY)
    d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse = True)}

    # plt.figure(figsize = (12, 8))
    # plt.pie(d.values(), labels = d.keys(), colors = d.keys())
    return d


def extract_colors(image_path, n_colors = 10):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    modified_image = preprocess(image)
    return analyze(modified_image, n_colors)