from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AP BTech Admissions 2026</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { font-family: Arial, sans-serif; background: linear-gradient(135deg, #007bff, #00bfff); min-height: 100vh; }
        .hero { background: rgba(255,255,255,0.9); padding: 2rem; border-radius: 10px; }
        footer { background: #343a40; color: white; padding: 1rem; text-align: center; }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="#">AP BTech Portal</a>
        </div>
    </nav>

    <section class="container my-5">
        <div class="hero text-center">
            <h1>🎓 AP BTech Admissions 2026</h1>
            <p>Official info from <a href="https://cets.apsche.ap.gov.in/EAPCET/" target="_blank">AP EAPCET portal</a></p>
            <p><strong>Eligibility:</strong> 10+2 with 60-75% in PCM</p>
        </div>
    </section>

    <section class="container my-5">
        <h2>📋 Admission Steps</h2>
        <ol class="list-group list-group-numbered">
            <li class="list-group-item">Register for AP EAPCET (~March 2026)</li>
            <li class="list-group-item">Appear for entrance exam</li>
            <li class="list-group-item">Web options entry during counseling</li>
            <li class="list-group-item">Report to allotted college</li>
        </ol>
    </section>

    <section class="container my-5">
        <h2>🏫 Top Government Colleges</h2>
        <div class="table-responsive">
            <table class="table table-striped">
                <thead><tr><th>College</th><th>Exam</th><th>Eligibility</th><th>Fees</th></tr></thead>
                <tbody>
                    <tr><td>NIT Andhra Pradesh</td><td>JEE Main</td><td>75% PCM</td><td>₹1.47L</td></tr>
                    <tr><td>Andhra University</td><td>AP EAMCET</td><td>60% PCM</td><td>₹1.4L</td></tr>
                    <tr><td>IIITDM Kurnool</td><td>JEE Main</td><td>75% PCM</td><td>Varies</td></tr>
                    <tr><td>JNTUK Kakinada</td><td>AP EAMCET</td><td>60% PCM</td><td>₹80K-1L</td></tr>
                </tbody>
            </table>
        </div>
    </section>

    <footer>
        <p>&copy; 2026 AP BTech Info | <a href="https://cets.apsche.ap.gov.in/EAPCET/">Official Site</a></p>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
    """
    return html

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
