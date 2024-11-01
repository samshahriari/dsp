# Channel selection
Alla körde sedan 50 epoker och 128 embedding size

## .5 s 100 samples


### Cz
#### Clip level
Training Accuracy: 0.45
printing results
Accuracy: 0.3688
Classification Report:
              precision    recall  f1-score   support

           0       0.40      0.73      0.52       700
           1       0.35      0.13      0.19       600
           2       0.19      0.10      0.13       400

    accuracy                           0.37      1700
   macro avg       0.31      0.32      0.28      1700
weighted avg       0.33      0.37      0.31      1700

Confusion Matrix:
[[511  91  98]
 [454  77  69]
 [307  54  39]]
stopped printing results

#### Subject level
{'sub-001': 0.71, 'sub-007': 0.67, 'sub-011': 0.75, 'sub-017': 0.77, 'sub-023': 0.72, 'sub-027': 0.65, 'sub-034': 0.84, 'sub-038': 0.14, 'sub-043': 0.1, 'sub-049': 0.13, 'sub-053': 0.17, 'sub-060': 0.13, 'sub-065': 0.1, 'sub-069': 0.03, 'sub-073': 0.14, 'sub-079': 0.08, 'sub-086': 0.14}
   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  71.0  16.0  13.0  
1     sub-007  tensor(0, dtype=torch.int32)       0  67.0   8.0  25.0  
2     sub-011  tensor(0, dtype=torch.int32)       0  75.0  11.0  14.0  
3     sub-017  tensor(0, dtype=torch.int32)       0  77.0  11.0  12.0  
4     sub-023  tensor(0, dtype=torch.int32)       0  72.0  17.0  11.0  
5     sub-027  tensor(0, dtype=torch.int32)       0  65.0  18.0  17.0  
6     sub-034  tensor(0, dtype=torch.int32)       0  84.0  10.0   6.0  
7     sub-038  tensor(1, dtype=torch.int32)       0  81.0  14.0   5.0  
8     sub-043  tensor(1, dtype=torch.int32)       0  70.0  10.0  20.0  
9     sub-049  tensor(1, dtype=torch.int32)       0  79.0  13.0   8.0  
10    sub-053  tensor(1, dtype=torch.int32)       0  74.0  17.0   9.0  
11    sub-060  tensor(1, dtype=torch.int32)       0  80.0  13.0   7.0  
12    sub-065  tensor(1, dtype=torch.int32)       0  70.0  10.0  20.0  
13    sub-069  tensor(2, dtype=torch.int32)       0  75.0  22.0   3.0  
14    sub-073  tensor(2, dtype=torch.int32)       0  78.0   8.0  14.0  
15    sub-079  tensor(2, dtype=torch.int32)       0  80.0  12.0   8.0  
16    sub-086  tensor(2, dtype=torch.int32)       0  74.0  12.0  14.0  

              precision    recall  f1-score   support

           0       0.41      1.00      0.58         7
           1       0.00      0.00      0.00         6
           2       0.00      0.00      0.00         4

    accuracy                           0.41        17
   macro avg       0.14      0.33      0.19        17
weighted avg       0.17      0.41      0.24        17

### CzT5
#### Clip level

Training Accuracy: 0.53
printing results
Accuracy: 0.4559
Classification Report:
              precision    recall  f1-score   support

           0       0.46      0.73      0.57       700
           1       0.59      0.35      0.44       600
           2       0.23      0.14      0.17       400

    accuracy                           0.46      1700
   macro avg       0.43      0.41      0.39      1700
weighted avg       0.45      0.46      0.43      1700

Confusion Matrix:
[[510  80 110]
 [314 209  77]
 [276  68  56]]
stopped printing results

#### Subject level

{'sub-001': 0.79, 'sub-007': 0.76, 'sub-011': 0.63, 'sub-017': 0.84, 'sub-023': 0.68, 'sub-027': 0.67, 'sub-034': 0.73, 'sub-038': 0.34, 'sub-043': 0.07, 'sub-049': 0.64, 'sub-053': 0.5, 'sub-060': 0.25, 'sub-065': 0.29, 'sub-069': 0.01, 'sub-073': 0.19, 'sub-079': 0.21, 'sub-086': 0.15}
   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  79.0   2.0  19.0  
1     sub-007  tensor(0, dtype=torch.int32)       0  76.0  10.0  14.0  
2     sub-011  tensor(0, dtype=torch.int32)       0  63.0  26.0  11.0  
3     sub-017  tensor(0, dtype=torch.int32)       0  84.0   7.0   9.0  
4     sub-023  tensor(0, dtype=torch.int32)       0  68.0  18.0  14.0  
5     sub-027  tensor(0, dtype=torch.int32)       0  67.0  11.0  22.0  
6     sub-034  tensor(0, dtype=torch.int32)       0  73.0   6.0  21.0  
7     sub-038  tensor(1, dtype=torch.int32)       0  54.0  34.0  12.0  
8     sub-043  tensor(1, dtype=torch.int32)       0  75.0   7.0  18.0  
9     sub-049  tensor(1, dtype=torch.int32)       1  25.0  64.0  11.0  
10    sub-053  tensor(1, dtype=torch.int32)       1  41.0  50.0   9.0  
11    sub-060  tensor(1, dtype=torch.int32)       0  68.0  25.0   7.0  
12    sub-065  tensor(1, dtype=torch.int32)       0  51.0  29.0  20.0  
13    sub-069  tensor(2, dtype=torch.int32)       0  87.0  12.0   1.0  
14    sub-073  tensor(2, dtype=torch.int32)       0  73.0   8.0  19.0  
15    sub-079  tensor(2, dtype=torch.int32)       0  55.0  24.0  21.0  
16    sub-086  tensor(2, dtype=torch.int32)       0  61.0  24.0  15.0  
              precision    recall  f1-score   support

           0       0.47      1.00      0.64         7
           1       1.00      0.33      0.50         6
           2       0.00      0.00      0.00         4

    accuracy                           0.53        17
   macro avg       0.49      0.44      0.38        17
weighted avg       0.55      0.53      0.44        17

### CzT5C4
#### Clip level

Training Accuracy: 0.53
printing results
Accuracy: 0.4388
Classification Report:
              precision    recall  f1-score   support

           0       0.45      0.70      0.55       700
           1       0.54      0.30      0.39       600
           2       0.27      0.18      0.22       400

    accuracy                           0.44      1700
   macro avg       0.42      0.40      0.38      1700
weighted avg       0.44      0.44      0.41      1700

Confusion Matrix:
[[492  91 117]
 [340 182  78]
 [263  65  72]]
stopped printing results
#### Subject level

{'sub-001': 0.7, 'sub-007': 0.79, 'sub-011': 0.56, 'sub-017': 0.83, 'sub-023': 0.6, 'sub-027': 0.78, 'sub-034': 0.66, 'sub-038': 0.18, 'sub-043': 0.13, 'sub-049': 0.65, 'sub-053': 0.48, 'sub-060': 0.07, 'sub-065': 0.31, 'sub-069': 0.01, 'sub-073': 0.25, 'sub-079': 0.27, 'sub-086': 0.19}
   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  70.0  10.0  20.0  
1     sub-007  tensor(0, dtype=torch.int32)       0  79.0   6.0  15.0  
2     sub-011  tensor(0, dtype=torch.int32)       0  56.0  30.0  14.0  
3     sub-017  tensor(0, dtype=torch.int32)       0  83.0   6.0  11.0  
4     sub-023  tensor(0, dtype=torch.int32)       0  60.0  25.0  15.0  
5     sub-027  tensor(0, dtype=torch.int32)       0  78.0  12.0  10.0  
6     sub-034  tensor(0, dtype=torch.int32)       0  66.0   2.0  32.0  
7     sub-038  tensor(1, dtype=torch.int32)       0  67.0  18.0  15.0  
8     sub-043  tensor(1, dtype=torch.int32)       0  63.0  13.0  24.0  
9     sub-049  tensor(1, dtype=torch.int32)       1  31.0  65.0   4.0  
10    sub-053  tensor(1, dtype=torch.int32)       1  46.0  48.0   6.0  
11    sub-060  tensor(1, dtype=torch.int32)       0  86.0   7.0   7.0  
12    sub-065  tensor(1, dtype=torch.int32)       0  47.0  31.0  22.0  
13    sub-069  tensor(2, dtype=torch.int32)       0  88.0  11.0   1.0  
14    sub-073  tensor(2, dtype=torch.int32)       0  62.0  13.0  25.0  
15    sub-079  tensor(2, dtype=torch.int32)       0  57.0  16.0  27.0  
16    sub-086  tensor(2, dtype=torch.int32)       0  56.0  25.0  19.0  

              precision    recall  f1-score   support

           0       0.47      1.00      0.64         7
           1       1.00      0.33      0.50         6
           2       0.00      0.00      0.00         4

    accuracy                           0.53        17
   macro avg       0.49      0.44      0.38        17
weighted avg       0.55      0.53      0.44        17



### CzT5C4T3
#### Clip level

Training Accuracy: 0.53
printing results
Accuracy: 0.4541
Classification Report:
              precision    recall  f1-score   support

           0       0.48      0.74      0.58       700
           1       0.52      0.29      0.37       600
           2       0.28      0.20      0.23       400

    accuracy                           0.45      1700
   macro avg       0.43      0.41      0.40      1700
weighted avg       0.45      0.45      0.43      1700

Confusion Matrix:
[[518  88  94]
 [310 173 117]
 [248  71  81]]
stopped printing results

#### Subject level

{'sub-001': 0.67, 'sub-007': 0.75, 'sub-011': 0.74, 'sub-017': 0.89, 'sub-023': 0.61, 'sub-027': 0.81, 'sub-034': 0.71, 'sub-038': 0.28, 'sub-043': 
0.04, 'sub-049': 0.52, 'sub-053': 0.36, 'sub-060': 0.27, 'sub-065': 0.26, 
'sub-069': 0.0, 'sub-073': 0.19, 'sub-079': 0.21, 'sub-086': 0.41}        
   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  67.0  12.0  21.0     
1     sub-007  tensor(0, dtype=torch.int32)       0  75.0   8.0  17.0     
2     sub-011  tensor(0, dtype=torch.int32)       0  74.0  21.0   5.0     
3     sub-017  tensor(0, dtype=torch.int32)       0  89.0   5.0   6.0     
4     sub-023  tensor(0, dtype=torch.int32)       0  61.0  24.0  15.0     
5     sub-027  tensor(0, dtype=torch.int32)       0  81.0   7.0  12.0     
6     sub-034  tensor(0, dtype=torch.int32)       0  71.0  11.0  18.0     
7     sub-038  tensor(1, dtype=torch.int32)       0  63.0  28.0   9.0     
8     sub-043  tensor(1, dtype=torch.int32)       2  47.0   4.0  49.0     
9     sub-049  tensor(1, dtype=torch.int32)       1  38.0  52.0  10.0     
10    sub-053  tensor(1, dtype=torch.int32)       0  49.0  36.0  15.0     
11    sub-060  tensor(1, dtype=torch.int32)       0  62.0  27.0  11.0     
12    sub-065  tensor(1, dtype=torch.int32)       0  51.0  26.0  23.0     
13    sub-069  tensor(2, dtype=torch.int32)       0  74.0  26.0   0.0     
14    sub-073  tensor(2, dtype=torch.int32)       0  62.0  19.0  19.0     
15    sub-079  tensor(2, dtype=torch.int32)       0  67.0  12.0  21.0     
16    sub-086  tensor(2, dtype=torch.int32)       0  45.0  14.0  41.0     
              precision    recall  f1-score   support

           0       0.47      1.00      0.64         7
           1       1.00      0.17      0.29         6
           2       0.00      0.00      0.00         4

    accuracy                           0.47        17
   macro avg       0.49      0.39      0.31        17
weighted avg       0.55      0.47      0.36        17
### CzT5C4T3Pz
#### Clip level

Training Accuracy: 0.54
printing results
Accuracy: 0.4382
Classification Report:
              precision    recall  f1-score   support

           0       0.46      0.68      0.55       700
           1       0.55      0.31      0.40       600
           2       0.26      0.21      0.24       400

    accuracy                           0.44      1700
   macro avg       0.42      0.40      0.39      1700
weighted avg       0.45      0.44      0.42      1700

Confusion Matrix:
[[474  88 138]
 [311 185 104]
 [253  61  86]]
stopped printing results

#### Subject level

{'sub-001': 0.59, 'sub-007': 0.73, 'sub-011': 0.68, 'sub-017': 0.78, 'sub-023': 0.6, 'sub-027': 0.68, 'sub-034': 0.68, 'sub-038': 0.27, 'sub-043': 0.12, 'sub-049': 0.55, 'sub-053': 0.46, 'sub-060': 0.15, 'sub-065': 0.3, 'sub-069': 0.02, 'sub-073': 0.13, 'sub-079': 0.22, 'sub-086': 0.49}
   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  59.0  12.0  29.0     
1     sub-007  tensor(0, dtype=torch.int32)       0  73.0   7.0  20.0     
2     sub-011  tensor(0, dtype=torch.int32)       0  68.0  23.0   9.0     
3     sub-017  tensor(0, dtype=torch.int32)       0  78.0   6.0  16.0     
4     sub-023  tensor(0, dtype=torch.int32)       0  60.0  25.0  15.0     
5     sub-027  tensor(0, dtype=torch.int32)       0  68.0   6.0  26.0     
6     sub-034  tensor(0, dtype=torch.int32)       0  68.0   9.0  23.0     
7     sub-038  tensor(1, dtype=torch.int32)       0  62.0  27.0  11.0     
8     sub-043  tensor(1, dtype=torch.int32)       0  54.0  12.0  34.0     
9     sub-049  tensor(1, dtype=torch.int32)       1  30.0  55.0  15.0     
10    sub-053  tensor(1, dtype=torch.int32)       1  40.0  46.0  14.0     
11    sub-060  tensor(1, dtype=torch.int32)       0  70.0  15.0  15.0     
12    sub-065  tensor(1, dtype=torch.int32)       0  55.0  30.0  15.0     
13    sub-069  tensor(2, dtype=torch.int32)       0  77.0  21.0   2.0     
14    sub-073  tensor(2, dtype=torch.int32)       0  74.0  13.0  13.0     
15    sub-079  tensor(2, dtype=torch.int32)       0  53.0  25.0  22.0     
16    sub-086  tensor(2, dtype=torch.int32)       0  49.0   2.0  49.0     

              precision    recall  f1-score   support

           0       0.47      1.00      0.64         7
           1       1.00      0.33      0.50         6
           2       0.00      0.00      0.00         4

    accuracy                           0.53        17
   macro avg       0.49      0.44      0.38        17
weighted avg       0.55      0.53      0.44        17


### CzT5C4T3PzP4
#### Clip level

Training Accuracy: 0.54
printing results
Accuracy: 0.4312
Classification Report:
              precision    recall  f1-score   support

           0       0.47      0.69      0.56       700
           1       0.49      0.28      0.35       600
           2       0.26      0.22      0.24       400

    accuracy                           0.43      1700
   macro avg       0.40      0.39      0.38      1700
weighted avg       0.43      0.43      0.41      1700

Confusion Matrix:
[[481  97 122]
 [306 165 129]
 [236  77  87]]
stopped printing results

#### Subject level

{'sub-001': 0.64, 'sub-007': 0.77, 'sub-011': 0.6, 'sub-017': 0.83, 'sub-023': 0.57, 'sub-027': 0.77, 'sub-034': 0.63, 'sub-038': 0.25, 'sub-043': 0.1, 'sub-049': 0.54, 'sub-053': 0.36, 'sub-060': 0.18, 'sub-065': 0.22, 'sub-069': 0.08, 'sub-073': 0.22, 'sub-079': 0.26, 'sub-086': 0.31}
   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  64.0  17.0  19.0     
1     sub-007  tensor(0, dtype=torch.int32)       0  77.0   5.0  18.0     
2     sub-011  tensor(0, dtype=torch.int32)       0  60.0  28.0  12.0     
3     sub-017  tensor(0, dtype=torch.int32)       0  83.0   7.0  10.0     
4     sub-023  tensor(0, dtype=torch.int32)       0  57.0  22.0  21.0     
5     sub-027  tensor(0, dtype=torch.int32)       0  77.0   7.0  16.0     
6     sub-034  tensor(0, dtype=torch.int32)       0  63.0  11.0  26.0     
7     sub-038  tensor(1, dtype=torch.int32)       0  67.0  25.0   8.0     
8     sub-043  tensor(1, dtype=torch.int32)       0  47.0  10.0  43.0     
9     sub-049  tensor(1, dtype=torch.int32)       1  35.0  54.0  11.0     
10    sub-053  tensor(1, dtype=torch.int32)       0  46.0  36.0  18.0     
11    sub-060  tensor(1, dtype=torch.int32)       0  61.0  18.0  21.0     
12    sub-065  tensor(1, dtype=torch.int32)       0  50.0  22.0  28.0     
13    sub-069  tensor(2, dtype=torch.int32)       0  65.0  27.0   8.0     
14    sub-073  tensor(2, dtype=torch.int32)       0  69.0   9.0  22.0     
15    sub-079  tensor(2, dtype=torch.int32)       0  45.0  29.0  26.0     
16    sub-086  tensor(2, dtype=torch.int32)       0  57.0  12.0  31.0     
              precision    recall  f1-score   support

           0       0.44      1.00      0.61         7
           1       1.00      0.17      0.29         6
           2       0.00      0.00      0.00         4

    accuracy                           0.47        17
   macro avg       0.48      0.39      0.30        17
weighted avg       0.53      0.47      0.35        17

### CzT5C4T3PzP4P3
#### Clip level

Training Accuracy: 0.53
printing results
Accuracy: 0.4406
Classification Report:
              precision    recall  f1-score   support

           0       0.46      0.73      0.56       700
           1       0.53      0.29      0.37       600
           2       0.25      0.17      0.20       400

    accuracy                           0.44      1700
   macro avg       0.42      0.39      0.38      1700
weighted avg       0.44      0.44      0.41      1700

Confusion Matrix:
[[509  97  94]
 [324 173 103]
 [279  54  67]]
stopped printing results

#### Subject level

{'sub-001': 0.82, 'sub-007': 0.81, 'sub-011': 0.68, 'sub-017': 0.83, 'sub-023': 0.58, 'sub-027': 0.75, 'sub-034': 0.62, 'sub-038': 0.22, 'sub-043': 
0.14, 'sub-049': 0.44, 'sub-053': 0.43, 'sub-060': 0.2, 'sub-065': 0.3, 'sub-069': 0.03, 'sub-073': 0.21, 'sub-079': 0.18, 'sub-086': 0.25}
   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  82.0  11.0   7.0     
1     sub-007  tensor(0, dtype=torch.int32)       0  81.0   5.0  14.0     
2     sub-011  tensor(0, dtype=torch.int32)       0  68.0  21.0  11.0     
3     sub-017  tensor(0, dtype=torch.int32)       0  83.0  11.0   6.0     
4     sub-023  tensor(0, dtype=torch.int32)       0  58.0  24.0  18.0     
5     sub-027  tensor(0, dtype=torch.int32)       0  75.0  10.0  15.0     
6     sub-034  tensor(0, dtype=torch.int32)       0  62.0  15.0  23.0     
7     sub-038  tensor(1, dtype=torch.int32)       0  67.0  22.0  11.0     
8     sub-043  tensor(1, dtype=torch.int32)       0  47.0  14.0  39.0     
9     sub-049  tensor(1, dtype=torch.int32)       0  51.0  44.0   5.0     
10    sub-053  tensor(1, dtype=torch.int32)       0  47.0  43.0  10.0     
11    sub-060  tensor(1, dtype=torch.int32)       0  64.0  20.0  16.0     
12    sub-065  tensor(1, dtype=torch.int32)       0  48.0  30.0  22.0     
13    sub-069  tensor(2, dtype=torch.int32)       0  87.0  10.0   3.0     
14    sub-073  tensor(2, dtype=torch.int32)       0  67.0  12.0  21.0     
15    sub-079  tensor(2, dtype=torch.int32)       0  62.0  20.0  18.0     
16    sub-086  tensor(2, dtype=torch.int32)       0  63.0  12.0  25.0     

              precision    recall  f1-score   support

           0       0.41      1.00      0.58         7
           1       0.00      0.00      0.00         6
           2       0.00      0.00      0.00         4

    accuracy                           0.41        17
   macro avg       0.14      0.33      0.19        17
weighted avg       0.17      0.41      0.24        17

## 2 second clips 100 samples
### Cz
#### Clip level

Training Accuracy: 0.45
printing results
Accuracy: 0.3488
Classification Report:
              precision    recall  f1-score   support

           0       0.39      0.69      0.50       700
           1       0.32      0.13      0.18       600
           2       0.14      0.09      0.11       400

    accuracy                           0.35      1700
   macro avg       0.29      0.30      0.26      1700
weighted avg       0.31      0.35      0.30      1700

Confusion Matrix:
[[482  98 120]
 [441  77  82]
 [300  66  34]]
stopped printing results

#### Subject level

{'sub-001': 0.69, 'sub-007': 0.68, 'sub-011': 0.71, 'sub-017': 0.71, 'sub-023': 0.78, 'sub-027': 0.48, 'sub-034': 0.77, 'sub-038': 0.14, 'sub-043': 
0.05, 'sub-049': 0.19, 'sub-053': 0.14, 'sub-060': 0.12, 'sub-065': 0.13, 
'sub-069': 0.0, 'sub-073': 0.14, 'sub-081': 0.15, 'sub-085': 0.05}        
   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  69.0  12.0  19.0     
1     sub-007  tensor(0, dtype=torch.int32)       0  68.0  18.0  14.0     
2     sub-011  tensor(0, dtype=torch.int32)       0  71.0  15.0  14.0     
3     sub-017  tensor(0, dtype=torch.int32)       0  71.0  16.0  13.0     
4     sub-023  tensor(0, dtype=torch.int32)       0  78.0  10.0  12.0     
5     sub-027  tensor(0, dtype=torch.int32)       0  48.0  21.0  31.0     
6     sub-034  tensor(0, dtype=torch.int32)       0  77.0   6.0  17.0     
7     sub-038  tensor(1, dtype=torch.int32)       0  75.0  14.0  11.0     
8     sub-043  tensor(1, dtype=torch.int32)       0  78.0   5.0  17.0     
9     sub-049  tensor(1, dtype=torch.int32)       0  64.0  19.0  17.0     
10    sub-053  tensor(1, dtype=torch.int32)       0  76.0  14.0  10.0     
11    sub-060  tensor(1, dtype=torch.int32)       0  83.0  12.0   5.0     
12    sub-065  tensor(1, dtype=torch.int32)       0  65.0  13.0  22.0     
13    sub-069  tensor(2, dtype=torch.int32)       0  56.0  44.0   0.0     
14    sub-073  tensor(2, dtype=torch.int32)       0  83.0   3.0  14.0     
15    sub-081  tensor(2, dtype=torch.int32)       0  77.0   8.0  15.0     
16    sub-085  tensor(2, dtype=torch.int32)       0  84.0  11.0   5.0     

              precision    recall  f1-score   support

           0       0.41      1.00      0.58         7
           1       0.00      0.00      0.00         6
           2       0.00      0.00      0.00         4

    accuracy                           0.41        17
   macro avg       0.14      0.33      0.19        17
weighted avg       0.17      0.41      0.24        17

### CzT5
#### Clip level

Training Accuracy: 0.56
printing results
Accuracy: 0.4976
Classification Report:
              precision    recall  f1-score   support

           0       0.48      0.82      0.61       700
           1       0.75      0.37      0.50       600
           2       0.23      0.12      0.16       400

    accuracy                           0.50      1700
   macro avg       0.49      0.44      0.42      1700
weighted avg       0.52      0.50      0.46      1700

Confusion Matrix:
[[574  54  72]
 [284 224  92]
 [331  21  48]]
stopped printing results

#### Subject level

{'sub-001': 0.82, 'sub-007': 0.96, 'sub-011': 0.55, 'sub-017': 0.98, 'sub-023': 0.71, 'sub-027': 0.89, 'sub-034': 0.83, 'sub-038': 0.36, 'sub-043': 
0.03, 'sub-049': 0.77, 'sub-053': 0.65, 'sub-060': 0.06, 'sub-065': 0.37, 
'sub-069': 0.0, 'sub-073': 0.23, 'sub-081': 0.14, 'sub-085': 0.11}        
   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  82.0   1.0  17.0     
1     sub-007  tensor(0, dtype=torch.int32)       0  96.0   0.0   4.0     
2     sub-011  tensor(0, dtype=torch.int32)       0  55.0  31.0  14.0     
3     sub-017  tensor(0, dtype=torch.int32)       0  98.0   0.0   2.0     
4     sub-023  tensor(0, dtype=torch.int32)       0  71.0  21.0   8.0     
5     sub-027  tensor(0, dtype=torch.int32)       0  89.0   0.0  11.0     
6     sub-034  tensor(0, dtype=torch.int32)       0  83.0   1.0  16.0     
7     sub-038  tensor(1, dtype=torch.int32)       0  51.0  36.0  13.0     
8     sub-043  tensor(1, dtype=torch.int32)       0  74.0   3.0  23.0     
9     sub-049  tensor(1, dtype=torch.int32)       1  18.0  77.0   5.0     
10    sub-053  tensor(1, dtype=torch.int32)       1  29.0  65.0   6.0     
11    sub-060  tensor(1, dtype=torch.int32)       0  80.0   6.0  14.0     
12    sub-065  tensor(1, dtype=torch.int32)       1  32.0  37.0  31.0     
13    sub-069  tensor(2, dtype=torch.int32)       0  85.0  15.0   0.0     
14    sub-073  tensor(2, dtype=torch.int32)       0  72.0   5.0  23.0     
15    sub-081  tensor(2, dtype=torch.int32)       0  85.0   1.0  14.0     
16    sub-085  tensor(2, dtype=torch.int32)       0  89.0   0.0  11.0     

              precision    recall  f1-score   support

           0       0.50      1.00      0.67         7
           1       1.00      0.50      0.67         6
           2       0.00      0.00      0.00         4

    accuracy                           0.59        17
   macro avg       0.50      0.50      0.44        17
weighted avg       0.56      0.59      0.51        17

### CzT5C4
#### Clip level

Training Accuracy: 0.56
printing results
Accuracy: 0.4665
Classification Report:
              precision    recall  f1-score   support

           0       0.47      0.75      0.58       700
           1       0.60      0.29      0.40       600
           2       0.32      0.22      0.26       400

    accuracy                           0.47      1700
   macro avg       0.46      0.42      0.41      1700
weighted avg       0.48      0.47      0.44      1700

Confusion Matrix:
[[527  74  99]
 [334 177  89]
 [269  42  89]]
stopped printing results

#### Subject level

{'sub-001': 0.66, 'sub-007': 0.91, 'sub-011': 0.51, 'sub-017': 0.91, 'sub-023': 0.63, 'sub-027': 0.89, 'sub-034': 0.76, 'sub-038': 0.17, 'sub-043': 
0.01, 'sub-049': 0.74, 'sub-053': 0.59, 'sub-060': 0.04, 'sub-065': 0.22, 
'sub-069': 0.0, 'sub-073': 0.36, 'sub-081': 0.34, 'sub-085': 0.19}        
   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  66.0   2.0  32.0     
1     sub-007  tensor(0, dtype=torch.int32)       0  91.0   2.0   7.0     
2     sub-011  tensor(0, dtype=torch.int32)       0  51.0  39.0  10.0     
3     sub-017  tensor(0, dtype=torch.int32)       0  91.0   3.0   6.0     
4     sub-023  tensor(0, dtype=torch.int32)       0  63.0  21.0  16.0     
5     sub-027  tensor(0, dtype=torch.int32)       0  89.0   6.0   5.0     
6     sub-034  tensor(0, dtype=torch.int32)       0  76.0   1.0  23.0     
7     sub-038  tensor(1, dtype=torch.int32)       0  72.0  17.0  11.0     
8     sub-043  tensor(1, dtype=torch.int32)       0  75.0   1.0  24.0     
9     sub-049  tensor(1, dtype=torch.int32)       1  20.0  74.0   6.0     
10    sub-053  tensor(1, dtype=torch.int32)       1  38.0  59.0   3.0     
11    sub-060  tensor(1, dtype=torch.int32)       0  87.0   4.0   9.0     
12    sub-065  tensor(1, dtype=torch.int32)       0  42.0  22.0  36.0     
13    sub-069  tensor(2, dtype=torch.int32)       0  68.0  32.0   0.0     
14    sub-073  tensor(2, dtype=torch.int32)       0  57.0   7.0  36.0     
15    sub-081  tensor(2, dtype=torch.int32)       0  65.0   1.0  34.0     
16    sub-085  tensor(2, dtype=torch.int32)       0  79.0   2.0  19.0     

              precision    recall  f1-score   support

           0       0.47      1.00      0.64         7
           1       1.00      0.33      0.50         6
           2       0.00      0.00      0.00         4

    accuracy                           0.53        17
   macro avg       0.49      0.44      0.38        17
weighted avg       0.55      0.53      0.44        17

### CzT5C4T3
#### Clip level
Training Accuracy: 0.60
printing results
Accuracy: 0.4806
Classification Report:
              precision    recall  f1-score   support

           0       0.49      0.75      0.59       700
           1       0.74      0.40      0.52       600
           2       0.18      0.14      0.16       400

    accuracy                           0.48      1700
   macro avg       0.47      0.43      0.42      1700
weighted avg       0.50      0.48      0.46      1700

Confusion Matrix:
[[524  60 116]
 [232 238 130]
 [321  24  55]]
stopped printing results

#### Subject level

{'sub-001': 0.47, 'sub-007': 0.9, 'sub-011': 0.66, 'sub-017': 0.97, 'sub-023': 0.54, 'sub-027': 0.88, 'sub-034': 0.82, 'sub-038': 0.45, 'sub-043': 0.07, 'sub-049': 0.74, 'sub-053': 0.39, 'sub-060': 0.26, 'sub-065': 0.47, 'sub-069': 0.0, 'sub-073': 0.22, 'sub-081': 0.19, 'sub-085': 0.14}
   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       2  47.0   3.0  50.0       
1     sub-007  tensor(0, dtype=torch.int32)       0  90.0   5.0   5.0       
2     sub-011  tensor(0, dtype=torch.int32)       0  66.0  27.0   7.0       
3     sub-017  tensor(0, dtype=torch.int32)       0  97.0   2.0   1.0       
4     sub-023  tensor(0, dtype=torch.int32)       0  54.0  18.0  28.0       
5     sub-027  tensor(0, dtype=torch.int32)       0  88.0   2.0  10.0       
6     sub-034  tensor(0, dtype=torch.int32)       0  82.0   3.0  15.0       
7     sub-038  tensor(1, dtype=torch.int32)       0  48.0  45.0   7.0       
8     sub-043  tensor(1, dtype=torch.int32)       2  38.0   7.0  55.0       
9     sub-049  tensor(1, dtype=torch.int32)       1  13.0  74.0  13.0       
10    sub-053  tensor(1, dtype=torch.int32)       0  48.0  39.0  13.0       
11    sub-060  tensor(1, dtype=torch.int32)       0  51.0  26.0  23.0       
12    sub-065  tensor(1, dtype=torch.int32)       1  34.0  47.0  19.0       
13    sub-069  tensor(2, dtype=torch.int32)       0  94.0   6.0   0.0       
14    sub-073  tensor(2, dtype=torch.int32)       0  70.0   8.0  22.0       
15    sub-081  tensor(2, dtype=torch.int32)       0  80.0   1.0  19.0       
16    sub-085  tensor(2, dtype=torch.int32)       0  77.0   9.0  14.0       
              precision    recall  f1-score   support

           0       0.46      0.86      0.60         7
           1       1.00      0.33      0.50         6
           2       0.00      0.00      0.00         4

    accuracy                           0.47        17
   macro avg       0.49      0.40      0.37        17
weighted avg       0.54      0.47      0.42        17

### CzT5C4T3Pz
#### Clip level
Training Accuracy: 0.61
printing results
Accuracy: 0.5206
Classification Report:
              precision    recall  f1-score   support

           0       0.49      0.83      0.62       700
           1       0.77      0.43      0.55       600
           2       0.26      0.12      0.16       400

    accuracy                           0.52      1700
   macro avg       0.51      0.46      0.44      1700
weighted avg       0.53      0.52      0.49      1700

Confusion Matrix:
[[580  56  64]
 [270 257  73]
 [331  21  48]]
stopped printing results
#### Subject level

{'sub-001': 0.72, 'sub-007': 0.95, 'sub-011': 0.72, 'sub-017': 0.95, 'sub-023': 0.65, 'sub-027': 0.95, 'sub-034': 0.86, 'sub-038': 0.45, 'sub-043': 0.05, 'sub-049': 0.83, 'sub-053': 0.58, 'sub-060': 0.25, 'sub-065': 0.41, 'sub-069': 0.0, 'sub-073': 0.23, 'sub-081': 0.13, 'sub-085': 0.12}
   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  72.0   3.0  25.0       
1     sub-007  tensor(0, dtype=torch.int32)       0  95.0   2.0   3.0       
2     sub-011  tensor(0, dtype=torch.int32)       0  72.0  24.0   4.0       
3     sub-017  tensor(0, dtype=torch.int32)       0  95.0   4.0   1.0       
4     sub-023  tensor(0, dtype=torch.int32)       0  65.0  22.0  13.0       
5     sub-027  tensor(0, dtype=torch.int32)       0  95.0   1.0   4.0       
6     sub-034  tensor(0, dtype=torch.int32)       0  86.0   0.0  14.0       
7     sub-038  tensor(1, dtype=torch.int32)       0  51.0  45.0   4.0       
8     sub-043  tensor(1, dtype=torch.int32)       0  63.0   5.0  32.0       
9     sub-049  tensor(1, dtype=torch.int32)       1  13.0  83.0   4.0       
10    sub-053  tensor(1, dtype=torch.int32)       1  36.0  58.0   6.0       
11    sub-060  tensor(1, dtype=torch.int32)       0  63.0  25.0  12.0       
12    sub-065  tensor(1, dtype=torch.int32)       0  44.0  41.0  15.0       
13    sub-069  tensor(2, dtype=torch.int32)       0  96.0   4.0   0.0       
14    sub-073  tensor(2, dtype=torch.int32)       0  69.0   8.0  23.0       
15    sub-081  tensor(2, dtype=torch.int32)       0  86.0   1.0  13.0       
16    sub-085  tensor(2, dtype=torch.int32)       0  80.0   8.0  12.0       
              precision    recall  f1-score   support

           0       0.47      1.00      0.64         7
           1       1.00      0.33      0.50         6
           2       0.00      0.00      0.00         4

    accuracy                           0.53        17
   macro avg       0.49      0.44      0.38        17
weighted avg       0.55      0.53      0.44        17

### CzT5C4T3PzP4
#### Clip level
Training Accuracy: 0.59
printing results
Accuracy: 0.4441
Classification Report:
              precision    recall  f1-score   support

           0       0.47      0.70      0.56       700
           1       0.66      0.33      0.44       600
           2       0.19      0.16      0.17       400

    accuracy                           0.44      1700
   macro avg       0.44      0.40      0.39      1700
weighted avg       0.47      0.44      0.43      1700

Confusion Matrix:
[[492  65 143]
 [267 198 135]
 [299  36  65]]
stopped printing results
{'sub-001': 0.61, 'sub-007': 0.64, 'sub-011': 0.68, 'sub-017': 0.9, 'sub-023': 0.59, 'sub-027': 0.78, 'sub-034': 0.72, 'sub-038': 0.3, 'sub-043': 0.07, 
'sub-049': 0.64, 'sub-053': 0.57, 'sub-060': 0.09, 'sub-065': 0.31, 'sub-069': 0.02, 'sub-073': 0.22, 'sub-081': 0.27, 'sub-085': 0.14}
   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  61.0   4.0  35.0       
1     sub-007  tensor(0, dtype=torch.int32)       0  64.0  10.0  26.0       
2     sub-011  tensor(0, dtype=torch.int32)       0  68.0  19.0  13.0       
3     sub-017  tensor(0, dtype=torch.int32)       0  90.0   6.0   4.0       
4     sub-023  tensor(0, dtype=torch.int32)       0  59.0  20.0  21.0       
5     sub-027  tensor(0, dtype=torch.int32)       0  78.0   5.0  17.0       
6     sub-034  tensor(0, dtype=torch.int32)       0  72.0   1.0  27.0       
7     sub-038  tensor(1, dtype=torch.int32)       0  59.0  30.0  11.0       
8     sub-043  tensor(1, dtype=torch.int32)       2  42.0   7.0  51.0       
9     sub-049  tensor(1, dtype=torch.int32)       1  26.0  64.0  10.0       
10    sub-053  tensor(1, dtype=torch.int32)       1  32.0  57.0  11.0       
11    sub-060  tensor(1, dtype=torch.int32)       0  73.0   9.0  18.0       
12    sub-065  tensor(1, dtype=torch.int32)       0  35.0  31.0  34.0       
13    sub-069  tensor(2, dtype=torch.int32)       0  78.0  20.0   2.0       
14    sub-073  tensor(2, dtype=torch.int32)       0  70.0   8.0  22.0       
15    sub-081  tensor(2, dtype=torch.int32)       0  71.0   2.0  27.0       
16    sub-085  tensor(2, dtype=torch.int32)       0  80.0   6.0  14.0       
              precision    recall  f1-score   support

           0       0.50      1.00      0.67         7
           1       1.00      0.33      0.50         6
           2       0.00      0.00      0.00         4

    accuracy                           0.53        17
   macro avg       0.50      0.44      0.39        17
weighted avg       0.56      0.53      0.45        17

### CzT5C4T3PzP4P3
#### Clip level
Training Accuracy: 0.58
printing results
Accuracy: 0.5041
Classification Report:
              precision    recall  f1-score   support

           0       0.49      0.76      0.59       700
           1       0.68      0.40      0.50       600
           2       0.34      0.22      0.27       400

    accuracy                           0.50      1700
   macro avg       0.50      0.46      0.45      1700
weighted avg       0.52      0.50      0.48      1700

Confusion Matrix:
[[531  86  83]
 [273 238  89]
 [284  28  88]]
stopped printing results
{'sub-001': 0.78, 'sub-007': 0.8, 'sub-011': 0.59, 'sub-017': 0.95, 'sub-023': 0.66, 'sub-027': 0.82, 'sub-034': 0.71, 'sub-038': 0.51, 'sub-043': 0.1, 
'sub-049': 0.71, 'sub-053': 0.56, 'sub-060': 0.15, 'sub-065': 0.35, 'sub-069': 0.12, 'sub-073': 0.33, 'sub-081': 0.29, 'sub-085': 0.14}
   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  78.0  12.0  10.0       
1     sub-007  tensor(0, dtype=torch.int32)       0  80.0   4.0  16.0       
2     sub-011  tensor(0, dtype=torch.int32)       0  59.0  33.0   8.0       
3     sub-017  tensor(0, dtype=torch.int32)       0  95.0   5.0   0.0       
4     sub-023  tensor(0, dtype=torch.int32)       0  66.0  18.0  16.0       
5     sub-027  tensor(0, dtype=torch.int32)       0  82.0   5.0  13.0       
6     sub-034  tensor(0, dtype=torch.int32)       0  71.0   9.0  20.0       
7     sub-038  tensor(1, dtype=torch.int32)       1  46.0  51.0   3.0       
8     sub-043  tensor(1, dtype=torch.int32)       0  49.0  10.0  41.0       
9     sub-049  tensor(1, dtype=torch.int32)       1  24.0  71.0   5.0       
10    sub-053  tensor(1, dtype=torch.int32)       1  39.0  56.0   5.0       
11    sub-060  tensor(1, dtype=torch.int32)       0  73.0  15.0  12.0       
12    sub-065  tensor(1, dtype=torch.int32)       0  42.0  35.0  23.0       
13    sub-069  tensor(2, dtype=torch.int32)       0  71.0  17.0  12.0       
14    sub-073  tensor(2, dtype=torch.int32)       0  62.0   5.0  33.0       
15    sub-081  tensor(2, dtype=torch.int32)       0  67.0   4.0  29.0       
16    sub-085  tensor(2, dtype=torch.int32)       0  84.0   2.0  14.0       
              precision    recall  f1-score   support

           0       0.50      1.00      0.67         7
           1       1.00      0.50      0.67         6
           2       0.00      0.00      0.00         4

    accuracy                           0.59        17
   macro avg       0.50      0.50      0.44        17
weighted avg       0.56      0.59      0.51        17

### 100-2Fp1CzPzT5
Training Accuracy: 0.60
printing results
Accuracy: 0.4894
Classification Report:
              precision    recall  f1-score   support

           0       0.50      0.80      0.62       700
           1       0.60      0.36      0.45       600
           2       0.25      0.14      0.18       400

    accuracy                           0.49      1700
   macro avg       0.45      0.43      0.42      1700
weighted avg       0.48      0.49      0.46      1700

Confusion Matrix:
[[558  83  59]
 [273 219 108]
 [280  65  55]]
stopped printing results
{'sub-001': 0.91, 'sub-007': 0.91, 'sub-011': 0.37, 'sub-017': 0.97, 'sub-023': 0.68, 'sub-027': 0.93, 'sub-034': 0.81, 'sub-038': 0.53, 'sub-043': 0.18, 'sub-049': 0.59, 'sub-053': 0.66, 'sub-060': 0.11, 'sub-065': 0.12, 'sub-069': 0.01, 'sub-073': 0.11, 'sub-081': 0.15, 'sub-085': 
0.28}
   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  91.0   2.0   7.0  
1     sub-007  tensor(0, dtype=torch.int32)       0  91.0   5.0   4.0  
2     sub-011  tensor(0, dtype=torch.int32)       1  37.0  44.0  19.0  
3     sub-017  tensor(0, dtype=torch.int32)       0  97.0   3.0   0.0  
4     sub-023  tensor(0, dtype=torch.int32)       0  68.0  17.0  15.0  
5     sub-027  tensor(0, dtype=torch.int32)       0  93.0   5.0   2.0  
6     sub-034  tensor(0, dtype=torch.int32)       0  81.0   7.0  12.0  
7     sub-038  tensor(1, dtype=torch.int32)       1  42.0  53.0   5.0  
8     sub-043  tensor(1, dtype=torch.int32)       0  60.0  18.0  22.0  
9     sub-049  tensor(1, dtype=torch.int32)       1  35.0  59.0   6.0  
10    sub-053  tensor(1, dtype=torch.int32)       1  20.0  66.0  14.0  
11    sub-060  tensor(1, dtype=torch.int32)       0  86.0  11.0   3.0  
12    sub-065  tensor(1, dtype=torch.int32)       2  30.0  12.0  58.0  
13    sub-069  tensor(2, dtype=torch.int32)       0  56.0  43.0   1.0  
14    sub-073  tensor(2, dtype=torch.int32)       0  74.0  15.0  11.0  
15    sub-081  tensor(2, dtype=torch.int32)       0  81.0   4.0  15.0  
16    sub-085  tensor(2, dtype=torch.int32)       0  69.0   3.0  28.0  
              precision    recall  f1-score   support

           0       0.50      0.86      0.63         7
           1       0.75      0.50      0.60         6
           2       0.00      0.00      0.00         4

    accuracy                           0.53        17
   macro avg       0.42      0.45      0.41        17
weighted avg       0.47      0.53      0.47        17
## 2 seconds 50 samples
### 50-2CzT5C4T3Pz
### 50-2CzT5C4T3PzP4
Training Accuracy: 0.61
printing results
Accuracy: 0.5212
Classification Report:
              precision    recall  f1-score   support

           0       0.50      0.75      0.60       350
           1       0.72      0.49      0.58       300
           2       0.26      0.16      0.20       200

    accuracy                           0.52       850
   macro avg       0.50      0.47      0.46       850
weighted avg       0.52      0.52      0.50       850

Confusion Matrix:
[[264  33  53]
 [117 147  36]
 [143  25  32]]
stopped printing results
{'sub-001': 0.7, 'sub-007': 0.66, 'sub-011': 0.76, 'sub-017': 0.96, 'sub-023': 0.58, 'sub-027': 0.86, 'sub-034': 0.76, 'sub-039': 0.66, 'sub-045': 0.12, 'sub-049': 0.68, 'sub-054': 0.74, 'sub-060': 0.22, 'sub-065': 0.52, 'sub-069': 0.0, 'sub-073': 0.32, 'sub-079': 0.18, 'sub-085': 0.14}
   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  35.0   5.0  10.0  
1     sub-007  tensor(0, dtype=torch.int32)       0  33.0   4.0  13.0  
2     sub-011  tensor(0, dtype=torch.int32)       0  38.0   7.0   5.0  
3     sub-017  tensor(0, dtype=torch.int32)       0  48.0   1.0   1.0  
4     sub-023  tensor(0, dtype=torch.int32)       0  29.0  13.0   8.0  
5     sub-027  tensor(0, dtype=torch.int32)       0  43.0   2.0   5.0  
6     sub-034  tensor(0, dtype=torch.int32)       0  38.0   1.0  11.0  
7     sub-039  tensor(1, dtype=torch.int32)       1  17.0  33.0   0.0  
8     sub-045  tensor(1, dtype=torch.int32)       0  35.0   6.0   9.0  
9     sub-049  tensor(1, dtype=torch.int32)       1   7.0  34.0   9.0  
10    sub-054  tensor(1, dtype=torch.int32)       1  10.0  37.0   3.0  
11    sub-060  tensor(1, dtype=torch.int32)       0  35.0  11.0   4.0  
12    sub-065  tensor(1, dtype=torch.int32)       1  13.0  26.0  11.0  
13    sub-069  tensor(2, dtype=torch.int32)       0  43.0   7.0   0.0  
14    sub-073  tensor(2, dtype=torch.int32)       0  28.0   6.0  16.0  
15    sub-079  tensor(2, dtype=torch.int32)       0  31.0  10.0   9.0  
16    sub-085  tensor(2, dtype=torch.int32)       0  41.0   2.0   7.0  

              precision    recall  f1-score   support

           0       0.54      1.00      0.70         7
           1       1.00      0.67      0.80         6
           2       0.00      0.00      0.00         4

    accuracy                           0.65        17
   macro avg       0.51      0.56      0.50        17
weighted avg       0.57      0.65      0.57        17
### 50-2CzT5C4T3PzP4P3
Training Accuracy: 0.60
printing results
Accuracy: 0.5176
Classification Report:
              precision    recall  f1-score   support

           0       0.49      0.76      0.60       350
           1       0.67      0.48      0.56       300
           2       0.31      0.15      0.20       200

    accuracy                           0.52       850
   macro avg       0.49      0.46      0.45       850
weighted avg       0.51      0.52      0.49       850

Confusion Matrix:
[[265  46  39]
 [126 145  29]
 [146  24  30]]
stopped printing results
{'sub-001': 0.76, 'sub-007': 0.86, 'sub-011': 0.5, 'sub-017': 0.98, 'sub-023': 0.7, 'sub-027': 0.92, 'sub-034': 0.58, 'sub-039': 0.74, 'sub-045': 0.26, 'sub-049': 0.56, 'sub-054': 0.84, 'sub-060': 0.12, 'sub-065': 0.38, 'sub-069': 0.08, 'sub-073': 0.32, 'sub-079': 0.12, 'sub-085': 0.08}
   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  38.0   3.0   9.0  
1     sub-007  tensor(0, dtype=torch.int32)       0  43.0   3.0   4.0  
2     sub-011  tensor(0, dtype=torch.int32)       0  25.0  25.0   0.0  
3     sub-017  tensor(0, dtype=torch.int32)       0  49.0   0.0   1.0  
4     sub-023  tensor(0, dtype=torch.int32)       0  35.0   8.0   7.0  
5     sub-027  tensor(0, dtype=torch.int32)       0  46.0   1.0   3.0  
6     sub-034  tensor(0, dtype=torch.int32)       0  29.0   6.0  15.0  
7     sub-039  tensor(1, dtype=torch.int32)       1  12.0  37.0   1.0  
8     sub-045  tensor(1, dtype=torch.int32)       0  30.0  13.0   7.0  
9     sub-049  tensor(1, dtype=torch.int32)       1  19.0  28.0   3.0  
10    sub-054  tensor(1, dtype=torch.int32)       1   6.0  42.0   2.0  
11    sub-060  tensor(1, dtype=torch.int32)       0  33.0   6.0  11.0  
12    sub-065  tensor(1, dtype=torch.int32)       0  26.0  19.0   5.0  
13    sub-069  tensor(2, dtype=torch.int32)       0  41.0   5.0   4.0  
14    sub-073  tensor(2, dtype=torch.int32)       0  27.0   7.0  16.0  
15    sub-079  tensor(2, dtype=torch.int32)       0  34.0  10.0   6.0  
16    sub-085  tensor(2, dtype=torch.int32)       0  44.0   2.0   4.0  

              precision    recall  f1-score   support

           0       0.50      1.00      0.67         7
           1       1.00      0.50      0.67         6
           2       0.00      0.00      0.00         4

    accuracy                           0.59        17
   macro avg       0.50      0.50      0.44        17
weighted avg       0.56      0.59      0.51        17

### 50-2Fp1CzPzT5

Training Accuracy: 0.61
printing results
Accuracy: 0.5506
Classification Report:
              precision    recall  f1-score   support

           0       0.55      0.74      0.63       350
           1       0.63      0.47      0.54       300
           2       0.45      0.33      0.38       200

    accuracy                           0.55       850
   macro avg       0.54      0.52      0.52       850
weighted avg       0.55      0.55      0.54       850

Confusion Matrix:
[[260  52  38]
 [116 142  42]
 [101  33  66]]
stopped printing results
{'sub-001': 0.76, 'sub-007': 0.84, 'sub-011': 0.34, 'sub-017': 0.92, 'sub-023': 0.68, 'sub-027': 0.86, 'sub-034': 0.8, 'sub-039': 0.78, 'sub-045': 0.34, 'sub-049': 0.56, 'sub-054': 0.8, 'sub-060': 0.22, 'sub-065': 0.14, 'sub-069': 0.04, 'sub-073': 0.14, 'sub-079': 0.86, 'sub-085': 0.28}
   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  38.0   4.0   8.0  
1     sub-007  tensor(0, dtype=torch.int32)       0  42.0   4.0   4.0  
2     sub-011  tensor(0, dtype=torch.int32)       1  17.0  23.0  10.0  
3     sub-017  tensor(0, dtype=torch.int32)       0  46.0   4.0   0.0  
4     sub-023  tensor(0, dtype=torch.int32)       0  34.0   7.0   9.0  
5     sub-027  tensor(0, dtype=torch.int32)       0  43.0   7.0   0.0  
6     sub-034  tensor(0, dtype=torch.int32)       0  40.0   3.0   7.0  
7     sub-039  tensor(1, dtype=torch.int32)       1  10.0  39.0   1.0  
8     sub-045  tensor(1, dtype=torch.int32)       0  26.0  17.0   7.0  
9     sub-049  tensor(1, dtype=torch.int32)       1  16.0  28.0   6.0  
10    sub-054  tensor(1, dtype=torch.int32)       1   9.0  40.0   1.0  
11    sub-060  tensor(1, dtype=torch.int32)       0  38.0  11.0   1.0  
12    sub-065  tensor(1, dtype=torch.int32)       2  17.0   7.0  26.0  
13    sub-069  tensor(2, dtype=torch.int32)       0  24.0  24.0   2.0  
14    sub-073  tensor(2, dtype=torch.int32)       0  38.0   5.0   7.0  
15    sub-079  tensor(2, dtype=torch.int32)       2   6.0   1.0  43.0  
16    sub-085  tensor(2, dtype=torch.int32)       0  33.0   3.0  14.0  
              precision    recall  f1-score   support

           0       0.55      0.86      0.67         7
           1       0.75      0.50      0.60         6
           2       0.50      0.25      0.33         4

    accuracy                           0.59        17
   macro avg       0.60      0.54      0.53        17
weighted avg       0.61      0.59      0.56        17

### Fp1Fp2CzPz aka vår tidigare standard
Training Accuracy: 0.57
printing results
Accuracy: 0.5118
Classification Report:
              precision    recall  f1-score   support

           0       0.54      0.70      0.61       350
           1       0.49      0.39      0.43       300
           2       0.48      0.36      0.41       200

    accuracy                           0.51       850
   macro avg       0.50      0.48      0.48       850
weighted avg       0.51      0.51      0.50       850

Confusion Matrix:
[[245  74  31]
 [135 118  47]
 [ 77  51  72]]
stopped printing results
{'sub-001': 0.56, 'sub-007': 0.8, 'sub-011': 0.7, 'sub-017': 0.76, 'sub-023': 0.68, 'sub-027': 0.88, 'sub-034': 0.52, 'sub-039': 0.8, 'sub-045': 0.32, 'sub-049': 0.42, 'sub-054': 0.32, 'sub-060': 0.36, 'sub-065': 
0.14, 'sub-069': 0.02, 'sub-073': 0.22, 'sub-079': 0.86, 'sub-085': 0.34}
   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  28.0  15.0   7.0  
1     sub-007  tensor(0, dtype=torch.int32)       0  40.0   6.0   4.0  
2     sub-011  tensor(0, dtype=torch.int32)       0  35.0  10.0   5.0  
3     sub-017  tensor(0, dtype=torch.int32)       0  38.0   9.0   3.0  
4     sub-023  tensor(0, dtype=torch.int32)       0  34.0  11.0   5.0  
5     sub-027  tensor(0, dtype=torch.int32)       0  44.0   3.0   3.0  
6     sub-034  tensor(0, dtype=torch.int32)       0  26.0  20.0   4.0  
7     sub-039  tensor(1, dtype=torch.int32)       1   8.0  40.0   2.0  
8     sub-045  tensor(1, dtype=torch.int32)       0  25.0  16.0   9.0  
9     sub-049  tensor(1, dtype=torch.int32)       0  24.0  21.0   5.0  
10    sub-054  tensor(1, dtype=torch.int32)       0  32.0  16.0   2.0  
11    sub-060  tensor(1, dtype=torch.int32)       0  29.0  18.0   3.0  
12    sub-065  tensor(1, dtype=torch.int32)       2  17.0   7.0  26.0  
13    sub-069  tensor(2, dtype=torch.int32)       1  24.0  25.0   1.0  
14    sub-073  tensor(2, dtype=torch.int32)       0  21.0  18.0  11.0  
15    sub-079  tensor(2, dtype=torch.int32)       2   6.0   1.0  43.0  
16    sub-085  tensor(2, dtype=torch.int32)       0  26.0   7.0  17.0  
              precision    recall  f1-score   support

           0       0.54      1.00      0.70         7
           1       0.50      0.17      0.25         6
           2       0.50      0.25      0.33         4

    accuracy                           0.53        17
   macro avg       0.51      0.47      0.43        17
weighted avg       0.52      0.53      0.45        17

## With added F channel and 2 seconds and 50 samples
### 50-2Fp1Cz
Training Accuracy: 0.52
printing results
Accuracy: 0.4882
Classification Report:
              precision    recall  f1-score   support

           0       0.50      0.76      0.60       350
           1       0.59      0.26      0.36       300
           2       0.38      0.34      0.36       200

    accuracy                           0.49       850
   macro avg       0.49      0.46      0.44       850
weighted avg       0.50      0.49      0.46       850

Confusion Matrix:
[[267  40  43]
 [149  79  72]
 [117  14  69]]
stopped printing results
{'sub-001': 0.7, 'sub-007': 0.84, 'sub-011': 0.6, 'sub-017': 0.9, 'sub-023': 0.64, 'sub-027': 0.94, 'sub-034': 0.72, 'sub-039': 0.54, 'sub-045': 0.2, 'sub-049': 0.28, 'sub-054': 0.3, 'sub-060': 0.22, 'sub-065': 0.04, 'sub-069': 0.0, 'sub-073': 0.14, 'sub-079': 0.84, 'sub-085': 0.4}  
   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  35.0   4.0  11.0  
1     sub-007  tensor(0, dtype=torch.int32)       0  42.0   1.0   7.0  
2     sub-011  tensor(0, dtype=torch.int32)       0  30.0  14.0   6.0  
3     sub-017  tensor(0, dtype=torch.int32)       0  45.0   4.0   1.0  
4     sub-023  tensor(0, dtype=torch.int32)       0  32.0   8.0  10.0  
5     sub-027  tensor(0, dtype=torch.int32)       0  47.0   0.0   3.0  
6     sub-034  tensor(0, dtype=torch.int32)       0  36.0   9.0   5.0  
7     sub-039  tensor(1, dtype=torch.int32)       1  17.0  27.0   6.0  
8     sub-045  tensor(1, dtype=torch.int32)       0  24.0  10.0  16.0  
9     sub-049  tensor(1, dtype=torch.int32)       0  32.0  14.0   4.0  
10    sub-054  tensor(1, dtype=torch.int32)       0  34.0  15.0   1.0  
11    sub-060  tensor(1, dtype=torch.int32)       0  35.0  11.0   4.0  
12    sub-065  tensor(1, dtype=torch.int32)       2   7.0   2.0  41.0  
13    sub-069  tensor(2, dtype=torch.int32)       0  49.0   1.0   0.0  
14    sub-073  tensor(2, dtype=torch.int32)       0  36.0   7.0   7.0  
15    sub-079  tensor(2, dtype=torch.int32)       2   3.0   5.0  42.0  
16    sub-085  tensor(2, dtype=torch.int32)       0  29.0   1.0  20.0  
              precision    recall  f1-score   support

           0       0.50      1.00      0.67         7
           1       1.00      0.17      0.29         6
           2       0.50      0.25      0.33         4

    accuracy                           0.53        17
   macro avg       0.67      0.47      0.43        17
weighted avg       0.68      0.53      0.45        17

### 50-2Fp1CzT5 bäst sample
Training Accuracy: 0.60
printing results
Accuracy: 0.5800
Classification Report:
              precision    recall  f1-score   support

           0       0.55      0.80      0.65       350
           1       0.78      0.48      0.60       300
           2       0.44      0.34      0.38       200

    accuracy                           0.58       850
   macro avg       0.59      0.54      0.54       850
weighted avg       0.61      0.58      0.57       850

Confusion Matrix:
[[281  21  48]
 [118 145  37]
 [114  19  67]]
stopped printing results
{'sub-001': 0.66, 'sub-007': 0.94, 'sub-011': 0.66, 'sub-017': 0.88, 'sub-023': 0.68, 'sub-027': 0.98, 'sub-034': 0.82, 'sub-039': 0.72, 'sub-045': 0.26, 'sub-049': 0.64, 'sub-054': 0.84, 'sub-060': 0.14, 'sub-065': 0.3, 'sub-069': 0.0, 'sub-073': 0.18, 'sub-079': 0.86, 'sub-085': 0.3}
   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  33.0   3.0  14.0  
1     sub-007  tensor(0, dtype=torch.int32)       0  47.0   0.0   3.0  
2     sub-011  tensor(0, dtype=torch.int32)       0  33.0   9.0   8.0  
3     sub-017  tensor(0, dtype=torch.int32)       0  44.0   2.0   4.0  
4     sub-023  tensor(0, dtype=torch.int32)       0  34.0   5.0  11.0  
5     sub-027  tensor(0, dtype=torch.int32)       0  49.0   0.0   1.0  
6     sub-034  tensor(0, dtype=torch.int32)       0  41.0   2.0   7.0  
7     sub-039  tensor(1, dtype=torch.int32)       1  12.0  36.0   2.0  
8     sub-045  tensor(1, dtype=torch.int32)       0  29.0  13.0   8.0  
9     sub-049  tensor(1, dtype=torch.int32)       1  16.0  32.0   2.0  
10    sub-054  tensor(1, dtype=torch.int32)       1   7.0  42.0   1.0  
11    sub-060  tensor(1, dtype=torch.int32)       0  40.0   7.0   3.0  
12    sub-065  tensor(1, dtype=torch.int32)       2  14.0  15.0  21.0  
13    sub-069  tensor(2, dtype=torch.int32)       0  40.0  10.0   0.0  
14    sub-073  tensor(2, dtype=torch.int32)       0  37.0   4.0   9.0  
15    sub-079  tensor(2, dtype=torch.int32)       2   4.0   3.0  43.0  
16    sub-085  tensor(2, dtype=torch.int32)       0  33.0   2.0  15.0  
              precision    recall  f1-score   support

           0       0.58      1.00      0.74         7
           1       1.00      0.50      0.67         6
           2       0.50      0.25      0.33         4

    accuracy                           0.65        17
   macro avg       0.69      0.58      0.58        17
weighted avg       0.71      0.65      0.62        17

### 50-2Fp1CzT5C4
Training Accuracy: 0.61
printing results
Accuracy: 0.5471
Classification Report:
              precision    recall  f1-score   support

           0       0.52      0.79      0.63       350
           1       0.69      0.41      0.52       300
           2       0.48      0.32      0.38       200

    accuracy                           0.55       850
   macro avg       0.56      0.51      0.51       850
weighted avg       0.57      0.55      0.53       850

Confusion Matrix:
[[277  43  30]
 [137 124  39]
 [122  14  64]]
stopped printing results
{'sub-001': 0.92, 'sub-007': 0.94, 'sub-011': 0.6, 'sub-017': 0.86, 'sub-023': 0.62, 'sub-027': 0.84, 'sub-034': 0.76, 'sub-039': 0.64, 'sub-045': 0.16, 'sub-049': 0.6, 'sub-054': 0.56, 'sub-060': 0.2, 'sub-065': 
0.32, 'sub-069': 0.0, 'sub-073': 0.2, 'sub-079': 0.84, 'sub-085': 0.24}   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  46.0   3.0   1.0  
1     sub-007  tensor(0, dtype=torch.int32)       0  47.0   2.0   1.0  
2     sub-011  tensor(0, dtype=torch.int32)       0  30.0  17.0   3.0  
3     sub-017  tensor(0, dtype=torch.int32)       0  43.0   2.0   5.0  
4     sub-023  tensor(0, dtype=torch.int32)       0  31.0  10.0   9.0  
5     sub-027  tensor(0, dtype=torch.int32)       0  42.0   5.0   3.0  
6     sub-034  tensor(0, dtype=torch.int32)       0  38.0   4.0   8.0  
7     sub-039  tensor(1, dtype=torch.int32)       1  15.0  32.0   3.0  
8     sub-045  tensor(1, dtype=torch.int32)       0  35.0   8.0   7.0  
9     sub-049  tensor(1, dtype=torch.int32)       1  16.0  30.0   4.0  
10    sub-054  tensor(1, dtype=torch.int32)       1  21.0  28.0   1.0  
11    sub-060  tensor(1, dtype=torch.int32)       0  36.0  10.0   4.0  
12    sub-065  tensor(1, dtype=torch.int32)       2  14.0  16.0  20.0  
13    sub-069  tensor(2, dtype=torch.int32)       0  47.0   3.0   0.0  
14    sub-073  tensor(2, dtype=torch.int32)       0  32.0   8.0  10.0  
15    sub-079  tensor(2, dtype=torch.int32)       2   6.0   2.0  42.0  
16    sub-085  tensor(2, dtype=torch.int32)       0  37.0   1.0  12.0  
              precision    recall  f1-score   support

           0       0.58      1.00      0.74         7
           1       1.00      0.50      0.67         6
           2       0.50      0.25      0.33         4

    accuracy                           0.65        17
   macro avg       0.69      0.58      0.58        17
weighted avg       0.71      0.65      0.62        17
### 50-2Fp1CzT5C4T3 bäst subject
Training Accuracy: 0.62
printing results
Accuracy: 0.5482
Classification Report:
              precision    recall  f1-score   support

           0       0.51      0.75      0.61       350
           1       0.72      0.49      0.59       300
           2       0.43      0.28      0.34       200

    accuracy                           0.55       850
   macro avg       0.55      0.51      0.51       850
weighted avg       0.57      0.55      0.54       850

Confusion Matrix:
[[261  39  50]
 [125 148  27]
 [125  18  57]]
stopped printing results
{'sub-001': 0.56, 'sub-007': 0.92, 'sub-011': 0.56, 'sub-017': 0.96, 'sub-023': 0.6, 'sub-027': 0.82, 'sub-034': 0.8, 'sub-039': 0.58, 'sub-045': 0.2, 'sub-049': 0.76, 'sub-054': 0.86, 'sub-060': 0.1, 'sub-065': 0.46, 'sub-069': 0.0, 'sub-073': 0.14, 'sub-079': 0.82, 'sub-085': 0.18}   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  28.0   4.0  18.0  
1     sub-007  tensor(0, dtype=torch.int32)       0  46.0   2.0   2.0  
2     sub-011  tensor(0, dtype=torch.int32)       0  28.0  17.0   5.0  
3     sub-017  tensor(0, dtype=torch.int32)       0  48.0   1.0   1.0  
4     sub-023  tensor(0, dtype=torch.int32)       0  30.0  11.0   9.0  
5     sub-027  tensor(0, dtype=torch.int32)       0  41.0   1.0   8.0  
6     sub-034  tensor(0, dtype=torch.int32)       0  40.0   3.0   7.0  
7     sub-039  tensor(1, dtype=torch.int32)       1  20.0  29.0   1.0  
8     sub-045  tensor(1, dtype=torch.int32)       0  36.0  10.0   4.0  
9     sub-049  tensor(1, dtype=torch.int32)       1   9.0  38.0   3.0  
10    sub-054  tensor(1, dtype=torch.int32)       1   5.0  43.0   2.0  
11    sub-060  tensor(1, dtype=torch.int32)       0  41.0   5.0   4.0  
12    sub-065  tensor(1, dtype=torch.int32)       1  14.0  23.0  13.0  
13    sub-069  tensor(2, dtype=torch.int32)       0  46.0   4.0   0.0  
14    sub-073  tensor(2, dtype=torch.int32)       0  35.0   8.0   7.0  
15    sub-079  tensor(2, dtype=torch.int32)       2   6.0   3.0  41.0  
16    sub-085  tensor(2, dtype=torch.int32)       0  38.0   3.0   9.0  
              precision    recall  f1-score   support

           0       0.58      1.00      0.74         7
           1       1.00      0.67      0.80         6
           2       1.00      0.25      0.40         4

    accuracy                           0.71        17
   macro avg       0.86      0.64      0.65        17
weighted avg       0.83      0.71      0.68        17

### 50-2Fp1CzT5C4T3Fp2
Training Accuracy: 0.59
printing results
Accuracy: 0.5118
Classification Report:
              precision    recall  f1-score   support

           0       0.49      0.77      0.60       350
           1       0.66      0.39      0.49       300
           2       0.41      0.24      0.30       200

    accuracy                           0.51       850
   macro avg       0.52      0.47      0.46       850
weighted avg       0.53      0.51      0.49       850

Confusion Matrix:
[[270  42  38]
 [151 117  32]
 [133  19  48]]
stopped printing results
{'sub-001': 0.86, 'sub-007': 0.82, 'sub-011': 0.68, 'sub-017': 0.92, 'sub-023': 0.64, 'sub-027': 0.86, 'sub-034': 0.62, 'sub-039': 0.44, 'sub-045': 0.12, 'sub-049': 0.62, 'sub-054': 0.66, 'sub-060': 0.14, 'sub-065': 0.36, 'sub-069': 0.02, 'sub-073': 0.28, 'sub-079': 0.48, 'sub-085': 
0.18}
   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  43.0   2.0   5.0  
1     sub-007  tensor(0, dtype=torch.int32)       0  41.0   4.0   5.0  
2     sub-011  tensor(0, dtype=torch.int32)       0  34.0  10.0   6.0  
3     sub-017  tensor(0, dtype=torch.int32)       0  46.0   2.0   2.0  
4     sub-023  tensor(0, dtype=torch.int32)       0  32.0  10.0   8.0  
5     sub-027  tensor(0, dtype=torch.int32)       0  43.0   2.0   5.0  
6     sub-034  tensor(0, dtype=torch.int32)       0  31.0  12.0   7.0  
7     sub-039  tensor(1, dtype=torch.int32)       0  27.0  22.0   1.0  
8     sub-045  tensor(1, dtype=torch.int32)       0  41.0   6.0   3.0  
9     sub-049  tensor(1, dtype=torch.int32)       1  15.0  31.0   4.0  
10    sub-054  tensor(1, dtype=torch.int32)       1  17.0  33.0   0.0  
11    sub-060  tensor(1, dtype=torch.int32)       0  36.0   7.0   7.0  
12    sub-065  tensor(1, dtype=torch.int32)       1  15.0  18.0  17.0  
13    sub-069  tensor(2, dtype=torch.int32)       0  44.0   5.0   1.0  
14    sub-073  tensor(2, dtype=torch.int32)       0  29.0   7.0  14.0  
15    sub-079  tensor(2, dtype=torch.int32)       2  21.0   5.0  24.0  
16    sub-085  tensor(2, dtype=torch.int32)       0  39.0   2.0   9.0  
              precision    recall  f1-score   support

           0       0.54      1.00      0.70         7
           1       1.00      0.50      0.67         6
           2       1.00      0.25      0.40         4

    accuracy                           0.65        17
   macro avg       0.85      0.58      0.59        17
weighted avg       0.81      0.65      0.62        17
