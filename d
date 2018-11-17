import requests
with open("phone.txt") as f: 
    lines= f.readlines()
    
from flask import Flask
app = Flask(__name__) 

@app.route('/') 
def index(): 
    name=request.args.get('name') 
    print(name, flush=True) 

 
    for k in lines: 
        a = k.split(',') 
        if a[0] == name: 
            print(a, flush=True) 
            return a[0] +','+ a[1]
            continue
        return "not found"

   
if __name__ == '__main__': 
    app.run(debug=True) 
