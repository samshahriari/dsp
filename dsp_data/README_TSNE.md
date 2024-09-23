
The two t-SNE components (or "axes" in the 2D plot) are derived from the high-dimensional features of your data. In this case, the t-SNE components are based on the Power Spectral Density (PSD) features from your EEG data. Here's a breakdown of what the two t-SNE components represent and the data they contain:

1. Input to t-SNE:
In your pipeline, you're using PSD data as the input for t-SNE. Here's the flow:

EEG Data: For each subject, you compute the PSD for each EEG channel (e.g., Fp1, Fp2, etc.) over different frequency bands.
Example frequency bands: delta (0.5-4 Hz), theta (4-8 Hz), alpha (8-12 Hz), beta (12-30 Hz), gamma (>30 Hz).
Feature Vector: You then aggregate the band power values across different channels, creating a feature vector that contains the power in each frequency band for each EEG channel.
For instance, if you have 19 EEG channels and 5 frequency bands (delta, theta, alpha, beta, gamma), the feature vector for each subject would contain 19 × 5 = 95, 19×5=95 features.
Input Matrix: The entire dataset is a matrix where each row represents a subject and each column represents a feature (frequency-band/channel combination).
Matrix size: 89 × 95
89×95 (89 subjects, each with 95 features).
2. How t-SNE Works:
t-SNE reduces the dimensionality of the 95-dimensional feature space (or however many features you have) to a 2D space while trying to preserve the relationships (or structure) between the data points:

Preserving Local Similarity: t-SNE tries to map the high-dimensional distances (relationships) between the feature vectors of each subject into the low-dimensional space (the 2D plot). Points that are close together in the high-dimensional space will ideally stay close together in the 2D t-SNE plot.

Nonlinear Dimensionality Reduction: Unlike methods like PCA (Principal Component Analysis), which reduce dimensions by finding linear correlations between features, t-SNE is a nonlinear technique. It focuses on maintaining the structure of local neighborhoods, so nearby points in high-dimensional space should remain near each other in the 2D projection.

3. What the Two t-SNE Components Represent:
t-SNE Component 1 and 2: These components are new dimensions that are created by t-SNE to represent the high-dimensional structure of your data in 2D.
They don’t correspond directly to any of the original EEG channels or frequency bands but rather summarize the relationships between subjects based on their PSD features.
Clusters in the t-SNE plot represent groups of subjects who have similar PSD characteristics across channels and frequency bands. Subjects close together in the plot likely have similar power distributions across the different EEG frequency bands.

4. Data Contained in the t-SNE Components:
The t-SNE components capture patterns based on PSD features. So the structure you see in the 2D space is based on the frequency-domain characteristics of the EEG data, which could reflect:
Variability in power within specific frequency bands (e.g., subjects with high alpha power might cluster together).
Differences between subjects in overall EEG activity patterns across the scalp (since each subject has data from 19 channels).
If you colored the points using metadata (e.g., age, group, MMSE score), you might start to see patterns where certain clusters correspond to specific cognitive or demographic traits.