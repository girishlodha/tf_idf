# read the index.txt and prepare documents, vocab , idf
import os
import chardet
data=[]
Q_name=[]
i=0
#C:\Users\hp\Downloads\bootcamp_tf_idf-main\bootcamp_tf_idf-main\Leetcode-Questions-Scrapper-master\Qdata\1\1.txt

#filename = "Leetcode-Questions-Scrapper-master/index.txt"
#my_encoding = find_encoding(filename)

with open("Leetcode-Questions-Scrapper-master/Qdata/index.txt", 'r') as f:
   for line in f:
      i+=1
      text=line.strip()
      extracted_question_name=text.split('.',1)[-1]
      Q_name.append(extracted_question_name)      
      extracted_question_name=extracted_question_name.replace('-', ' ')     
      folder_path = f"Leetcode-Questions-Scrapper-master/Qdata/{i}"
      file_path = os.path.join(folder_path, f"{i}.txt")
      with open(file_path, 'r',encoding='utf-8', errors='ignore') as file:
         extracted_question_text=file.read()
         index = extracted_question_text.find("Example")
         extracted_question_text=extracted_question_text[:index]
        #  extracted_question_text=extracted_question_text.replace('\n', ' ')
         extracted_question_text=extracted_question_text.replace('-', ' ')
      data.append(extracted_question_name.lower()+" "+extracted_question_text.lower())



def preprocess(document_text):
    # remove the leading numbers from the string, remove not alpha numeric characters, make everything lowercase
    terms = [term.lower() for term in document_text.strip().split()[1:]]
    return terms

vocab = {}
documents = []
for index, line in enumerate(data):
    # read statement and add it to the line and then preprocess
    tokens = preprocess(line)
    documents.append(tokens)
    tokens = set(tokens)
    for token in tokens:
        if token not in vocab:
            vocab[token] = 1
        else:
            vocab[token] += 1

# reverse sort the vocab by the values
vocab = dict(sorted(vocab.items(), key=lambda item: item[1], reverse=True))

print('Number of documents: ', len(documents))
print('Size of vocab: ', len(vocab))
print('Sample document: ', documents[0])

# save the vocab in a text file
with open('tf-idf/vocab.txt', 'w',encoding='utf-8') as f:
    for key in vocab.keys():
        f.write("%s\n" % key)

# save the idf values in a text file
with open('tf-idf/idf-values.txt', 'w' , encoding='utf-8') as f:
    for key in vocab.keys():
        f.write("%s\n" % vocab[key])

# save the documents in a text file
with open('tf-idf/documents.txt', 'w' , encoding='utf-8') as f:
    for document in documents:
        f.write("%s\n" % ' '.join(document))


inverted_index = {}
for index, document in enumerate(documents):
    for token in document:
        if token not in inverted_index:
            inverted_index[token] = [index]
        else:
            inverted_index[token].append(index)

# save the inverted index in a text file
with open('tf-idf/inverted-index.txt', 'w' , encoding='utf-8') as f:
    for key in inverted_index.keys():
        f.write("%s\n" % key)
        f.write("%s\n" % ' '.join([str(doc_id) for doc_id in inverted_index[key]]))
