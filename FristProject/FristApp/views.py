from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    print("welcome/url is requested & display() is executed");#view-function
    #ss-->is the html-data/code
   

    ss='''
       <center>
        <h2 style="color:blue;">
            Hello user,welcome to django Frist-Project Frist-app
                        </h2>
        <h3> This is sreenivas</h3>
        <h4>Visit agian;;; </h4>
            <hr/>
            </center>
            

    '''
    return HttpResponse(ss);
    
    
def show(request):
    ss='''
    <!..
	html webpage to display
	..>
<html>
	<head>
		<title>www.welcome.com</title>
		<style>
			h1{color:blue;}
			h2{color:red;}
			h3{color:brown;}
			h4{color:yellow;}
			h1,h3{background-color:yellow;}
			h2,h4{background-color:violet;}
		</style>
		</head>
		<body>
		<center>
		<h1>Welcome to my web-page***>
		<hr color="brown" width="95%"/>
		<h2>MY SELF SREENIVAS</h2>
		<hr color="yellow", width="85%"/>
		<h3> HOW CAN I HELP YOU</h3>
		<hr color="green", width="75%"/>
		<h4>VISIT AGAIN</h4>
		<hr color="blue", width="65%"/>
		</center>
		</body>
</html>
    
    
    
    '''
    return HttpResponse(ss);
    
        

def hello(request):
	print("hello/ url is requested & hello() is executed");
	ss='''
	<html>
		<head>
			<title>Hello Webpage</title>
			<style>
				h1{
					color:Blue;
					width:90%;
				}
				h2{
					color:Green;
					width:80%;
				}
				h3{
					color:Red;
					width:70%;
				}
				h1,h2,h3{
					background-color:lightblue;
					border:2px Solid Brown;
				}
			</style>
		</head>
		<body>
			<center>
				<h1>Hello User..!!!</h1>
				<hr color='brown' width='80%'/>
				<h2>Welcome to Django-App</h2>
				<hr color='brown' width='60%'/>
				<h3>Have a nice day...</h3>
				<hr color='brown' width='40%'/>
			</center>
		</body>
	</html>
	''';
	return HttpResponse(ss);
    
    
import time;	
def senddatetime(request):
	print("dtime/ url is requested & senddatetime() is executed");
	ct = time.ctime()
	print("Client Request Date & time on server :: ",ct);
	ss='''
	<html>
		<head>
			<title>Date-time Webpage</title>
			<style>
				h1{
					color:Blue;
					width:90%;
				}
				h2{
					color:Green;
					width:80%;
				}
				h3{
					color:Red;
					width:70%;
				}
				h1,h2,h3{
					background-color:lightgreen;
					border:2px Solid Brown;
				}
			</style>
		</head>
		<body>
			<center>
				<h1>Welcome to DJango-User..!!!</h1>
				<hr color='brown' width='80%'/>
				<h2>Server-Date & Time :: </h2>
				<hr color='brown' width='70%'/>
				<h3>''',ct,'''</h3>
				<hr color='brown' width='60%'/>
			</center>
		</body>
	</html>
	''';
	return HttpResponse(ss);
    
    
def demo(request):   
	print("mulitple-Requests-URLs same response");
	htmldata='''<center>
		<h1>Welcome Demo User!!!</h1>
		<hr />
		<h2>This is Same-Output for diff-mulitple-Requests-URLs</h2>
		<hr />
		<h3>Have a Great Day...</h3>
		</center>''';
	return HttpResponse(htmldata);
    
    
#default-url-request-view-func
def homepage(request):
    htmldata='''<center>
        <h1>Welcome to DEFAULT Home-Page!!!</h1>
        <hr />
        <h2>Your Request Page is Not-Found...</h2>
        <hr />
        <h3>Plz try other URL or Links!!!</h3>
    </center>''';
    return HttpResponse(htmldata);


