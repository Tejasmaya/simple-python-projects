# #Method 1


# import numpy as npy
# from PIL import Image
# from wordcloud import WordCloud, STOPWORDS
#
# dataset = open("lilFamily.txt", "r").read()
#
#
# def create_word_cloud(string):
#     maskArray = npy.array(Image.open('wallpaper.JPG'))
#     cloud = WordCloud(background_color="black", max_words=22200, mask=maskArray, stopwords=set(STOPWORDS))
#     cloud.generate(string)
#     cloud.to_file("FamilyCloud.png")
#
#
# dataset = dataset.lower()
# create_word_cloud(dataset)

#
#
#
#
#
#
#
#
#
#
#


# # Method 2
#
#
# import matplotlib
#
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud, STOPWORDS
#
#
# def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
#     h = int(360.0 * 45.0 / 255.0)
#     s = int(100.0 * 255.0 / 255.0)
#     l = int(100.0 * float(random_state.randint(60, 120)) / 255.0)
#
#     return "hsl({}, {}%, {}%)".format(h, s, l)
#
#
# # file_content = open("ManiTejas.txt").read()
# file_content = open("lilFamily.txt").read()
#
# wordcloud = WordCloud(font_path=r'C:\Windows\Fonts\Verdana.ttf',
#                       stopwords=STOPWORDS,
#                       background_color='blue',
#                       width=1200,
#                       height=1000,
#                       color_func=random_color_func
#                       ).generate(file_content)
#
# plt.imshow(wordcloud)
# plt.axis('off')
# plt.show()
#
#
#
#
#
#
#
#
#
#
#
#


# # Method 3


# """
# Python script to generate word cloud image.
# Author - Anurag Rana
# Read more on - https://www.pythoncircle.com
# """
#
# from wordcloud import WordCloud
#
# # image configurations
# background_color = "#101010"
# height = 1920
# width = 3 * 1080
#
# # with open("stopwords.txt", "r") as f:
# #     stop_words = f.read().split()
#
# # Read a text file and calculate frequency of words in it
# with open("ManiTejas.txt", "r") as f:
#     words = f.read().split()
#
# data = dict()
#
# for word in words:
#     word = word.lower()
#     # if word in stop_words:
#     #     continue
#
#     data[word] = data.get(word, 0) + 1
#
# word_cloud = WordCloud(
#     background_color=background_color,
#     width=width,
#     height=height
# )
#
# word_cloud.generate_from_frequencies(data)
# word_cloud.to_file('wordcloudManiTejas💙.png')
