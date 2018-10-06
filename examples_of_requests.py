import requests

def main():
    res = requests.get("https://data.fixer.io/api/latest?base=USD&symbols=EUR")
    if res.status_code !=200: 
        raise Exception("Error: API request unsuccessful.")
    
    data = res.json()
    print(data)

    code = data["error"]['code']  #{'success': False, 'error': {'code': 101, 'type': 'missing_access_key', 'info': 'You have not supplied an API Access Key. [Required format: access_key=YOUR_ACCESS_KEY]'}}
    print(code)
    print(f"Received error cose is {code}")

if __name__ == "__main__":
    main()