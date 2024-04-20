# Libraries Used:
*numpy (as np): For numerical operations.
*pandas (as pd): For handling data in DataFrame format.
*requests: For making HTTP requests to retrieve web content.
*BeautifulSoup (from bs4): For parsing HTML content.
*nltk: For natural language processing tasks like tokenization and stopwords removal.


# Data Retrieval and Processing:
### Reading Data:
The code reads an Excel file (Output Data Structure.xlsx) using pd.read_excel() to obtain URLs.
### Looping Through URLs:
The code iterates through the URLs obtained from the Excel file (data['URL']).
For each URL (up to the first 100 URLs due to the loop range limitation), it retrieves the HTML content using requests.get() and parses it using BeautifulSoup to extract text.
### Text Preprocessing:
The extracted text is filtered to include only specific HTML block elements ('title', 'p', 'ol', 'li') using list comprehension (text_elements).
### Stopwords Removal and Tokenization:
Stopwords are loaded from various text files (StopWords_Geographic.txt, StopWords_Names.txt, etc.) and combined into a list (stop_words).
The extracted text is tokenized using nltk.word_tokenize() and filtered to remove stopwords, punctuation, and other unwanted elements.
### Linguistic Analysis:
Various linguistic metrics are computed based on the processed text:
**Positive and Negative Word Counts:** Count of positive and negative words from predefined lists (positive-words.txt, negative-words.txt).
**Polarity Score:** A measure of text sentiment based on positive and negative word counts.
**Subjectivity Score:** Ratio of subjective words (positive + negative) to the total words.
**Average Sentence Length:** Average number of words per sentence.
**Percentage of Complex Words:** Ratio of complex words (words with three or more syllables) to the total words.
**Fog Index:** A readability index calculated using average sentence length and percentage of complex words.
**Personal Pronouns Count:** Count of personal pronouns ('I', 'we', 'my', 'ours', 'us') in the text.
**Average Word Length:** Average length of words in the text.
**Total Syllables Count:** Count of syllables in words (approximated based on vowel count).
### Data Population:
The computed metrics are used to populate the respective columns ('POSITIVE SCORE', 'NEGATIVE SCORE', etc.) in the data DataFrame.
