from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    """Serve the main admissions page"""
    colleges = [
        {
            "name": "NIT Andhra Pradesh",
            "exam": "JEE Main + JoSAA",
            "eligibility": "10+2 with 75% PCM",
            "fees": "₹1.47L+"
        },
        {
            "name": "Andhra University College of Engineering",
            "exam": "AP EAMCET",
            "eligibility": "10+2 with 60% PCM",
            "fees": "₹1.4L"
        },
        {
            "name": "IIITDM Kurnool",
            "exam": "JEE Main + JoSAA",
            "eligibility": "10+2 with 75% PCM",
            "fees": "Varies by branch"
        }
    ]
    
    admission_steps = [
        "Register for AP EAPCET at cets.apsche.ap.gov.in",
        "Appear for entrance exam (AP EAMCET/JEE Main)",
        "Complete web options entry during counseling",
        "Check seat allotment and report to allotted college"
    ]
    
    context = {
        "title": "AP BTech Admissions 2026",
        "official_link": "https://cets.apsche.ap.gov.in/EAPCET/",
        "colleges": colleges,
        "steps": admission_steps,
        "eligibility": "10+2 with minimum 60-75% in PCM"
    }
    return render_template('index.html', **context)

@app.route('/colleges')
def colleges():
    """Dedicated colleges page"""
    colleges = [
        {"name": "Narayana Engineering College Gudur", "exam": "AP EAMCET", "fees": "₹1.47L+", "seats": "High demand"},
        {"name": "Narayana Engineering College Nellore", "exam": "AP EAMCET", "fees": "₹1.4L", "seats": "Large intake"},
        {"name": "SV university", "exam": "JEE Main", "fees": "Varies", "seats": "Moderate"},
        {"name": "JNTUK Ananthapur", "exam": "AP EAMCET", "fees": "₹80K-1L", "seats": "High"}
    ]
    return render_template('colleges.html', colleges=colleges)

@app.route('/admissions')
def admissions():
    """Dedicated admissions process page"""
    return render_template('admissions.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
