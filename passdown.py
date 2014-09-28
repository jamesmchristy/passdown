#!/usr/bin/env python

print "## Passdown !"
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 


lines = []
def default_lines(): ##builds default list to work on
	for x in range(1,7):
		lines.append([str(x)])
		lines[x-1].append("fine")
		lines[x-1].append("---")

		
default_lines()
		

def print_lines():
	for item in lines:
		print item

print "In an ideal world, things would look like this:"
print_lines()


def any_problems(): #ground zero function	
	print "Which lines are giving you problems, if any? \n(\"1-6\" or \"n\" to send email, \"q\" for quit)"
	problems = raw_input("> ")
	if problems.lower() == "n":
		print "okay cool"
		print_lines()
		send_or_not()
	elif problems.lower() == "q":
		quit()
	elif int(problems) in range(1,7):
		major_or_minor(problems)
	else:
		print "invalid input, try again"
		any_problems()
		
		
def major_or_minor(line):
	print "Are these problems major or minor?\n(\"1\" for major, \"2\" for minor, \"n\" to go back)"
	problem_value = raw_input("> ")
	if problem_value == "1":
		lines[int(line)-1][1] = "major issue(s)"
		print "Please provide additional comments."
		lines[int(line)-1][2] = (raw_input(" >"))
		print "Here is how the table currently looks:"
		print_lines()
		any_problems()			
	elif problem_value == "2":
		lines[int(line)-1][1] = "minor issue(s)"
		print "Please provide additional comments."
		lines[int(line)-1][2] = (raw_input(" >"))
		print_lines()
		any_problems()
	elif problem_value.lower() == "n":
		any_problems()
	else:
		print "Invalid input, try again."
		major_or_minor(line) 

from_email = "passdownbot@gmail.com"
to_email = "XXX@XXX.com"

def change_email():
	print "Type in the full email address of the recipient (i.e. mechanic@alere.com):"
	global to_email 
	to_email = raw_input("> ")
	if "@" in to_email:
		send_or_not()
	else:
		print "That's not an email address"
		change_email()

def send_or_not(): 
	print "Send email to %s? \n(\"y\" to send, \"n\" to go back, \"c\" to change recipient)" % to_email
	send_it = raw_input("> ")
	if send_it.lower() == "y":
		send_email()
	elif send_it.lower() == "n":
		any_problems()
	elif send_it.lower() == "c":
		change_email()
	else:
		print "Invalid, try again"
		send_or_not()
		

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587


def send_email():
	# me == my email address
	# you == recipient's email address
	me = from_email
	you = to_email ##use your own email address here, will later have a function to change this inside the program

	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Passdown"
	msg['From'] = me
	msg['To'] = you

	# Create the body of the message (a plain-text and an HTML version).
	text = "Should be a table in html, but here's the relevant data:\n" + str(lines[0]) + "\n" + str(lines[1]) + "\n"+ str(lines[2]) + "\n" + str(lines[3]) + "\n" + str(lines[4]) +"\n" + str(lines[5])
	
	##there's gotta be a way i could have automated this table
	## a for loop that wraps the inner list items in <td>?
	## but then how do you wrap all those <tr>? a for loop within a for loop?
	## yep and here it is:
	## with color coding!
	wrapped_text = []
	for x in lines:
		wrapped_text.append("<tr align=\"center\">")
		for y in x:
			if y == "major issue(s)":
				wrapped_text.append("<td><font color = \"red\">" + y + "</font></td>")
			elif y == "minor issue(s)":
				wrapped_text.append("<td><font color = \"orange\">" + y + "</font></td>")
			elif y == "fine":
				wrapped_text.append("<td><font color = \"green\">" + y + "</font></td>")
			else:	
				wrapped_text.append("<td>" + y + "</td>")
		wrapped_text.append("<tr align=\"center\">")
	wrapped_text = ''.join(wrapped_text)
	print "debugging code:" 
	print wrapped_text
	html = """<html>
	<head></head>
	<body>
		<h3>Alere Freehold Site Mechanic Passdown</h3>
			<table width=\"100%%\">
				<tr>				
					<th>Line</th>
					<th>Status</th>
					<th>Comment</th>
				</tr>
				%s """ % wrapped_text
	"""

			</table>
		<hr>
	</body>
	</html>
	"""

	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')

	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	msg.attach(part1)
	msg.attach(part2)
	session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
 
	session.ehlo()
	session.starttls()
	session.ehlo
	session.login(me, "jameschristy")
	# Send the message via local SMTP server.
	# sendmail function takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
	session.sendmail(me, you, msg.as_string())
	session.quit()
	
	
any_problems()