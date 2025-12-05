# Automated-Document-Intelligence-System

IntelliDoc is an AI-based document intelligence platform that automatically extracts key insights from structured documents (PDFs, reports, invoices) using layout-aware NLP (LayoutLMv3) and LangChain for advanced processing. It reduces manual review time by automating sentiment analysis and data extraction.

**Features**

Document Parsing: Handles PDFs with complex layouts using LayoutLMv3.

Layout-Aware NLP: Extracts tables, text blocks, headers, and key-value pairs.

Sentiment Analysis: Evaluates sentiment of financial narratives automatically.

LangChain Integration: Chains multiple AI models for processing, summarization, and reasoning.

Batch Processing: Supports multiple documents.

Export Results: Saves insights to CSV or JSON.

**Requirements**

pip install torch transformers langchain pandas
pip install pdfplumber

transformers → for LayoutLMv3

langchain → for chaining AI operations

pdfplumber → for extracting text from PDFs

pandas → for saving results
