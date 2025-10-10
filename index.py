<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plateforme d'Apprentissage de Mathématiques</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
            color: white;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px;
            text-align: center;
        }
        
        .container {
            max-width: 800px;
            width: 100%;
            background-color: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        h1 {
            font-size: 2.5rem;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }
        
        .status {
            font-size: 1.2rem;
            margin-bottom: 30px;
            opacity: 0.9;
        }
        
        .progress-container {
            width: 100%;
            background-color: rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            margin: 30px 0;
            overflow: hidden;
            height: 20px;
        }
        
        .progress-bar {
            height: 100%;
            width: 50%;
            background: linear-gradient(90deg, #ff9a00, #ffcc00);
            border-radius: 10px;
            transition: width 0.5s ease;
            position: relative;
            overflow: hidden;
        }
        
        .progress-bar::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            bottom: 0;
            right: 0;
            background-image: linear-gradient(
                -45deg, 
                rgba(255, 255, 255, 0.2) 25%, 
                transparent 25%, 
                transparent 50%, 
                rgba(255, 255, 255, 0.2) 50%, 
                rgba(255, 255, 255, 0.2) 75%, 
                transparent 75%, 
                transparent
            );
            background-size: 20px 20px;
            animation: move 1s linear infinite;
        }
        
        @keyframes move {
            0% {
                background-position: 0 0;
            }
            100% {
                background-position: 20px 0;
            }
        }
        
        .percentage {
            margin-top: 10px;
            font-weight: bold;
            font-size: 1.5rem;
        }
        
        .levels {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            margin-top: 40px;
        }
        
        .level {
            background-color: rgba(255, 255, 255, 0.15);
            border-radius: 15px;
            padding: 20px;
            margin: 10px;
            flex: 1;
            min-width: 150px;
            transition: transform 0.3s ease, background-color 0.3s ease;
            cursor: pointer;
        }
        
        .level:hover {
            transform: translateY(-5px);
            background-color: rgba(255, 255, 255, 0.25);
        }
        
        .level-icon {
            font-size: 2.5rem;
            margin-bottom: 10px;
        }
        
        .level-title {
            font-size: 1.2rem;
            font-weight: bold;
        }
        
        .construction {
            margin-top: 30px;
            padding: 15px;
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            font-style: italic;
        }
        
        .contact {
            margin-top: 30px;
            font-size: 0.9rem;
            opacity: 0.8;
        }
        
        @media (max-width: 600px) {
            .container {
                padding: 20px;
            }
            
            h1 {
                font-size: 1.8rem;
            }
            
            .levels {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Plateforme d'Apprentissage de Mathématiques</h1>
        <p class="status">Site en cours de développement</p>
        
        <div class="progress-container">
            <div class="progress-bar"></div>
        </div>
        <div class="percentage">50%</div>
        
        <p class="construction">Cette plateforme est actuellement en construction.<br>Revenez plus tard pour découvrir toutes les fonctionnalités !</p>
        
        <div class="levels">
            <div class="level">
                <div class="level-icon">📊</div>
                <div class="level-title">Collège</div>
            </div>
            <div class="level">
                <div class="level-icon">📐</div>
                <div class="level-title">Lycée</div>
            </div>
            <div class="level">
                <div class="level-icon">📈</div>
                <div class="level-title">Université</div>
            </div>
        </div>
        
        <div class="contact">
            Contact: contact@maths-platforme.fr
        </div>
    </div>
    
    <script>
        // Animation pour la barre de progression
        document.addEventListener('DOMContentLoaded', function() {
            const progressBar = document.querySelector('.progress-bar');
            
            // Animation de chargement
            setTimeout(() => {
                progressBar.style.width = '50%';
            }, 500);
            
            // Effet de clic sur les niveaux
            const levels = document.querySelectorAll('.level');
            levels.forEach(level => {
                level.addEventListener('click', function() {
                    alert('Cette section sera bientôt disponible !');
                });
            });
        });
    </script>
</body>
</html>
