
# Linear SVM  

## Accuracy (%) For Each Digit  

|       | Digit 0 | Digit 1 | Digit 2 | Digit 3 | Digit 4 | Digit 5 | Digit 6 | Digit 7 | Digit 8 | Digit 9 |
| :---: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| C = 2 |  98.73  |  99.32  |  97.96  |  97.47  |  98.14  |  97.06  |  98.07  |  98.28  |  95.71  |  96.31  |
| C = 4 |  98.68  |  99.22  |  97.92  |  97.42  |  98.02  |  97.49  |  98.04  |  98.21  |  95.59  |  96.31  |
| C = 8 |  98.54  |  99.13  |  97.87  |  97.48  |  97.96  |  97.36  |  97.92  |  98.08  |  95.55  |  96.36  |

## Number Of Support Vectors For Each Digit  

|       | Digit 0 | Digit 1 | Digit 2 | Digit 3 | Digit 4 | Digit 5 | Digit 6 | Digit 7 | Digit 8 | Digit 9 |
| :---: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
| C = 2 |   464   |   505   |  1211   |  1422   |   900   |  1326   |   686   |   779   |  2093   |  1848   |
| C = 4 |   455   |   486   |  1201   |  1416   |   880   |  1292   |   671   |   770   |  2097   |  1836   |
| C = 8 |   436   |   455   |  1189   |  1400   |   869   |  1253   |   651   |   744   |  2077   |  1816   |

## The 3 Examples Of Largest Lagrange Multiplier On Both Sides Of The Discriminant Plane For Each Digit

### C = 2

|        |            Digit 0            |            Digit 1            |            Digit 2            |            Digit 3            |            Digit 4            |            Digit 5            |            Digit 6            |            Digit 7            |            Digit 8            |            Digit 9            |
| :----: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: |
| y = 1  | ![](img/c_2_digit_0_max3.png) | ![](img/c_2_digit_1_max3.png) | ![](img/c_2_digit_2_max3.png) | ![](img/c_2_digit_3_max3.png) | ![](img/c_2_digit_4_max3.png) | ![](img/c_2_digit_5_max3.png) | ![](img/c_2_digit_6_max3.png) | ![](img/c_2_digit_7_max3.png) | ![](img/c_2_digit_8_max3.png) | ![](img/c_2_digit_9_max3.png) |
| y = -1 | ![](img/c_2_digit_0_min3.png) | ![](img/c_2_digit_1_min3.png) | ![](img/c_2_digit_2_min3.png) | ![](img/c_2_digit_3_min3.png) | ![](img/c_2_digit_4_min3.png) | ![](img/c_2_digit_5_min3.png) | ![](img/c_2_digit_6_min3.png) | ![](img/c_2_digit_7_min3.png) | ![](img/c_2_digit_8_min3.png) | ![](img/c_2_digit_9_min3.png) |

### C = 4

|        |            Digit 0            |            Digit 1            |            Digit 2            |            Digit 3            |            Digit 4            |            Digit 5            |            Digit 6            |            Digit 7            |            Digit 8            |            Digit 9            |
| :----: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: |
| y = 1  | ![](img/c_4_digit_0_max3.png) | ![](img/c_4_digit_1_max3.png) | ![](img/c_4_digit_2_max3.png) | ![](img/c_4_digit_3_max3.png) | ![](img/c_4_digit_4_max3.png) | ![](img/c_4_digit_5_max3.png) | ![](img/c_4_digit_6_max3.png) | ![](img/c_4_digit_7_max3.png) | ![](img/c_4_digit_8_max3.png) | ![](img/c_4_digit_9_max3.png) |
| y = -1 | ![](img/c_4_digit_0_min3.png) | ![](img/c_4_digit_1_min3.png) | ![](img/c_4_digit_2_min3.png) | ![](img/c_4_digit_3_min3.png) | ![](img/c_4_digit_4_min3.png) | ![](img/c_4_digit_5_min3.png) | ![](img/c_4_digit_6_min3.png) | ![](img/c_4_digit_7_min3.png) | ![](img/c_4_digit_8_min3.png) | ![](img/c_4_digit_9_min3.png) |

### C = 8  

|        |            Digit 0            |            Digit 1            |            Digit 2            |            Digit 3            |            Digit 4            |            Digit 5            |            Digit 6            |            Digit 7            |            Digit 8            |            Digit 9            |
| :----: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: | :---------------------------: |
| y = 1  | ![](img/c_8_digit_0_max3.png) | ![](img/c_8_digit_1_max3.png) | ![](img/c_8_digit_2_max3.png) | ![](img/c_8_digit_3_max3.png) | ![](img/c_8_digit_4_max3.png) | ![](img/c_8_digit_5_max3.png) | ![](img/c_8_digit_6_max3.png) | ![](img/c_8_digit_7_max3.png) | ![](img/c_8_digit_8_max3.png) | ![](img/c_8_digit_9_max3.png) |
| y = -1 | ![](img/c_8_digit_0_min3.png) | ![](img/c_8_digit_1_min3.png) | ![](img/c_8_digit_2_min3.png) | ![](img/c_8_digit_3_min3.png) | ![](img/c_8_digit_4_min3.png) | ![](img/c_8_digit_5_min3.png) | ![](img/c_8_digit_6_min3.png) | ![](img/c_8_digit_7_min3.png) | ![](img/c_8_digit_8_min3.png) | ![](img/c_8_digit_9_min3.png) |

## CDF of the margin for each digit

|         |            C = 2             |            C = 4             |            C = 8             |
| :-----: | :--------------------------: | :--------------------------: | :--------------------------: |
| Digit 0 | ![](img/c_2_digit_0_cdf.png) | ![](img/c_4_digit_0_cdf.png) | ![](img/c_8_digit_0_cdf.png) |
| Digit 1 | ![](img/c_2_digit_1_cdf.png) | ![](img/c_4_digit_1_cdf.png) | ![](img/c_8_digit_1_cdf.png) |
| Digit 2 | ![](img/c_2_digit_2_cdf.png) | ![](img/c_4_digit_2_cdf.png) | ![](img/c_8_digit_2_cdf.png) |
| Digit 3 | ![](img/c_2_digit_3_cdf.png) | ![](img/c_4_digit_3_cdf.png) | ![](img/c_8_digit_3_cdf.png) |
| Digit 4 | ![](img/c_2_digit_4_cdf.png) | ![](img/c_4_digit_4_cdf.png) | ![](img/c_8_digit_4_cdf.png) |
| Digit 5 | ![](img/c_2_digit_5_cdf.png) | ![](img/c_4_digit_5_cdf.png) | ![](img/c_8_digit_5_cdf.png) |
| Digit 6 | ![](img/c_2_digit_6_cdf.png) | ![](img/c_4_digit_6_cdf.png) | ![](img/c_8_digit_6_cdf.png) |
| Digit 7 | ![](img/c_2_digit_7_cdf.png) | ![](img/c_4_digit_7_cdf.png) | ![](img/c_8_digit_7_cdf.png) |
| Digit 8 | ![](img/c_2_digit_8_cdf.png) | ![](img/c_4_digit_8_cdf.png) | ![](img/c_8_digit_8_cdf.png) |
| Digit 9 | ![](img/c_2_digit_9_cdf.png) | ![](img/c_4_digit_9_cdf.png) | ![](img/c_8_digit_9_cdf.png) |
