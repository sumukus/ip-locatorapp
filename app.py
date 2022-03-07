from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def getIPDetails(ip_address):
	ip_loc = requests.get(f"https://ipapi.co/{ip_address}/json/").json()
	required_ip_loc = {
				"IP Address": ip_loc['ip'],
				"Version": ip_loc['version'],
				"Country": ip_loc['country_name'],
				"Country Code": ip_loc['country_code'],
				"Region": ip_loc['region'],
				"City": ip_loc['city'],
				"Country Capital": ip_loc["country_capital"],
				"Continent Code": ip_loc['continent_code'],
				"Latitude": ip_loc['latitude'],
				"Longitude": ip_loc['longitude'],
				"Time Zone": ip_loc['timezone'],
				"Country Calling Code": ip_loc['country_calling_code'],
				"Currency": ip_loc['currency'],
				"Currency Name": ip_loc['currency_name'],
				"Language": ip_loc['languages'],
				"Country Area": ip_loc['country_area'],
				"Country Population": ip_loc['country_population'],
				"ASN": ip_loc['asn'],
				"Organization": ip_loc['org']

			}

	return required_ip_loc


@app.route("/", methods=["POST", "GET"])
def index():
	required_ip_loc = dict()
	if request.method == "POST":
		if request.form.get("getMyIPDetails") == "myIPDetails":
			ip_address = requests.get("https://api64.ipify.org?format=json").json()['ip']
			required_ip_loc = getIPDetails(ip_address)
			return render_template("index.html", ip_location=required_ip_loc)

		if request.form.get("getIPDetails") == "getIPDetails":
			ip_address = request.form.get("ip_address")
			required_ip_loc = getIPDetails(ip_address)
			return render_template("index.html", ip_location=required_ip_loc)

	return render_template("index.html", ip_location=required_ip_loc)


if "__name__" == "__main__":
	app.run(debug=True)
