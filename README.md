# IndustryClassification

## About Problem 
![](https://miro.medium.com/max/960/0*NjOVwfcpoIYT7FxB.)

### Background on the Industry Classification
You can think of the job industry as the category or general field in which you work. On a job application, "industry" refers to a broad category under which a number of job titles can fall. For example, sales is an industry; job titles under this category can include sales associate, sales manager, manufacturing sales rep, pharmaceutical sales and so on.

### Background on the Original NLP Problem
The problem is supervised text classification problem, and our goal is to investigate which supervised machine learning methods are best suited to solve it. Given a new job title that comes in, we want to assign it to one of 4 industry categories. The classifier makes the assumption that each new complaint is assigned to one and only one category. This is multi-class text classification problem.

## About dataset
1. The Dataset that has two variables (Job title & Industry) in a csv format of more than 8,500 samples.

2. The dataset is imbalanced (Imbalance means that the number of data points available for different classes is different).

3. [Click here to view and download the dataset. ](https://drive.google.com/file/d/1W_MO19MlDDUn0qCfxEaVxGKKlKHsFFly/view)
It is also available in the Repo if the link fails to connect.

## About Model: My solution to the problem
When working on a supervised machine learning problem with a given data set, we try
different algorithms and techniques. The same principles apply to text (or document)
classification where there are many models can be used to train a text classifier. The
answer to the question “What machine learning model should I use?” is always “It
depends.” Even the most experienced data scientists can’t tell which algorithm will
perform best before experimenting them.
In the shade of that, i tried 3 types of models (LinearSVC, Multi Nominal NB, Logistic
Regression). I also tried to use simple features out of text (CountVectorizier and TF-IDF)
and complex features (word2vec) while the second is supposed to be promising, it
unfortunately was not the best results. So, I just kept the results of the first 3
approaches with simple features in the notebook.

### Cleaning the data and preparing for model.
Firstly, I noticed that there are a lot of duplicates in the data instances (job titles). The
unique job titles in data were 3000+ while the entire data was 8000+.So, the first
cleaning technique I performed was removing the duplicates in the data. I decided that
because if those duplicates are to appear in both train and test sets that would produce
a false accuracy increase as the model would have seen this data before losing all what
a test data supposed to mean which is unseen data to the model.
Secondly, I applied various text preprocessing techniques including removing stop
words (the,a,...), removing words less than 2 letters, removing numbers and  using
lower case for all the text . I tried also lemmatization and stemming the words but that
didn’t do so well when processed in classification.

### Choice of Classiffier
I tried three classifiers (LinearSVC, Multinomial NaiveBayes, LR), each for the reason of
experimenting and trying different approaches to discover what is best for my data.
Multinomial NB is a good base for the problem, LinearSVC is regarded to be one of the
best text classification algorithms and LR is a simple and easy to understand algorithm.
I choose my final model to be the highest in measure (accuracy) of those three
classifiers which was LinearSVC which won over NB with 1% and over LR with 2%, so i
would say all three classifiers did nice.

### Dealing with Data Imbalance 
When we encounter such problems, we are bound to have difficulties solving them with
standard algorithms. Conventional algorithms are often biased towards the majority
class, not taking the data distribution into consideration.In the worst case, minority
classes are treated as outliers and ignored. There are several ways to deal with
Imbalance learning such as upsampling, downsampling and adding class weights into
consideration when training.
Interestingly, when I removed the duplicates it turned out to be most of them were in
the majority class (“IT”). This semi-solved the imbalance problem at least between three
classes, and one class was yet too small relative to them. So, I also decided to add
sample weights to the classifier when training to further solve this issue of imbalance.

### Limitations and possible improvements
My limitations are mostly in the data, although I tried to handle class imbalance with
sample weights and removing those duplicates, misclassifying for classes with lower
relative samples still occurs (My model would fail for this case). Normally The text
classification problem is a problem that requires a lot of data. Those pretrained models
achieving state of the art performance have millions and billions of words to play with.

I think my model performance can be further improved if the data was more in that
case. Removing the duplicates cut the size of the data into halves leaving me with
3000+ samples only to play with. Also after the train-test split it went down to 2000+
samples only. I also think using a pre-trained word embeddings model like Word2vec or
GloVe on my small dataset would further increase my model performance.


## About Deploying the Model: Flask API 
I used Flask API to create a RESTful API for my model. The Model is not recompiled or trained each request, it just predicts upon the given data in request.

### To test and use my Model's RESTful API service:

1. The Server only supoorts GET Requests. 

2. The Server is run by simply running the script from terminal using command (python api_server.py) 

3. After running the server you can direct GET requests to it using Postman or any other tool.

### Example Request/Response:

-Request: "http://127.0.0.1:5000/model/api/JS developer"  (Job title added to request)

-Response: "IT" (Predicted Industry by model)




