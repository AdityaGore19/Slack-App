# Slack-App
#Slack App Description:

The Slack Forward app is a simple application built to facilitate communication between two Slack channels within a workspace. It enables users to forward messages from one channel to another using a custom slash command.

#Features:

    Create Two Channels: The app automatically creates two channels named "Channel 1" and "Channel 2" within the Slack workspace. These channels serve as the source and destination for message forwarding.

    Slash Command (/forward): Users can use the /forward slash command to forward messages from Channel 1 to Channel 2. When a message is sent in Channel 1 with the /forward command followed by text, the app automatically echoes the message in uppercase to Channel 2.

#Technologies Used:

    Programming Language: Python
    Framework: Flask
    Slack API Libraries: slackeventsapi, slack
    Development Tools: Ngrok (for local server tunneling)
    Version Control: Git

#Usage Instructions:

    Clone the repository to your local machine.
    Install the required Python packages using pip install -r requirements.txt.
    Set up a new Slack app in your Slack workspace and configure slash commands with appropriate endpoints.
    Create a .env file and add your Slack signing secret and bot token.
    Start the Flask server locally using python app.py.
    Expose the local server to the internet using Ngrok or a similar tool.
    Add the Ngrok URL as the Request URL for slash commands in your Slack app settings.
    Use the /forward command in Channel 1 followed by a message to forward it to Channel 2.

#Demo Video:
__to be added__


Additional Notes:

    Ensure that your Slack app has the necessary permissions to read messages from and post messages to both Channel 1 and Channel 2.
    Test the functionality thoroughly to ensure proper message forwarding between channels.
    Feel free to customize the app further based on your requirements or preferences.
