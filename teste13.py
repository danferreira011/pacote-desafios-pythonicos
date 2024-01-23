with open('letras.txt','r') as file:
    text = file.read().lower().split()

words_dict = {}
for word in text:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

top_dict = {}
for word, freq in words_dict.items():
    top_dict[freq] = word

top_list = list(sorted(top_dict.items(), reverse=True))[:20]
for element in top_list:
    print(f'{element[1]} {element[0]}')