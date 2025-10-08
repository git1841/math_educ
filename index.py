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
            font-size: 14px;
        }

        .container {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 15px;
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
            width: 60px;
            height: 60px;
            top: 10%;
            left: 5%;
            animation-delay: 0s;
        }

        .shape:nth-child(2) {
            width: 80px;
            height: 80px;
            top: 60%;
            right: 5%;
            animation-delay: 2s;
        }

        .shape:nth-child(3) {
            width: 40px;
            height: 40px;
            bottom: 15%;
            left: 15%;
            animation-delay: 4s;
        }

        .shape:nth-child(4) {
            width: 70px;
            height: 70px;
            top: 25%;
            right: 15%;
            animation-delay: 1s;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-15px) rotate(180deg); }
        }

        .main-content {
            text-align: center;
            z-index: 1;
            position: relative;
            max-width: 800px;
            width: 100%;
        }

        .logo {
            font-size: 2.5rem;
            margin-bottom: 0.8rem;
            animation: bounce 2s ease-in-out infinite;
        }

        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-8px); }
            60% { transform: translateY(-4px); }
        }

        .title {
            font-size: 2rem;
            font-weight: 600;
            background: linear-gradient(45deg, #fff, #f0f0f0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 1.5rem;
            text-shadow: 0 2px 4px rgba(0,0,0,0.2);
            line-height: 1.3;
            padding: 0 10px;
        }

        .warning-container {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255, 193, 7, 0.8);
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1.5rem 0;
            box-shadow: 
                0 15px 30px rgba(0,0,0,0.1),
                0 0 0 1px rgba(255, 255, 255, 0.2),
                inset 0 0 30px rgba(255, 193, 7, 0.1);
            transform-style: preserve-3d;
            perspective: 1000px;
            animation: glow 3s ease-in-out infinite, slideIn 1s ease-out;
        }

        @keyframes glow {
            0%, 100% { 
                box-shadow: 
                    0 15px 30px rgba(0,0,0,0.1),
                    0 0 0 1px rgba(255, 255, 255, 0.2),
                    inset 0 0 30px rgba(255, 193, 7, 0.1);
            }
            50% { 
                box-shadow: 
                    0 15px 30px rgba(0,0,0,0.15),
                    0 0 0 1px rgba(255, 255, 255, 0.3),
                    inset 0 0 30px rgba(255, 193, 7, 0.2),
                    0 0 20px rgba(255, 193, 7, 0.3);
            }
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(40px) rotateX(-30deg);
            }
            to {
                opacity: 1;
                transform: translateY(0) rotateX(0);
            }
        }

        .warning-icon {
            font-size: 2rem;
            margin-bottom: 0.8rem;
            animation: pulse 2s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }

        .warning-title {
            font-size: 1.3rem;
            font-weight: 600;
            color: #ff6b35;
            margin-bottom: 0.8rem;
            text-shadow: 0 1px 2px rgba(0,0,0,0.1);
        }

        .warning-text {
            font-size: 0.9rem;
            color: #2d3748;
            line-height: 1.5;
            font-weight: 500;
        }

        .progress-container {
            width: 100%;
            max-width: 300px;
            height: 6px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 8px;
            margin: 1.5rem auto;
            overflow: hidden;
        }

        .progress-bar {
            height: 100%;
            background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
            border-radius: 8px;
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
            font-size: 0.9rem;
            margin-top: 1.5rem;
            font-weight: 300;
            letter-spacing: 1px;
            text-transform: uppercase;
            animation: fadeInOut 3s ease-in-out infinite;
        }

        @keyframes fadeInOut {
            0%, 100% { opacity: 0.7; }
            50% { opacity: 1; }
        }

        .interactive-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 0.8rem;
            margin-top: 2rem;
            width: 100%;
            max-width: 500px;
            padding: 0 10px;
        }

        .grid-item {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 12px;
            padding: 1rem 0.8rem;
            text-align: center;
            color: white;
            font-weight: 500;
            font-size: 0.85rem;
            cursor: pointer;
            transition: all 0.3s ease;
            animation: gridAppear 0.6s ease-out forwards;
            opacity: 0;
            transform: translateY(15px);
            min-height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .grid-item:hover {
            background: rgba(255, 255, 255, 0.2);
            transform: translateY(-3px) scale(1.03);
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
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

        /* Responsive pour très petits écrans */
        @media (max-width: 480px) {
            body {
                font-size: 13px;
            }
            
            .container {
                padding: 10px;
                justify-content: flex-start;
                padding-top: 2rem;
            }
            
            .logo {
                font-size: 2rem;
                margin-bottom: 0.5rem;
            }
            
            .title {
                font-size: 1.5rem;
                margin-bottom: 1rem;
            }
            
            .warning-container {
                padding: 1rem;
                margin: 1rem 0;
                border-radius: 12px;
            }
            
            .warning-icon {
                font-size: 1.5rem;
                margin-bottom: 0.5rem;
            }
            
            .warning-title {
                font-size: 1.1rem;
                margin-bottom: 0.5rem;
            }
            
            .warning-text {
                font-size: 0.8rem;
                line-height: 1.4;
            }
            
            .progress-container {
                max-width: 250px;
                height: 5px;
                margin: 1rem auto;
            }
            
            .interactive-grid {
                grid-template-columns: repeat(2, 1fr);
                gap: 0.6rem;
                max-width: 300px;
                margin-top: 1.5rem;
            }
            
            .grid-item {
                padding: 0.8rem 0.5rem;
                font-size: 0.8rem;
                min-height: 50px;
                border-radius: 10px;
            }
            
            .coming-soon {
                font-size: 0.8rem;
                margin-top: 1rem;
            }
            
            .shape:nth-child(1),
            .shape:nth-child(2),
            .shape:nth-child(3),
            .shape:nth-child(4) {
                display: none;
            }
        }

        @media (max-width: 320px) {
            .interactive-grid {
                grid-template-columns: 1fr;
                max-width: 200px;
            }
            
            .title {
                font-size: 1.3rem;
            }
        }

        /* Pour les grands écrans */
        @media (min-width: 1200px) {
            body {
                font-size: 15px;
            }
            
            .title {
                font-size: 2.2rem;
            }
            
            .warning-container {
                padding: 2rem;
            }
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
            <h1 class="title">Plateforme d'Apprentissage de Mathématiques</h1>

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
                width: 15px;
                height: 15px;
                background: rgba(255, 255, 255, 0.6);
                border-radius: 50%;
                pointer-events: none;
                left: ${e.clientX - 7}px;
                top: ${e.clientY - 7}px;
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
                    transform: scale(15);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);

        // Animation du texte principal
        const title = document.querySelector('.title');
        title.addEventListener('mouseenter', () => {
            title.style.transform = 'scale(1.03)';
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
