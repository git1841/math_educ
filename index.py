<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Éducative</title>
    <link rel="stylesheet" href="style.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: #f4f4f9;
        }

        .dashboard-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        h1,
        h2,
        h3 {
            text-align: center;
            color: #333;
        }

        .dashboard-buttons {
            text-align: center;
            margin: 20px 0;
        }

        .btn {
            display: inline-block;
            margin: 5px 10px;
            padding: 10px 20px;
            background-color: #0066cc;
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
            transition: 0.3s;
        }

        .btn:hover {
            background-color: #004d99;
        }

        .etudiants,
        .admin-contact,
        .images-dashboard {
            margin: 30px 0;
        }

        ul {
            list-style-type: none;
            padding: 0;
        }

        li {
            padding: 5px 0;
            text-align: center;
        }

        .images-section {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 15px;
        }

        .images-section img {
            width: 200px;
            height: 150px;
            object-fit: cover;
            border-radius: 8px;
            border: 2px solid #ccc;
            transition: 0.3s;
        }

        .images-section img:hover {
            transform: scale(1.05);
            border-color: #0066cc;
        }
    </style>
</head>

<body>
    <div class="dashboard-container">
        <h1>Dashboard Éducative</h1>
        <p style="text-align:center;">Projet pour collège, lycée et université, dirigé par Jacques et Marie</p>

        <div class="dashboard-buttons">
            <a href="#" class="btn">Inscription</a>
            <a href="#" class="btn">Contact</a>
        </div>

        <section class="etudiants">
            <h2>Étudiants responsables</h2>
            <ul>
                <li>Jacques - Étudiant</li>
                <li>Marie - Étudiant</li>
            </ul>
        </section>

        <section class="images-dashboard">
            <h2>Images du projet</h2>

            <h3>Collège</h3>
            <div class="images-section">
                <img src="images/college1.jpg" alt="Collège 1">
                <img src="images/college2.jpg" alt="Collège 2">
                <img src="images/college3.jpg" alt="Collège 3">
                <img src="images/college4.jpg" alt="Collège 4">
            </div>

            <h3>Lycée</h3>
            <div class="images-section">
                <img src="images/lycee.jpg" alt="Lycée">
            </div>

            <h3>Université</h3>
            <div class="images-section">
                <img src="images/univ1.jpg" alt="Université 1">
                <img src="images/univ2.jpg" alt="Université 2">
                <img src="images/admin_univ.jpg" alt="Administrateur Université">
            </div>
        </section>

        <section class="admin-contact">
            <h2>Contact de l'administrateur</h2>
            <ul>
                <li>Nom: Administrateur</li>
                <li>Email: <a href="mailto:admin@example.com">admin@example.com</a></li>
                <li>Contact: +261 34 00 000 00</li>
                <li>Facebook: <a href="https://facebook.com/admin">facebook.com/admin</a></li>
                <li>WhatsApp: +261 34 00 000 00</li>
                <li>Telegram: @admin</li>
            </ul>
        </section>
    </div>
</body>

</html>
