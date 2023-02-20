# semantic_similarity_NLP_CT_1
The repository contains three files:
1/ semantic.py
2/ example_en_core_web_sm.py
3/ T 38_ Obligatory task 1 - using the md and sm model in pdf

semantic.py and example_en_core_web_sm.py files use python's spaCY library, require prior installation and import of the spaCY module and the language model en_core_web_sm (smaller model) or en_core_web_md (medium).

semantic.py file - performs semantic analysis and looks for similarities for a set of words:
cat, monkey, banana;
earthworm, butterfly, flower;
and makes comparasion of the one word with the rest of the words into the group by using NLP processing:
group1 - 'cat apple monkey banana '
group2 - 'earthworm butterfly flower grass'

Output:
similarity value: 'cat', 'monkey', 'banana'
'cat' + 'monkey' = 0.5929930274321619
'banana' + 'monkey' = 0.40415016164997786
'banana' + 'cat' = 0.22358825939615987

Comparasion of the one word with the rest of the words into the group1;
cat cat 1.0
cat apple 0.2036806046962738   
cat monkey 0.5929930210113525  
cat banana 0.2235882580280304  
apple cat 0.2036806046962738   
apple apple 1.0
apple monkey 0.2342509925365448
apple banana 0.6646699905395508 
monkey cat 0.5929930210113525   
monkey apple 0.2342509925365448 
monkey monkey 1.0
monkey banana 0.4041501581668854

banana cat 0.2235882580280304   
banana apple 0.6646699905395508
banana monkey 0.4041501581668854
banana banana 1.0

Output:
similarity value: 'earthworm', 'butterfly', 'flower', 'grass'
'earthworm' + 'butterfly' = 0.5496174933532416
'flower' + 'butterfly' = 0.5566176195123479
'flower' + 'earthworm' = 0.42709759249199675

Comparasion of the one word with the rest of the words into the group2:
earthworm earthworm 1.0
earthworm butterfly 0.5496175289154053
earthworm flower 0.4270976185798645
earthworm grass 0.45206910371780396
butterfly earthworm 0.5496175289154053
butterfly butterfly 1.0
butterfly flower 0.5566176176071167
butterfly grass 0.4564971625804901
flower earthworm 0.4270976185798645
flower butterfly 0.5566176176071167
flower flower 1.0
flower grass 0.5303848385810852
grass earthworm 0.45206910371780396
grass butterfly 0.4564971625804901
grass flower 0.5303848385810852
grass grass 1.0

File example_en_core_web_sm.py was created for examination how the change of the language model from medium (md) to smaller (sd) affects the final effect.
As a result, less accurate coefficients of similarity analysis were obtained, the results are in a T 38_ Obligatory task 1.pdf file, when executing the code, the following message appears:
"\example_en_core_web_sm.py:69: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available."
3/  - using the md and sm model in pdf
