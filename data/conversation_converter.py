import json

def procesar_conversaciones(input_file, output_file):
    conversations = []
    current_conversation = []
    conversation_id = None

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                if line.isdigit():
                    if current_conversation:
                        conversations.append({
                            'conversation_id': conversation_id,
                            'messages': current_conversation
                        })
                    conversation_id = int(line)
                    current_conversation = []
                else:
                    current_conversation.append(line)

            if current_conversation:
                conversations.append({
                    'conversation_id': conversation_id,
                    'messages': current_conversation
                })

        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(conversations, json_file, ensure_ascii=False, indent=4)
        print(f"Archivo procesado y guardado como: {output_file}")

    except UnicodeDecodeError as e:
        print(f"Error de decodificación: {e}")
    except Exception as e:
        print(f"Se produjo un error: {e}")