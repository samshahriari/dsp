# 50-2Fp1CzT5
## Fold 1

Training Accuracy: 0.60
printing results
Accuracy: 0.5671
Classification Report:
              precision    recall  f1-score   support

           0       0.53      0.78      0.63       350
           1       0.76      0.46      0.57       300
           2       0.45      0.35      0.40       200

    accuracy                           0.57       850
   macro avg       0.58      0.53      0.53       850
weighted avg       0.59      0.57      0.56       850

Confusion Matrix:
[[273  27  50]
 [125 138  37]
 [113  16  71]]
stopped printing results
{'sub-001': 0.7, 'sub-007': 0.88, 'sub-011': 0.6, 'sub-017': 0.9, 
'sub-023': 0.64, 'sub-027': 0.96, 'sub-034': 0.78, 'sub-039': 0.68, 'sub-045': 0.22, 'sub-049': 0.62, 'sub-054': 0.8, 'sub-060': 0.18, 'sub-065': 0.26, 'sub-069': 0.0, 'sub-073': 0.24, 'sub-079': 0.9, 'sub-085': 0.28}
   subject_id                        y_test  ...     1     2
0     sub-001  tensor(0, dtype=torch.int32)  ...   3.0  12.0      
1     sub-007  tensor(0, dtype=torch.int32)  ...   1.0   5.0      
2     sub-011  tensor(0, dtype=torch.int32)  ...  11.0   9.0      
3     sub-017  tensor(0, dtype=torch.int32)  ...   2.0   3.0      
4     sub-023  tensor(0, dtype=torch.int32)  ...   6.0  12.0      
5     sub-027  tensor(0, dtype=torch.int32)  ...   1.0   1.0      
6     sub-034  tensor(0, dtype=torch.int32)  ...   3.0   8.0      
7     sub-039  tensor(1, dtype=torch.int32)  ...  34.0   3.0      
8     sub-045  tensor(1, dtype=torch.int32)  ...  11.0   6.0      
9     sub-049  tensor(1, dtype=torch.int32)  ...  31.0   1.0      
10    sub-054  tensor(1, dtype=torch.int32)  ...  40.0   2.0      
11    sub-060  tensor(1, dtype=torch.int32)  ...   9.0   3.0      
12    sub-065  tensor(1, dtype=torch.int32)  ...  13.0  22.0      
13    sub-069  tensor(2, dtype=torch.int32)  ...  12.0   0.0      
14    sub-073  tensor(2, dtype=torch.int32)  ...   1.0  12.0      
15    sub-079  tensor(2, dtype=torch.int32)  ...   0.0  45.0      
16    sub-085  tensor(2, dtype=torch.int32)  ...   3.0  14.0      

[17 rows x 6 columns]
              precision    recall  f1-score   support

           0       0.58      1.00      0.74         7
           1       1.00      0.50      0.67         6
           2       0.50      0.25      0.33         4

    accuracy                           0.65        17
   macro avg       0.69      0.58      0.58        17
weighted avg       0.71      0.65      0.62        17

## Fold 2
Training Accuracy: 0.63
printing results
Accuracy: 0.4329
Classification Report:
              precision    recall  f1-score   support

           0       0.44      0.64      0.52       350
           1       0.46      0.47      0.46       250
           2       0.32      0.11      0.16       250

    accuracy                           0.43       850
   macro avg       0.41      0.41      0.38       850
weighted avg       0.41      0.43      0.40       850

Confusion Matrix:
[[223 101  26]
 [101 118  31]
 [184  39  27]]
stopped printing results
{'sub-002': 0.4, 'sub-006': 0.34, 'sub-012': 0.62, 'sub-018': 0.84, 'sub-021': 0.6, 'sub-028': 0.9, 'sub-032': 0.76, 'sub-040': 0.58, 'sub-043': 0.22, 'sub-048': 0.82, 'sub-055': 0.7, 'sub-059': 0.04, 'sub-066': 0.02, 'sub-070': 0.16, 'sub-074': 0.04, 'sub-081': 0.06, 'sub-086': 0.26}
   subject_id                        y_test  ...     1     2
0     sub-002  tensor(0, dtype=torch.int32)  ...  30.0   0.0      
1     sub-006  tensor(0, dtype=torch.int32)  ...  30.0   3.0      
2     sub-012  tensor(0, dtype=torch.int32)  ...  10.0   9.0      
3     sub-018  tensor(0, dtype=torch.int32)  ...   8.0   0.0      
4     sub-021  tensor(0, dtype=torch.int32)  ...  13.0   7.0      
5     sub-028  tensor(0, dtype=torch.int32)  ...   4.0   1.0      
6     sub-032  tensor(0, dtype=torch.int32)  ...   6.0   6.0      
7     sub-040  tensor(1, dtype=torch.int32)  ...  29.0   5.0      
8     sub-043  tensor(1, dtype=torch.int32)  ...  11.0   0.0      
9     sub-048  tensor(1, dtype=torch.int32)  ...  41.0   1.0      
10    sub-055  tensor(1, dtype=torch.int32)  ...  35.0   9.0      
11    sub-059  tensor(1, dtype=torch.int32)  ...   2.0  16.0      
12    sub-066  tensor(2, dtype=torch.int32)  ...  10.0   1.0      
13    sub-070  tensor(2, dtype=torch.int32)  ...   3.0   8.0      
14    sub-074  tensor(2, dtype=torch.int32)  ...   8.0   2.0      
15    sub-081  tensor(2, dtype=torch.int32)  ...   4.0   3.0      
16    sub-086  tensor(2, dtype=torch.int32)  ...  14.0  13.0      

[17 rows x 6 columns]
              precision    recall  f1-score   support

           0       0.42      0.71      0.53         7
           1       0.60      0.60      0.60         5
           2       0.00      0.00      0.00         5

    accuracy                           0.47        17
   macro avg       0.34      0.44      0.38        17
weighted avg       0.35      0.47      0.39        17

## Fold 4
Training Accuracy: 0.63
printing results
Accuracy: 0.4933
Classification Report:
              precision    recall  f1-score   support

           0       0.52      0.74      0.61       350
           1       0.44      0.55      0.49       250
           2       0.55      0.16      0.25       300

    accuracy                           0.49       900
   macro avg       0.50      0.48      0.45       900
weighted avg       0.51      0.49      0.46       900

Confusion Matrix:
[[258  69  23]
 [ 96 138  16]
 [142 110  48]]
stopped printing results
{'sub-004': 0.8, 'sub-009': 0.64, 'sub-014': 0.86, 'sub-016': 0.9, 'sub-025': 0.2, 'sub-029': 0.9, 'sub-035': 0.86, 'sub-042': 0.78, 'sub-046': 
0.72, 'sub-051': 0.52, 'sub-056': 0.44, 'sub-057': 0.3, 'sub-068': 0.02, 'sub-075': 0.58, 'sub-077': 0.16, 'sub-080': 0.02, 'sub-083': 0.16, 'sub-088': 0.02}
   subject_id                        y_test  y_pred     0     1     2
0     sub-004  tensor(0, dtype=torch.int32)       0  40.0   2.0   8.0   
1     sub-009  tensor(0, dtype=torch.int32)       0  32.0  14.0   4.0   
2     sub-014  tensor(0, dtype=torch.int32)       0  43.0   6.0   1.0   
3     sub-016  tensor(0, dtype=torch.int32)       0  45.0   3.0   2.0   
4     sub-025  tensor(0, dtype=torch.int32)       1  10.0  38.0   2.0   
5     sub-029  tensor(0, dtype=torch.int32)       0  45.0   3.0   2.0   
6     sub-035  tensor(0, dtype=torch.int32)       0  43.0   3.0   4.0   
7     sub-042  tensor(1, dtype=torch.int32)       1   9.0  39.0   2.0   
8     sub-046  tensor(1, dtype=torch.int32)       1  13.0  36.0   1.0   
9     sub-051  tensor(1, dtype=torch.int32)       1  20.0  26.0   4.0   
10    sub-056  tensor(1, dtype=torch.int32)       0  22.0  22.0   6.0   
11    sub-057  tensor(1, dtype=torch.int32)       0  32.0  15.0   3.0   
12    sub-068  tensor(2, dtype=torch.int32)       1  22.0  27.0   1.0   
13    sub-075  tensor(2, dtype=torch.int32)       2   9.0  12.0  29.0   
14    sub-077  tensor(2, dtype=torch.int32)       0  39.0   3.0   8.0   
15    sub-080  tensor(2, dtype=torch.int32)       1  12.0  37.0   1.0   
16    sub-083  tensor(2, dtype=torch.int32)       0  37.0   5.0   8.0   
17    sub-088  tensor(2, dtype=torch.int32)       1  23.0  26.0   1.0   
              precision    recall  f1-score   support

           0       0.60      0.86      0.71         7
           1       0.43      0.60      0.50         5
           2       1.00      0.17      0.29         6

    accuracy                           0.56        18
   macro avg       0.68      0.54      0.50        18
weighted avg       0.69      0.56      0.51        18

## Fold 5
Training Accuracy: 0.62
printing results
Accuracy: 0.4963
Classification Report:
              precision    recall  f1-score   support

           0       0.52      0.58      0.55       350
           1       0.53      0.57      0.55       300
           2       0.28      0.17      0.21       150

    accuracy                           0.50       800
   macro avg       0.44      0.44      0.43       800
weighted avg       0.48      0.50      0.48       800

Confusion Matrix:
[[202 121  27]
 [ 94 170  36]
 [ 95  30  25]]
stopped printing results
{'sub-005': 0.54, 'sub-010': 0.68, 'sub-015': 0.26, 'sub-020': 0.86, 'sub-024': 0.96, 'sub-031': 0.44, 'sub-036': 0.3, 'sub-037': 0.32, 'sub-038': 0.54, 'sub-053': 0.38, 'sub-058': 0.6, 'sub-062': 0.68, 'sub-064': 0.88, 'sub-071': 0.16, 'sub-078': 0.16, 'sub-084': 0.18}
   subject_id                        y_test  y_pred     0     1     2
0     sub-005  tensor(0, dtype=torch.int32)       0  27.0  13.0  10.0   
1     sub-010  tensor(0, dtype=torch.int32)       0  34.0  14.0   2.0   
2     sub-015  tensor(0, dtype=torch.int32)       1  13.0  34.0   3.0   
3     sub-020  tensor(0, dtype=torch.int32)       0  43.0   6.0   1.0   
4     sub-024  tensor(0, dtype=torch.int32)       0  48.0   0.0   2.0   
5     sub-031  tensor(0, dtype=torch.int32)       1  22.0  24.0   4.0   
6     sub-036  tensor(0, dtype=torch.int32)       1  15.0  30.0   5.0   
7     sub-037  tensor(1, dtype=torch.int32)       0  34.0  16.0   0.0   
8     sub-038  tensor(1, dtype=torch.int32)       1  20.0  27.0   3.0   
9     sub-053  tensor(1, dtype=torch.int32)       1  16.0  19.0  15.0   
10    sub-058  tensor(1, dtype=torch.int32)       1  11.0  30.0   9.0   
11    sub-062  tensor(1, dtype=torch.int32)       1  11.0  34.0   5.0   
12    sub-064  tensor(1, dtype=torch.int32)       1   2.0  44.0   4.0   
13    sub-071  tensor(2, dtype=torch.int32)       0  24.0  18.0   8.0   
14    sub-078  tensor(2, dtype=torch.int32)       0  31.0  11.0   8.0   
15    sub-084  tensor(2, dtype=torch.int32)       0  40.0   1.0   9.0   

              precision    recall  f1-score   support

           0       0.50      0.57      0.53         7
           1       0.62      0.83      0.71         6
           2       0.00      0.00      0.00         3

    accuracy                           0.56        16
   macro avg       0.38      0.47      0.42        16
weighted avg       0.45      0.56      0.50        16

# 50-2Fp1CzT5C4T3

## Fold 1
Training Accuracy: 0.63
printing results
Accuracy: 0.5553
Classification Report:
              precision    recall  f1-score   support

           0       0.52      0.74      0.61       350
           1       0.74      0.51      0.60       300
           2       0.43      0.30      0.35       200

    accuracy                           0.56       850
   macro avg       0.56      0.52      0.52       850
weighted avg       0.57      0.56      0.55       850

Confusion Matrix:
[[259  41  50]
 [116 153  31]
 [126  14  60]]
stopped printing results
{'sub-001': 0.56, 'sub-007': 0.88, 'sub-011': 0.54, 'sub-017': 0.98, 'sub-023': 0.56, 'sub-027': 0.82, 'sub-034': 0.84, 'sub-039': 0.62, 'sub-045': 0.2, 'sub-049': 0.76, 'sub-054': 0.86, 'sub-060': 0.08, 'sub-065': 0.54, 'sub-069': 0.0, 'sub-073': 0.16, 'sub-079': 0.82, 'sub-085': 0.22} 
   subject_id                        y_test  y_pred     0     1     2
0     sub-001  tensor(0, dtype=torch.int32)       0  28.0   4.0  18.0   
1     sub-007  tensor(0, dtype=torch.int32)       0  44.0   2.0   4.0   
2     sub-011  tensor(0, dtype=torch.int32)       0  27.0  17.0   6.0   
3     sub-017  tensor(0, dtype=torch.int32)       0  49.0   0.0   1.0   
4     sub-023  tensor(0, dtype=torch.int32)       0  28.0  15.0   7.0   
5     sub-027  tensor(0, dtype=torch.int32)       0  41.0   0.0   9.0   
6     sub-034  tensor(0, dtype=torch.int32)       0  42.0   3.0   5.0   
7     sub-039  tensor(1, dtype=torch.int32)       1  18.0  31.0   1.0   
8     sub-045  tensor(1, dtype=torch.int32)       0  35.0  10.0   5.0   
9     sub-049  tensor(1, dtype=torch.int32)       1   9.0  38.0   3.0   
10    sub-054  tensor(1, dtype=torch.int32)       1   5.0  43.0   2.0   
11    sub-060  tensor(1, dtype=torch.int32)       0  39.0   4.0   7.0   
12    sub-065  tensor(1, dtype=torch.int32)       1  10.0  27.0  13.0   
13    sub-069  tensor(2, dtype=torch.int32)       0  46.0   4.0   0.0   
14    sub-073  tensor(2, dtype=torch.int32)       0  36.0   6.0   8.0   
15    sub-079  tensor(2, dtype=torch.int32)       2   6.0   3.0  41.0   
16    sub-085  tensor(2, dtype=torch.int32)       0  38.0   1.0  11.0   
              precision    recall  f1-score   support

           0       0.58      1.00      0.74         7
           1       1.00      0.67      0.80         6
           2       1.00      0.25      0.40         4

    accuracy                           0.71        17
   macro avg       0.86      0.64      0.65        17
weighted avg       0.83      0.71      0.68        17

## Fold 2
Training Accuracy: 0.62
printing results
Accuracy: 0.4647
Classification Report:
              precision    recall  f1-score   support

           0       0.47      0.65      0.55       350
           1       0.45      0.48      0.46       250
           2       0.48      0.19      0.27       250

    accuracy                           0.46       850
   macro avg       0.47      0.44      0.43       850
weighted avg       0.47      0.46      0.44       850

Confusion Matrix:
[[229 106  15]
 [ 96 119  35]
 [163  40  47]]
stopped printing results
{'sub-002': 0.26, 'sub-006': 0.3, 'sub-012': 0.58, 'sub-018': 0.96, 'sub-021': 0.76, 'sub-028': 0.92, 'sub-032': 0.8, 'sub-040': 0.56, 'sub-043': 0.22, 'sub-048': 0.88, 'sub-055': 0.64, 'sub-059': 0.08, 'sub-066': 0.04, 'sub-070': 0.52, 'sub-074': 0.0, 'sub-081': 0.04, 'sub-086': 0.34}  
   subject_id                        y_test  y_pred     0     1     2
0     sub-002  tensor(0, dtype=torch.int32)       1  13.0  33.0   4.0   
1     sub-006  tensor(0, dtype=torch.int32)       1  15.0  34.0   1.0   
2     sub-012  tensor(0, dtype=torch.int32)       0  29.0  15.0   6.0   
3     sub-018  tensor(0, dtype=torch.int32)       0  48.0   2.0   0.0   
4     sub-021  tensor(0, dtype=torch.int32)       0  38.0   8.0   4.0   
5     sub-028  tensor(0, dtype=torch.int32)       0  46.0   4.0   0.0   
6     sub-032  tensor(0, dtype=torch.int32)       0  40.0  10.0   0.0   
7     sub-040  tensor(1, dtype=torch.int32)       1  21.0  28.0   1.0   
8     sub-043  tensor(1, dtype=torch.int32)       0  35.0  11.0   4.0   
9     sub-048  tensor(1, dtype=torch.int32)       1   2.0  44.0   4.0   
10    sub-055  tensor(1, dtype=torch.int32)       1  11.0  32.0   7.0   
11    sub-059  tensor(1, dtype=torch.int32)       0  27.0   4.0  19.0   
12    sub-066  tensor(2, dtype=torch.int32)       0  44.0   4.0   2.0   
13    sub-070  tensor(2, dtype=torch.int32)       2  22.0   2.0  26.0   
14    sub-074  tensor(2, dtype=torch.int32)       0  41.0   9.0   0.0   
15    sub-081  tensor(2, dtype=torch.int32)       0  44.0   4.0   2.0   
16    sub-086  tensor(2, dtype=torch.int32)       1  12.0  21.0  17.0   
              precision    recall  f1-score   support

           0       0.50      0.71      0.59         7
           1       0.50      0.60      0.55         5
           2       1.00      0.20      0.33         5

    accuracy                           0.53        17
   macro avg       0.67      0.50      0.49        17
weighted avg       0.65      0.53      0.50        17

## Fold 4

Training Accuracy: 0.63
printing results
Accuracy: 0.5000
Classification Report:
              precision    recall  f1-score   support

           0       0.53      0.75      0.62       350
           1       0.45      0.63      0.52       250
           2       0.57      0.10      0.17       300

    accuracy                           0.50       900
   macro avg       0.51      0.49      0.44       900
weighted avg       0.52      0.50      0.44       900

Confusion Matrix:
[[262  70  18]
 [ 87 158   5]
 [143 127  30]]
stopped printing results
{'sub-004': 0.78, 'sub-009': 0.84, 'sub-014': 0.82, 'sub-016': 0.88, 'sub-025': 0.1, 'sub-029': 0.88, 'sub-035': 0.94, 'sub-042': 0.86, 'sub-046': 0.86, 'sub-051': 0.32, 'sub-056': 0.7, 'sub-057': 0.42, 'sub-068': 0.04, 'sub-075': 0.38, 'sub-077': 0.14, 'sub-080': 0.02, 'sub-083': 0.0, 'sub-088': 0.02}
   subject_id                        y_test  y_pred     0     1     2
0     sub-004  tensor(0, dtype=torch.int32)       0  39.0   4.0   7.0   
1     sub-009  tensor(0, dtype=torch.int32)       0  42.0   5.0   3.0   
2     sub-014  tensor(0, dtype=torch.int32)       0  41.0   8.0   1.0   
3     sub-016  tensor(0, dtype=torch.int32)       0  44.0   5.0   1.0   
4     sub-025  tensor(0, dtype=torch.int32)       1   5.0  44.0   1.0   
5     sub-029  tensor(0, dtype=torch.int32)       0  44.0   4.0   2.0   
6     sub-035  tensor(0, dtype=torch.int32)       0  47.0   0.0   3.0   
7     sub-042  tensor(1, dtype=torch.int32)       1   6.0  43.0   1.0   
8     sub-046  tensor(1, dtype=torch.int32)       1   7.0  43.0   0.0   
9     sub-051  tensor(1, dtype=torch.int32)       0  32.0  16.0   2.0   
10    sub-056  tensor(1, dtype=torch.int32)       1  14.0  35.0   1.0   
11    sub-057  tensor(1, dtype=torch.int32)       0  28.0  21.0   1.0   
12    sub-068  tensor(2, dtype=torch.int32)       0  28.0  20.0   2.0   
13    sub-075  tensor(2, dtype=torch.int32)       1  10.0  21.0  19.0   
14    sub-077  tensor(2, dtype=torch.int32)       0  37.0   6.0   7.0   
15    sub-080  tensor(2, dtype=torch.int32)       1   6.0  43.0   1.0   
16    sub-083  tensor(2, dtype=torch.int32)       0  42.0   8.0   0.0   
17    sub-088  tensor(2, dtype=torch.int32)       1  20.0  29.0   1.0   
              precision    recall  f1-score   support

           0       0.55      0.86      0.67         7
           1       0.43      0.60      0.50         5
           2       0.00      0.00      0.00         6

    accuracy                           0.50        18
   macro avg       0.32      0.49      0.39        18
weighted avg       0.33      0.50      0.40        18

## Fold 5
Training Accuracy: 0.62
printing results
Accuracy: 0.5587
Classification Report:
              precision    recall  f1-score   support

           0       0.56      0.61      0.59       350
           1       0.63      0.69      0.66       300
           2       0.29      0.17      0.22       150

    accuracy                           0.56       800
   macro avg       0.49      0.49      0.49       800
weighted avg       0.54      0.56      0.54       800

Confusion Matrix:
[[215  95  40]
 [ 70 206  24]
 [ 98  26  26]]
stopped printing results
{'sub-005': 0.74, 'sub-010': 0.68, 'sub-015': 0.24, 'sub-020': 0.72, 'sub-024': 0.98, 'sub-031': 0.4, 'sub-036': 0.54, 'sub-037': 0.64, 'sub-038': 0.46, 'sub-053': 0.62, 'sub-058': 0.76, 'sub-062': 0.76, 'sub-064': 0.88, 'sub-071': 0.14, 'sub-078': 0.18, 'sub-084': 0.2}
   subject_id                        y_test  y_pred     0     1     2
0     sub-005  tensor(0, dtype=torch.int32)       0  37.0   5.0   8.0   
1     sub-010  tensor(0, dtype=torch.int32)       0  34.0   8.0   8.0   
2     sub-015  tensor(0, dtype=torch.int32)       1  12.0  35.0   3.0   
3     sub-020  tensor(0, dtype=torch.int32)       0  36.0   4.0  10.0   
4     sub-024  tensor(0, dtype=torch.int32)       0  49.0   1.0   0.0   
5     sub-031  tensor(0, dtype=torch.int32)       1  20.0  25.0   5.0   
6     sub-036  tensor(0, dtype=torch.int32)       0  27.0  17.0   6.0   
7     sub-037  tensor(1, dtype=torch.int32)       1  16.0  32.0   2.0   
8     sub-038  tensor(1, dtype=torch.int32)       0  26.0  23.0   1.0   
9     sub-053  tensor(1, dtype=torch.int32)       1  10.0  31.0   9.0   
10    sub-058  tensor(1, dtype=torch.int32)       1   6.0  38.0   6.0   
11    sub-062  tensor(1, dtype=torch.int32)       1   6.0  38.0   6.0   
12    sub-064  tensor(1, dtype=torch.int32)       1   6.0  44.0   0.0   
13    sub-071  tensor(2, dtype=torch.int32)       0  22.0  21.0   7.0   
14    sub-078  tensor(2, dtype=torch.int32)       0  38.0   3.0   9.0   
15    sub-084  tensor(2, dtype=torch.int32)       0  38.0   2.0  10.0   

              precision    recall  f1-score   support

           0       0.56      0.71      0.63         7
           1       0.71      0.83      0.77         6
           2       0.00      0.00      0.00         3

    accuracy                           0.62        16
   macro avg       0.42      0.52      0.46        16
weighted avg       0.51      0.62      0.56        16