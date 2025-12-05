# Automated-Document-Intelligence-System

Automated Document Intelligence System automatically processes documents (PDFs, Word files, or text files) and extracts key insights, including summaries, named entities, keywords, and sentiment analysis. It can be applied in business intelligence, legal tech, finance, and research.

**Features**

Document Loading: Supports PDF, DOCX, and plain text files.

Text Preprocessing: Cleans and normalizes text for NLP analysis.

Keyword Extraction: Identifies important keywords or phrases from the document.

Named Entity Recognition (NER): Detects entities like people, organizations, dates, and locations.

Document Summarization: Produces concise summaries of long documents.

Sentiment Analysis: Detects the overall sentiment (positive, negative, neutral).

Export Results: Saves extracted insights to CSV or JSON.

**Requirements**

pip install pandas numpy spacy nltk PyPDF2 python-docx gensim
python -m spacy download en_core_web_sm

PyPDF2 → read PDF files

python-docx → read DOCX files

spaCy → NER and NLP preprocessing

gensim → text summarization

nltk → text cleaning and sentiment analysis
