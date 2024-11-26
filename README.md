# What is Automated Machine Learning?

![image](https://github.com/user-attachments/assets/10a9ab18-e52f-4c4b-8b1c-313ece98e3cd)

Automated Machine Learning is a system designed to automate the process of training machine learning models. It integrates various stages from preprocessing, to model evaluation automatically, reducing manual involvement and enabling faster and more consistent training.

## What is the difference between Traditional ML and Automated ML??

Traditional Machine Learning refers to the conventional process of manually developing machine learning models. This process usually involves a series of iterative steps that require expertise in data preprocessing, feature engineering, model selection, and hyperparameter tuning. Each step requires human intervention to optimize the model for a particular problem.

![image](https://github.com/user-attachments/assets/6349a51d-f43b-42e2-804f-903826d60e0a)

Whereas, Automated Machine Learning (AutoML) is an approach that automates the entire machine learning path, from data preprocessing to model selection and hyperparameter optimization. AutoML systems aim to make machine learning more accessible to non-experts by reducing the need for manual intervention, so that data scientists and business analysts can focus on higher-level tasks.

### Key Differences Between AutoML and Traditional ML

![image](https://github.com/user-attachments/assets/2a400c67-5582-4d25-90d3-74e8bc951b2a)

## How to Automate Machine Learning Work?

![image](https://github.com/user-attachments/assets/8ebb297b-92f8-41ad-bc9e-bc8e4b444dfd)

The Automated Training Model works as follows:
1. Data Preprocessing: The data used in the model has gone through a preprocessing stage or is already in a clean condition. This preprocessing includes data cleaning, normalization, and transformations needed to make the data ready for further processing by the model. Clean and well-structured data can be directly inputted into the model without the need for additional intervention.
2. Model Training: After the data has been processed, the model will undergo a training process using the prepared dataset. During this process, the model will learn from the data to make appropriate predictions or classifications. The results of the model training will be assessed based on accuracy and other performance.
3. Evaluation and Storage: The results of the model training will be evaluated to determine its quality. The model is designed to only store the training results if the accuracy obtained reaches a predefined threshold of above 85%. If the accuracy does not meet this standard, the training results will not be saved, and the model will return to the training stage for further improvement. Qualified training results will be saved in the provided storage, in the form of a model training result file that can be used for future predictions.

Automated model training has several benefits such as reducing the time required for model training, improving overall efficiency. In addition, it ensures consistency in model training with predefined standards, avoiding variability caused by human factors. The use of this model also allows for a larger scale of training and more flexibility with various dataset sizes.

However, this model has specifications and limitations. For example, if the model is designed to predict employee performance, only data relevant to employee performance indicators can be processed. Data that does not have a corresponding target column or is irrelevant to the purpose of the model cannot be processed, ensuring that the model is trained specifically and accurately for a predefined task.


