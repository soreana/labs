
import shutil
import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def get_image(url):
    response = requests.get(url, stream=True)
    with open('response.jpg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

if __name__ == "__main__":
    from sys import argv
    url = 'http://localhost/'
    if len(argv) == 2:
        url = 'http://' + argv[1] + '/'
    get_image(url)
    img=mpimg.imread('response.jpg')
    imgplot = plt.imshow(img)
    plt.show()