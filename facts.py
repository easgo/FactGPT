from fuzzywuzzy import fuzz
import spacy

# Load the large English NLP model
nlp = spacy.load('en_core_web_lg')

def correct_facts(text1, text2, similarity_threshold=70):
    # Parse the documents with spaCy
    doc1 = nlp(text1)
    doc2 = nlp(text2)

    # Split the documents into sentences
    sentences1 = list(doc1.sents)
    sentences2 = list(doc2.sents)

    # For each sentence in the first document
    for i, sentence1 in enumerate(sentences1):
        # For each sentence in the second document
        for sentence2 in sentences2:
            # Calculate the similarity between the two sentences
            similarity = fuzz.ratio(str(sentence1), str(sentence2))
            # If the sentences are similar
            if similarity > similarity_threshold:
                # Replace the sentence in the first document with the sentence from the second document
                sentences1[i] = sentence2

    # Join the corrected sentences back together
    corrected_text = ' '.join(map(str, sentences1))
    return corrected_text