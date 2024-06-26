# Understanding TF-IDF

TF-IDF (Term Frequency-Inverse Document Frequency) is a statistical measure used to evaluate the importance of a word in a document relative to a collection of documents (corpus). It combines two metrics:

- **Term Frequency (TF)**: Measures how frequently a term appears in a document.
- **Inverse Document Frequency (IDF)**: Measures how important a term is by reducing the weight of terms that appear frequently in many documents.

## Example

Consider a small corpus with three documents:

- Document 1: "I love playing guitar"
- Document 2: "I love singing"
- Document 3: "playing guitar is fun"

### Step-by-Step Calculation

#### Step 1: Calculate Term Frequency (TF)

| Term    | Document 1 (TF) | Document 2 (TF) | Document 3 (TF) |
|---------|-----------------|-----------------|-----------------|
| I       | 1/4             | 1/3             | 0/4             |
| love    | 1/4             | 1/3             | 0/4             |
| playing | 1/4             | 0/3             | 1/4             |
| guitar  | 1/4             | 0/3             | 1/4             |
| singing | 0/4             | 1/3             | 0/4             |
| is      | 0/4             | 0/3             | 1/4             |
| fun     | 0/4             | 0/3             | 1/4             |

#### Step 2: Calculate Inverse Document Frequency (IDF)

| Term    | IDF              |
|---------|------------------|
| I       | log(3/2) ≈ 0.176 |
| love    | log(3/2) ≈ 0.176 |
| playing | log(3/2) ≈ 0.176 |
| guitar  | log(3/2) ≈ 0.176 |
| singing | log(3/1) ≈ 0.477 |
| is      | log(3/1) ≈ 0.477 |
| fun     | log(3/1) ≈ 0.477 |

#### Step 3: Calculate TF-IDF

Multiply the TF and IDF values for each term in each document.

| Term    | Document 1 (TF-IDF) | Document 2 (TF-IDF) | Document 3 (TF-IDF) |
|---------|---------------------|---------------------|---------------------|
| I       | 0.176 * 1/4 ≈ 0.044 | 0.176 * 1/3 ≈ 0.059 | 0.176 * 0/4 = 0     |
| love    | 0.176 * 1/4 ≈ 0.044 | 0.176 * 1/3 ≈ 0.059 | 0.176 * 0/4 = 0     |
| playing | 0.176 * 1/4 ≈ 0.044 | 0.176 * 0/3 = 0     | 0.176 * 1/4 ≈ 0.044 |
| guitar  | 0.176 * 1/4 ≈ 0.044 | 0.176 * 0/3 = 0     | 0.176 * 1/4 ≈ 0.044 |
| singing | 0 * 0               | 0.477 * 1/3 ≈ 0.159 | 0 * 0               |
| is      | 0 * 0               | 0 * 0               | 0.477 * 1/4 ≈ 0.119 |
| fun     | 0 * 0               | 0 * 0               | 0.477 * 1/4 ≈ 0.119 |

### Implementation with TfidfVectorizer in scikit-learn

In Python using scikit-learn's TfidfVectorizer, you can achieve TF-IDF vectorization easily:

```python
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    "I love playing guitar",
    "I love singing",
    "playing guitar is fun"
]

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)

# tfidf_matrix is the TF-IDF representation of the corpus
