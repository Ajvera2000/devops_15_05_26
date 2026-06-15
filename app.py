from flask import Flask
from datetime import datetime

app = Flask(__name__)

VERSION = "1.0.0"

@app.route("/")
def inicio():
    # Obtenemos la hora actual
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"""
    <h1>Aplicación Flask - Reloj</h1>
    <h2>Versión {VERSION}</h2>
    <p style="color: blue;"><strong>¡Funcionando correctamente!</strong></p>
    
    <h3>Hora del servidor:</h3>
    <ul>
        <li><strong>Fecha y Hora:</strong> {ahora}</li>
    </ul>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)