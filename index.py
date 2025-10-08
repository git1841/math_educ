from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MathLearn Pro</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', system-ui, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            overflow-x: hidden;
        }

        .container {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 20px;
            position: relative;
        }

        .floating-shapes {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 0;
        }

        .shape {
            position: absolute;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            animation: float 6s ease-in-out infinite;
        }

        .shape:nth-child(1) {
            width: 80px;
            height: 80px;
            top: 10%;
            left: 10%;
            animation-delay: 0s;
        }

        .shape:nth-child(2) {
            width: 120px;
            height: 120px;
            top: 60%;
            right: 10%;
            animation-delay: 2s;
        }

        .shape:nth-child(3) {
            width: 60px;
            height: 60px;
            bottom: 20%;
            left: 20%;
            animation-delay: 4s;
        }

        .shape:nth-child(4) {
            width: 100px;
            height: 100px;
            top: 30%;
            right: 20%;
            animation-delay: 1s;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(180deg); }
        }

        .main-content {
            text-align: center;
            z-index: 1;
            position: relative;
            max-width: 800px;
        }

        .logo {
            font-size: 4rem;
            margin-bottom: 1rem;
            animation: bounce 2s ease-in-out infinite;
        }

        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-10px); }
            60% { transform: translateY(-5px); }
        }

        .title {
            font-size: 3.5rem;
            font-weight: 700;
            background: linear-gradient(45deg, #fff, #f0f0f0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 2rem;
            text-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }

        .warning-container {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255, 193, 7, 0.8);
            border-radius: 20px;
            padding: 2.5rem;
            margin: 2rem 0;
            box-shadow: 
                0 20px 40px rgba(0,0,0,0.1),
                0 0 0 1px rgba(255, 255, 255, 0.2),
                inset 0 0 50px rgba(255, 193, 7, 0.1);
            transform-style: preserve-3d;
            perspective: 1000px;
            animation: glow 3s ease-in-out infinite, slideIn 1s ease-out;
        }

        @keyframes glow {
            0%, 100% { 
                box-shadow: 
                    0 20px 40px rgba(0,0,0,0.1),
                    0 0 0 1px rgba(255, 255, 255, 0.2),
                    inset 0 0 50px rgba(255, 193, 7, 0.1);
            }
            50% { 
                box-shadow: 
                    0 20px 40px rgba(0,0,0,0.15),
                    0 0 0 1px rgba(255, 255, 255, 0.3),
                    inset 0 0 50px rgba(255, 193, 7, 0.2),
                    0 0 30px rgba(255, 193, 7, 0.3);
            }
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(50px) rotateX(-30deg);
            }
            to {
                opacity: 1;
                transform: translateY(0) rotateX(0);
            }
        }

        .warning-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
            animation: pulse 2s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.1); }
        }

        .warning-title {
            font-size: 2rem;
            font-weight: 700;
            color: #ff6b35;
            margin-bottom: 1rem;
            text-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .warning-text {
            font-size: 1.3rem;
            color: #2d3748;
            line-height: 1.6;
            font-weight: 500;
        }

        .progress-container {
            width: 100%;
            max-width: 400px;
            height: 8px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            margin: 2rem auto;
            overflow: hidden;
        }

        .progress-bar {
            height: 100%;
            background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
            border-radius: 10px;
            animation: progress 3s ease-in-out infinite;
            transform-origin: left;
        }

        @keyframes progress {
            0% { transform: scaleX(0); }
            50% { transform: scaleX(0.7); }
            100% { transform: scaleX(0); }
        }

        .coming-soon {
            color: rgba(255, 255, 255, 0.9);
            font-size: 1.2rem;
            margin-top: 2rem;
            font-weight: 300;
            letter-spacing: 2px;
            text-transform: uppercase;
            animation: fadeInOut 3s ease-in-out infinite;
        }

        @keyframes fadeInOut {
            0%, 100% { opacity: 0.7; }
            50% { opacity: 1; }
        }

        .interactive-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1rem;
            margin-top: 3rem;
            width: 100%;
            max-width: 600px;
        }

        .grid-item {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 15px;
            padding: 1.5rem;
            text-align: center;
            color: white;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            animation: gridAppear 0.6s ease-out forwards;
            opacity: 0;
            transform: translateY(20px);
        }

        .grid-item:hover {
            background: rgba(255, 255, 255, 0.2);
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        }

        @keyframes gridAppear {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .grid-item:nth-child(1) { animation-delay: 0.1s; }
        .grid-item:nth-child(2) { animation-delay: 0.2s; }
        .grid-item:nth-child(3) { animation-delay: 0.3s; }
        .grid-item:nth-child(4) { animation-delay: 0.4s; }

        /* Responsive */
        @media (max-width: 768px) {
            .title { font-size: 2.5rem; }
            .warning-title { font-size: 1.5rem; }
            .warning-text { font-size: 1.1rem; }
            .logo { font-size: 3rem; }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Formes flottantes animées -->
        <div class="floating-shapes">
            <div class="shape"></div>
            <div class="shape"></div>
            <div class="shape"></div>
            <div class="shape"></div>
        </div>

        <div class="main-content">
            <!-- Logo et titre -->
            <div class="logo">🎓</div>
            <h1 class="title">Platforme d'Apprentissage de Mathématique</h1>

            <!-- Message de développement -->
            <div class="warning-container">
                <div class="warning-icon"></div>
                <h2 class="warning-title">Site en cours de développement</h2>
                <p class="warning-text">
                    Cette plateforme est actuellement en construction.<br>
                    Revenez plus tard pour découvrir toutes les fonctionnalités !
                </p>
            </div>

            <!-- Barre de progression animée -->
            <div class="progress-container">
                <div class="progress-bar"></div>
            </div>

            <!-- Grille interactive -->
            <div class="interactive-grid">
                <div class="grid-item" onclick="showComingSoon('Collège')">
                    📊 Collège
                </div>
                <div class="grid-item" onclick="showComingSoon('Lycée')">
                    📐 Lycée
                </div>
                <div class="grid-item" onclick="showComingSoon('Université')">
                    📈 Université
                </div>
                
            </div>

            <!-- Texte animé -->
            <div class="coming-soon">Bientôt disponible</div>
        </div>
    </div>

    <script>
        // Animation des interactions
        function showComingSoon(module) {
            const originalText = event.target.textContent;
            event.target.textContent = '🚧 Bientôt...';
            event.target.style.background = 'rgba(255, 107, 53, 0.3)';
            
            setTimeout(() => {
                event.target.textContent = originalText;
                event.target.style.background = '';
            }, 1000);
        }

        // Effets de particules au clic
        document.addEventListener('click', function(e) {
            createRipple(e);
        });

        function createRipple(e) {
            const ripple = document.createElement('div');
            ripple.style.cssText = `
                position: fixed;
                width: 20px;
                height: 20px;
                background: rgba(255, 255, 255, 0.6);
                border-radius: 50%;
                pointer-events: none;
                left: ${e.clientX - 10}px;
                top: ${e.clientY - 10}px;
                animation: rippleEffect 0.6s ease-out forwards;
                z-index: 1000;
            `;
            
            document.body.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        }

        const style = document.createElement('style');
        style.textContent = `
            @keyframes rippleEffect {
                to {
                    transform: scale(20);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);

        // Animation du texte principal
        const title = document.querySelector('.title');
        title.addEventListener('mouseenter', () => {
            title.style.transform = 'scale(1.05)';
            title.style.transition = 'transform 0.3s ease';
        });
        
        title.addEventListener('mouseleave', () => {
            title.style.transform = 'scale(1)';
        });
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
