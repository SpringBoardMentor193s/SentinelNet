MAYA: Mixture of Attention Yields Results for Tabular Data (February 2025)
Authors: Xuechen Li, Yupeng Li, Jian Liu, Xiaolin Jin, Tian Yang, and Xin Hu.  
Date: Published February 18, 2025  


Overview & Key Innovations

Core Idea: The authors present MAYA, an encoder-decoder Transformer architecture designed specifically for tabular data.

Mixture of Attention (MOA): The encoder uses multiple parallel attention branches. It averages features from these branches, which allows for better management of diverse feature types common in tabular datasets while controlling parameter growth.  


Dynamic Consistency Regularization: They use collaborative learning with a dynamic consistency weight. This improves the robustness of feature representation.  


Decoder with Cross-Attention: The decoder combines tabular feature embeddings with label information through cross-attention. This approach effectively models both intra-instance (within a row) and inter-instance (across rows) interactions.  


Evaluation: MAYA outperforms existing transformer-based methods on classification and regression tasks across various datasets, showing significant empirical gains.  


Why This Paper Stands Out

Recent advancement: It is among the latest published works (Feb 2025) that optimizes transformer architectures for the challenges of tabular data.

Design for diversity: The Mixture of Attention mechanism directly tackles the issue of different feature types, a major challenge in tabular modeling.

Empirical proof: It shows substantial performance improvements in classification and regression, going beyond just theoretical insights.

Other Recent Transformer-Based Papers for Context

TabTreeFormer (Jan 2025): A hybrid tree-transformer model for generating tabular data. It combines tree-based biases with a dual-quantization tokenizer to improve efficiency and quality in synthetic data generation.  
 

TTVAE (Mar 2025): A Transformer-based Variational Autoencoder for creating tabular data. It is notable for using attention in the latent space with interpolation to enhance data generation quality.

TabDPT (Oct 2024): A foundation model for tabular data, allowing in-context learning without task-specific fine-tuning and achieving strong results as models and data grow. 

 
 Summary Table  
Paper / Model | Purpose | Key Feature | Benefit  
--- | --- | --- | ---  
MAYA | Classification/Regression | Mixture of Attention + dynamic consistency + cross-attention | Better handling of feature diversity and interactions  
TabTreeFormer | Data Generation | Hybrid tree-transformer + dual-quantization tokenizer | Efficient, compact, high-quality synthetic data  
TTVAE | Synthetic Data VAE | Attention-enabled latent interpolation | Flexible and effective generative modeling  
TabDPT | Foundation Model | Self-supervised pre-training + in-context learning | Adaptable across datasets, no fine-tuning needed  