NOTE: 
- I use chatGPT for faster pace of documenting this methodology
- Process of my approach:
    1. Before dive deep into data, I first need to understand the bussiness chain(the sound of animal in real life), and how AI can help the bussiness(break down and shorten the bussiness chain).
    2. Find if there are any existed/similar solution, which include of feature engineering, machine learning model, evaluation method on ML approach.
    3. Aggregate information and POC to stakeholder
    4. I start EDA the data (data distribution, cleaness-level of data, outlier ratio, missing data,...).
    5. Do the step 2 with coding
    6. launch the project
 
- In this task, we focus on step 2, 4 and 5
  

#*= Unsupervised Animal Sound Classification (ESC-50)
This project explores **unsupervised learning for animal voice classification** using the **ESC-50 environmental sound dataset**
We focus on **10 animal classes**, apply **MFCC feature engineering** , reduce dimensionality using **PCA**, and cluster sounds using **K-Means**, folowed by visualization and evaluation.
## .1 Dataset I - **Dataset**: ESC-50
**Sampling Rate**: Original sampling rate preserved ('sr=None) 
**Selected Classes**: 10 animal sound categories (e.g., dog, cat, bird, insect, frog, etc.)

2. Problem Definition
**Goal**:
   Cluster animal vocalizations into **10 groups** using **unsupervised learning**, based solely on acoustic similarity.
**Challenges**:
- Animal sounds vary in pitch, timbre, and noisiness
- No temporal rhythm like music
- High-dimensional audio features
## 3. Feature Engineering 
### 3.1 Selected Features ( we can choose 1 or many feature to do multiple task and aggregate latter)
| Feature | Purpose |
| **MFCC** | Compact timbral representation | 
| **A MFCC (Delta)** | Temporal dynamics |
| **ДД MFCC (Delta-Delta)** | Acceleration of spectral changes | 
| **Spectral Centroid** | Frequency "brightness" |
| **Spectral Bandwidth** | Tonal vs noisy spread |
| **Spectral Rolof** | High-frequency energy distribution | **Zero Crossing Rate** | Noisiness indicator |
| **RMS Energy** | Loudness and callstrength | 
| **Spectral Contrast** | Peak-valley structure |
>These features capture **frequency range**, **harmonic structure**, and **noise characteristics**
which are critical for distinguishing animal calls
---
### 3.2 Feature Aggregation
Since clustering algorithms require fixed-length vectors, frame-level features are summarized using popular methods:
- Mean/mode/median/std/etc...
This results in one feature vector per audio clip.

## 4. Feature Normalization (base on the features we gonna use)
All features are standardized using:
StandardScaler (zero mean, unit variance)
This prevents dominance of high-magnitude features
such as RMS or spectral rolloff.

## 5. Dimensionality
Reduction (PCA)
### 5.1 Motivation
Audio features extracted from animal sounds are mutiple dimentions
Dimensionality reduction is applied to:
- Reduce feature redundancy/noise impact
- Improve clustering stability
- Enable low-dimensional visualization
### 5.2 Method
-Algorithm: **Principal Component Analysis (PCA)**
- Applied after feature scaling
- Number of components selected to retain **90-95% of total variance theoretically**
PCA-transformed features are used as input for clustering.

## 6. Unsupervised Learning: K-Means Clustering
### 6.1 Clustering Objective
Group animal vocalizations based purely on **acoustic similarity** ,without
### 6.2 Algorithm
- Method: **K-Means**
- Number of clusters: k = 10
## 7. Cluster Visualization
After clustering, low-dimensional projections are used to visually inspect the structure of the learned clusters.
Feature vectors are projected into two- or three-dimensional space using PCA, enabling visual comparison between cluster assignments and ground-truth animal categories.
Visualization helps assess cluster separability, identify overlapping animal vocalizations, and detect outliers that may affect clustering performance.

 ## 8. Evaluation Strategy
Although the learning process is fully unsupervised, evaluation si
performed using
the known ESC-50 labels for analysis purposes only.
Since cluster indices have no inherent semantic meaning, an optimal
alignment between predicted clusters and true animal labels is computed before evaluation.
This alignment ensures that quantitative metrics reflect true clustering quality rather than arbitrary label ordering.
# 9. Evaluation Metrics
Clustering performance is measured using multiple standard metrics that capture different aspects of agreement between clusters and true labels.
These metrics provide both global and class-level insights into model behavior.
The following metrics are reported:
- Clustering Accuracy (after optimal label matching) (done)
- Adjusted Rand Index (ARI)
- Normalized Mutual Information (NMI)
- Confusion Matrix for error analysis
 
 ## 10. Results Analysis
The clustering results indicate that animal vocalizations with distinct acoustic signatures tend to form well-separated clusters with single feature engineering MFCC

## 11. Limitations
Several limitations are observed in the current methodology.
K-Means assumes spherical cluster structures and equal variance across clusters, which may not fully capture the complex distributions of natural sounds.
Additionally, temporal dynamics of animal calls are partially lost due to statistical feature aggregation, and short or low-energy events may be more difficult to cluster accurately.
## 12. Conclusion
 This project demonstrates an simple feature engineering, high-impact audio features combined with dimensionality reduction and K-Means clustering can effectively group animal vocalizations in an unsupervised setting.
Despite the simplicity of the approach, meaningful acoustic structure emerges in the clustering results, providing a strong baseline for future extensions involving more new research/approach audio representations.
