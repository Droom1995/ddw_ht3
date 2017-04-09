from collections import Counter
from string import punctuation
from nltk.corpus import stopwords
from nltk.sentiment.util import *
import re
import wikipedia


def tokenCounts(tokens):
    counts = Counter(tokens)
    sortedCounts = sorted(counts.items(), key=lambda count: count[1], reverse=True)
    return sortedCounts


def extractEntities(ne_chunked):
    data = {}
    for entity in ne_chunked:
        if isinstance(entity, nltk.tree.Tree):
            text = " ".join([word for word, tag in entity.leaves()])
            ent = entity.label()
            data[text] = ent
        else:
            continue
    return data


def prettyPrint(ner_dict):
    entity_words_keys = ner_dict.keys()
    entity_words = {x: 0 for x in entity_words_keys}
    for key in entity_words:
        entity_words[key] = text.count(key)
    entity_words_counts = entity_words
    pretty_entity_words_counts = []
    for key in entity_words_counts:
        pretty_entity_words_counts.append((key, entity_words_counts[key]))
    pretty_entity_words_counts = sorted(pretty_entity_words_counts, key=lambda item: item[1], reverse=True)
    pretty_entity_words_counts = [item for item in pretty_entity_words_counts if item[1] > 0]
    return pretty_entity_words_counts


def filterTagged(tokens, filter):
    result = []
    for token in tokens:
        if re.match(filter, token[1]) is not None:
            result.append(token)
    return result


def wikipediaSearch(entity):
    try:
        page = wikipedia.page(entity[0])
        summary = page.summary
        summary_tokens = nltk.word_tokenize(summary)
        tagged = nltk.pos_tag(summary_tokens)  # POS tagging
        ans = ""
        start = False
        for entity in tagged:
            if start:
                if entity[1] not in punctuation:
                    ans += " " + entity[0]
                else:
                    break
            if entity[1] == "VBZ":
                start = True
        return ans
    except:
        return "Thing"


text = None
with open('korea.txt', 'r') as f:
    text = f.read()

sentences = nltk.sent_tokenize(text)
number_of_values = 5
tokens = nltk.word_tokenize(text)
filtered_tokens = [token for token in tokens if token not in punctuation]
stops = stopwords.words('english')
tokens = [token for token in filtered_tokens if token not in stops]
tagged = nltk.pos_tag(tokens)  # POS tagging
counts = tokenCounts(tokens)
print("POS tagging top counts: ", counts)

ne_chunked = nltk.ne_chunk(tagged, binary=False)
entities = extractEntities(ne_chunked)

top_entities = prettyPrint(entities)[:10]
print("NE chunk top counts:", top_entities)
for entity in top_entities:
    print(entity[0] + " || " + wikipediaSearch(entity))

# noun_re = re.compile("NN*")
# nouns = filterTagged(tagged, noun_re)
# noun_re = re.compile("JJ*")
# nouns = nouns + filterTagged(tagged, noun_re)
# print("Top adj/noun counts:", nouns)

custom_ner = {}

entity = []
for tagged_entry in tagged:
    if (tagged_entry[1].startswith("JJ") or (entity and tagged_entry[1].startswith("NN"))):
        entity.append(tagged_entry)
    else:
        if entity and entity[-1][1].startswith("IN"):
            entity.pop()
        if (entity and " ".join(e[0] for e in entity)[0].isupper()):
            str = " ".join(e[0] for e in entity)
            custom_ner[str] = 0
        entity = []
print("========================================")
print("Custom entities top counts: ", prettyPrint(custom_ner))
