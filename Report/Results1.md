# Domain Adaptation Via Activation Shaping

## 0 - Baseline

| Experiment | Target | Accuracy | Loss |
| :---: | :---: | :---: | :---: |
| 0.1 | Cartoon | 54.52 | 0.01067 |
| 0.2 | Sketch  | 40.57 | 0.01512 |
| 0.3 | Photo   | 95.87 | 0.00107 |

## 1 - Activation Shaping module

### 1.1 - One Activation Shaping module

#### 1.1.1 - ASH module after layer1.0.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.1.1 | 0.5 | Cartoon | 46.76 | 0.01264 | -07.76 |
| 1.1.1.2 | 0.5 | Sketch  | 22.19 | 0.01755 | -18.38 |
| 1.1.1.3 | 0.5 | Photo   | 86.77 | 0.00295 | -09.10 |

#### 1.1.2 - ASH module after layer1.0.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.2.1 | 0.5 | Cartoon | 40.91 | 0.01318 | -13.61 |
| 1.1.2.2 | 0.5 | Sketch  | 32.58 | 0.01297 | -07.99 |
| 1.1.2.3 | 0.5 | Photo   | 84.73 | 0.00402 | -11.14 |

#### 1.1.3 - ASH module after layer1.1.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.3.1 | 0.5 | Cartoon | 55.25 | 0.00976 | +00.73 |
| 1.1.3.2 | 0.5 | Sketch  | 38.43 | 0.01234 | -02.14 |
| 1.1.3.3 | 0.5 | Photo   | 87.90 | 0.00266 | -07.97 |

#### 1.1.4 - ASH module after layer1.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.4.1 | 0.5 | Cartoon | 52.47 | 0.01101 | -02.05 |
| 1.1.4.2 | 0.5 | Sketch  | 34.11 | 0.01727 | -06.46 |
| 1.1.4.3 | 0.5 | Photo   | 92.93 | 0.00172 | -02.94 |

#### 1.1.5 - ASH module after layer2.0.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.4.1 | 0.5 | Cartoon | 25.09 | 0.01923 | -29.43 |
| 1.1.4.2 | 0.5 | Sketch  | 19.60 | 0.01820 | -20.97 |
| 1.1.4.3 | 0.5 | Photo   | 68.92 | 0.00860 | -26.95 |

#### 1.1.6 - ASH module after layer2.0.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.5.1 | 0.5 | Cartoon | 50.77 | 0.01255 | -03.75 |
| 1.1.5.2 | 0.5 | Sketch  | 24.76 | 0.01966 | -15.81 |
| 1.1.5.3 | 0.5 | Photo   | 79.16 | 0.00476 | -16.71 |

#### 1.1.7 - ASH module after layer2.1.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.6.1 | 0.5 | Cartoon | 28.50 | 0.02081 | -26.02 |
| 1.1.6.2 | 0.5 | Sketch  | 29.80 | 0.02179 | -10.77 |
| 1.1.6.3 | 0.5 | Photo   | 59.30 | 0.00881 | -36.57 |

#### 1.1.8 - ASH module after layer2.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.7.1 | 0.5 | Cartoon | 59.30 | 0.00881 | +04.78 |
| 1.1.7.2 | 0.5 | Sketch  | 48.84 | 0.01148 | +08.27 |
| 1.1.7.3 | 0.5 | Photo   | 88.98 | 0.00272 | -06.89 |

#### 1.1.9 - ASH module after layer3.0.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.9.1 | 0.5 | Cartoon | 46.08 | 0.01424 | -08.44 |
| 1.1.9.2 | 0.5 | Sketch  | 34.54 | 0.01466 | -06.03 |
| 1.1.9.3 | 0.5 | Photo   | 93.29 | 0.00171 | -02.58 |

#### 1.1.10 - ASH module after layer3.0.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.10.1 | 0.5 | Cartoon | 38.05 | 0.01337 | -16.47 |
| 1.1.10.2 | 0.5 | Sketch  | 23.49 | 0.01533 | -17.08 |
| 1.1.10.3 | 0.5 | Photo   | 58.62 | 0.00965 | -37.25 |

#### 1.1.11 - ASH module after layer3.1.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.11.1 | 0.5 | Cartoon | 44.20 | 0.01451 | -10.32 |
| 1.1.11.2 | 0.5 | Sketch  | 30.41 | 0.01424 | -10.16 |
| 1.1.11.3 | 0.5 | Photo   | 84.43 | 0.00412 | -11.44 |

#### 1.1.12 - ASH module after layer3.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.12.1 | 0.5 | Cartoon | 52.52 | 0.01039 | -02.00 |
| 1.1.12.2 | 0.5 | Sketch  | 32.86 | 0.01526 | -07.71 |
| 1.1.12.3 | 0.5 | Photo   | 79.70 | 0.00451 | -16.17 |

#### 1.1.13 - ASH module after layer4.0.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.13.1 | 0.5 | Cartoon | 49.91 | 0.01075 | -04.61 |
| 1.1.13.2 | 0.5 | Sketch  | 27.44 | 0.01382 | -13.13 |
| 1.1.13.3 | 0.5 | Photo   | 80.12 | 0.00429 | -15.75 |

#### 1.1.14 - ASH module after layer4.0.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.14.1 | 0.5 | Cartoon | 35.24 | 0.01921 | -19.28 |
| 1.1.14.2 | 0.5 | Sketch  | 22.47 | 0.02752 | -18.10 |
| 1.1.14.3 | 0.5 | Photo   | 49.52 | 0.01271 | -46.35 |

#### 1.1.15 - ASH module after layer4.1.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.15.1 | 0.5 | Cartoon | 40.02 | 0.01223 | -14.50 |
| 1.1.15.2 | 0.5 | Sketch  | 06.64 | 0.01611 | -33.93 |
| 1.1.15.3 | 0.5 | Photo   | 82.28 | 0.00676 | -13.59 |

#### 1.1.16 - ASH module after layer4.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.1.16.1 | 0.5 | Cartoon | 38.91 | 0.01431 | -15.61 |
| 1.1.16.2 | 0.5 | Sketch  | 32.58 | 0.01496 | -07.99 |
| 1.1.16.3 | 0.5 | Photo   | 92.22 | 0.01116 | -03.65 |

#### Average improvements

| Experiment | Placement | Avg Improvement |
| :---: | :---: | :---: |
| 1.1.1 | layer1.0.conv1 | -11.75 |
| 1.1.2 | layer1.0.conv2 | -10.91 |
| 1.1.3 | layer1.1.conv1 | -12.38 |
| 1.1.4 | layer1.1.conv2 | -03.82 |
| 1.1.5 | layer2.0.conv1 | -25.78 |
| 1.1.6 | layer2.0.conv2 | -12.09 |
| 1.1.7 | layer2.1.conv1 | -24.45 |
| 1.1.8 | layer2.1.conv2 | +02.05 |
| 1.1.9 | layer3.0.conv1 | -01.66 |
| 1.1.10 | layer3.0.conv2 | -23.60 |
| 1.1.11 | layer3.1.conv1 | -10.64 |
| 1.1.12 | layer3.1.conv2 | -08.63 |
| 1.1.13 | layer4.0.conv1 | -11.16 |
| 1.1.14 | layer4.0.conv2 | -27.91 |
| 1.1.15 | layer4.1.conv1 | -20.67 |
| 1.1.16 | layer4.1.conv2 | -09.08 |

### 1.2 - Two Activation Shaping modules

#### 1.2.1 - ASH module after layer1.1.conv2 and layer2.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.2.1.1 | 0.5 | Cartoon | _____ | _______ | ______ |
| 1.2.1.2 | 0.5 | Sketch  | _____ | _______ | ______ |
| 1.2.1.3 | 0.5 | Photo   | _____ | _______ | ______ |

#### 1.2.2 - ASH module after layer1.1.conv2 and layer3.0.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.2.2.1 | 0.5 | Cartoon | _____ | _______ | ______ |
| 1.2.2.2 | 0.5 | Sketch  | _____ | _______ | ______ |
| 1.2.2.3 | 0.5 | Photo   | _____ | _______ | ______ |

#### 1.2.3 - ASH module after layer1.1.conv2 and layer3.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.2.3.1 | 0.5 | Cartoon | _____ | _______ | ______ |
| 1.2.3.2 | 0.5 | Sketch  | _____ | _______ | ______ |
| 1.2.3.3 | 0.5 | Photo   | _____ | _______ | ______ |

#### 1.2.4 - ASH module after layer2.1.conv2 and layer3.0.conv1

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.2.4.1 | 0.5 | Cartoon | _____ | _______ | ______ |
| 1.2.4.2 | 0.5 | Sketch  | _____ | _______ | ______ |
| 1.2.4.3 | 0.5 | Photo   | _____ | _______ | ______ |

#### 1.2.5 - ASH module after layer2.1.conv2 and layer3.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.2.5.1 | 0.5 | Cartoon | _____ | _______ | ______ |
| 1.2.5.2 | 0.5 | Sketch  | _____ | _______ | ______ |
| 1.2.5.3 | 0.5 | Photo   | _____ | _______ | ______ |

#### 1.2.6 - ASH module after layer3.0.conv1 and layer3.1.conv2

| Experiment | Mask out ratio | Target | Accuracy | Loss | Improvement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1.2.6.1 | 0.5 | Cartoon | _____ | _______ | ______ |
| 1.2.6.2 | 0.5 | Sketch  | _____ | _______ | ______ |
| 1.2.6.3 | 0.5 | Photo   | _____ | _______ | ______ |

#### Average improvements

| Experiment | Placement | Avg Improvement |
| :---: | :---: | :---: |
| 1.2.1 | layer1.1.conv2, layer2.1.conv2 | ______ |
| 1.2.2 | layer1.1.conv2, layer3.0.conv1 | ______ |
| 1.2.3 | layer1.1.conv2, layer3.1.conv2 | ______ |
| 1.2.4 | layer2.1.conv2, layer3.0.conv1 | ______ |
| 1.2.5 | layer2.1.conv2, layer2.1.conv2 | ______ |
| 1.2.6 | layer3.0.conv1, layer3.1.conv2 | ______ |