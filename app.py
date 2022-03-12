from flask import Flask
import os, requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	construct_url = "https://api.openweathermap.org/data/2.5/weather?q=Rijeka&appid=" + "2b7ff133347019b4518aac70754d0056"
	response = requests.get(construct_url)

	list_of_data = response.json()
	print(list_of_data)
	html_data = f"""
    <table border="1">
		<tr>
			<td>Naziv grada</td>
			<td>Kod drzave</td>
			<td>Koordinate</td>
			<td>Temperatura</td>
			<td>Tlak</td>
			<td>Vlaga</td>
		</tr>
		<tr>
			<td>{str(list_of_data['name'])}</td>
			<td>{str(list_of_data['sys']['country'])}</td>
			<td>{str(list_of_data['coord']['lon']) + ' '
				 + str(list_of_data['coord']['lat'])}</td>
			<td>{str(list_of_data['main']['temp']) + 'k'}</td>
			<td>{str(list_of_data['main']['pressure'])}</td>
			<td>{str(list_of_data['main']['humidity'])}</td>
		</tr>
	</table>
    """
	return html_data

if __name__ == "__main__":
	app.run(port=8000, debug=True)