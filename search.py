import requests
import json
import smtplib
from datetime import date
from dateutil.relativedelta import relativedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email import encoders
from flight_search import FlightSearch

# f = open('/home/aziz/Downloads/flight-club-end-2/info.json')
# data = json.load(f)

def send_email(to, data):
	# filename = ".pdf"
	receivers = [to]
	subject= "Flight Details from Flight Club!"
	server = smtplib.SMTP('smtp.gmail.com', 587)
	message = MIMEMultipart()
	message["From"] = "Flight Club"
	message['To'] = '_'.join(receivers)
	message["Subject"] = subject
	# with open(filename, "rb") as attachment:
	# 	part = MIMEBase("application", "octet-stream")
	# 	part.set_payload(attachment.read())
	# 	encoders.encode_base64(part)
	# part.add_header(
	# "Content-Disposition",
	# f"attachment; filename= {filename}",
	# )
	html = """\
	<!DOCTYPE html>
	<html>
		<head?></head>
		<body style="padding: 5%;">
		<p><strong>Hey, Flight Club here - welcome and thanks for joining our club! Here&rsquo;s a quick peek into what we&rsquo;re all about and what you can expect with our cheap flight deals...<br /><br /><strong><strong>Firstly, we&rsquo;re&nbsp;not&nbsp;a flight comparison site like Skyscanner or Kayak and we're&nbsp;not&nbsp;a booking site. Instead, think of us as a helpful friend who gives you a buzz when we&rsquo;ve found a ridiculously cheap flight deal, with every detail you need to book it and saving you hours of searching in the process. We monitor thousands of flights to destinations all around the globe and notify you when various routes go really, reaaally cheap!<br /><br /><strong><strong><strong><strong>W</strong>e're completely unbiased and&nbsp;<strong>we don't accept referral fees from your clicks or bookings, so our sole incentive is to help you score the best deal possible.</strong></strong></strong></strong></strong></strong></strong><br /><br />To give you an idea of some of the deals we find, here are just a few of the flights our members have been able to grab in recent weeks:<br /><br /></p>
			<ul style="background-color: rgb(166, 197, 187); padding: 10px;">
			"""+data+"""
			</ul>
	<p><br /><strong><strong><strong><strong><strong><strong><strong><strong>People often think there&rsquo;s an optimal time to book flights, but the truth is, fares fluctuate&nbsp;all&nbsp;the time and "secret" (unannounced) sales, price drops, and especially&nbsp;error fares&nbsp;are nearly impossible to predict. So, the trick is to look everywhere,&nbsp;all&nbsp;the time - which is exactly what we do! That means you&rsquo;ll have first dibs at booking and saving loads before fares go back up.</strong><br /><br /></strong></strong></strong></strong></strong></strong><strong><strong><strong><strong><strong>If you manage to grab a deal and head off on holiday, all we ask is that you hit reply and let us know you booked it :-)</strong></strong></strong></strong></strong><br /><br />Cheers,<br />Flight Club</strong></p>
	</body>
	</html>
	"""
	# message.attach(part)
	message.attach(MIMEText(html, "html"))
	message = message.as_string()
	# start TLS for security user_to
	server.starttls()
	# Authentication 
	server.login("flightclub2021@gmail.com", "NewYear2021")
	sender = "email"
	try:
		server.sendmail(sender, receivers, message)
	except Exception as e:
		raise e

def check_flights(email, frm, to):
	search = FlightSearch()
	origin_city_code = search.get_destination_code(to)
	destination_city_code = search.get_destination_code(frm)
	six_months = date.today() + relativedelta(months=+6)
	to_time =  six_months
	from_time = date.today()
	# print (date.today(), six_months)
	res =  search.check_flights(origin_city_code, destination_city_code, from_time, to_time)
	print ("data > ",res)
	if res:
		send_email(email, str(res))