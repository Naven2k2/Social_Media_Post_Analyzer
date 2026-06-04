import json

def parse_response(response_text):

    try:

        response_text = response_text.strip()

        if response_text.startswith("```json"):
            response_text = response_text.replace("```json", "")

        if response_text.endswith("```"):
            response_text = response_text[:-3]

        response_text = response_text.strip()

        return json.loads(response_text)

    except Exception as e:

        return {
            "tone": "Unknown",
            "intent": "Unknown",
            "communication_style": "Unknown",
            "summary": str(e)
        }