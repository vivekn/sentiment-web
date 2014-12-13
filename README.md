# Sentiment

This tool works by examining individual words and short sequences of words (n-grams) and comparing them with a probability model. The probability model is built on a prelabeled test set of IMDb movie reviews. It can also detect negations in phrases, i.e, the phrase "not bad" will be classified as positive despite having two individual words with a negative sentiment. The web service uses a coroutine server based on gevent, so that the trained database can be loaded into shared memory for all requests, which makes it quite scalable and fast. The API is specified [here](http://sentiment.vivekn.com/docs/api/), it supports batch calls so that network latency isn't the main bottleneck.

You can read more about the details of the model in <a href="http://arxiv.org/abs/1305.6143"> this paper </a>. The code for the training module is also open source and <a href="https://github.com/vivekn/sentiment"> available on Github </a>. 

AUTHOR: Vivek Narayanan < vivek.narayanan@outlook.com > 

LICENSE: BSD

	
## Setting up the API endpoint
Setting up the server is a fairly straightforward task, here are the steps:

1. Install pip, the python package manager.
2. cd to the directory containing the sentiment code and run `pip install -r requirements.txt` . This will install the dependencies.
3. Install redis and start the program redis-server. Eg: `redis-server --daemonize yes`. 
Redis is used here only for tracking/stats purposes, if you don't want it remove all references to redis in the code.
4. Finally, create a file called "config.py" and set the parameters as in the example below.

````python    
    HOST="http://ec2-54-xxxx.us-west-2.compute.amazonaws.com" 
    PORT=80 
    STATS_KEY="sentiment_stats" 
    RHOST=''
    RPORT=6379 
    RPASS=None
````
 HOST and PORT refer to where you want to host the python server
 STATS_KEY is the prefix used for the redis entries, RHOST, RPORT are RPASS are the host, port
 and password of the redis server.
 
 Run the server by executing the command `nohup python run.py &`
