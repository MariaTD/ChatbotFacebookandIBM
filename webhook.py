from __future__ import print_function
#from future.standard_library import install_aliases
#install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request, urlretrieve
from urllib.error import HTTPError
from pymessenger import Bot    
import calculoCredito 
import json
import os
import cliente
import requests
import wget
from flask import Flask, request, make_response, abort, render_template


my_token = 'token_webhook_test_watsonassistent'
fb_token = 'EAAHqstZBZAKQIBAE8oka8XJ4VZBpg9DrJcxjgGbIiH9tgNCxJ1XEWrOSyXTIxCKkuoKyEM4P1AZC8IMv7X1QTwFhqZASYIPvRwwoXMQFSDqGqC3ut8QS8T7AQi0Y1AKHU4hAdGrXne8CcHtapwpOviO0qtREu0uEulcla7HlzqLD3xrKJxSWs0yTLPXE7OYIZD'
bot=Bot(fb_token)
# Flask app should start in global layout
app = Flask(__name__)
texto=''

# VALIDAR LAS APP CONECTADAS
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        challenge = request.args.get('hub.challenge', '')
        token = request.args.get('hub.verify_token', '')
        if token == my_token:
            return challenge
    elif request.method == 'POST':
        req = request.get_json(silent=True, force=True)
        texto=req['entry'][0]['messaging'][0]['message']['text']
        PSID=req['entry'][0]['messaging'][0]['sender']['id'] 
        recipent_id=req['entry'][0]['messaging'][0]['recipient']['id']
        print("Mensaje: ")
        print(texto)
        print(PSID)
        mensaje_respuesta, intent_respuesta = cliente.cliente_funcion(texto)
        
        print(mensaje_respuesta)
        print (intent_respuesta)

        bot.send_text_message(PSID,mensaje_respuesta,)

            
            
        #bot.send_text_message(PSID,Cuota)
        #print("Request:")
        #print(json.dumps(req, indent=4)) #Esto imprime en tipo json
        return "ok",200 
    return abort(404)

    

@app.route('/test', methods=['GET'])
def test():
    return  "Bienvenido Prueba Team RPA Maria !!"
    
if __name__ == '__main__':
    port = int(os.getenv('PORT', 8081))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='127.0.0.1')