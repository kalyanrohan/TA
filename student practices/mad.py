mad_dictionary={"ing":"in'","and":"an'","hi":"ahoy","you":"ye","my":"me","friend":"matey","buddy":"matey","hey":"'ay","are":"be","is":"be","am":"be","have":"'ave"}
translated= input("What do you want to translate? ")
word_array=translated.split(" ")

for i in range(len(word_array)):
    for key in mad_dictionary:
        if key in word_array[i]:
            word_array[i]=mad_dictionary.get(key)

seperator=" "
new_sentence=seperator.join(word_array)
print(new_sentence+" !")