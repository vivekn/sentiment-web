# Sentiment

This tool works by examining individual words and short sequences of words (n-grams) and comparing them with a probability model. The probability model is built on a prelabeled test set of IMDb movie reviews. It can also detect negations in phrases, i.e, the phrase "not bad" will be classified as positive despite having two individual words with a negative sentiment. The web service uses a coroutine server based on gevent, so that the trained database can be loaded into shared memory for all requests, which makes it quite scalable and fast.

You can read more about the details of the model in <a href="http://arxiv.org/abs/1305.6143"> this paper </a>. The code for the training module is also open source and <a href="https://github.com/vivekn/sentiment"> available on Github </a>. 

AUTHOR: Vivek Narayanan < vivek_n@me.com >

LICENSE: BSD

	
