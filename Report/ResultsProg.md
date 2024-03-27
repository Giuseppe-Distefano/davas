# Domain Adaptation Via Activation Shaping

## 0 - Baseline

| Experiment | Target | Accuracy | Loss |
| :---: | :---: | :---: | :---: |
| 0.1 | Cartoon | 54.52 | 0.01067 |
| 0.2 | Sketch  | 40.57 | 0.01512 |
| 0.3 | Photo   | 95.87 | 0.00107 |

## 1 - Activation Shaping Module

### 1.1 - One Activation Shaping module

#### 1.1.1 - ASH module after layer1.0.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.1.1 | 0.5 | Cartoon | 46.76 | 0.01264 | -07.76 |
| 1.1.1.2 | 0.5 | Sketch  | 22.19 | 0.01755 | -18.38 |
| 1.1.1.3 | 0.5 | Photo   | 86.77 | 0.00295 | -09.10 |

#### 1.1.2 - ASH module after layer1.0.relu

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.2.1 | 0.5 | Cartoon | 15.70 | 0.02028 | -38.82 |
| 1.1.2.2 | 0.5 | Sketch  | 10.54 | 0.01751 | -30.03 |
| 1.1.2.3 | 0.5 | Photo   | 17.31 | 0.02376 | -78.56 |

#### 1.1.3 - ASH module after layer1.0.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.3.1 | 0.5 | Cartoon | 40.91 | 0.01318 | -13.61 |
| 1.1.3.2 | 0.5 | Sketch  | 32.58 | 0.01297 | -07.99 |
| 1.1.3.3 | 0.5 | Photo   | 84.73 | 0.00402 | -11.14 |

#### 1.1.4 - ASH module after layer1.1.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.4.1 | 0.5 | Cartoon | 55.25 | 0.00976 | +00.73 |
| 1.1.4.2 | 0.5 | Sketch  | 38.43 | 0.01234 | -02.14 |
| 1.1.4.3 | 0.5 | Photo   | 87.90 | 0.00266 | -07.97 |

#### 1.1.5 - ASH module after layer1.1.bn1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.5.1 | 0.5 | Cartoon | 49.02 | 0.01210 | -05.50 |
| 1.1.5.2 | 0.5 | Sketch  | 38.20 | 0.01363 | -02.37 |
| 1.1.5.3 | 0.5 | Photo   | 90.84 | 0.00218 | -05.03 |

#### 1.1.6 - ASH module after layer1.1.relu

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.6.1 | 0.5 | Cartoon | 27.18 | 0.01646 | -27.34 |
| 1.1.6.2 | 0.5 | Sketch  | 26.37 | 0.01496 | -14.20 |
| 1.1.6.3 | 0.5 | Photo   | 52.51 | 0.01046 | -43.36 |

#### 1.1.7 - ASH module after layer1.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.7.1 | 0.5 | Cartoon | 52.47 | 0.01101 | -02.05 |
| 1.1.7.2 | 0.5 | Sketch  | 34.11 | 0.01727 | -06.46 |
| 1.1.7.3 | 0.5 | Photo   | 92.93 | 0.00172 | -02.94 |

#### 1.1.8 - ASH module after layer1.1.bn2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.8.1 | 0.5 | Cartoon | 53.71 | 0.01110 | -00.81 |
| 1.1.8.2 | 0.5 | Sketch  | 31.87 | 0.02042 | -08.70 |
| 1.1.8.3 | 0.5 | Photo   | 95.51 | 0.00127 | -00.36 |

#### 1.1.9 - ASH module after layer2.0.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.9.1 | 0.5 | Cartoon | 25.09 | 0.01923 | -29.43 |
| 1.1.9.2 | 0.5 | Sketch  | 19.60 | 0.01820 | -20.97 |
| 1.1.9.3 | 0.5 | Photo   | 68.92 | 0.00860 | -26.95 |

#### 1.1.10 - ASH module after layer2.0.relu

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.10.1 | 0.5 | Cartoon | 20.95 | 0.01965 | -33.57 |
| 1.1.10.2 | 0.5 | Sketch  | 26.04 | 0.02162 | -14.53 |
| 1.1.10.3 | 0.5 | Photo   | 25.93 | 0.01897 | -69.94 |

#### 1.1.11 - ASH module after layer2.0.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.11.1 | 0.5 | Cartoon | 50.77 | 0.01255 | -03.75 |
| 1.1.11.2 | 0.5 | Sketch  | 24.76 | 0.01966 | -15.81 |
| 1.1.11.3 | 0.5 | Photo   | 79.16 | 0.00476 | -16.71 |

#### 1.1.12 - ASH module after layer2.1.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.12.1 | 0.5 | Cartoon | 28.50 | 0.02081 | -26.02 |
| 1.1.12.2 | 0.5 | Sketch  | 29.80 | 0.02179 | -10.77 |
| 1.1.12.3 | 0.5 | Photo   | 59.30 | 0.00881 | -36.57 |

#### 1.1.13 - ASH module after layer2.1.relu

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.13.1 | 0.5 | Cartoon | 15.49 | 0.02042 | -39.03 |
| 1.1.13.2 | 0.5 | Sketch  | 16.19 | 0.01797 | -24.38 |
| 1.1.13.3 | 0.5 | Photo   | 39.10 | 0.01348 | -56.77 |

#### 1.1.14 - ASH module after layer2.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.14.1 | 0.5 | Cartoon | 59.30 | 0.00881 | +04.78 |
| 1.1.14.2 | 0.5 | Sketch  | 48.84 | 0.01148 | +08.27 |
| 1.1.14.3 | 0.5 | Photo   | 88.98 | 0.00272 | -06.89 |

#### 1.1.15 - ASH module after layer3.0.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.15.1 | 0.5 | Cartoon | 46.08 | 0.01424 | -08.44 |
| 1.1.15.2 | 0.5 | Sketch  | 34.54 | 0.01466 | -06.03 |
| 1.1.15.3 | 0.5 | Photo   | 93.29 | 0.00171 | -02.58 |

#### 1.1.16 - ASH module after layer3.0.relu

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.16.1 | 0.5 | Cartoon | 37.41 | 0.01273 | -17.11 |
| 1.1.16.2 | 0.5 | Sketch  | 25.86 | 0.01433 | -14.71 |
| 1.1.16.3 | 0.5 | Photo   | 63.53 | 0.00926 | -32.34 |

#### 1.1.17 - ASH module after layer3.0.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.17.1 | 0.5 | Cartoon | 38.05 | 0.01337 | -16.47 |
| 1.1.17.2 | 0.5 | Sketch  | 23.49 | 0.01533 | -17.08 |
| 1.1.17.3 | 0.5 | Photo   | 58.62 | 0.00965 | -37.25 |

#### 1.1.18 - ASH module after layer3.1.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.18.1 | 0.5 | Cartoon | 44.20 | 0.01451 | -10.32 |
| 1.1.18.2 | 0.5 | Sketch  | 30.41 | 0.01424 | -10.16 |
| 1.1.18.3 | 0.5 | Photo   | 84.43 | 0.00412 | -11.44 |

#### 1.1.19 - ASH module after layer3.1.relu

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.19.1 | 0.5 | Cartoon | 35.67 | 0.01403 | -18.85 |
| 1.1.19.2 | 0.5 | Sketch  | 23.80 | 0.01389 | -16.77 |
| 1.1.19.3 | 0.5 | Photo   | 73.59 | 0.00689 | -22.28 |

#### 1.1.20 - ASH module after layer3.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.20.1 | 0.5 | Cartoon | 52.52 | 0.01039 | -02.00 |
| 1.1.20.2 | 0.5 | Sketch  | 32.86 | 0.01526 | -07.71 |
| 1.1.20.3 | 0.5 | Photo   | 79.70 | 0.00451 | -16.17 |

#### 1.1.21 - ASH module after layer4.0.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.21.1 | 0.5 | Cartoon | 49.91 | 0.01075 | -04.61 |
| 1.1.21.2 | 0.5 | Sketch  | 27.44 | 0.01382 | -13.13 |
| 1.1.21.3 | 0.5 | Photo   | 80.12 | 0.00429 | -15.75 |

#### 1.1.22 - ASH module after layer4.0.relu

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.22.1 | 0.5 | Cartoon | 42.32 | 0.01184 | -12.20 |
| 1.1.22.2 | 0.5 | Sketch  | 32.55 | 0.01404 | -08.02 |
| 1.1.22.3 | 0.5 | Photo   | 85.69 | 0.00292 | -10.18 |

#### 1.1.23 - ASH module after layer4.0.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.23.1 | 0.5 | Cartoon | 35.24 | 0.01921 | -19.28 |
| 1.1.23.2 | 0.5 | Sketch  | 22.47 | 0.02752 | -18.10 |
| 1.1.23.3 | 0.5 | Photo   | 49.52 | 0.01271 | -46.35 |

#### 1.1.24 - ASH module after layer4.1.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.24.1 | 0.5 | Cartoon | 40.02 | 0.01223 | -14.50 |
| 1.1.24.2 | 0.5 | Sketch  | 06.64 | 0.01611 | -33.93 |
| 1.1.24.3 | 0.5 | Photo   | 82.28 | 0.00676 | -13.59 |

#### 1.1.25 - ASH module after layer4.1.relu

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.25.1 | 0.5 | Cartoon | 32.21 | 0.01591 | -22.31 |
| 1.1.25.2 | 0.5 | Sketch  | 04.30 | 0.01906 | -36.27 |
| 1.1.25.3 | 0.5 | Photo   | 53.65 | 0.01274 | -42.22 |

#### 1.1.26 - ASH module after layer4.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.26.1 | 0.5 | Cartoon | 38.91 | 0.01431 | -15.61 |
| 1.1.26.2 | 0.5 | Sketch  | 32.58 | 0.01496 | -07.99 |
| 1.1.26.3 | 0.5 | Photo   | 92.22 | 0.01116 | -03.65 |

#### Average improvements

| Experiment | Placement | Avg Improvement |
| :---: | :---: | :---: |
| 1.1.1 | layer1.0.conv1 | -11.75 |
| 1.1.2 | layer1.0.relu | -49.14 |
| 1.1.3 | layer1.0.conv2 | -10.91 |
| **1.1.4** | **layer1.1.conv1** | -03.12 |
| **1.1.5** | **layer1.1.bn1** | -04.30 |
| 1.1.6 | layer1.1.relu | -28.30 |
| **1.1.7** | **layer1.1.conv2** | -03.82 |
| **1.1.8** | **layer1.1.bn2** | -03.29 |
| 1.1.9 | layer2.0.conv1 | -25.78 |
| 1.1.10 | layer2.0.relu | -39.35 |
| 1.1.11 | layer2.0.conv2 | -12.09 |
| 1.1.12 | layer2.1.conv1 | -24.45 |
| 1.1.13 | layer2.1.relu | -40.06 |
| **1.1.14** | **layer2.1.conv2** | +02.05 |
| **1.1.15** | **layer3.0.conv1** | -05.68 |
| 1.1.16 | layer3.0.relu | -21.39 |
| 1.1.17 | layer3.0.conv2 | -23.60 |
| 1.1.18 | layer3.1.conv1 | -10.64 |
| 1.1.19 | layer3.1.relu | -19.30 |
| **1.1.20** | **layer3.1.conv2** | -08.63 |
| 1.1.21 | layer4.0.conv1 | -11.16 |
| 1.1.22 | layer4.0.relu | -10.13 |
| 1.1.23 | layer4.0.conv2 | -27.91 |
| 1.1.24 | layer4.1.conv1 | -20.67 |
| 1.1.25 | layer4.1.relu | -33.60 |
| 1.1.26 | layer4.1.conv2 | -09.08 |

We choose experiments with an average improvement better than -09.00.

### 1.2 - Two Activation Shaping modules

#### 1.2.1 - ASH module after layer1.1.bn1 and layer1.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.2.1.1 | 0.5 | Cartoon | 54.35 | 0.01052 | -00.17 |
| 1.2.1.2 | 0.5 | Sketch  | 33.49 | 0.01763 | -07.08 |
| 1.2.1.3 | 0.5 | Photo   | 92.22 | 0.00188 | -03.65 |

#### 1.2.2 - ASH module after layer1.1.bn1 and layer1.1.bn2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.2.2.1 | 0.5 | Cartoon | 48.93 | 0.01213 | -05.59 |
| 1.2.2.2 | 0.5 | Sketch  | 33.19 | 0.01787 | -07.38 |
| 1.2.2.3 | 0.5 | Photo   | 93.59 | 0.00160 | -02.28 |

#### 1.2.3 - ASH module after layer1.1.bn1 and layer2.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.2.3.1 | 0.5 | Cartoon | 56.74 | 0.00946 | +02.22 |
| 1.2.3.2 | 0.5 | Sketch  | 47.37 | 0.01121 | +06.80 |
| 1.2.3.3 | 0.5 | Photo   | 85.99 | 0.00319 | -09.88 |

#### 1.2.4 - ASH module after layer1.1.bn1 and layer3.0.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.2.4.1 | 0.5 | Cartoon | 40.19 | 0.01512 | -14.33 |
| 1.2.4.2 | 0.5 | Sketch  | 41.64 | 0.01191 | +01.07 |
| 1.2.4.3 | 0.5 | Photo   | 87.31 | 0.00312 | -08.56 |

#### 1.2.5 - ASH module after layer1.1.bn1 and layer3.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.2.5.1 | 0.5 | Cartoon | 47.70 | 0.01237 | -06.75 |
| 1.2.5.2 | 0.5 | Sketch  | 40.09 | 0.01412 | -00.48 |
| 1.2.5.3 | 0.5 | Photo   | 73.35 | 0.00649 | -22.52 |

#### 1.2.6 - ASH module after layer1.1.conv2 and layer1.1.bn2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.2.6.1 | 0.5 | Cartoon | 47.82 | 0.01257 | -06.70 |
| 1.2.6.2 | 0.5 | Sketch  | 29.80 | 0.02227 | -10.77 |
| 1.2.6.3 | 0.5 | Photo   | 89.34 | 0.00264 | -06.53 |

#### 1.2.7 - ASH module after layer1.1.conv2 and layer2.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.2.7.1 | 0.5 | Cartoon | 55.72 | 0.00973 | +01.20 |
| 1.2.7.2 | 0.5 | Sketch  | 45.20 | 0.01266 | +04.63 |
| 1.2.7.3 | 0.5 | Photo   | 78.80 | 0.00490 | -17.07 |

#### 1.2.8 - ASH module after layer1.1.conv2 and layer3.0.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.2.8.1 | 0.5 | Cartoon | 42.75 | 0.01479 | -11.77 |
| 1.2.8.2 | 0.5 | Sketch  | 36.96 | 0.01518 | -03.61 |
| 1.2.8.3 | 0.5 | Photo   | 89.76 | 0.00260 | -06.11 |

#### 1.2.9 - ASH module after layer1.1.conv2 and layer3.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.2.9.1 | 0.5 | Cartoon | 53.71 | 0.01021 | -00.81 |
| 1.2.9.2 | 0.5 | Sketch  | 32.48 | 0.01442 | -08.09 |
| 1.2.9.3 | 0.5 | Photo   | 75.27 | 0.00534 | -20.60 |

#### 1.2.10 - ASH module after layer1.1.bn2 and layer2.1.bn2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.2.10.1 | 0.5 | Cartoon | 57.85 | 0.00995 | +03.33 |
| 1.2.10.2 | 0.5 | Sketch  | 39.70 | 0.01459 | -00.87 |
| 1.2.10.3 | 0.5 | Photo   | 83.29 | 0.00392 | -12.58 |

#### 1.2.11 - ASH module after layer1.1.bn2 and layer3.0.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.2.11.1 | 0.5 | Cartoon | 42.49 | 0.01468 | -12.03 |
| 1.2.11.2 | 0.5 | Sketch  | 31.97 | 0.01802 | -08.60 |
| 1.2.11.3 | 0.5 | Photo   | 92.16 | 0.00210 | -03.71 |

#### 1.2.12 - ASH module after layer1.1.bn2 and layer3.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.2.12.1 | 0.5 | Cartoon | 52.22 | 0.01146 | -02.30 |
| 1.2.12.2 | 0.5 | Sketch  | 25.55 | 0.01681 | -15.02 |
| 1.2.12.3 | 0.5 | Photo   | 80.78 | 0.00423 | -15.09 |

#### 1.2.13 - ASH module after layer2.1.conv2 and layer3.0.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.2.13.1 | 0.5 | Cartoon | 40.83 | 0.01336 | -13.69 |
| 1.2.13.2 | 0.5 | Sketch  | 29.07 | 0.01396 | -11.50 |
| 1.2.13.3 | 0.5 | Photo   | 75.81 | 0.00617 | -20.06 |

#### 1.2.14 - ASH module after layer2.1.conv2 and layer3.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.2.14.1 | 0.5 | Cartoon | 49.70 | 0.01051 | -04.82 |
| 1.2.14.2 | 0.5 | Sketch  | 28.86 | 0.01499 | -11.71 |
| 1.2.14.3 | 0.5 | Photo   | 58.92 | 0.01026 | -36.95 |

#### 1.2.15 - ASH module after layer3.0.conv1 and layer3.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.2.15.1 | 0.5 | Cartoon | 49.53 | 0.01154 | -04.99 |
| 1.2.15.2 | 0.5 | Sketch  | 33.19 | 0.01285 | -07.38 |
| 1.2.15.3 | 0.5 | Photo   | 62.81 | 0.00819 | -33.06 |

#### Average improvements

| Experiment | Placement | Avg Improvement |
| :---: | :---: | :---: |
| **1.2.1** | **layer1.1.bn1, layer1.1.conv2** | -03.63 |
| 1.2.2 | layer1.1.bn1, layer1.1.bn2 | -05.08 |
| **1.2.3** | **layer1.1.bn1, layer2.1.conv2** | -00.29 |
| 1.2.4 | layer1.1.bn1, layer3.0.conv1 | -07.27 |
| 1.2.5 | layer1.1.bn1, layer3.1.conv2 | -09.94 |
| 1.2.6 | layer1.1.conv2, layer1.1.bn2 | -08.00 |
| **1.2.7** | **layer1.1.conv2, layer2.1.conv2** | -03.75 |
| 1.2.8 | layer1.1.conv2, layer3.0.conv1 | -07.16 |
| 1.2.9 | layer1.1.conv2, layer3.1.conv2 | -09.83 |
| **1.2.10** | **layer1.1.bn2, layer2.1.conv2** | -03.37 |
| 1.2.11 | layer1.1.bn2, layer3.0.conv1 | -08.11 |
| 1.2.12 | layer1.1.bn2, layer3.1.conv2 | -10.80 |
| 1.2.13 | layer2.1.conv2, layer3.0.conv1 | -15.08 |
| 1.2.14 | layer2.1.conv2, layer3.1.conv2 | -17.83 |
| 1.2.15 | layer3.0.conv1, layer3.1.conv2 | -15.14 |

We choose experiments with an average improvement better than -05.00.

### 1.3 - Three Activation Shaping modules

#### 1.3.1 - ASH module after layer1.1.bn1, layer1.1.conv2, and layer1.1.bn2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.3.1.1 | 0.5 | Cartoon | 47.27 | 0.01250 | -07.25 |
| 1.3.1.2 | 0.5 | Sketch  | 29.14 | 0.02197 | -11.43 |
| 1.3.1.3 | 0.5 | Photo   | 88.50 | 0.00283 | -07.37 |

#### 1.3.2 - ASH module after layer1.1.bn1, layer1.1.conv2, and layer2.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.3.2.1 | 0.5 | Cartoon | 54.18 | 0.01033 | -00.34 |
| 1.3.2.2 | 0.5 | Sketch  | 42.05 | 0.01279 | +01.48 |
| 1.3.2.3 | 0.5 | Photo   | 76.59 | 0.00516 | -19.28 |

#### 1.3.3 - ASH module after layer1.1.bn1, layer1.1.conv2, and layer3.0.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.3.3.1 | 0.5 | Cartoon | 44.33 | 0.01394 | -10.19 |
| 1.3.3.2 | 0.5 | Sketch  | 34.36 | 0.01527 | -06.21 |
| 1.3.3.3 | 0.5 | Photo   | 89.82 | 0.00260 | -06.05 |

#### 1.3.4 - ASH module after layer1.1.bn1, layer1.1.conv2, and layer3.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.3.4.1 | 0.5 | Cartoon | 53.07 | 0.01053 | -01.45 |
| 1.3.4.2 | 0.5 | Sketch  | 31.84 | 0.01451 | -08.73 |
| 1.3.4.3 | 0.5 | Photo   | 77.13 | 0.00519 | -18.74 |

#### 1.3.5 - ASH module after layer1.1.bn1, layer1.1.bn2, and layer2.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.3.5.1 | 0.5 | Cartoon | 52.77 | 0.01073 | -01.75 |
| 1.3.5.2 | 0.5 | Sketch  | 37.49 | 0.01361 | -03.08 |
| 1.3.5.3 | 0.5 | Photo   | 81.38 | 0.00423 | -14.49 |

#### 1.3.6 - ASH module after layer1.1.bn1, layer2.1.conv2, and layer3.0.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.3.6.1 | 0.5 | Cartoon | 43.56 | 0.01269 | -10.96 |
| 1.3.6.2 | 0.5 | Sketch  | 40.98 | 0.01188 | +00.41 |
| 1.3.6.3 | 0.5 | Photo   | 70.72 | 0.00698 | -25.15 |

#### 1.3.7 - ASH module after layer1.1.bn1, layer2.1.conv2, and layer3.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.3.7.1 | 0.5 | Cartoon | 53.03 | 0.00997 | -01.49 |
| 1.3.7.2 | 0.5 | Sketch  | 33.42 | 0.01347 | -07.15 |
| 1.3.7.3 | 0.5 | Photo   | 62.46 | 0.00915 | -33.41 |

#### 1.3.8 - ASH module after layer1.1.conv2, layer1.1.bn2, and layer2.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.3.8.1 | 0.5 | Cartoon | 45.56 | 0.01307 | -08.96 |
| 1.3.8.2 | 0.5 | Sketch  | 33.98 | 0.01431 | -06.59 |
| 1.3.8.3 | 0.5 | Photo   | 66.35 | 0.00756 | -29.52 |

#### 1.3.9 - ASH module after layer1.1.conv2, layer2.1.conv2, and layer3.0.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.3.9.1 | 0.5 | Cartoon | 34.00 | 0.01484 | -20.52 |
| 1.3.9.2 | 0.5 | Sketch  | 44.03 | 0.01179 | +03.46 |
| 1.3.9.3 | 0.5 | Photo   | 49.70 | 0.01097 | -46.17 |

#### 1.3.10 - ASH module after layer1.1.conv2, layer2.1.conv2, and layer3.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.3.10.1 | 0.5 | Cartoon | 40.70 | 0.01251 | -13.82 |
| 1.3.10.2 | 0.5 | Sketch  | 31.38 | 0.01574 | -09.19 |
| 1.3.10.3 | 0.5 | Photo   | 48.50 | 0.01376 | -47.37 |

#### 1.3.11 - ASH module after layer1.1.bn2, layer2.1.conv2, and layer3.0.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.3.11.1 | 0.5 | Cartoon | 40.66 | 0.01329 | -13.86 |
| 1.3.11.2 | 0.5 | Sketch  | 40.16 | 0.01232 | -00.41 |
| 1.3.11.3 | 0.5 | Photo   | 72.51 | 0.00649 | -23.36 |

#### 1.3.12 - ASH module after layer1.1.bn2, layer2.1.conv2, and layer3.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.3.12.1 | 0.5 | Cartoon | 44.33 | 0.01438 | -10.19 |
| 1.3.12.2 | 0.5 | Sketch  | 22.91 | 0.01805 | -17.66 |
| 1.3.12.3 | 0.5 | Photo   | 54.25 | 0.01148 | -41.62 |

#### Average improvements

| Experiment | Placement | Avg Improvement |
| :---: | :---: | :---: |
| **1.3.1** | **layer1.1.bn1, layer1.1.conv2, layer1.1.bn2** | -08.68 |
| **1.3.2** | **layer1.1.bn1, layer1.1.conv2, layer2.1.conv2** | -06.05 |
| **1.3.3** | **layer1.1.bn1, layer1.1.conv2, layer3.0.conv1** | -07.48 |
| 1.3.4 | layer1.1.bn1, layer1.1.conv2, layer3.1.conv2 | -09.64 |
| **1.3.5** | **layer1.1.bn1, layer1.1.bn2, layer2.1.conv2** | -06.44 |
| 1.3.6 | layer1.1.bn1, layer2.1.conv2, layer3.0.conv1 | -11.90 |
| 1.3.7 | layer1.1.bn1, layer2.1.conv2, layer3.1.conv2 | -14.02 |
| 1.3.8 | layer1.1.conv2, layer1.1.bn2, layer2.1.conv2 | -15.02 |
| 1.3.9 | layer1.1.conv2, layer2.1.conv2, layer3.0.conv1 | -21.08 |
| 1.3.10 | layer1.1.conv2, layer2.1.conv2, layer3.1.conv2 | -23.46 |
| 1.3.11 | layer1.1.bn2, layer2.1.conv2, layer3.0.conv1 | -12.54 |
| 1.3.12 | layer1.1.bn2, layer2.1.conv2, layer3.1.conv2 | -23.16 |

We choose experiments with an average improvement better than -09.00.

### 1.4 - Four Activation Shaping modules

#### 1.4.1 - ASH module after layer1.1.bn1, layer1.1.conv2, layer1.1.bn2, and layer2.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.4.1.1 | 0.5 | Cartoon | 44.50 | 0.01346 | -10.02 |
| 1.4.1.2 | 0.5 | Sketch  | 37.11 | 0.01372 | -03.46 |
| 1.4.1.3 | 0.5 | Photo   | 64.49 | 0.00785 | -31.38 |

#### 1.4.2 - ASH module after layer1.1.bn1, layer1.1.conv2, layer1.1.bn2, and layer3.0.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.4.2.1 | 0.5 | Cartoon | 35.11 | 0.01649 | -19.41 |
| 1.4.2.2 | 0.5 | Sketch  | 28.71 | 0.02261 | -11.86 |
| 1.4.2.3 | 0.5 | Photo   | 78.44 | 0.00583 | -17.43 |

#### 1.4.3 - ASH module after layer1.1.bn1, layer1.1.conv2, layer1.1.bn2, and layer3.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.4.3.1 | 0.5 | Cartoon | 45.86 | 0.01296 | -08.66 |
| 1.4.3.2 | 0.5 | Sketch  | 22.83 | 0.02386 | -17.74 |
| 1.4.3.3 | 0.5 | Photo   | 64.79 | 0.00814 | -31.08 |

#### 1.4.4 - ASH module after layer1.1.bn1, layer1.1.conv2, layer2.1.conv2, and layer3.0.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.4.4.1 | 0.5 | Cartoon | 34.98 | 0.01408 | -19.54 |
| 1.4.4.2 | 0.5 | Sketch  | 44.54 | 0.01133 | +03.97 |
| 1.4.4.3 | 0.5 | Photo   | 51.86 | 0.01011 | -44.01 |

#### 1.4.5 - ASH module after layer1.1.bn1, layer1.1.conv2, layer2.1.conv2, and layer3.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.4.5.1 | 0.5 | Cartoon | 43.00 | 0.01228 | -11.52 |
| 1.4.5.2 | 0.5 | Sketch  | 28.38 | 0.01614 | -12.19 |
| 1.4.5.3 | 0.5 | Photo   | 50.48 | 0.01262 | -45.39 |

#### 1.4.6 - ASH module after layer1.1.bn1, layer1.1.conv2, layer3.0.conv1, and layer3.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.4.6.1 | 0.5 | Cartoon | 41.98 | 0.01436 | -12.54 |
| 1.4.6.2 | 0.5 | Sketch  | 31.61 | 0.01339 | -08.96 |
| 1.4.6.3 | 0.5 | Photo   | 56.77 | 0.00968 | -39.10 |

#### 1.4.7 - ASH module after layer1.1.bn1, layer1.1.bn2, layer2.1.conv2, and layer3.0.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.4.7.1 | 0.5 | Cartoon | 40.15 | 0.01322 | -14.37 |
| 1.4.7.2 | 0.5 | Sketch  | 45.18 | 0.01103 | -04.61 |
| 1.4.7.3 | 0.5 | Photo   | 66.71 | 0.00749 | -29.16 |

#### 1.4.8 - ASH module after layer1.1.bn1, layer1.1.bn2, layer2.1.conv2, and layer3.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.4.8.1 | 0.5 | Cartoon | 44.28 | 0.01197 | -10.24 |
| 1.4.8.2 | 0.5 | Sketch  | 27.79 | 0.01406 | -12.78 |
| 1.4.8.3 | 0.5 | Photo   | 53.41 | 0.01067 | -42.46 |

#### Average improvements

| Experiment | Placement | Avg Improvement |
| :---: | :---: | :---: |
| **1.4.1** | **layer1.1.bn1, layer1.1.conv2, layer1.1.bn2, layer2.1.conv2** | -14.95 |
| **1.4.2** | **layer1.1.bn1, layer1.1.conv2, layer1.1.bn2, layer3.0.conv1** | -16.23 |
| 1.4.3 | layer1.1.bn1, layer1.1.conv2, layer1.1.bn2, layer3.1.conv2 | -19.16 |
| 1.4.4 | layer1.1.bn1, layer1.1.conv2, layer2.1.conv2, layer3.0.conv1 | -19.86 |
| 1.4.5 | layer1.1.bn1, layer1.1.conv2, layer2.1.conv2, layer3.1.conv2 | -23.03 |
| 1.4.6 | layer1.1.bn1, layer1.1.conv2, layer3.0.conv1, layer3.1.conv2 | -20.02 |
| **1.4.7** | **layer1.1.bn1, layer1.1.bn2, layer2.1.conv2, layer3.0.conv1** | -16.05 |
| 1.4.8 | layer1.1.bn1, layer1.1.bn2, layer2.1.conv2, layer3.1.conv2 | -21.83 |

We choose experiments with an average improvement better than -18.00.

### 1.5 - Five Activation Shaping modules

#### 1.5.1 - ASH module after layer1.1.bn1, layer1.1.conv2, layer1.1.bn2, layer2.1.conv2, and layer3.0.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.5.1.1 | 0.5 | Cartoon | 36.56 | 0.01517 | -17.96 |
| 1.5.1.2 | 0.5 | Sketch  | 36.98 | 0.01385 | -03.59 |
| 1.5.1.3 | 0.5 | Photo   | 47.07 | 0.01148 | -48.80 |

#### 1.5.2 - ASH module after layer1.1.bn1, layer1.1.conv2, layer1.1.bn2, layer2.1.conv2, and layer3.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.5.2.1 | 0.5 | Cartoon | 29.05 | 0.01670 | -25.47 |
| 1.5.2.2 | 0.5 | Sketch  | 23.21 | 0.01624 | -17.36 |
| 1.5.2.3 | 0.5 | Photo   | 41.26 | 0.01592 | -54.61 |

#### 1.5.3 - ASH module after layer1.1.bn1, layer1.1.conv2, layer1.1.bn2, layer3.0.conv1, and layer3.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.5.3.1 | 0.5 | Cartoon | 42.83 | 0.01432 | -11.69 |
| 1.5.3.2 | 0.5 | Sketch  | 21.46 | 0.02198 | -19.11 |
| 1.5.3.3 | 0.5 | Photo   | 56.17 | 0.00990 | -39.70 |

#### 1.5.4 - ASH module after layer1.1.bn1, layer1.1.bn2, layer2.1.conv2, layer3.0.conv1, and layer3.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.5.4.1 | 0.5 | Cartoon | 36.77 | 0.01287 | -17.75 |
| 1.5.4.2 | 0.5 | Sketch  | 23.39 | 0.01400 | -17.18 |
| 1.5.4.3 | 0.5 | Photo   | 49.04 | 0.01107 | -46.83 |

#### Average improvements

| Experiment | Placement | Avg Improvement |
| :---: | :---: | :---: |
| 1.5.1 | layer1.1.bn1, layer1.1.conv2, layer1.1.bn2, layer2.1.conv2, layer3.0.conv1 | -23.45 |
| 1.5.2 | layer1.1.bn1, layer1.1.conv2, layer1.1.bn2, layer2.1.conv2, layer3.1.conv2 | -32.48 |
| 1.5.3 | layer1.1.bn1, layer1.1.conv2, layer1.1.bn2, layer3.0.conv1, layer3.1.conv2 | -23.50 |
| 1.5.4 | layer1.1.bn1, layer1.1.bn2, layer2.1.conv2, layer3.0.conv1, layer3.1.conv2 | -27.25 |

## 2 - Random Activation Maps

### 2.1 - mor = 0.00

#### 2.1.1 - ASH module after layer2.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.1.1.1 | 0.00 | Cartoon | 54.56 | 0.00988 | +00.04 |
| 2.1.1.2 | 0.00 | Sketch | 49.12 | 0.01045 | +08.55 |
| 2.1.1.3 | 0.00 | Photo | 76.71 | 0.00536 | -19.16 |

#### 2.1.2 - ASH module after layer1.1.bn1 and layer2.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.1.2.1 | 0.00 | Cartoon | 42.70 | 0.01253 | -11.82 |
| 2.1.2.2 | 0.00 | Sketch | 42.40 | 0.01196 | +01.83 |
| 2.1.2.3 | 0.00 | Photo | 68.14 | 0.00767 | -27.73 |

#### 2.1.3 - ASH module after layer1.1.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.1.3.1 | 0.00 | Cartoon | 54.99 | 0.00998 | +00.47 |
| 2.1.3.2 | 0.00 | Sketch | 33.04 | 0.01427 | -07.53 |
| 2.1.3.3 | 0.00 | Photo | 82.81 | 0.00364 | -13.06 |

#### 2.1.4 - ASH module after layer1.1.bn2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.1.4.1 | 0.00 | Cartoon | 46.97 | 0.01223 | -07.55 |
| 2.1.4.2 | 0.00 | Sketch | 29.73 | 0.02048 | -10.84 |
| 2.1.4.3 | 0.00 | Photo | 90.54 | 0.00264 | -05.33 |

#### 2.1.5 - ASH module after layer1.1.bn2 and layer2.1.bn2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.1.5.1 | 0.00 | Cartoon | 35.07 | 0.01683 | -19.45 |
| 2.1.5.2 | 0.00 | Sketch | 19.98 | 0.02203 | -20.59 |
| 2.1.5.3 | 0.00 | Photo | 30.54 | 0.01607 | -65.33 |

#### Average improvements

| Experiment | Placement | Avg Improvement |
| :---: | :---: | :---: |
| 2.1.1 | layer2.1.conv2 | -03.52 |
| 2.1.2 | layer1.1.bn1, layer2.1.conv2 | -09.57 |
| 2.1.3 | layer1.1.conv1 | -06.71 |
| 2.1.4 | layer1.1.bn2 | -07.91 |
| 2.1.5 | layer1.1.bn2 and layer2.1.bn2 | -35.12 |

### 2.2 - mor = 0.25

#### 2.2.1 - ASH module after layer2.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.2.1.1 | 0.25 | Cartoon | 60.15 | 0.0087 | +05.63 |
| 2.2.1.2 | 0.25 | Sketch | 51.31 | 0.01084 | +10.74 |
| 2.2.1.3 | 0.25 | Photo | 84.25 | 0.00366 | -11.62 |

#### 2.2.2 - ASH module after layer1.1.bn1 and layer2.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.2.2.1 | 0.25 | Cartoon | 53.84 | 0.01018 | -00.68 |
| 2.2.2.2 | 0.25 | Sketch | 50.75 | 0.01058 | +10.18 |
| 2.2.2.3 | 0.25 | Photo | 79.88 | 0.00467 | -15.99 |

#### 2.2.3 - ASH module after layer1.1.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.2.3.1 | 0.25 | Cartoon | 56.27 | 0.00986 | +01.75 |
| 2.2.3.2 | 0.25 | Sketch | 37.69 | 0.01354 | -02.88 |
| 2.2.3.3 | 0.25 | Photo | 88.14 | 0.00260 | -07.73 |

#### 2.2.4 - ASH module after layer1.1.bn2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.2.4.1 | 0.25 | Cartoon | 51.96 | 0.01132 | -02.56 |
| 2.2.4.2 | 0.25 | Sketch | 31.03 | 0.02062 | -09.54 |
| 2.2.4.3 | 0.25 | Photo | 94.97 | 0.00147 | -00.90 |

#### 2.2.5 - ASH module after layer1.1.bn2 and layer2.1.bn2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.2.5.1 | 0.25 | Cartoon | 40.02 | 0.01476 | -14.50 |
| 2.2.5.2 | 0.25 | Sketch | 19.47 | 0.02663 | -21.10 |
| 2.2.5.3 | 0.25 | Photo | 60.18 | 0.00933 | -35.69 |

#### Average improvements

| Experiment | Placement | Avg Improvement |
| :---: | :---: | :---: |
| 2.2.1 | layer2.1.conv2 | +01.58 |
| 2.2.2 | layer1.1.bn1, layer2.1.conv2 | -02.16 |
| 2.2.3 | layer1.1.conv1 | -2.96 |
| 2.2.4 | layer1.1.bn2 | -04.33 |
| 2.2.5 | layer1.1.bn2 and layer2.1.bn2 | -23.76 |

### 2.3 - mor = 0.50

#### 2.3.1 - ASH module after layer2.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.3.1.1 | 0.50 | Cartoon | 59.30 | 0.00878 | +04.78 |
| 2.3.1.2 | 0.50 | Sketch | 49.43 | 0.01130 | +08.86 |
| 2.3.1.3 | 0.50 | Photo | 88.80 | 0.00274 | -07.07 |

#### 2.3.2 - ASH module after layer1.1.bn1 and layer2.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.3.2.1 | 0.50 | Cartoon | 56.40 | 0.00951 | +01.88 |
| 2.3.2.2 | 0.50 | Sketch | 47.40 | 0.01103 | +06.83 |
| 2.3.2.3 | 0.50 | Photo | 85.99 | 0.00319 | -09.88 |

#### 2.3.3 - ASH module after layer1.1.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.3.3.1 | 0.50 | Cartoon | 55.55 | 0.00982 | +01.03 |
| 2.3.3.2 | 0.50 | Sketch | 37.97 | 0.01230 | -02.60 |
| 2.3.3.3 | 0.50 | Photo | 87.72 | 0.00264 | -08.15 |

#### 2.3.4 - ASH module after layer1.1.bn2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.3.4.1 | 0.50 | Cartoon | 53.84 | 0.01108 | -00.68 |
| 2.3.4.2 | 0.50 | Sketch | 31.84 | 0.02037 | -08.73 |
| 2.3.4.3 | 0.50 | Photo | 95.39 | 0.00127 | -00.48 |

#### 2.3.5 - ASH module after layer1.1.bn2 and layer2.1.bn2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.3.5.1 | 0.50 | Cartoon | 47.48 | 0.01310 | -07.04 |
| 2.3.5.2 | 0.50 | Sketch | 26.24 | 0.02575 | -14.33 |
| 2.3.5.3 | 0.50 | Photo | 80.54 | 0.00418 | -15.33 |

#### Average improvements

| Experiment | Placement | Avg Improvement |
| :---: | :---: | :---: |
| 2.3.1 | layer2.1.conv2 | +02.19 |
| 2.3.2 | layer1.1.bn1, layer2.1.conv2 | -00.39 |
| 2.3.3 | layer1.1.conv1 | -03.24 |
| 2.3.4 | layer1.1.bn2 | -03.30 |
| 2.3.5 | layer1.1.bn2 and layer2.1.bn2 | -12.23 |

### 2.4 - mor = 0.75

#### 2.4.1 - ASH module after layer2.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.4.1.1 | 0.75 | Cartoon | 55.67 | 0.00977 | +01.15 |
| 2.4.1.2 | 0.75 | Sketch | 43.70 | 0.01256 | +03.13 |
| 2.4.1.3 | 0.75 | Photo | 91.08 | 0.00212 | -04.79 |

#### 2.4.2 - ASH module after layer1.1.bn1 and layer2.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.4.2.1 | 0.75 | Cartoon | 54.78 | 0.00979 | +00.26 |
| 2.4.2.2 | 0.75 | Sketch | 33.77 | 0.01219 | -06.80 |
| 2.4.2.3 | 0.75 | Photo | 88.14 | 0.00280 | -07.73 |

#### 2.4.3 - ASH module after layer1.1.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.4.3.1 | 0.75 | Cartoon | 50.94 | 0.01067 | -03.58 |
| 2.4.3.2 | 0.75 | Sketch | 29.65 | 0.01336 | -10.92 |
| 2.4.3.3 | 0.75 | Photo | 81.98 | 0.00404 | -13.89 |

#### 2.4.4 - ASH module after layer1.1.bn2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.4.4.1 | 0.75 | Cartoon | 52.69 | 0.01148 | -01.83 |
| 2.4.4.2 | 0.75 | Sketch | 31.46 | 0.02057 | -09.11 |
| 2.4.4.3 | 0.75 | Photo | 92.69 | 0.00174 | -03.18 |

#### 2.4.5 - ASH module after layer1.1.bn2 and layer2.1.bn2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.4.5.1 | 0.75 | Cartoon | 42.92 | 0.01389 | -11.60 |
| 2.4.5.2 | 0.75 | Sketch | 28.30 | 0.02254 | -12.27 |
| 2.4.5.3 | 0.75 | Photo | 88.74 | 0.00249 | -07.13 |

#### Average improvements

| Experiment | Placement | Avg Improvement |
| :---: | :---: | :---: |
| 2.4.1 | layer2.1.conv2 | -00.17 |
| 2.4.2 | layer1.1.bn1, layer2.1.conv2 | -04.76 |
| 2.4.3 | layer1.1.conv1 | -09.46 |
| 2.4.4 | layer1.1.bn2 | -04.71 |
| 2.4.5 | layer1.1.bn2 and layer2.1.bn2 | -10.33 |

### 2.5 - mor = 1.00

#### 2.5.1 - ASH module after layer2.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.5.1.1 | 1.00 | Cartoon | 16.64 | 0.13514 | -37.88 |
| 2.5.1.2 | 1.00 | Sketch | 19.65 | 0.13187 | -20.92 |
| 2.5.1.3 | 1.00 | Photo | 11.50 | 0.14474 | -84.37 |

#### 2.5.2 - ASH module after layer1.1.bn1 and layer2.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.5.2.1 | 1.00 | Cartoon | 16.60 | 9.09029 | -37.92 |
| 2.5.2.2 | 1.00 | Sketch | 19.65 | 7.46906 | -20.92 |
| 2.5.2.3 | 1.00 | Photo | 11.32 | 9.86020 | -84.55 |

#### 2.5.3 - ASH module after layer1.1.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.5.3.1 | 1.00 | Cartoon | 16.60 | 2.68424 | -37.92 |
| 2.5.3.2 | 1.00 | Sketch | 19.65 | 2.67450 | -20.92 |
| 2.5.3.3 | 1.00 | Photo | 11.32 | 2.09453 | -84.55 |

#### 2.5.4 - ASH module after layer1.1.bn2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.5.4.1 | 1.00 | Cartoon | 45.61 | 0.01396 | -08.91 |
| 2.5.4.2 | 1.00 | Sketch | 27.23 | 0.01718 | -13.34 |
| 2.5.4.3 | 1.00 | Photo | 80.60 | 0.00627 | -15.20 |

#### 2.5.5 - ASH module after layer1.1.bn2 and layer2.1.bn2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2.5.5.1 | 1.00 | Cartoon | 30.55 | 0.01757 | -23.97 |
| 2.5.5.2 | 1.00 | Sketch | 21.33 | 0.02060 | -19.24 |
| 2.5.5.3 | 1.00 | Photo | 57.54 | 0.01128 | -38.33 |

#### Average improvements

| Experiment | Placement | Avg Improvement |
| :---: | :---: | :---: |
| 2.5.1 | layer2.1.conv2 | -47.72 |
| 2.5.2 | layer1.1.bn1, layer2.1.conv2 | -47.80 |
| 2.5.3 | layer1.1.conv1 | -47.80 |
| 2.5.4 | layer1.1.bn2 | -12.48 |
| 2.5.5 | layer1.1.bn2 and layer2.1.bn2 | -27.18 |

### Average improvements

| Placement | Improvement |
| :---: | :---: |
| **layer2.1.conv2** | -15.88 |
| layer1.1.bn1, layer2.1.conv2 | -21.56 |
| layer1.1.conv1 | -23.39 |
| **layer1.1.bn2** | -10.91 |
| layer1.1.bn2 and layer2.1.bn2 | -36.24 |

## 3 - Adapting Activation Maps Across Domains

#### 3.1 - ASH module after layer2.1.conv2

| Experiment | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: |
| 3.1.1 | Cartoon | 55.42 | 0.00968 | +01.00 |
| 3.1.2 | Sketch | 39.63 | 0.01254 | -00.94 |
| 3.1.3 | Photo | 89.70 | 0.00236 | -06.17 |

#### 3.2 - ASH module after layer1.1.bn2

| Experiment | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: |
| 3.2.1 | Cartoon | 51.71 | 0.01146 | -02.81 |
| 3.2.2 | Sketch | 31.61 | 0.02015 | -08.96 |
| 3.2.3 | Photo | 95.15 | 0.00137 | -00.72 |

#### Average improvements

| Experiment | Placement | Avg Improvement |
| :---: | :---: | :---: |
| 3.1 | layer2.1.conv2 | -02.04 |
| 3.2 | layer1.1.bn2 | -04.16 |
