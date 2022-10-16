import io

import fileupload
import wordcloud
from IPython.display import display
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# def _upload():
#     _upload_widget = fileupload.FileUploadWidget()
#
#     def _cb(change):
#         global file_contents
#         decoded = io.StringIO(change['owner'].data.decode('utf-8'))
#         filename = change['owner'].filename
#         print('Uploaded `{}` ({:.2f} kB)'.format(
#             filename, len(decoded.read()) / 2 ** 10))
#         file_contents = decoded.getvalue()
#
#     _upload_widget.observe(_cb, names='data')
#     display(_upload_widget)
#
#
# _upload()
file_contents = open('lilFamily.txt').read()


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
    # uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
    # "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",
    # "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",
    # "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",
    # "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    # LEARNER CODE START HERE
    frequencies = {}
    word_list = []
    # for mark in punctuations:
    #     file_contents = file_contents.replace(mark, '')
    # for words in uninteresting_words:
    #     file_contents = file_contents.replace(words, ' ')
    for word in file_contents.split():
        if word.lower() not in word_list:
            word_list.append(word.lower())
            if word not in frequencies:
                frequencies[word] = 1
            else:
                frequencies[word] += 1
    # frequencies['SoumyaIpsita'] = 0
    # frequencies['TejasmayaSmuti'] = 0
    print(frequencies)
    # word_list.remove('soumyaipsita')
    # word_list.remove('tejasmayasmuti')
    print(word_list)

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()


# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()
