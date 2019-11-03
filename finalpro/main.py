from flask import Flask, render_template, request
import smtplib
from waitress import serve


app = Flask(__name__)

@app.route('/success', methods=['POST'])
def temp():
    reciver = request.form['eaddress']
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('omar.ahmedaf@gmail.com', 'zngnsdiiegrrzhmp')

    subject = "Access granted!"
    body = 'Hello, \n Access to your software has been granted'

    msg = """You intsalltion link is bellow"""

    server.sendmail(
            'omar.ahmedaf@gmail.com',
            reciver,
            msg
        )
    print('HEY EMAIL HAS BEEN SENT')

    server.quit()



    return render_template('success.html')

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')






@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)
