# Michael Egler
# 04/04/2025

from ListUtils import get_words, clean_list
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image

def makeWordCloud(file, mask):
    #print('Lincoln\'s First Speech')
    words = get_words(file)

    cleanWordList = clean_list(words)

    text_data = ' '.join(cleanWordList)

    if mask:
        # found this image on pixabay.com
        mask_image = np.array(Image.open("dragonSil2.png"))
    else:
        mask_image = None
    
    # create a word cloud object with mask image
    wordcloud = WordCloud(width=1200,
                        height=800,
                        background_color='white', 
                        mask=mask_image,
                        contour_width=2,
                        max_font_size=100,
                        max_words=200,
                        colormap='plasma').generate(str(text_data))

    # display the word cloud using matplotlib
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def main():
    file = 'lincolnSpeech1.txt'
    mask = input("Type y if using a mask, n if not >> ")
    makeWordCloud(file, True if mask.lower() == 'y' else False)

if __name__ == '__main__':
    main()