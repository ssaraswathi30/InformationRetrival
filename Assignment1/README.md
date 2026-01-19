# Phrase-Based Academic Search Engine with Multi-Format Support

A comprehensive information retrieval system using positional indexing for exact phrase matching, supporting **5 different file formats**.

## Supported File Formats

✅ **.txt** - Plain text documents  
✅ **.pdf** - Portable Document Format  
✅ **.docx** - Microsoft Word documents  
✅ **.csv** - Comma-separated values  
✅ **.json** - JavaScript Object Notation  

## Setup Instructions

### Create Conda Environment
```bash
conda create -n irposindex python=3.10
conda activate irposindex
pip install -r requirements.txt
```

### Install Additional Format Support
```bash
pip install PyPDF2 python-docx openpyxl
```

## Usage

### Run the Jupyter Notebook
```bash
jupyter notebook Academic_Search_Engine.ipynb
```

### Convert to HTML
```bash
jupyter nbconvert --to html Academic_Search_Engine.ipynb --embed-images --no-input --output Academic_Search_Engine.html
```

## Key Features

- **Positional Indexing**: Exact phrase matching using word positions
- **Multi-Format Support**: Automatically processes 5 different document formats
- **Phrase Queries**: Find documents containing exact phrases
- **Keyword Queries**: Search for documents containing all keywords (any order)
- **Performance Metrics**: Precision, recall, and F1-score evaluation
- **Intelligent Parsing**: Smart text extraction from each format

## Documents

The system includes 14 sample documents:
- 10 text files (.txt)
- 1 PDF file (.pdf)
- 1 Word document (.docx)
- 1 CSV file (.csv)
- 1 JSON file (.json)

## Documentation

- **MULTI_FORMAT_SUPPORT_SUMMARY.md** - Overview of multi-format implementation
- **FORMAT_SUPPORT_STATUS.md** - Status and feature summary
- **IMPLEMENTATION_DETAILS.md** - Technical specifications and handler details

## Technologies Used

- **NLTK** - Natural language processing (tokenization, lemmatization)
- **PyPDF2** - PDF text extraction
- **python-docx** - Word document processing
- **Pandas** - Data analysis and visualization
- **Python csv** - CSV file handling
- **Python json** - JSON parsing

## Author

Saraswathi (ssaraswathi30)

## Branch

positionalAndKeywordSearchTXTfiles