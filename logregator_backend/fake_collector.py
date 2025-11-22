import os
import time
import json
import random
import urllib.request
from datetime import datetime

class App:
    API_URL = os.environ.get('API_URL', '')
    API_TOKEN = os.environ.get('API_TOKEN', '')
    
    # Sample quotes to replace Faker gem
    YODA_QUOTES = [
        "Do or do not. There is no try.",
        "Fear is the path to the dark side.",
        "In a dark place we find ourselves.",
        "Train yourself to let go of everything you fear to lose.",
        "The greatest teacher, failure is.",
        "Wars not make one great.",
        "Size matters not.",
        "Luminous beings are we, not this crude matter.",
        "Patience you must have.",
        "Always pass on what you have learned."
    ]
    
    DUNE_QUOTES = [
        "I must not fear. Fear is the mind-killer.",
        "The mystery of life isn't a problem to solve, but a reality to experience.",
        "Deep in the human unconscious is a pervasive need for a logical universe.",
        "The beginning of knowledge is the discovery of something we do not understand.",
        "Without change, something sleeps inside us.",
        "Hope clouds observation.",
        "The mind can go either direction under stress.",
        "Seek freedom and become captive of your desires.",
        "He who controls the spice controls the universe.",
        "The sleeper must awaken."
    ]
    
    def log(self):
        data = self.data()
        headers = self.headers()
        
        # Prepare the request
        req = urllib.request.Request(
            self.API_URL,
            data=json.dumps(data).encode('utf-8'),
            headers=headers,
            method='POST'
        )
        
        try:
            with urllib.request.urlopen(req) as response:
                return {
                    'status': response.status,
                    'body': response.read().decode('utf-8')
                }
        except urllib.error.HTTPError as e:
            return {
                'status': e.code,
                'body': e.read().decode('utf-8')
            }
        except Exception as e:
            return {
                'status': 0,
                'body': str(e)
            }
    
    def data(self):
        return {
            'ts': datetime.now().isoformat(),
            'level': random.choice(['info', 'warning', 'error']),
            'scope': random.choice(['db', 'controller', 'job', 'view']),
            'message': random.choice(self.YODA_QUOTES + self.DUNE_QUOTES)
        }
    
    def headers(self):
        return {
            'Content-Type': 'application/json',
            'X-Api-Token': f"Bearer {self.API_TOKEN}"
        }

if __name__ == '__main__':
    app = App()
    
    while True:
        sleep_time = random.randint(0, 10) / 10.0
        time.sleep(sleep_time)
        
        response = app.log()
        print(response['status'])
        # Uncomment the line below if you want to print the response body
        # print(f"{response['status']}: {json.loads(response['body']).get('data')}")