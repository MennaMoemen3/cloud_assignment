import nltk
from nltk.corpus import stopwords
import string
from collections import Counter

# Download NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

# Load stopwords and punctuation
stop_words = set(stopwords.words('english'))
punctuation = set(string.punctuation)

# Function to clean a paragraph
def clean_paragraph(paragraph):
    # Tokenize the paragraph into words
    words = nltk.word_tokenize(paragraph.lower())
    
    # Filter out stopwords and punctuation
    filtered_words = [word for word in words if word not in stop_words and word not in punctuation]
    
    return filtered_words

# Function to write cleaned paragraphs to a file
def write_cleaned_paragraphs_to_file(paragraphs, file_path):
    with open(file_path, 'w') as file:
        for i, paragraph in enumerate(paragraphs):
            cleaned_words = clean_paragraph(paragraph)
            cleaned_paragraph = ' '.join(cleaned_words)
           # file.write(f"Cleaned Paragraph {i+1}:\n")
            file.write(cleaned_paragraph)
            file.write("\n\n")

# Function to count word frequencies
def count_word_frequencies(file_path):
    word_frequencies = Counter()
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            word_frequencies.update(words)
    return word_frequencies

# Read paragraphs from unfiltered file
unfiltered_file_path = "paragraphs.txt"  
with open(unfiltered_file_path, 'r') as file:
    paragraphs = file.readlines()

# Write cleaned paragraphs to a new file
cleaned_file_path = "cleaned_paragraphs.txt"
write_cleaned_paragraphs_to_file(paragraphs, cleaned_file_path)

# Count word frequencies from cleaned file
word_frequencies = count_word_frequencies(cleaned_file_path)

# Print word frequencies
print("Word Frequencies:")
for word, freq in word_frequencies.items():
    print(f"{word}: {freq}")
