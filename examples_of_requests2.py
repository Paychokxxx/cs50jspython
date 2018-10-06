import requests

def main():
    base = input("First Currency:")
    other = input("Second Currency:")
    res = requests.get("https://api.exchangeratesapi.io/latest",
        params = {"base": base, "symbols": other}) #?base=USD&symbols=EUR

    if res.status_code !=200: 
        raise Exception("Error: API request unsuccessful.")
    
    data = res.json()
    print(data)
    value = data['rates']['EUR']

    print(f"1 {base} is equal to {value} {other}")

if __name__ == "__main__":
    main()