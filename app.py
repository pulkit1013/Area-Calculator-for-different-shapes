from flask import Flask,render_template,request

#Declare the app

app=Flask(__name__)

#Start an app route
@app.route('/')

#Declare the main function
def main():
    return render_template('app.html')

#Form submission URL
@app.route('/calc', methods=['POST',"GET"])
def send(circle=sum,square=max,radius=min):
    
#     ---------FOR POST METHOD----------
    if request.method=='POST':
        #Start Pulling DATA from form input
        X=request.form['X']

        sum=3.14*float(X)*float(X)
        max=float(X)*float(X)
        min=float(X)
        return render_template('app.html',circle=sum,square=max,radius=min)
#   --------FOR GET METHOD---------------
    else:
        
        X=request.args['X']
        sum=2*3.14*float(X)
        max=float(X)*float(X)
        min=float(X)

        return render_template('app.html',circle=sum,square=max,radius=min)
