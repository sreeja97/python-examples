import requests

if __name__ == "__main__":
    ploads = {'things':2,'total':25}
    r = requests.get('https://httpbin.org/get',params=ploads) #get request
    print(r.text)
    print(r.content)
    print(r.status_code)


    pload = {'username':'Olivia','password':'123'}
    r = requests.post('https://httpbin.org/post',data = pload) #post request
    print(r.text)   
    print(r.json())