from swarm import Swarm, Agent
from openai import OpenAI
import json

openai = OpenAI(
    api_key="sk-xxx",
    base_url="http://localhost:11434/v1"
)

client = Swarm(client=openai)

def get_weather(location, time="now"):
    """Get the current weather in a given location. Location MUST be a city."""
    return json.dumps({"location": location, "temperature": "65", "time": time})


def send_email(recipient, subject, body):
    print("Sending email...")
    print(f"To: {recipient}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    return "Sent!"


weather_agent = Agent(
    name="Weather Agent",
    instructions="You are a helpful agent.",
    functions=[get_weather, send_email],
)

response = client.run(
    agent=weather_agent,
    messages=[{"role": "user", "content": "Query the weather in Beijing today and email the results to me."}],
    model_override="llama3.1:8b"
)

for message in response.messages:
    print(message)

print(f"Response: {response.messages[-1]['content']}")
