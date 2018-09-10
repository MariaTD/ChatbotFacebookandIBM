# receives response.
import watson_developer_cloud
import json
import calculoCredito

# Set up Assistant service.
service = watson_developer_cloud.AssistantV1(
    username = 'b2a35ee3-73e4-4a5e-af75-069d499dd29e', # replace with service username
    password = '1fR7OR03uBs4', # replace with service password
    version = '2018-02-16'
  )



def cliente_funcion(texto):
  workspace_id = '624a1e2c-c475-4be0-8152-e68caf79f95c' # replace with workspace 
  with open('read.json') as data_file:    
    context = json.load(data_file)
  # Send message to Assistant service.
  response = service.message(
      workspace_id = workspace_id,
      input = {
        'text': texto
      },
      context =  context
  )
  print("response:   ")
  print(json.dumps(response, indent=4))
  #response es un diccionario
  mensaje_respuesta=response['output']['text'][0]
  context_respuesta=response['context']
  with open('read.json', 'w') as outfile:
    json.dump(context_respuesta, outfile, sort_keys=True, indent=4)



  if len(response['intents'])!= 0 :
    intent_respuesta=response['intents'][0]['intent'] 
  else :
    varAux=response['output']
    print(varAux)
    if "intents" in response['output']:
      print ("aca")
      intent_respuesta=response['output']['intents'][0]['intent']
      if intent_respuesta=="SimuladorCuota2":
        mensaje_respuesta=calculoCredito.GetValorDeCuota(texto)
    else:
      intent_respuesta=""
   
  return mensaje_respuesta, intent_respuesta

