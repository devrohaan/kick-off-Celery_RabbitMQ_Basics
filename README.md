[![Wisdomic Panda](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/panda.png)](http://www.rohanbagwe.com/)  **Wisdomic Panda**
> *Hold the Vision, Trust the Process.*

# Beginner's guide to "Celery: Distributed Task Queue"  with "RabbitMQ: Message Broker" [![Latest Status](https://img.shields.io/badge/Celery-4.2-brightgreen.svg)](http://www.celeryproject.org/)
*... a technique used for asynchronous computation of expensive queries/processes/tasks.*
###### EOD/BOD Issue, May 2018.

<img src="https://github.com/robagwe/wisdomic-panda/blob/master/imgs/celery1.gif" width=750>

###### Asynchronous processing in python using Celery and its best fit RabbitMQ.

### What is Asynchronous?

Asynchronous operation means that a process operates independently of other processes, whereas synchronous operation means that the process runs only as a result of some other process being completed or handing off operation.

Asynchronous & Synchronous in Real-world

**Synch:**

> You're in a queue to get a movie ticket. You cannot get one until everybody in front of you gets one, and the same applies to the people queued behind you.

**Asynch:**

> You're in a restaurant with many other people. You order your food. Other people can also order their food, they don't have to wait for your food to be cooked and served to you before they can order. In the kitchen restaurant workers are continuously cooking, serving, and taking orders. People will get their food served as soon as it is cooked.


###### In asynchronous server call  all the operations within your browser doesn't stop while you wait for the response. When the response from the query is received the execution jumps to the callback which is suppose to execute after that particular response is received.


> Consider There is an API which performs below task for the user:
	   
	   
	   def getCristianoRonaldoImages():
		      #Fetch top 100 images of CR7 from google.


This is going to take few minutes to do, at best. Thus, fundamental implementations could be:


**Imple1: Using Normal HTTP request**

Now imagine waiting for response from multiple servers which cane take upto several minutes. Your browser will have to wait till then to do anything else. This has the side effect of making your user wait while you do stuff. Which isn't the worst thing in
the world, but it certainly isn't good. Users sit and stare at a blank screen while your server
feverishly works away.

**Imple2: Using Ajax Request**

Jquery ajax function which calls "CRImageFetch.py" from the server (Let's say it takes 3 minutes to process).

	$.ajax( "CRImageFetch.py" ) 
		 .done(function() {    
			console.log("Download Completed!\n"); 
		});
 		console.log("Hello there!\n")
		
		
If it was a sync call then you will have to wait for 3 minutes till you can see output "Hello there!"  on the screen because the browser will wait for the response from the server.
But, as this is a AJAX call you will most likely see output as:
Hello there!
Download Completed!
###### This is because the execution doesn't stop in async call!

**Even if you use AJAX you are still tieing up valuable connection resources associated with Apache
or Nginx because those live connections (HTTP Requests) aren't really doing anything but waiting
for the pictures to download. They are a limited commodity.**


**Imple3: Celery - Distributed Task Queue**
This takes the "out of process" idea even further by not tying up a HTTP request for very long at
all. The basic idea is the same, except we need to introduce a few more tools outside of the HTTP
server: a message queue.
The concept is simple: intensive processes are moved outside of the request process entirely.
That means instead of a request taking many seconds (or worse, minutes!), you get a bunch of split
second responses like: nope, CR7 pictures aren't ready, nope, still waiting… and finally, here are
your CR7 pictures!

![flow](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/flow.png)


### What is celery?
Celery is an asynchronous task queue. It can be used for anything that needs to be run
asynchronously. For example, background computation of expensive queries.
RabbitMQ is a message broker widely used with Celery. This is now confusing. 

###### Why do we need another thing called broker?
> *“It’s because Celery does not actually construct a message queue itself, so it needs an extra message
transport (a broker) to do that work. You can think of Celery as a wrapper around a message broker.”*
In fact, you can choose from a few different brokers, like RabbitMQ, Redis, or a database (e.g.,
a Django database)


### Celery and RabbitMQ Architecture: 

![arch](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/celery.png)

**Message Broker**
The Broker (RabbitMQ) is responsible for the creation of task queues, dispatching tasks to task
queues according to some routing rules, and then delivering tasks from task queues to workers.
**Consumer (Celery Workers)**
The Consumer is the one or multiple Celery workers executing the tasks. You could start many
workers depending on your use case.
**Result Backend**
The Result Backend is used for storing the results of your tasks.

> So in nutshell:
Your application just needs to push messages to a broker, like RabbitMQ, and Celery workers will pop
them and schedule task execution.

#### :construction: [Configuration](https://github.com/robagwe/kick-off-Celery_RabbitMQ_Basics/blob/master/Cookbook.txt)

#### :construction: [SourceCode](https://github.com/robagwe/kick-off-Celery_RabbitMQ_Basics/blob/master/CeleryApp.py)

### Create the app and set the broker location (RabbitMQ)
        
        app = Celery('CeleryApp',
                      backend='rpc://',
                      broker='amqp://rdbagwe: rdbagwe123@localhost/rdbawge_vhost',
                      include='Tasks')
 

**Above code creates:**
- A Celery application named 'CeleryApp' [CeleryApp.py](https://github.com/robagwe/kick-off-Celery_RabbitMQ_Basics/blob/master/CeleryApp.py)
- A broker on the localhost that will accept message via *Advanced Message Queuing Protocol
(AMQP), the protocol used by RabbitMQ
- A response backend where workers will store the return value of the task so that clients can retrieve it
later (remember that task execution is asynchronous). If you omit backend, the task will still run, but 
the return value will be lost. rpc means the response will be sent to a RabbitMQ queue in a Remote
Procedure Call pattern.
- Include indicates the source file which contains the list of tasks that can be addressed by the
Celery Workers




### Application:
These are some common use cases:

- Running something in the background. For example, to finish the web request as soon as
possible, then update the user’s page incrementally. This gives the user the impression of
good performance and “snappiness”, even though the real work might actually take some
time.
- Running something after the web request has finished.
- Making sure something is done, by executing it asynchronously and using retries.
- Scheduling periodic work.

And to some degree:

- Distributed computing.
- Parallel execution.
> Most frequent uses are horizontal application scaling by running resource intensive tasks on Celery
workers distributed across a cluster, or to manage long asynchronous tasks in a web app, like
thumbnail generation when a user post an image. This guide will take you through installation and
usage of Celery with an example application that delegate file downloads to Celery workers via
rabitMQ.


**Follow [this](https://www.linode.com/docs/development/python/task-queue-celery-rabbitmq/) for more information on production setup.**



		-------------- worker1@rohanbagwe v4.2.0 (windowlicker)
		---- **** -----
		--- * *** * -- Linux-4.13.0-36-generic-x86_64-with-debian-stretch-sid 2018-07-04 00:34:37
		-- * - **** ---
		- ** ---------- [config]
		- ** ---------- .> app: CeleryApp:0x7fef1039e2b0
		- ** ---------- .> transport: amqp://rdbagwe:**@localhost:5672/rdbawge_vhost
		- ** ---------- .> results: rpc://
		- *** --- * --- .> concurrency: 4 (prefork)
		-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
		--- ***** -----
		-------------- [queues]
		 .> celery exchange=celery(direct) key=celery

## [Flower](https://flower.readthedocs.io/en/latest/) - a web based tool for monitoring and administrating Celery clusters. 
![flower](https://github.com/robagwe/wisdomic-panda/blob/master/imgs/Flower.png)

#### :construction: Get hands on: [Kick-off](https://github.com/robagwe/kick-off-Celery_RabbitMQ_Basics/blob/master/Task_run.py)

#### :heavy_exclamation_mark: I run on Mac OS/Ubuntu so you might have to slightly modify the code to make it work in your env.

### :coffee: Ingredients:

- celery
- rabbitMQ
- python
- Anaconda, spyder
- Ubuntu 16.4 LTS



## <img src="https://github.com/robagwe/wisdomic-panda/blob/master/imgs/acr.png" width="50">   Hey Buddy!</img>

> This repository explains asynchronous processing in python using Celery and its best fit RabbitMQ. If you have any suggestions for more commands that should be on this page, let me know or consider submitting a pull request so others can benefit from your work. Thank you very much for reaching out! Please follow if you find it handy and hit :star: to get more kick-off repo updates.

:email: [Drop In!!](https://www.rohanbagwe.com) Seriously, it'd be great to discuss Technology.

> *"You’re only here for a short visit. Don’t hurry, don’t worry. And be sure to smell the flowers along the way." — Walter Hagen*


<img src="https://github.com/robagwe/wisdomic-panda/blob/master/imgs/rabbit.gif" width = 750>

