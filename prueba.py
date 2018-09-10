# receives response.
import watson_developer_cloud


def cliente_funcion(texto):
  # Set up Assistant service.
  print("holaaaaa")
  service = watson_developer_cloud.AssistantV1(
    username = 'b2a35ee3-73e4-4a5e-af75-069d499dd29e', # replace with service username
    password = '1fR7OR03uBs4', # replace with service password
    version = '2018-02-16'
  )
  workspace_id = '624a1e2c-c475-4be0-8152-e68caf79f95c' # replace with workspace ID

  # Initialize with empty value to start the conversation.
  user_input = texto
  context = {}
  current_action = ''
  # Main input/output loop
  
  while current_action != 'finalConversacion':

    # Send message to Assistant service.
    response = service.message(
      workspace_id = workspace_id,
      input = {
        'text': user_input
      },
      context = context
      
    )
    # If an intent was detected, print it to the console
    if response['intents']:
      print('Detected intent: #' + response['intents'][0]['intent'])
    # Print the output from dialog, if any.
    if response['output']['text']:
      print(response['output']['text'][0])
    # Update the stored context with the latest received from the dialog.
    context = response['context']
    if 'action' in response['output']:
      current_action = response['output']['action']
    if current_action != 'finalConversacion':
      user_input = input('>> ')



