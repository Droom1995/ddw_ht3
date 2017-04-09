# ddw_ht3

Data used for processing was taken from a bunch of connected BBC articles about Korea.

For custom entities, I added only ones starting with and adjective(JJ\*) and ending with a noun(NN\*).

Top 10 entities on each step:

POS tagging top counts:  [('Korea', 142), ("'s", 113), ('South', 110), ('North', 102), ('The', 91), ('Korean', 74), ('Park', 69), ("''", 55), ('\`\`', 53), ('US', 45)]

NE chunk top counts: [('So', 140), ('South', 110), ('South Korea', 105), ('North', 102), ('North Korea', 90), ('Korean', 83), ('Image', 76), ('Park', 69), ('US', 46), ('Kim', 42)]

Custom entities top counts:  [('Chinese', 17), ('Malaysian police', 6), ('North Korean leader', 4), ('Chinese tourists', 4), ('Korean protesters', 3), ('Chinese territory', 2), ('Chinese missiles', 1), ('South Korean Navy', 1), ('North Korean missile range', 1), ('North Korean business representatives', 1), ('Rogue nation', 1), ('Most', 1), ('Chinese banks', 1), ('Chinese border', 1), ('North Korean newscaster Ri Chun-hee', 1), ('Many questions', 1), ('Malaysian police arrest', 1), ('Malaysian officials', 1), ('North Korean organisations capable', 1), ('Chinese partners', 1), ('Other incidents', 1), ('Chinese customers', 1), ('Chinese e-commerce site JD.com', 1), ('South Korean news agency Yonhap', 1), ('South Korean court', 1), ('North Korean attacks', 1), ('American diplomatic cable', 1), ('South Korean cable TV station', 1), ('Left-wing critics', 1), ('Korean Wave', 1), ('Soviet troops', 1), ('North Korean invasion', 1)]

# Wikipedia extracted definitions
For NE chunks:

So || Thing

South ||  a noun

South Korea ||  a sovereign state in East Asia

North ||  one of the four cardinal directions or compass points

North Korea ||  a country in East Asia

Korean || Thing

Image ||  an artifact that depicts visual perception

Park ||  an area of natural

US ||  a constitutional federal republic composed of 50 states

For custom:

Chinese || Thing

Malaysian police ||  a

North Korean leader ||  a list of political leaders of North Korea

Chinese tourists ||  greatly expanded over the last few decades since the beginning of reform and opening

Korean protesters || Thing

Chinese territory ||  a term for types of administrative division

Chinese missiles || Thing

South Korean Navy ||  the naval warfare service branch of the South Korean armed forces

North Korean missile range ||  also fired a number of short-range missiles into the Sea of Japan

North Korean business representatives ||  that the likely number of excess deaths between 1993 and 2000 was 500,000 to 600,000

# Issues

Didn't find useful text pattern search in nltk, custom workaround is too bulky:
```
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
```

# Possible improvements

Improve definition(the whole wikipedia summary is a actually a good idea).
