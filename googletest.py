from flask import Flask, request, render_template_string, redirect, url_for
import requests
import os

app = Flask(__name__)

# URL de ton FastAPI qui reçoit les fichiers
UPLOAD_API_URL = "https://fastapi-blog-zonantenainasecondraymond9003-uclkvshl.leapcell.dev/upload"

HTML_FORM = '''
<!DOCTYPE html>
<html>
<head>
    <title>Envoyer un fichier</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f5f5f5; }}
        .container {{ max-width: 500px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        h1 {{ color: #333; text-align: center; }}
        input[type="file"] {{ display: block; margin: 20px auto; }}
        button {{ padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer; }}
        .success {{ color: #4CAF50; font-weight: bold; text-align: center; }}
        .error {{ color: #f44336; font-weight: bold; text-align: center; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📤 Envoyer un fichier vers Google Drive</h1>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file" required>
            <button type="submit">Envoyer</button>
        </form>
        {% if message %}
            <p class="{{ 'success' if success else 'error' }}">{{ message }}</p>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    message = None
    success = False
    if request.method == 'POST':
        uploaded_file = request.files.get('file')
        if uploaded_file:
            try:
                # Préparer le fichier pour l'envoyer au Back-End FastAPI
                files = {'file': (uploaded_file.filename, uploaded_file.stream, uploaded_file.mimetype)}
                response = requests.post(UPLOAD_API_URL, files=files)
                data = response.json()
                
                if response.status_code == 200 and 'file_id' in data:
                    message = f"Fichier envoyé avec succès ! ID Google Drive : {data['file_id']}"
                    success = True
                else:
                    message = f"Erreur lors de l'envoi : {data.get('error', 'Inconnu')}"
            except Exception as e:
                message = f"Erreur de connexion : {str(e)}"
        else:
            message = "Aucun fichier sélectionné."
    
    return render_template_string(HTML_FORM, message=message, success=success)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
