import json
import string
import re
import pyLDAvis
import nltk
from nltk.corpus import stopwords
from gensim import corpora, models
from gensim.models.coherencemodel import CoherenceModel
from nltk.tokenize import word_tokenize
import pyLDAvis.gensim_models
import matplotlib.pyplot as plt
import webbrowser
# nltk.download('stopwords')
# nltk.download('punkt_tab')


# topics within the defined year range (all records are within 1157-2020) 
# can look at a specific time frame e.g. 20th century

def topics(dataset: str, start_year: int, end_year: int, topic_no: int, output_vis: str):

    with open(dataset, "r", encoding="utf-8") as new_file:
        data = json.load(new_file)

    events = []

    # select events within the year range 
    
    for event in data: 
        for date, event_text in event.items():
            if int(date[-4:]) >= start_year and int(date[-4:]) <= end_year:
                text_content = event_text
                events.append(text_content)

    print(f'Number of events: {len(events)}')

    preprocessed_texts = []

    stop_words = nltk.corpus.stopwords.words('english')

    # based on the dataset, added stopwords that are either too frequent or less meaningful
    new_stopwords = ['workers','worker','work','working','people','men','history','many','dozens','year','days','day','us','several','took','later','however','courtesy','following','general','new','began','held','made','others','would','years','months','week','weeks','also','went','around','across','including','place','part','mostly','one','two','three','four','five','six','seven','eight','nine','ten','thousands','thousand','hundred','hundreds','percent','ing','set','little','give','ku','called','walked','back','commons','wikimedia','january','february','march','april','may','june','july','august','september','october','november','december']
    stop_words.extend(new_stopwords)

    # Regular expression pattern to remove punctuations
    pattern = r'[^\w\s]' # Matches any character that is not an alphanumeric character or whitespace

    # lowercase
    for text in events:
        text = text.lower()

    # Tokenize the text using NLTK's word_tokenize()
        tokens = word_tokenize(text)

    # Remove stopwords and numbers, and join words back into a string
        filtered_text = [word for word in tokens if word not in stop_words and not word.isdigit()]
        preprocessed_text = ' '.join(filtered_text)

    # Remove remaining punctuation marks using regular expressions
        preprocessed_text = re.sub(pattern, '', preprocessed_text)

    # Append preprocessed text to the list
        preprocessed_texts.append(preprocessed_text)

    # Tokenize each string into a list of words
    tokenized_texts = [word_tokenize(text) for text in preprocessed_texts]

    # Create a dictionary and a corpus
    dictionary = corpora.Dictionary(tokenized_texts)
    corpus = [dictionary.doc2bow(text) for text in tokenized_texts]

    # LDA model
    lda_model = models.LdaModel(corpus, alpha='auto', num_topics = topic_no, id2word = dictionary)

    # Coherence
    # cm = CoherenceModel(model=lda_model, corpus=corpus, coherence='u_mass')
    # coherence = cm.get_coherence()

    # Print & save the topics
    print(f'Topics for time period {start_year} - {end_year}:')

    for topic_id, topic_words in lda_model.print_topics():
        print(f'Topic {topic_id + 1}: {topic_words}')

    #print(f'Coherence: {coherence}')
    
    lda_model.save('lda_model')


    # Visualize the topics

    lda_display = pyLDAvis.gensim_models.prepare(lda_model, corpus, dictionary, sort_topics = False)
    pyLDAvis.save_html(lda_display, output_vis)

    webbrowser.open(output_vis)

    return lda_model



# count keyword frequencies by year

def keyword_frequency(keyword: str):

    year = ""
    count = 0  # keyword count in each event
    frequency = {} # keyword frequencies by year
    line_kw = [] # keyword frequencies aggregated by decades
    dict_lines = {} # put multiple keyword frequencies in a dictionary


    with open("wch_data.txt") as new_file:
        for line in new_file: # each line is an event
            parts = line.split(" ")
            for part in parts:
                #if part == keyword: 
                if part.startswith(keyword) == True: # e.g. student & students, miner & miners are treated as the same word
                    count += 1
                year = int(parts[2]) # year is the 3rd part in each event
            if year not in frequency:
                frequency[year] = count
            else:
                frequency[year] = frequency[year] + count # keyword frequency by year in a dictionary
            count = 0
    

    # aggregate keyword frequencies
    # focus on 1850-2000 for now

    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    count10 = 0
    count11 = 0
    count12 = 0
    count13 = 0
    count14 = 0
    count15 = 0


    for key, value in frequency.items():

        if key < 1860 and key >= 1850:
            count1 += value        
        elif key < 1870 and key >= 1860:
            count2 += value         
        elif key < 1880 and key >= 1870:
            count3 += value        
        elif key < 1890 and key >= 1880:
            count4 += value        
        elif key < 1900 and key >= 1890:
            count5 += value       
        elif key < 1910 and key >= 1900:
            count6 += value       
        elif key < 1920 and key >= 1910:
            count7 += value        
        elif key < 1930 and key >= 1920:
            count8 += value    
        elif key < 1940 and key >= 1930:
            count9 += value       
        elif key < 1950 and key >= 1940:
            count10 += value
        elif key < 1960 and key >= 1950:
            count11 += value       
        elif key < 1970 and key >= 1960:
            count12 += value        
        elif key < 1980 and key >= 1970:
            count13 += value    
        elif key < 1990 and key >= 1980:
            count14 += value       
        elif key < 2000 and key >= 1990:
            count15 += value
    

    line_kw.append(count1)
    line_kw.append(count2)
    line_kw.append(count3)
    line_kw.append(count4)
    line_kw.append(count5)
    line_kw.append(count6)
    line_kw.append(count7)
    line_kw.append(count8)
    line_kw.append(count9)
    line_kw.append(count10)
    line_kw.append(count11)
    line_kw.append(count12)
    line_kw.append(count13)
    line_kw.append(count14)
    line_kw.append(count15)


    return line_kw # keyword frequencies aggregated by decades


# topics within the defined year range

topics("wch_events.json", 1157, 2020, 15, "wch_lda_vis.html")



# plot frequency change over time;
# can compare multiple keywords;
# plotting multiple words in one graph because they might be relevant
# but no specific relationships should be assumed 

dict_lines = {
    
    # related to minorities
    
    'women': keyword_frequency("women"),
    'miners': keyword_frequency("miner"),
    'students': keyword_frequency("student"),
    'black': keyword_frequency("black"),
    
    # related to resistance & rebellion

    #'strike': keyword_frequency("strike"),
    #'protest': keyword_frequency("protest"),
    #'movement': keyword_frequency("movement"),
    #'union': keyword_frequency("union")
    
}

for years, frequencies in dict_lines.items():
    plt.plot(["1850-1860","1860-1870","1870-1880","1880-1890","1890-1900","1900-1910","1910-1920","1920-1930","1930-1940","1940-1950","1950-1960","1960-1970","1970-1980","1980-1990","1990-2000"], frequencies, '.-', label=years)
    
plt.legend()  
plt.show()

