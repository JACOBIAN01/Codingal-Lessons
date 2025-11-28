import requests , html , random

api_url = "https://opentdb.com/api.php?amount=1&category=9&type=multiple"

def Get_Question():
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data['results']
    
q = Get_Question()
print(q[0].get('question'))
print(q[0].get('incorrect_answers')[0])
print(q[0].get('correct_answer'))
print(q[0].get('incorrect_answers')[1])
print(q[0].get('incorrect_answers')[2])
