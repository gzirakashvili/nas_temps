import requests, json, time, os
last_data = []
f = open('sample.json')
data = json.load(f)
count = 0
try:
    for i in data['data']:
        for model in i['models']['data']:
            gen = requests.get('https://api.wheel-size.com/v2/generations/?make='+i['slug']+'&model='+model['slug']+'&user_key=f07f9d78b51de62d9546049d2771d5d0')
            gen = gen.json()
            for c in gen['data']:
                mod = requests.get('https://api.wheel-size.com/v2/modifications/?make='+i['slug']+'&model='+model['slug']+'&generation='+str(c['slug'])+'&user_key=f07f9d78b51de62d9546049d2771d5d0')
                mod = mod.json()
                params = requests.get('https://api.wheel-size.com/v2/search/by_model/?make='+i['slug']+'&model='+model['slug']+'&generation='+str(c['slug'])+'&modification='+mod['data'][0]['slug']+'&user_key=f07f9d78b51de62d9546049d2771d5d0')
                params = params.json()
                last_data.append(params['data'])
        del data['data'][0]
    with open("data.json", "w") as outfile:
        json.dump(last_data, outfile, indent=4, sort_keys=True)
        print("ფაილი ჩაიწერა წარმატებით in Try Last+Data")
except Exception as e:
    print(e)
    with open("sample2.json", "w") as outfile:
        json.dump(data, outfile, indent=4, sort_keys=True)
        print("ფაილი ჩაიწერა წარმატებით Out Data")
    with open("data.json", "w") as outfile:
        json.dump(last_data, outfile, indent=4, sort_keys=True)
        print("ფაილი ჩაიწერა წარმატებით Out Last Data")
