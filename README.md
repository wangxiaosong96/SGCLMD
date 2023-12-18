# SGCLMD
### SGCLMD: Signed Graph-based Contrastive Learning Model for Predicting Somatic Mutation-Drug Association 


![image](https://github.com/wangxiaosong96/SGCLMD/blob/main/SGCLMD-main/Images/graph.png)

## Tutorial
1. Split data for cross validation and indenpendent test experiment via the script split_data.py: python split_data.py fold_number DATANAME seed_indent seed_cross

2. To perform cross validation for finding the optimal hyperparameters by running the script command_optimal.py (if you don't want to finetune the hyperparameters, just skip this step):

3. python command_optimal.py --dataName DATANAME --exp_name mid_dim/num_layer/alp_beta --seed_cross seed_cross --seed_indent seed_indent

To get the experiment results by running the script command_optimal.py

## Requirements
numpy 1.18.0

pandas 1.1.0

scipy 1.4.1

scikit-learn 0.22

tensorflow 1.15.0

pytorch 1.6.0

python 3.7.1

## Contact

Please feel free to contact us if you need any help: xiaosongwang@ahau.edu.cn
