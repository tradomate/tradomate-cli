import click
import requests

API_BASE_URL = "https://api.tradomate.io/api/v1"


@click.group()
def cli():
    """A CLI application for building and deploying AI Chatbots."""
    pass


@cli.command()
@click.option("--email", prompt="Email", help="Your email address.")
@click.option("--password", prompt="Password", help="Your password.", hide_input=True)
def create_account(email, password):
    """Create an account for the Chatbot Builder."""
    data = {"email": email, "password": password}
    response = requests.post(f"{API_BASE_URL}/accounts", json=data)
    if response.status_code == 201:
        click.echo("Account created successfully!")
    else:
        click.echo(f"Error creating account: {response.text}")


@cli.command()
@click.option("--api_key", prompt="API Key", help="Your API key for authentication.")
@click.option("--name", prompt="Chatbot Name", help="The name of your chatbot.")
def create_chatbot(api_key, name):
    """Create a new chatbot."""
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {"name": name}
    response = requests.post(f"{API_BASE_URL}/chatbots", json=data, headers=headers)

    if response.status_code == 201:
        chatbot_id = response.json()["id"]
        click.echo(f"Chatbot created successfully! Chatbot ID: {chatbot_id}")
    else:
        click.echo(f"Error creating chatbot: {response.text}")


@cli.command()
@click.option("--api_key", prompt="API Key", help="Your API key for authentication.")
@click.option("--chatbot_id", prompt="Chatbot ID", help="The ID of your chatbot.")
def deploy_chatbot(api_key, chatbot_id):
    """Deploy a chatbot to chatbot.tradomate.io."""
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post(
        f"{API_BASE_URL}/chatbots/{chatbot_id}/deploy", headers=headers
    )

    if response.status_code == 200:
        click.echo("Chatbot deployed successfully!")
    else:
        click.echo(f"Error deploying chatbot: {response.text}")


if __name__ == "__main__":
    cli()
