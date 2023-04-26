
    #  Install the Python Requests library:
# `pip install requests`
import requests
import json
import re



def send_request(request):
    response = requests.get(
        url="https://app.scrapingbee.com/api/v1/store/google",
        params={
            "api_key": "1YMLW4SSRC7R77D1YHRS2Q07KD652AVQG871V278TIN25K3QGF1T6WPX6QPSKBSR7KGWULQ9CZ4UTLOG",
            "search": request,
            "nb_results": 10000
        },

    )
    #print('Response HTTP Status Code: ', response.status_code)
    #print ("----hello---")
    data=response.content
    # Assume 'data' is the bytes object containing JSON data
    json_data = data.decode('utf-8') # convert bytes to string
    json_obj = json.loads(json_data) # parse the JSON string into a Python object

    #print('---hiii',json_obj)
    #print('----dataaaaa',type(json_obj))
    #print('Response HTTP Response Body: ', response.content)
    print(json_obj)
    new_lst=[]
    for i in json_obj['organic_results']:
        new_lst.append(i['url'])
    print(new_lst)

    # code to match the list of matched youtube links


    # Define the regular expression pattern to match YouTube channel links
    pattern = r"(?:https?:\/\/)?(?:www\.)?(?:m\.)?youtube\.com\/(?:c\/([\w-]{1,50})|channel\/([\w-]{1,50})|([\w-]+))(?:\/[\w=?&%-]*)?"
    new_lst2=[]

    # Loop through the URLs and search for the pattern
    for url in new_lst:
        match = re.search(pattern, url)
        if match:
            print(match.group(1)) # prints the channel ID
            if match.group(1) != None:
            
                new_lst2.append(match.group(1))

    return new_lst,new_lst2
    
