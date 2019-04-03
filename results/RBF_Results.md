# RBF SVM (Radial Basis Function)  

To find the model with the highest accuracy, I try to set log2C in range of -1 to 3, and log2gamma in range of -4 to 1, and obtain C = 2 and gamma = 0.0625.

## Accuracy (%) For Each Digit  

| Digit 0 | Digit 1 | Digit 2 | Digit 3 | Digit 4 | Digit 5 | Digit 6 | Digit 7 | Digit 8 | Digit 9 |
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
|  99.53  |  99.76  |  98.88  |  98.85  |  99.15  |  98.74  |  99.3   |  99.06  |  98.36  |  98.83  |

## Number Of Support Vectors For Each Digit  

| Digit 0 | Digit 1 | Digit 2 | Digit 3 | Digit 4 | Digit 5 | Digit 6 | Digit 7 | Digit 8 | Digit 9 |
| :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
|  5860   |  2419   |  6882   |  7123   |  6303   |  6682   |  5648   |  5734   |  7666   |  6488   |

## The 3 Examples Of Largest Lagrange Multiplier On Both Sides Of The Discriminant Plane For Each Digit

|        |         Digit 0          |         Digit 1          |         Digit 2          |         Digit 3          |         Digit 4          |         Digit 5          |         Digit 6          |         Digit 7          |         Digit 8          |         Digit 9          |
| :----: | :----------------------: | :----------------------: | :----------------------: | :----------------------: | :----------------------: | :----------------------: | :----------------------: | :----------------------: | :----------------------: | :----------------------: |
| y = 1  | ![](img/rbf_d0_max3.png) | ![](img/rbf_d1_max3.png) | ![](img/rbf_d2_max3.png) | ![](img/rbf_d3_max3.png) | ![](img/rbf_d4_max3.png) | ![](img/rbf_d5_max3.png) | ![](img/rbf_d6_max3.png) | ![](img/rbf_d7_max3.png) | ![](img/rbf_d8_max3.png) | ![](img/rbf_d9_max3.png) |
| y = -1 | ![](img/rbf_d0_min3.png) | ![](img/rbf_d1_min3.png) | ![](img/rbf_d2_min3.png) | ![](img/rbf_d3_min3.png) | ![](img/rbf_d4_min3.png) | ![](img/rbf_d5_min3.png) | ![](img/rbf_d6_min3.png) | ![](img/rbf_d7_min3.png) | ![](img/rbf_d8_min3.png) | ![](img/rbf_d9_min3.png) |

## CDF of the margin for each digit

|         |                         |
| :-----: | :---------------------: |
| Digit 0 | ![](img/rbf_cdf_d0.png) |
| Digit 1 | ![](img/rbf_cdf_d1.png) |
| Digit 2 | ![](img/rbf_cdf_d2.png) |
| Digit 3 | ![](img/rbf_cdf_d3.png) |
| Digit 4 | ![](img/rbf_cdf_d4.png) |
| Digit 5 | ![](img/rbf_cdf_d5.png) |
| Digit 6 | ![](img/rbf_cdf_d6.png) |
| Digit 7 | ![](img/rbf_cdf_d7.png) |
| Digit 8 | ![](img/rbf_cdf_d8.png) |
| Digit 9 | ![](img/rbf_cdf_d9.png) |
