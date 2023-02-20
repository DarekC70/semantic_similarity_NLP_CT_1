import spacy
nlp = spacy.load('en_core_web_md')
# Comparison of three words with each other
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#================ Similarity (earthworm, butterfly, flower)
print('***********************************************************************')

word1 = nlp("earthworm")
word2 = nlp("butterfly")
word3 = nlp("flower")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
# Comparasion of the one word with the rest of the words into the group
tokens = nlp('earthworm butterfly flower grass')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#========================== Notes ===================================================================
# Example 1:
# In the comparison of three words: cat, monkey, banana
# The similarity value is the highest for the comparison of cat and monkey (0.59)this is because both
# words mean animal. The lowest similarity coefficient (0.22) is determined for the banana and cat
# comparison - the cat has nothing in common with a banana, except that they are living organisms, 
# but this is a very distant similarity. The similarity between a monkey and a banana is 
# much greater (0.40), the monkey eats bananas - with pleasure :o).

# Example 2:
# When comparing three words: earthworm, butterfly, flower, the similarity value is at a similar level:
# for the comparison of earthworm and butterfly, the similarity is 0.55, for cat and butterfly 0.56, 
# and for flower and worm 0.42. The words describe various living objects, but often associated
#  with one ecosystem, such as a garden. Of these three words, butterfly and flower have 
# the greatest similarity, the butterfly is often associated with a flower because it sits on it, 
# feeds on pollen. The lowest similarity coefficient is between the earthworm and the flower, 
# they live rather separated from each other, the earthworm underground, and the flower has a significant
# part above the ground.
