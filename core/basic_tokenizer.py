class BasicTokenizer:
    def __init__(self, text):
        """Initialize tokenizer by creating vocabulary from text with special tokens"""
        self.word_to_id = self.create_vocab(text)
        self.id_to_word = {i: s for s, i in self.word_to_id.items()}
    
    @staticmethod
    def tokenize_text(text):
        """Tokenize text into tokens"""
        tokens = re.findall(r"[a-zA-Z]+(?:'[a-zA-Z]+)?|[0-9]|[^\w\s]", text)
        return tokens
    
    @staticmethod
    def create_vocab(text):
        """Create vocabulary from raw text with special tokens"""
        # Split text into tokens using regex
        tokens = re.findall(r"[a-zA-Z]+(?:'[a-zA-Z]+)?|[0-9]|[^\w\s]", text)
        
        # Get unique tokens and sort them
        all_words = sorted(set(tokens))
        
        # Add special tokens at the end
        all_words.extend(["<|endoftext|>", "<|unknown|>"])
        
        # Create vocabulary mapping
        vocab = {word: i for i, word in enumerate(all_words)}
        
        return vocab
    
    def encode(self, text):
        # Split text into tokens using the same regex pattern
        tokens = re.findall(r"[a-zA-Z]+(?:'[a-zA-Z]+)?|[0-9]|[^\w\s]", text)
        
        # Convert tokens to their integer IDs
        # Use <|unknown|> token for words not in vocabulary
        ids = [
            self.word_to_id.get(token, self.word_to_id["<|unknown|>"]) 
            for token in tokens
        ]
        return ids
    
    def decode(self, ids):
        # Convert integer IDs back to tokens
        tokens = [self.id_to_word[i] for i in ids]
        
        # Join tokens with spaces
        text = " ".join(tokens)
        
        # Remove spaces before punctuation
        text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)
        
        return text