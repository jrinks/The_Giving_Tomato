from typing import ItemsView

from flask.wrappers import Response
from requests import status_codes
from . import bp as text
from app import db
from flask import render_template, redirect, url_for, flash, request
from .forms import ComposeSMS
from config import Config
import vonage

VONAGE_KEY='662f6ac2'
VONAGE_SECRET= 'Pki64W56BzXtZONK'
VONAGE_NUMBER='18885212655'


client = vonage.Client(key="662f6ac2", secret="Pki64W56BzXtZONK")
sms = vonage.Sms(client)


@text.route('/')
def compose():
    """ A view that renders the Send SMS form. """
    return render_template('text.html')

    


@text.route('/send', methods=['GET', 'POST'])
def response():
    to_number = request.form['to_number']
    message = request.form['message']
    responseData = sms.send_message(
    {
        "from": "18885212655",
        "to": to_number,
        "text": message
    }
)

    if responseData["messages"][0]["status"] == "0":
        flash(f'Message sent successfully.')
    else:
        flash(f"Message failed with error: {responseData['messages'][0]['error-text']}")
    return redirect(url_for('text.compose'))



