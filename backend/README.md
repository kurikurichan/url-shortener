# url shortener


The URL shortener application is used to map a URL to a shorter URL. Some reasons you might find this helpful are


- **Character Limit** Some platforms, or online forms, might impose character limits on posts or messages. 
- **Readability and Shareability**  Long URLs with complex strings of characters can be difficult to read and comprehend, especially when sharing them verbally or in print. 
- **Aesthetics and Appearance** Shortened URLs can enhance the visual appeal of content.


## Installation

This app was created using Python 3.11 and is suggested to create a python virtual environment to install the needed python modules.
Example how to create your virtual environment in the directory your application code lives. 

Make sure to be in the backend directory for the installation
```
cd backend
python3 -m venv venv
source venv/bin/activate

```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install python packages from requirements.txt file.

```
pip install -r requirements.txt

```

Use this command to run test cases using unnitest.

```
 python -m unittest test_urls.py

```
Examples how to post your URL
```
curl -X POST -H "Content-Type: application/json" -d '{"url":"https://www.amazon.com/Citizen-Eco-Drive-Weekender-Chronograph-Titanium/dp/B09CQGYDFN"}' http://127.0.0.1:5000/url -i
```

Returns a JSON object
```commandline
{
  "key": "wBQx0K", 
  "long_url": "https://www.amazon.com/Citizen-Eco-Drive-Weekender-Chronograph-Titanium/dp/B09CQGYDFN", 
  "short_url": "http://127.0.0.1:5000/url/wBQx0K"
}
```
Example how to Get your URL
```commandline
curl http://127.0.0.1:5000/url/wBQx0K -i
```
Returns the location header, so the Long URL will be displayed.
```commandline
HTTP/1.0 302 FOUND
Location: https://www.amazon.com/Citizen-Eco-Drive-Weekender-Chronograph-Titanium/dp/B09CQGYDFN
Content-Type: text/html; charset=utf-8
Content-Length: 0
Server: Werkzeug/1.0.1 Python/3.11.2
Date: Wed, 12 Jul 2023 02:56:37 GMT
```




