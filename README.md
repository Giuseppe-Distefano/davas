# DAVAS - Domain Adaptation Via Activation Shaping

Repository for the "*Activation Shaping for Domain Adaptation*" project

<a href="https://didattica.polito.it/pls/portal30/gap.pkg_guide.viewGap?p_cod_ins=01URWOV&p_a_acc=2024&p_header=S&p_lang=IT&multi=N">Advanced Machine Learning</a> course 2023/2024 @ <a href="https://www.polito.it/">PoliTo</a>

## Roadmap

- [ ] Before starting
  - [ ] Read paper [1]
  - [ ] Read paper [2]
  - [ ] Impostare dataset e ambiente di sviluppo utilizzando il repository [3]
- [ ] Reproduce the baseline
  - [ ] Train the unmodified feature extractor (ResNet-18) and the object classifier (one FC layer for category prediction), minimizing Cross-Entropy loss on the source domain
  - [ ] Test model on target domain *Cartoon*
  - [ ] Test model on target domain *Sketch*
  - [ ] Test model on target domain *Photo*
- [ ] Activation shaping module
  - [ ] Implement custom activation shaping layer, using *forward_hook* function
  - [ ] Insert activation shaping module after a layer in the base architecture
- [ ] Random activation maps
  - [ ] Define several versions of **M**, with different ratios of zeros and ones
  - [ ] Train network on the source domain
  - [ ] Test network on the target domain
- [ ] Adapting activation maps across domains
  - [ ] Define **M** using input samples from target domain
  - [ ] Test network using samples from source domain as input. Collect results
  - [ ] Compare results from previous point with labels of source domain
- [ ] Binarization ablation
  - [ ] Define **M** without binarization and multiply by **A**
  - [ ] Binarize **M**
  - [ ] Compute TopK values of **A**
  - [ ] Set to 0 all elements of **M** that are not in the TopK of previous point
  - [ ] Multiply **A** and **M**
  - [ ] Reproduce points 2 and 3

## Project structure

- *Material* - Project presentation and introduction to Domain Adaptation
- *Papers* - PDFs of suggested papers
- *Skeleton* - Starting project

## Starting project

<a href="https://arxiv.org/abs/1505.07818">GitHub project repository</a>

## Useful links

### Papers

1. <a href="https://arxiv.org/abs/2209.09858">Djurisic - "Extremely Simple Activation Shaping for Out-of-Distribution Detection" - ICLR 2023</a>
2. <a href="https://arxiv.org/abs/1505.07818">Ganin, Yaroslav - "Domain-adversarial training of neural networks" - The journal of machine learning research 17.1 (2016)</a>
3. PACS Dataset, <a href="https://arxiv.org/abs/1710.03077">Li, Da - "Deeper, broader and artier domain generalization" - ICCV 2017</a>
4. <a href="https://web.stanford.edu/~nanbhas/blog/forward-hooks-pytorch/">Forward hooks PyTorch</a>
