# Web Content Analysis Tool
This tool analyzes web content from a list of URLs provided in an Excel file and extracts various linguistic features and sentiment analysis metrics. It can be used to gain insights into the textual content of web pages, including polarity, subjectivity, readability, and more.

# Features
* **Data Extraction:** Scrapes text content from web pages using BeautifulSoup.
* **Linguistic Analysis:** Calculates linguistic features such as word count, average word length, average sentence length, percentage of complex words, syllables per word, and more.
* **Sentiment Analysis:** Determines polarity and subjectivity scores based on the presence of positive and negative words.
* **Fog Index Calculation:** Calculates readability using the Fog Index formula, which considers the average sentence length and percentage of complex words.
* **Personal Pronoun Detection:** Identifies and counts personal pronouns in the text.

# Dependencies
* **Python 3.x**
* **pandas:** For data manipulation and handling Excel files.
```
pip install pandas
```
* **requests:** For making HTTP requests to fetch web pages.
```
pip install requests
```
* **BeautifulSoup (bs4):** For web scraping and parsing HTML content.
```
pip install beautifulsoup4
```
* **nltk:** For natural language processing tasks such as tokenization and sentiment analysis.
```
pip install nltk
```

# Installation
1.Clone the repository to your local machine:
```
git clone https://github.com/your_username/web-content-analysis-tool.git
```

2.Install the required dependencies using pip:
```
pip install -r requirements.txt
```

3.Download NLTK resources by running the following commands in Python:
```
import nltk
nltk.download('punkt')
```
# Usage
1.Prepare your input data:
  * Create an Excel file named "Output Data Structure.xlsx" with a column named "URL" containing the URLs of the web pages you want to analyze.

2.Run the script **'web_content_analysis.py'**:
```
python web_content_analysis.py
```

3.The script will iterate over each URL, extract the text content, perform linguistic and sentiment analysis, and update the Excel file with the results.

# Data Retrieval and Processing:
## Reading Data:
The code reads an Excel file (Output Data Structure.xlsx) using pd.read_excel() to obtain URLs.

## Looping Through URLs:
The code iterates through the URLs obtained from the Excel file (data['URL']).
For each URL (up to the first 100 URLs due to the loop range limitation), it retrieves the HTML content using requests.get() and parses it using BeautifulSoup to extract text.

## Text Preprocessing:
The extracted text is filtered to include only specific HTML block elements ('title', 'p', 'ol', 'li') using list comprehension (text_elements).

## Stopwords Removal and Tokenization:
Stopwords are loaded from various text files (StopWords_Geographic.txt, StopWords_Names.txt, etc.) and combined into a list (stop_words).
The extracted text is tokenized using nltk.word_tokenize() and filtered to remove stopwords, punctuation, and other unwanted elements.

## Linguistic Analysis:
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

## Data Population:
The computed metrics are used to populate the respective columns ('POSITIVE SCORE', 'NEGATIVE SCORE', etc.) in the data DataFrame.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests with improvements or additional features.
