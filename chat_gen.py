import io
from datetime import datetime
import markdown2  # assuming markdown2 is installed

def generate_html(messages):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    chat_content = ""
    interaction_count = 0
    user_emoji = "User"  # Emoji for user
    assistant_emoji = "AI-Tutor"  # Emoji for assistant

    for message in messages:
        role_class = 'user' if message['role'] == 'user' else 'assistant'
        emoji = user_emoji if role_class == 'user' else assistant_emoji
        if role_class == 'user':
            interaction_count += 1
        
        formatted_content = markdown2.markdown(message['content']).replace('\\n', '<br>')
        chat_content += f"<div class='message {role_class}'><span class='emoji'>{emoji}</span>{formatted_content}</div>"

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>EduMentor Chat History</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <style>
        .container {{
            margin-top: 20px;
            background: white;
            border-radius: 0.25rem;
            box-shadow: 0 0.125rem 0.25rem rgba(0,0,0,.075);
        }}
        .header {{
            background-color: #30694b; /* A deep, elegant shade of green */
            color: white;
            padding: 1rem;
            text-align: center;
        }}
        .message {{
            padding: 0.5rem 1rem;
            margin-bottom: 0.5rem;
            border-radius: 10px;
            color: #000080; /* Navy */
        }}
        .user {{
            background-color: #e8f5e9; /* Light Emerald Green */
            align-self: flex-start;
            text-align: left;
        }}
        .assistant {{
            background-color: #d4edda;
        }}
        .footer {{
            background-color: #30694b; /* A deep, elegant shade of green */
            color: white;
            padding: 1rem;
            text-align: center;
        }}
        .timestamp, .interaction-count {{
            font-size: 0.875rem;
            color: #6c757d;
            text-align: center;
            padding: 0.5rem 0;
        }}
        .emoji {{
            font-size: 1.2em;
            margin-right: 0.5rem;
        }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>EduMentor Chat History</h1>
                <div>Generated on: {timestamp}</div>
                <div>Total Q&A Interactions: {interaction_count}</div>
            </div>
            <div>
                {chat_content}
            </div>
            <div class="footer">
                This conversation is generated by EduMentor AI Tutor.
            </div>
        </div>
    </body>
    </html>
    """
    return html_content
