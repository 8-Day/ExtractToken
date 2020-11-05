from requests import Session
from stdiomask import getpass
from simplejson.errors import JSONDecodeError

def extract(username: str, password: str) -> str or bool:
		"""
		Your username should be an email
		Example username: user@mail.com.
		"""
		session = requests.Session()
		session.get('https://discord.com')
		login_data = json.dumps({
			'captcha_key': '',
			'email': username,
			'login_source': '',
			'password': password,
			'undelete': 'false'
		})
		try:
			session.headers.update({'Content-Type': 'application/json'})
			data = session.post("https://discord.com/api/v6/auth/login", data=data).json()
			return data['token'] if "token" in data.keys() else False
		except:
			return

if __name__ == "__main__":
		"""
		Here I'm basically going to just simply ask for the login and mask password input with *
		If you import the module, you'd have to call the above function with the data required.
		When creds are given, I'll call the function and if it returns 'False', the login failed.
		"""
		for attempt in range(3):
				username = input('Username[email]: ')
				password = getpass()
				token = extract(username, password)
				print(token if token else f"[{str(attempt)}/3] Failed to extract token.")
