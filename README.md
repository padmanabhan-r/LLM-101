# LLM-101

A hands-on educational repository for learning the fundamental building blocks of Large Language Models (LLMs). This project provides step-by-step tutorials covering tokenization, data sampling, and embeddings using Python and PyTorch.

## 📚 Overview

This repository takes you through the essential components needed to understand how LLMs process text:

1. **Tokenization** - Converting text into numerical tokens
2. **Data Sampling** - Creating training batches with sliding windows
3. **Token Embeddings** - Transforming tokens into dense vector representations

All tutorials use Shakespeare's *Romeo and Juliet* from Project Gutenberg as sample data.

## 📁 Project Structure

```
LLM-101/
├── 01_tokenization.ipynb          # Tokenization tutorial
├── 02_data_sampling.ipynb         # Data sampling and DataLoader tutorial
├── 03_token_embeddings.ipynb      # Token embeddings tutorial
├── core/
│   ├── basic_tokenizer.py         # Custom tokenizer implementation
│   └── data_loader.py             # PyTorch Dataset/DataLoader utilities
├── data/
│   ├── romeo_juliet_gutenberg.txt # Sample text corpus
│   └── notes.md                   # Data source information
└── notebooks/                     # Directory for your experiments
```

## 🎓 Tutorials

### 01. Tokenization
Learn how to convert text into numerical representations:
- Load and explore text data
- Tokenize text using regex patterns
- Build a vocabulary mapping tokens to IDs
- Create a custom `BasicTokenizer` class
- Handle special tokens (unknown words, end-of-text markers)
- Compare with Byte Pair Encoding (BPE) used in GPT models

### 02. Data Sampling
Understand how to prepare data for LLM training:
- Create sliding window sequences for efficient learning
- Build PyTorch Datasets and DataLoaders
- Generate input-target pairs for next-token prediction
- Configure batch size, sequence length, and stride parameters

### 03. Token Embeddings
Explore how tokens become dense vectors:
- Convert token IDs into embedding vectors
- Add positional information to embeddings
- Combine token and positional embeddings for model input

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- PyTorch
- tiktoken (OpenAI's tokenizer)
- Jupyter Notebook

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/padmanabhan-r/LLM-101.git
cd LLM-101
```

2. **Install dependencies**:
```bash
pip install torch tiktoken jupyter
```

3. **Launch Jupyter Notebook**:
```bash
jupyter notebook
```

4. **Open and run the tutorials** in order (01, 02, 03) to follow the learning path.

## 🛠️ Core Modules

### `core/basic_tokenizer.py`
A simple regex-based tokenizer that:
- Creates vocabulary from text
- Encodes text to token IDs
- Decodes IDs back to text
- Handles special tokens

### `core/data_loader.py`
PyTorch utilities for LLM data preparation:
- `SlidingWindowDataset`: Creates overlapping sequences from text
- `create_dataloader()`: Configures DataLoader with batching options

## 📖 Data Source

The text corpus is Shakespeare's *Romeo and Juliet* from Project Gutenberg:
- Source: https://www.gutenberg.org/ebooks/1513
- Direct link: https://www.gutenberg.org/cache/epub/1513/pg1513.txt

## 🎯 Learning Objectives

By completing these tutorials, you'll understand:
- How neural networks process text data
- The difference between word-level and subword tokenization
- How to create efficient training data pipelines
- The role of embeddings in neural language models
- Key concepts used in modern LLMs like GPT

## 🚧 Roadmap

**More tutorials coming soon!** Future topics will include:
- Attention mechanisms and self-attention
- Transformer architecture from scratch
- Multi-head attention
- Layer normalization and residual connections
- Building a complete GPT-style model
- Training and fine-tuning strategies
- Evaluation and inference

*Stay tuned for updates as we continue building toward a complete LLM implementation!*

## 📝 License

This project is for educational purposes. The text data is sourced from Project Gutenberg and is in the public domain.

## 🤝 Contributing

Feel free to open issues or submit pull requests if you find errors or have suggestions for improvements!

## 📧 Contact

Repository maintained by [padmanabhan-r](https://github.com/padmanabhan-r)

---

**Happy Learning! 🚀**
