# SGCLMD: Signed Graph-based Contrastive Learning Model for Predicting Somatic Mutation-Drug Association 

![image](https://github.com/wangxiaosong96/SGCLMD/blob/main/SGCLMD-main/Images/graph.png)

## Datasets
### Database
We first consolidated the four datasets by removing duplicates and retaining three columns representing mutation-drug association data. The processed data was then matched with the mutant-drug name file, and the encoded data was retained. The sensitivity and resistance of the associations were encoded as 1 and -1, respectively. Finally, we split the dataset to generate the file "drug_mutation_training.txt".

**We constructed a somatic mutation-drug association dataset. we randomly select 10% of the links as test set, 5% for validation set, and the remaining 85% as training set for each of our datasets. You can download it in datasets foalder.**

## Requirements
In order to run this code, you need to install following dependencies:
```
pip install torch numpy sklearn torch_geometric
```
python >= 3.9

torch >= 1.7.0

scikit-learn >= 0.24.0

torch_geometric >= 2.1.0.post1

## Run Example
```
python train.py --dataset=drug_mutation --epochs=300
```
## Contact

Please feel free to contact us if you need any help: xiaosongwang@ahau.edu.cn
