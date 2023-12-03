import os
from requests.exceptions import ReadTimeout
from bardapi import Bard

BARD_API_KEY = os.getenv('BARD_API_KEY')
token = BARD_API_KEY

bard = Bard(token=token)

if not BARD_API_KEY:
    raise ValueError("BARD_API_KEY environment variable not set")


def perform_search(query):
    try:
        response = bard.get_answer(query)
        print(response, "check perform response")
        if response:
            return response['content']
        else:
            return "No search results found."
    except ReadTimeout as e:
        raise ReadTimeout("Bard API request timed out") from e
    except Exception as e:
        print(f"Error in perform_search: {str(e)}")


def google_bard(query):
    try:
        response = perform_search(query)
        if 'content' in response:
            return response['content']
        else:
            return "No description found."
    except ReadTimeout:
        return "Bard API request timed out. Please try again."


def google_search(query):
    try:
        content = perform_search(query)
        print(content)
        return content
    except ReadTimeout:
        return "Bard API request timed out. Please try again."


async def on_message(bot, message):
    print("\n\nai_response", message, "\n\n")
    content = message.content.lower()
    if content:
        print(content, "inside if")
        your_intro_prompt = f"""

        your are cyber security bot from thecyberhub.
                
                Prompt: {content}
                """

        bard_response = google_search(your_intro_prompt)
        await message.channel.send(bard_response)
        await bot.process_commands(message)
