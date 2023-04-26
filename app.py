from flask import Flask, jsonify,render_template,request
import findResults
import json
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def get_input():
    name=request.form['name']
    lst1,lst2=findResults.send_request(name)
    

    # Create the JSON objects
    url_json = [{'url': str(url)} for url in lst1]
    name_json = [{'YouTube channel': str(name)} for name in lst2]
    # Combine the JSON objects into a single dictionary
    url_dict = json.loads(url_json)
    channel_dict = json.loads(name_json)

    return render_template('displayresults.html',url_dict,channel_dict)


if __name__=="__main__":
    app.run(debug=True)