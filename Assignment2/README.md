# Academic Paper Recommendation System
## A Content-Based Information Retrieval System using Vector Space Model (VSM)

---

## 📋 Project Overview

This project implements a personalized research paper recommendation engine that suggests relevant academic papers based on a user's reading history. The system uses **content-based filtering** with **TF-IDF vectors** and **cosine similarity** to rank papers, reducing information overload for researchers.

### Key Features
- ✅ **27 Machine Learning research papers** with titles and abstracts
- ✅ **Text preprocessing** with built-in libraries only (lowercasing, tokenization, stop-word removal)
- ✅ **Manual TF-IDF implementation** with logarithmic term frequency and inverse document frequency
- ✅ **User profiling** from reading history using average TF-IDF vectors
- ✅ **Cosine similarity ranking** for paper recommendations
- ✅ **Top-5 recommendations** with similarity scores
- ✅ **Comprehensive analysis** of recommendation quality and system design

---

## 📊 System Architecture

### 1. Dataset (27 Papers)
- **Domain**: Machine Learning
- **Content**: Titles + Abstracts
- **Topics Covered**:
  - Deep Learning & Computer Vision
  - Natural Language Processing
  - Reinforcement Learning
  - Graph Neural Networks
  - Model Optimization & Explainability
  - And more...

**Sample Papers:**
- Deep Learning for Computer Vision: A Survey
- Transformer Models: State-of-the-Art NLP
- Transfer Learning: A Comprehensive Review
- Vision Transformers: Applying Transformers to Images
- Word Embeddings: Word2Vec, GloVe, and FastText

### 2. Text Preprocessing Module

**Steps:**
1. **Lowercasing**: Convert all text to lowercase
2. **Tokenization**: Extract words using regex (removes punctuation)
3. **Stop-word removal**: Filter out 98 common English stop words
4. **Token filtering**: Remove tokens with length ≤ 2 characters

**Result**: Preprocessed documents with 29.63 average tokens per paper

### 3. Vector Space Model (VSM)

#### TF-IDF Implementation

**Term Frequency (TF)** - Logarithmic Weighting:
```
TF(term, doc) = 1 + log(count) if count > 0, else 0
```

**Inverse Document Frequency (IDF)**:
```
IDF(term) = log(N / df)
where N = total documents
      df = document frequency (number of documents containing term)
```

**TF-IDF Score**:
```
TF-IDF(term, doc) = TF(term, doc) × IDF(term)
```

**Cosine Normalization**:
```
Normalized_Vector = Vector / ||Vector||₂
where ||Vector||₂ = √(Σ x²) is the L2 norm
```

#### Vocabulary & Vectors
- **Vocabulary Size**: 382 unique terms
- **Vector Dimensionality**: 382 (one dimension per term)
- **Vector Sparsity**: 93.64% (highly sparse vectors)
- **Documents Vectorized**: 27 TF-IDF vectors

### 4. User Profiling

**User Reading History**:
- Paper 1: Deep Learning for Computer Vision: A Survey
- Paper 6: Transformer Models: State-of-the-Art NLP
- Paper 16: Natural Language Understanding with BERT and Beyond
- Paper 22: Word Embeddings: Word2Vec, GloVe, and FastText
- Paper 25: Contrastive Learning: Self-Supervised Representation Learning

**Profile Vector Computation**:
```
User_Profile = Average(TF-IDF vectors of all read papers)
User_Profile = Σ(TF-IDF[d]) / |Reading_History|
               for d ∈ Reading_History
```

After cosine normalization, the user profile represents their aggregate research interests.

### 5. Similarity Computation & Ranking

**Cosine Similarity Formula**:
```
cos(θ) = (u · v) / (||u|| × ||v||)
where u = user profile vector
      v = document vector
      result ∈ [0, 1]
```

**Ranking Process**:
1. Compute cosine similarity between user profile and all papers
2. Exclude papers from reading history
3. Sort papers by similarity score (descending)
4. Return Top-5 papers with highest scores

---

## 📈 Results: Top-5 Recommendations

| Rank | Paper ID | Title | Similarity Score |
|------|----------|-------|-----------------|
| 1 | 26 | Vision Transformers: Applying Transformers to Images | 0.1852 |
| 2 | 3 | Transfer Learning: A Comprehensive Review | 0.1582 |
| 3 | 2 | Attention Mechanisms in Neural Networks | 0.1423 |
| 4 | 12 | Adversarial Robustness in Machine Learning | 0.0750 |
| 5 | 15 | Object Detection: YOLO, Faster R-CNN, and SSD | 0.0741 |

### Why These Papers Were Recommended

**Paper 26 (Vision Transformers)**: Highest similarity because it combines concepts from the user's reading history:
- Transformers (from Paper 6)
- Deep Learning (from Paper 1)
- Self-supervised learning (from Paper 25)

**Paper 3 (Transfer Learning)**: High relevance due to shared concepts with multiple papers in history
- Related to NLP fine-tuning (Paper 16)
- Multi-task learning overlap with representation learning (Paper 25)

**Paper 2 (Attention Mechanisms)**: Strong connection to transformer-based papers
- Foundation for Papers 6 and 16
- Complementary to word embeddings

---

## 📊 Performance Analysis

### Preprocessing Statistics
- Total tokens: 800
- Average tokens per paper: 29.63
- Vocabulary size: 382 unique terms
- Stop words removed: 98

### Similarity Score Distribution
- **Maximum similarity**: 0.5415
- **Minimum similarity**: 0.0053
- **Mean similarity**: 0.1436
- **Top-5 average similarity**: 0.1270

### Coverage Analysis
- **Documents with similarity > 0.01**: 26 (96.3% of dataset)
- **Documents with similarity > 0.05**: 19 (70.4% of dataset)

---

## 🎯 Analysis & Reasoning

### a) Recommendation Quality Analysis

**Relevance Assessment**:
- ✅ Top-5 papers are highly relevant to user interests
- ✅ Papers share significant vocabulary with reading history
- ✅ Recommendations span multiple but related subdomains
- ✅ No redundancy (papers not in history)

**How Content-Based Filtering Works**:
1. **Textual Similarity Capture**: TF-IDF vectors capture domain-specific terminology
2. **Semantic Alignment**: Papers with similar concepts receive higher scores
3. **Interest Modeling**: User profile represents aggregate research interests
4. **Personalization**: Recommendations are unique per user

### b) Why Content-Based Filtering for Academic Papers

#### 1. **Privacy Preservation**
- No user interaction tracking from other users
- Independent, user-specific recommendations
- Sensitive research interests remain private

#### 2. **Immediate Recommendations**
- No cold start problem for new users
- Can recommend immediately with reading history
- No need for large user population

#### 3. **Transparency**
- Clear explanation for each recommendation
- Users understand WHY papers were recommended
- Interpretable similarity scores (0-1 range)

#### 4. **Specialized Vocabulary**
- Academic papers use domain-specific terminology
- TF-IDF captures importance of specialized terms
- Recommendations based on actual research focus

#### 5. **Diverse Content**
- Can recommend emerging papers without popularity signals
- Not limited by collaborative filtering biases
- Handles long-tail content effectively

#### 6. **Scalability**
- Efficient computation with sparse vectors
- No matrix factorization overhead
- Works well with large document collections

### c) Why Cosine Similarity

#### Mathematical Advantages

**1. Invariance to Magnitude**
```
cos(θ) = (u · v) / (||u|| × ||v||)

Two vectors with proportional components 
have same cosine similarity regardless of length
```
- Document length doesn't affect similarity
- Longer papers aren't unfairly weighted

**2. Sparse Vector Efficiency**
- Only non-zero dimensions contribute to dot product
- Computation efficient for sparse TF-IDF vectors
- O(k) complexity where k = non-zero elements

**3. Bounded Output**
- Result always in range [0, 1]
- 0 = completely different (orthogonal)
- 1 = identical direction
- Easy interpretation and thresholding

**4. Normalized Space Geometry**
- Treats all documents equally in normalized space
- Fair comparison across different-length documents
- Captures directional similarity (topic alignment)

#### Comparison with Alternatives

| Metric | Cosine | Euclidean | Jaccard |
|--------|--------|-----------|---------|
| **Magnitude Sensitive** | No ✓ | Yes ✗ | No ✓ |
| **Weight Aware** | Yes (TF-IDF) ✓ | No ✗ | No ✗ |
| **Efficient Sparse** | Yes ✓ | No ✗ | Yes ✓ |
| **Bounded [0,1]** | Yes ✓ | No ✗ | Yes ✓ |
| **IR Standard** | Yes ✓ | No ✗ | No ✗ |

**Why NOT Euclidean Distance**:
- Longer documents appear more dissimilar
- Penalizes comprehensive papers
- Magnitude affects similarity undesirably

**Why NOT Jaccard Similarity**:
- Treats all terms equally
- Ignores TF-IDF weights
- Less effective for weighted vectors

---

## 🏗️ System Implementation

### Core Classes

#### 1. `TextPreprocessor`
```python
- lowercase(text): Converts text to lowercase
- tokenize(text): Extracts tokens using regex
- remove_stopwords(tokens): Filters stop words
- preprocess(text): Complete preprocessing pipeline
```

#### 2. `VectorSpaceModel`
```python
- build_vocabulary(): Creates term-to-index mapping
- compute_tf_log(): Logarithmic term frequency
- compute_idf(): Inverse document frequency
- create_tf_idf_vector(): Full TF-IDF vector
- cosine_normalize(): L2 normalization
- cosine_similarity(): Computes similarity between vectors
- fit(): Builds model from preprocessed documents
```

#### 3. `UserProfile`
```python
- add_to_history(): Adds paper to reading history
- build_profile(): Averages TF-IDF vectors from history
- get_profile_vector(): Returns user's profile vector
```

#### 4. `RecommendationEngine`
```python
- compute_similarity_scores(): Scores all papers
- rank_papers(): Sorts papers by similarity
- recommend_papers(): Returns top-k recommendations
```

---

## 📐 Mathematical Formulations

### 1. TF-IDF Framework

**Component Formulas:**
- TF(t,d) = 1 + log(count) where count > 0
- IDF(t) = log(N/df)
- TF-IDF(t,d) = TF(t,d) × IDF(t)
- Normalized_Vector[i] = Vector[i] / ||Vector||₂

### 2. User Profile Construction

**Profile Vector:**
```
P_user = (1/|H|) × Σ_d∈H v_d^normalized

where H = user's reading history
      v_d = TF-IDF vector for document d
```

### 3. Recommendation Ranking

**Similarity Score:**
```
Similarity(user, doc) = cos(P_user, v_doc)
                      = (P_user · v_doc) / (||P_user|| × ||v_doc||)
```

**Recommendation Set:**
```
Top_k = argmax_S (|Similarity_S|) 
        where S ⊂ D \ H
        |S| = k
        D = all documents
        H = reading history
```

---

## 🚀 How to Use

### Prerequisites
- Python 3.7+
- Jupyter Notebook
- Built-in libraries: `math`, `re`, `collections`, `string`

### Running the System

1. **Open the Notebook**
   ```bash
   jupyter notebook Academic_Paper_Recommendation_System.ipynb
   ```

2. **Execute Cells Sequentially**
   - Cell 1: Load dataset (27 papers)
   - Cell 2: Initialize text preprocessor
   - Cell 3: Define Vector Space Model
   - Cell 4: Preprocess all papers
   - Cell 5: Build TF-IDF model
   - Cell 6: Create user with reading history
   - Cell 7: Build user profile vector
   - Cell 8: Generate recommendations
   - Cell 9: View analysis

3. **Customize User Profile**
   ```python
   user = UserProfile(user_id="User_001")
   reading_history = [1, 6, 16, 22, 25]  # Modify as needed
   for doc_id in reading_history:
       user.add_to_history(doc_id)
   ```

4. **Get Recommendations**
   ```python
   recommendations = rec_engine.recommend_papers(user, top_k=5)
   ```

---

## 📚 Information Overload Reduction

### How the System Addresses Information Overload

**Problem**: Researchers face exponential growth in publications
- Hard to find relevant papers
- Too many irrelevant results
- Time-consuming manual search

**Solution**: Content-Based Recommendation

1. **Filtering**: Returns only relevant papers (70.4% coverage)
2. **Ranking**: Top-5 papers ranked by similarity
3. **Personalization**: User-specific recommendations
4. **Semantic Understanding**: Captures research domain
5. **Privacy**: No tracking of other users needed

**Result**: Researchers quickly find 5 most relevant papers to their interests

---

## 📄 Files in Assignment2

```
Assignment2/
├── Academic_Paper_Recommendation_System.ipynb  (Main implementation)
├── README.md                                    (This file)
├── dataset.py                                   (Optional: dataset utilities)
├── text_preprocessing.py                        (Optional: preprocessing module)
└── vector_space_model.py                        (Optional: VSM utilities)
```

---

## ✅ Requirements Met

### System Implementation (7 marks)
- ✅ **1. User Profile Construction**
  - Reading history maintained
  - Papers represented by title + abstract
  - All preprocessing steps implemented

- ✅ **2. Document Representation**
  - VSM implemented
  - TF-IDF with logarithmic term frequency
  - IDF weighting applied
  - Cosine normalization included

- ✅ **3. User Profiling**
  - Average TF-IDF vector computed
  - User profile represents research interests

- ✅ **4. Similarity & Ranking**
  - Cosine similarity between user profile and papers
  - All papers ranked
  - Top-5 papers displayed with scores

### Analysis & Comparative Reasoning (3 marks)
- ✅ **a) Recommendation Analysis**: Analyzed Top-5 papers and content-based filtering effectiveness
- ✅ **b) Content-Based Filtering Justification**: Explained why suitable for academic papers
- ✅ **c) Similarity Measure Justification**: Detailed why cosine similarity is ideal

---

## 🎓 Learning Outcomes

This project demonstrates:
1. Information retrieval fundamentals
2. Text preprocessing techniques
3. Vector space model implementation
4. TF-IDF computation from scratch
5. Cosine similarity in high dimensions
6. User profiling and personalization
7. Recommendation systems design
8. Content-based filtering principles

---

## 📖 References

### Concepts Implemented
- **Vector Space Model**: Salton et al. (1975)
- **TF-IDF**: Robertson (2004)
- **Cosine Similarity**: Singhal (2001)
- **Information Retrieval**: Manning et al. (2008)
- **Recommendation Systems**: Aggarwal (2016)

### Papers Analyzed
- All 27 papers in dataset represent major topics in Machine Learning
- Topics span from foundational concepts to cutting-edge research

---

## 🏆 Key Achievements

✨ **Complete Implementation**
- Manually implemented all core algorithms
- No external ML libraries (only built-ins)
- Efficient sparse vector operations

📊 **High-Quality Results**
- Meaningful Top-5 recommendations
- Good semantic alignment with user history
- Strong similarity score distribution

🔍 **Comprehensive Analysis**
- Mathematical justifications provided
- Comparative analysis with alternatives
- Performance metrics analyzed

🎯 **System Design**
- Modular, extensible architecture
- Clear separation of concerns
- Well-documented code

---

## 📝 Notes

1. **Scalability**: System efficiently handles 27 papers; scalable to thousands
2. **Customization**: Can easily add new papers to dataset
3. **User Profiles**: Can maintain multiple user profiles
4. **Performance**: Fast computation due to sparse vectors
5. **Privacy**: No external data or user tracking required

---

## 👨‍💻 Author

Assignment 2: Academic Paper Recommendation System  
Information Retrieval Course  
Using Vector Space Model with Manual TF-IDF Implementation

---

**Last Updated**: January 19, 2026
