# Computational Literacy Final Project, 2024

## Themes in the Working Class History


## Introduction

The rebellion and solidarity in social movements, the struggles against colonization and racism, the waves of feminism, the students movements, etc. have always been inspiring me to think about challenges we are facing in our society today and what we can possibly do as individuals and communities.

The Working Class History - Everyday Acts of Resistance & Rebellion (WCH) project is a collaborative archive of people’s history, where events and people are collected to commemorate grassroots movements, struggles of the working class, hidden stories of marginalized communities, and so on. Founded in 2014, the WCH team is an international collective of worker-activists who launched a social media project and podcast to uncover our collective history of fighting for a better world (Working Class History, 2020).

The events documented reflect how the WCH team define working class history and imply what are considered as important lessons and learnings for us today. In terms of what the “working class” entails,  their perspective is quite open: “we take an expansive, intersectional, and internationalist view of class, and we present snapshots of all kinds of battles against exploitation and oppression.”(Working Class History, 2020). From these events we can see actions taken by women, young people, people of color, workers, migrants, indigenous people, LGBT+ people, disabled people, the unemployed, and every other part of the working class. 

While the people and stories selected in the project are empowering in different ways, I wonder if we combine the close reading with a view from the distance, what will the events reveal collectively that might be invisible otherwise.

As Chomsky says in his foreword for this book, “In these tumultuous time, Working Class History is important, because a functioning democracy requires active citizens participation in setting social policy”. Inspired by the project’s mission and Chomsky’s comment, I aim at delving into ordinary people’s participation in social movements and their resistance against oppression. My research questions are:

1. What are the common themes in the Working Class History project?
   
2. Through the main topics reflected in the Working Class History project, what can we learn about ordinary people’s resistance and participation in social movements?  

This analysis is based on the events curated by the WCH team, which don’t fully mirror the entire history and may involve biases inevitably. Nonetheless, it’s still a powerful archive reflecting historical facts and collaborative memories, encouraging us to learn from the past, contemplate on current social issues and advocate for our communities today.

## Dataset

The dataset is the textual content of the historical events documented in the “Working Class History - Everyday Acts of Resistance & Rebellion” book. 

The events are organized by date, and a date usually associates with events from multiple years. For instance, December 12 has two entries: December 12, 1948 and December 12, 1969. Each event contains an article describing the process, the result, a person or community, relevant places, etc. The event description is unstructured text.

Originally, these records were posted by the WCH team on social media on anniversaries of the events, allowing the public to learn about the historical movements in a more relatable way. The book was published in 2020, but events are still being updated online. Due to copyright reasons, the raw data from the book used in this assignment won’t be shared publicly. Readers can visit the official website of  Working Class History (https://workingclasshistory.com/) and their social media platforms for stories, podcasts and more. 

## Process

For this analysis, I focused on the event texts and excluded content before and after the events section, such as introduction, foreword, and references. Each event was put in one paragraph, showing up in the .txt file as one line starting with the date. The data is saved in wch_data.txt.  

Next, each event was stored in a dictionary or a distinct document for the purpose of topic modeling. The event dictionary has the date as key, event text as value. After some initial topic modeling trials, I realized that “women”, “students”, “miners” etc. are salient terms and potential concepts that I would like to focus on, and the singular forms should be treated as the same concept, so I replaced these words with their plural forms. This is problematic and will be discussed in the Problems and Biases section. The documents are stored in the wch_events.json file, and the code for converting txt to json file is text_to_json.py. 

Putting the text into Voyant tools to get a general idea, I realized words like “workers / work / working” are so important that they appear too frequently and might overshadow other key concepts. So I added these words in the list of stop words, along with other words that are either too frequent or less meaningful based on our context.

Preprocessing steps included lowercasing, removing numbers and punctuations, and tokenizing.

Then the LDA model in Gensim was used to conduct the topic modeling. Part of the preprocessing and topic modeling process was based on the code from Nan Jiang’s project “An analysis of Finnish milk propaganda” (DOI: 10.5281/zenodo.10419360) with some modifications or adjustments. I put these steps in a function named topics(dataset: str, start_year: int, end_year: int, topic_no: int, output_vis: str), which takes the data file name, year range, number of topics and the visualization file name as its arguments, and returns the lda_model. The year range allows us to focus on specific time frame such as 20th century, or compare different time ranges, such as 1930-1950 vs. 1960-1980.

The initial topic modeling trials yielded fairly similar topics from looking at the terms, although the Intertopic Distance Map does show some distinction. The alpha parameter of the LdaModel was defaulted to ‘symmetric’. After consulting the professor, I learned that terms such as "strike" appeared constantly and that may hurt the model’s ability to divide the rest of the material. Following his advice, I set the parameter to alpha=‘auto’ so that the model learns an asymmetric prior from the corpus. I used the CoherenceModel in Gensim to calculate the topic coherence. After alpha was set to ‘auto’, it resulted in better coherence score.

To determine the number of topics, I tried setting it to 5, 10 and 15, comparing the results based on the terms in each topic, the Intertopic Distance visualization, and coherence scores. When the number was lower, although the coherence score was higher, they were less unique from each other, making it harder to come up with meaningful interpretations. Since the dataset is not very diverse due to the nature of the theme and the editorial choices, I tried to reveal more distinct terms. Eventually I settled on 15 topics, when the thematic structure of WCH was summarized relatively better. The evaluation of the topic model could be based on perplexity, coherence, visualization and human interpretability. My decision was the tradeoffs between these factors and was inevitably biased by my subjective interpretations and limited knowledge.

In addition to topic modeling, I’d like to see how certain keywords’ frequencies change over time and visualize them in line charts. I wrote a function named keyword_frequency(keyword: str), which takes the keyword as its argument. For each event, I counted the keyword’s frequency and put them in a dictionary, using the year as key, frequency as the value. When multiple events happened in the same year, the keyword frequencies would be added up. Next, to simply the line charts, I aggregated the frequencies by decades. After a few trials I currently set the year range to 1850-2000, where we can see a change between the two centuries and some fluctuations in different decades of the 20th century. But we can choose different time ranges based on our purposes. Then the frequencies were summed up by decades and put in a list named line_kw.  Next, we can plot the frequencies over time as a line chart using the Matplotlib library, with the x-axis showing the decades, y-axis showing the keywords counts.

I plotted multiple keywords in one chart to see if they might reveal any interesting patterns, such as women, miners, students, black, which could be considered as communities or minorities who have made specific contributions to the working class history. But at this point we shouldn’t assume the statistics of these concepts have any specific relationships with each other.

The code for preprocessing, topic modeling and keyword frequency is in wch_lda_frequency.py.

## Analysis
### Topic Modeling

In order to obtain an understanding on the main themes in the Working Class History project, the top 30 salient terms for each the 15 topics were examined based on the original text and the historical context. 

1	union, women, black, strike, police, white, sailors, arrested, british, local, american, first, pay, war, group, members, government, despite, african, iww, troops, navy, end, eventually, support, world, killed, attacked, without, city

2	strike, women, police, union, black, government, british, pay, killed, support, white, movement, south, authorities, children, arrested, first, national, company, city, protest, war, attempted, group, increase, members, african, strikers, end, class	

3	strike, women, union, british, police, government, first, prison, world, party, fire, drivers, children, communist, killing, organized, killed, massacre, even, anarchist, troops, mexican, strikers, arrested, subsequently, protest, army, war, black, soldiers 

4	strike, police, government, british, city, murdered, attacked, union, london, class, french, death, pay, resistance, war, world, troops, movement, factory, women, civil, members, known, protest, mass, strikers, protests, camp, army, independence	

5	police, black, killed, british, white, killing, government, movement, death, shot, land, strike, prison, factory, public, uprising, protest, arrested, time, demanding, officer, ramón, women, massacre, military, students, american, rebellion, trial, occupation

6	british, women, government, police, french, strike, troops, military, refused, black, island, soldiers, white, colonial, union, murdered, twenty, anarchist, killed, local, army, member, class, states, pay, american, area, forces, shot, arrested

7	police, white, women, rights, black, war, american, government, shot, union, york, city, revolution, world, strike, british, civil, fascists, attacked, class, freedom, known, african, young, fought, national, killed, lincoln, first, organization

8	strike, police, women, government, black, students, killed, miners, pay, union, killing, british, company, forces, attacked, class, military, striking, national, protests, broke, protest, white, despite, fire, massacre, members, african, shot, demanding

9	strike, women, police, government, pay, black, arrested, union, first, african, white, local, british, south, company, strikers, class, demanding, protest, refused, forced, military, members, power, state, rights, joined, army, american, group

10	strike, police, women, union, city, arrested, pay, killed, protest, french, strikers, british, government, black, war, troops, prison, movement, york, action, world, state, death, rights, known, agreed, eventually, soldiers, anarchists, free

11	strike, black, police, white, women, local, hours, union, killed, military, strikers, miners, first, african, coal, government, return, laws, pay, time, students, rights, protest, death, americans, war, civil, rebellion, jailed, murdered

12	strike, police, miners, killing, group, fire, troops, women, black, organized, enslaved, students, national, fascist, movement, joined, british, local, government, state, rebellion, armed, executed, fascists, pay, war, support, class, union, previous

13	police, protest, strike, government, armed, war, students, movement, women, black, city, south, law, uprising, crowd, national, enslaved, troops, killed, british, authorities, local, officers, protesters, forced, high, military, control, end, panthers 

14	women, strike, union, war, police, world, movement, protest, rebellion, arrested,	japanese, riots, first, black, government, asian, streets, food, struggle, york, england, fbi, prison, country, killed, fire, arrest, class, spread, led

15	strike, police, government, union, group, pay, increase, members, killed, black, attacked, york, authorities, movement, fire, strikers, protest, guillotine, repression, world, continued, public, local, city, students, war, strikes, supporters, party, country

![topic visualization](https://github.com/mengdii/Computational-Literacy-WCH/blob/main/topics%20visualization.png?raw=true)

I tried to come up with labels that potentially describe the themes, however, due to the overlaps between topics, the nature of the events, and the limitation of my subjective interpretation, some of the themes might be vague, broad or biased at this point. In this section, I mainly discuss the prominent topics and the topics that reveal unexpected or interesting perspectives.

A large number of events contain multiple different keywords within a short paragraph due to the real situation of the struggles, which might be one of the factors leading to the mixed topics. For example, in the events below, we can see strike, women, workers, violent, police, pay etc. all at once. 

January 3, 1913: The Little Falls textile strike in New York ended when the workforce of predominantly migrant women organized in the revolutionary Industrial Workers of the World union (IWW; aka Wobblies) won their demands. They had walked out on October 9, and in the face of violent police repression, the workers held firm and achieved a reduction in weekly working hours from sixty to fifty-four, with no loss of pay.

Topic 8 is the most prominent topic followed by Topic 2 and Topic 1. The top 30 relevant terms for Topic 8 take up 13.1% of tokens, and “women”, “Black”, “miners”, “students” appear in the top 10. The main theme of Topic 8 could be associated with minorities.

“Women” stands out persistently in almost all the topics, reflecting the WCH project’s emphasis on women’s actions and contributions in the movements or presence in the events at the very least. 

Besides Topic 8, “Black”, “students”, “miners” are frequently seen in many topics, which could reflect how minorities or communities that had been subordinate and oppressed responded to the social issues as active participants. To see the context of these terms and get an idea about their potential roles, I used Voyant’s collocation analysis function and referred to the original text. 

![Collocation](https://github.com/mengdii/Computational-Literacy-WCH/blob/61e5724f2fb8999eca28199bbdcb77a61400f81a/collocations.png)

“Organized” being one of the collocates of “women”may indicate that at least in some of the events women are associated with organized actions as oppose to a brief mention. “Including” may imply that women had to be explicitly included because they had been underrepresented or ignored in certain aspects previously. For example, “January 27,1918 Revolution broke out in Finland as workers took over Helsinki, with many of the country’s other large towns following in the next few days. The ‘People’s Republic of Finland’ instituted numerous far-reaching reforms, including women’s suffrage, workers’ control of production, a maximum eight-hour workday, the abolition of the old mode of land distribution, and the emancipation of domestic servants and farmhands.”

In the collocates of “students”, “peacefully” and the context reveals that students tried to protest peacefully, but were prevented and hurt by the authorities. “White” ranks high in the collocates list of “black”, showing the major conflicts and the anti-racist discourse. And for “miners”, terms related to the miners’ family stand out, such as wives, women, and children; “walked” refers to “walked out” on strikes in this context.

Terms associated with Topic 2 are mixed and similar to other topics, but “support” appears within the top 10 terms. If we look at its context in Voyant, we could see many events involve people under oppression helping each other, which could imply solidarity.

![Context for support](https://github.com/mengdii/Computational-Literacy-WCH/blob/61e5724f2fb8999eca28199bbdcb77a61400f81a/support_context.png)

For Topic 1, terms such as “Black”, “white”, “African” and “American” may indicate anti-racist narratives.

Topic 6 has “British” as the most frequent term, along with French, island, colonial, army. Checking the context of “British” and “French”, we could see most events are associated with colonial power. Therefore, this topic can be viewed as mainly about colonialism.

The terms in Topic 9 also lack coherence, but we can see terms like pay, company, and demanding. The term “demanding” felt interesting but vague, so I went back to the original text again. From excerpts such as  “…the strikers, mostly wool workers and rural laborers, were demanding better pay and conditions…”, and “…protests and riots broke out across the country, demanding democratic rights and cultural rights for Amazigh people…”, we could see the agency of people being exploited and their courage fighting against authorities.

![Context for demanding](https://github.com/mengdii/Computational-Literacy-WCH/blob/61e5724f2fb8999eca28199bbdcb77a61400f81a/demanding_context.png)

Overall, terms related to conflicts, violence, exploitation and oppression such as police, troops, arrested, killed, massacre, prison etc. are present in almost all topics. At the same time, from the frequent appearance of strike, protest, movement, union, support etc., we are also empowered by the participation, resistance and solidarity of the working class. 

Next, besides looking at all the topics for the entire time period covered by the project, I wanted to find out how the topics are different in specific time frames. So I ran the topic modeling function for time periods of 1900s-1930s (roughly the decades before and after WWI), 1930s-1960s (roughly before and after WWII), and 1960s-1980s, when many major social changes happened around the world. For the purpose of comparison, the number of topics was set to 5.

From the results, the prominent topics for each of these time ranges appear to be different based on the historical context, reflecting how ordinary individuals of the working class have taken actions to social crisis in each historical period. The terms for the prominent topic during 1900s -1930s include miners, pay, industrial, conditions, etc., which are related to miners’ strikes for better working conditions. For 1930s - 1960s, terms in the prominent topic contain nazi, jewish, fascists, which explicitly ties to the anti-fascist theme. The terms associated with the prominent topic for 1960s - 1980s include black, students, women, civil, rights, etc., connecting to minorities’ struggles in the social movements during this period.

The piecharts below illustrate the different topic distributions for the three periods (the piecharts were generated in excel based on percentage of tokens for each topic. The topics with highest percentages are labelled. The salient terms can be found in Appendix).

![Topic distribution in different time ranges](https://github.com/mengdii/Computational-Literacy-WCH/blob/61e5724f2fb8999eca28199bbdcb77a61400f81a/Topics_time%20ranges.png)


### Keyword Frequency Over Time

While the topic modeling results provide a snapshot of the thematic structure of Working Class History, I’m curious to dive into certain key concepts and see how they have changed over time and what they reflect about the socio-historical context. 

I plotted the frequencies of “women”, “students”, “miners” and “black” on the same graph, because they are groups who had been suppressed previously and minorities who have made specific contributions to the history. Their fluctuations over time might be relevant to specific time periods and historical events, but we shouldn’t assume any specific correlations or causal relationships between these lines

![keyword frequency over time](https://github.com/mengdii/Computational-Literacy-WCH/blob/main/keyword%20frequency%20over%20time.png?raw=true)
 
The spike in “women” during 1960s - 1980s is a probable reflection of the second wave of Feminism. The spike in “students” in the 1960s could be related to the student movements. A close reading on the events from these period proved the relevancy. 

An increase of frequency can also be observed for “miners” around 1900s - 1920s. After a search for events containing “miners” during this time frame, among the 16 results, 8 took place in the United States, and all of them were related to strikes. This is largely in line with the American history during this time, “nowhere was the economic and social change which produced American radicalism in the late nineteenth century so rapid and so unsettling as in the mining West” (Dubofsky, 1966).

The “women” line also sees a spike during the early 20th century. No statistical correlations between “miners” and “women” should be assumed here only based on the graph, but I wanted to see if there are potential connections. I searched for events during this time frame that contain “women” and “miners”, and found that while miners’ wives and children were victims, they also supported and helped the striking miners, E.g. “…striking Indian mine workers in South Africa demonstrated against a new tax on former indentured laborers. Around two thousand miners marched, as did some women and children…”, and “…The Rockefellers evicted the striking miners and their families from their homes, so they set up collective “tent cities” which miners’ wives helped run. Company thugs harassed strikers and occasionally drove by camps riddling them with machine-gun fire, killing and injuring workers and their children…”

Further looking into events related to women in the early 20th century, we can see ordinary people like housewives going out on demonstrations, and the courageous sacrifice of women who are hidden from the mainstream history:

January 25, 1911: Kanno Sugako, a Japanese anarchist feminist, was executed for her part in a plot to assassinate the emperor. She remains the only woman to be executed in Japan for treason. Radicalized at the age of fourteen, after being raped, in addition to being a pioneering feminist, she was one of Japan’s first female journalists and a prolific writer of fiction and nonfiction…

In her prison diary she wrote: “Needless to say, I was prepared for the death sentence. My only concern day and night was to see as many of my . . . fellow defendants saved as possible. . . . I am convinced our sacrifice is not in vain. It will bear fruit in the future. I am confident that because I firmly believe my death will serve a valuable purpose I will be able to maintain my self-respect until the last moment on the scaffold. I will be enveloped in the marvelously comforting thought that I am sacrificing myself for the cause. I believe I will be able to die a noble death without fear or anguish.”

## Biases and Problems

As the authors of the WCH project explain in the book, “We do not claim to recount every movement or incident of importance to our collective history of struggle…we have attempted to present a diverse range of historical events, but due to our locations, primarily the UK and the US, the languages we speak and the nature and biases of sources available to us, there is, unfortunately but unavoidably, a bias in the events toward the European languages of English, Spanish, French, and Italian and toward countries with colonial relationships with those languages.” (Working Class History, 2020) So the topic modeling and analysis reflects the working class history from the team’s perspectives, affected by the events included in the book as well as the inevitable biases related to locations and languages.

The goal of the WCH project is to uncover the collective history of fighting against exploitation, discrimination, colonization and oppression, promoting this people’s history to educate and inspire a new generation of activists. This is of great value and inspiration, and explains the choices of the events; but the persistent narrative did make it hard for the model to form distinct and coherent topics. This could also imply that topic modeling might not be the most suitable method for analyzing corpora with concentrated topics. 

The keyword frequencies over time could also be affected by the events selected and documented for each year, so low frequency during a certain period doesn’t necessarily mean it’s unimportant. In the future, more diverse contributors and a larger quantity of text might lead to more diverse and balanced themes and better topic modeling results. 

Ambiguity in certain terms also affects the results and interpretation. Some terms entail multiple meanings or aspects, making it hard to judge without context, For example, “Japanese” is associated with violence and colonialism, as well as revolutions and anarchists. For terms that refer to people (e.g. women), we can’t tell if it’s introducing a significant person or group, or it’s a person showing up only in passing, so there might be some false positives.

Despite the nature of the data, interpretations of the topics are affected by my limited knowledge and biased perspectives. A lot of them are subjective and may appear to be a stretch based on a few terms. Analysis of the topics for specific time frames is based on the assumption that they might be related to the larger historical events, so the interpretation could be just trying to prove this.

There are also problems in the preprocessing phase. A few keywords were chosen to match the single and plural forms based on the initial trials and the purpose of analysis, but lemmatization should have been done properly. Regarding stop words, I added stop words to the list based on preliminary explorations in frequency and topic modeling, but still omitted some less meaningful words. I treated “workers” as a stop word because it’s a basic concept and the most frequent word that would affect the topic modeling process; however, “strike” is the second most frequent word and did affect the results, but I chose to keep it because it reflects a significant aspect of resistance and participation of the working class. But this decision is debatable and there could be better alternatives.

## Concluding Remarks

The topic modeling and keyword frequency of the Working Class History reflects ordinary people’s struggles against oppression, reinforcing the roles of active participation of individuals and grassroots communities in social movements. 

Looking at the Working Class History through distant reading has uncovered some aspects that may not be apparent only based on close reading of individual events. Across the collection, the agency and resilience of women and minorities are emphasized persistently. Solidarity between the suppressed groups are identified. History is shaped by the actions of individuals and communities.

Biases and limitations in the quantitative approaches and human interpretations suggest a combination of close reading and distant reading in the socio-historical context. The recurring terms have affected the topic modeling results and interpretability to some extent, but they also manifest the commonality of these struggles and the crucial aspect of the Working Class History that the collective wants to convey - victories and improvements have been won only by years of violent conflict and sacrifice of ordinary people.

## References

Working Class History (Eds.). (2020) Working Class History: Everyday Acts of Resistance & Rebellion. PM Press.
Working Class History. Stories. https://stories.workingclasshistory.com/
Gensim. Latent Dirichlet Allocation. https://radimrehurek.com/gensim/models/ldamodel.html
Gensim. Topic coherence pipeline. https://radimrehurek.com/gensim/models/coherencemodel.html
Voyant Tools. https://voyant-tools.org/
Nan Jiang. (2024). An analysis of Finnish milk propaganda - DOI: 10.5281/zenodo.10419360
Dubofsky, M. (1966). The origins of western working class radicalism, 1890–1905. Labor History, 7(2), 131-154.



