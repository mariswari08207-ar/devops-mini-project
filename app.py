from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DevOps Hub | CI/CD Automation</title>
<style>
:root{--bg:#07111f;--card:#101f35;--line:rgba(148,163,184,.18);--text:#f8fafc;--muted:#94a3b8;--blue:#38bdf8;--blue2:#0ea5e9;--green:#22c55e;--purple:#8b5cf6}
*{margin:0;padding:0;box-sizing:border-box;scroll-behavior:smooth;font-family:Arial,sans-serif}
body{background:radial-gradient(circle at 15% 10%,rgba(14,165,233,.16),transparent 28%),radial-gradient(circle at 85% 20%,rgba(139,92,246,.14),transparent 28%),var(--bg);color:var(--text)}
a{color:inherit}
nav{position:sticky;top:0;z-index:100;height:72px;padding:0 6%;display:flex;align-items:center;justify-content:space-between;background:rgba(7,17,31,.86);backdrop-filter:blur(18px);border-bottom:1px solid var(--line)}
.logo{display:flex;align-items:center;gap:10px;font-size:23px;font-weight:800}.logo-icon{width:38px;height:38px;display:grid;place-items:center;border-radius:11px;background:linear-gradient(135deg,var(--blue2),var(--purple));box-shadow:0 8px 25px rgba(14,165,233,.28)}.logo span{color:var(--blue)}
.links{display:flex;gap:28px}.links a{color:#cbd5e1;text-decoration:none;font-size:14px}.links a:hover{color:var(--blue)}
.nav-status{display:flex;align-items:center;gap:8px;padding:8px 13px;border:1px solid rgba(34,197,94,.25);background:rgba(34,197,94,.08);border-radius:999px;color:#86efac;font-size:12px;font-weight:700}.dot{width:8px;height:8px;border-radius:50%;background:var(--green);box-shadow:0 0 12px var(--green)}
.hero{min-height:620px;padding:105px 7% 85px;display:grid;place-items:center;text-align:center;position:relative;overflow:hidden}.hero:before{content:"";position:absolute;width:600px;height:600px;border-radius:50%;background:rgba(14,165,233,.1);filter:blur(90px);top:-250px;left:50%;transform:translateX(-50%)}
.eyebrow{display:inline-flex;padding:8px 15px;border:1px solid rgba(56,189,248,.25);background:rgba(56,189,248,.07);border-radius:999px;color:#7dd3fc;font-size:13px;font-weight:700;margin-bottom:25px}.hero h1{max-width:950px;font-size:clamp(42px,7vw,78px);line-height:1.02;letter-spacing:-2.5px;margin-bottom:25px}.gradient{background:linear-gradient(90deg,#38bdf8,#818cf8,#c084fc);-webkit-background-clip:text;background-clip:text;color:transparent}.hero p{max-width:760px;margin:auto;color:var(--muted);font-size:18px;line-height:1.8}
.buttons{margin-top:35px;display:flex;justify-content:center;gap:14px;flex-wrap:wrap}.btn{display:inline-flex;padding:14px 22px;border-radius:10px;text-decoration:none;font-weight:800}.btn-primary{color:white;background:linear-gradient(135deg,#0284c7,#2563eb);box-shadow:0 12px 30px rgba(37,99,235,.25)}.btn-secondary{border:1px solid rgba(56,189,248,.55);color:#7dd3fc;background:rgba(15,23,42,.35)}
.stats{width:88%;max-width:1150px;margin:-30px auto 0;position:relative;z-index:2;display:grid;grid-template-columns:repeat(4,1fr);gap:15px}.stat{padding:22px;background:rgba(16,31,53,.9);border:1px solid var(--line);border-radius:15px;text-align:center}.stat strong{display:block;font-size:27px;margin-bottom:5px}.stat span{color:var(--muted);font-size:12px}
.section{width:88%;max-width:1180px;margin:115px auto}.section-head{text-align:center;margin-bottom:45px}.tag{color:var(--blue);font-size:12px;font-weight:800;letter-spacing:2px;text-transform:uppercase;margin-bottom:12px}.section-head h2{font-size:clamp(30px,4vw,44px);margin-bottom:12px}.section-head p{color:var(--muted);max-width:650px;margin:auto;line-height:1.7}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}.card{position:relative;padding:28px;background:linear-gradient(145deg,rgba(25,43,70,.9),rgba(13,27,47,.9));border:1px solid var(--line);border-radius:18px;transition:.3s;overflow:hidden}.card:hover{transform:translateY(-5px);border-color:rgba(56,189,248,.35);box-shadow:0 20px 50px rgba(0,0,0,.18)}.card-icon{width:50px;height:50px;display:grid;place-items:center;border-radius:13px;background:rgba(56,189,248,.1);font-size:25px;margin-bottom:20px}.card h3{margin-bottom:9px;font-size:19px}.card p{color:var(--muted);line-height:1.65;font-size:14px}.status{display:inline-flex;align-items:center;gap:7px;margin-bottom:10px;color:#4ade80;font-size:12px;font-weight:800}.status i{width:7px;height:7px;border-radius:50%;background:var(--green);box-shadow:0 0 10px var(--green)}
.pipeline-wrap{padding:35px 25px;background:rgba(15,30,51,.65);border:1px solid var(--line);border-radius:22px}.pipeline{display:flex;align-items:center;justify-content:center;gap:10px;flex-wrap:wrap}.stage{width:135px;min-height:110px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:9px;border-radius:15px;background:#182941;border:1px solid #2b405c}.stage:hover{border-color:var(--blue);transform:translateY(-4px)}.stage .emoji{font-size:27px}.stage small{color:var(--muted)}.arrow{color:var(--blue);font-size:25px}
.architecture,.live-panel{display:grid;grid-template-columns:1fr 1fr;gap:22px}.arch-card,.deploy-card{padding:30px;background:#101f35;border:1px solid var(--line);border-radius:18px}.arch-card h3{margin-bottom:20px}.flow-item{display:flex;align-items:center;gap:13px;padding:14px 0;border-bottom:1px solid rgba(148,163,184,.1);color:#cbd5e1}.flow-item:last-child{border-bottom:0}.num{width:30px;height:30px;display:grid;place-items:center;border-radius:9px;background:rgba(56,189,248,.1);color:var(--blue);font-size:12px;font-weight:800}
.tech{display:grid;grid-template-columns:repeat(4,1fr);gap:17px}.tech-box{padding:27px 18px;text-align:center;background:#101f35;border:1px solid var(--line);border-radius:15px}.tech-icon{font-size:32px;margin-bottom:13px}
.terminal{background:#050b14;border:1px solid #26364d;border-radius:17px;overflow:hidden}.terminal-top{padding:12px 16px;display:flex;gap:7px;border-bottom:1px solid #1e293b}.terminal-top i{width:9px;height:9px;border-radius:50%;background:#475569}.terminal-body{padding:25px;color:#94a3b8;font-family:Consolas,monospace;line-height:2;font-size:13px}.green{color:#4ade80}.blue{color:#38bdf8}.deploy-card{background:linear-gradient(145deg,rgba(14,165,233,.13),rgba(139,92,246,.12));border-color:rgba(56,189,248,.2)}.deploy-card .big{font-size:44px;margin-bottom:18px}.deploy-card p{color:var(--muted);line-height:1.7}
footer{margin-top:120px;padding:45px 7%;background:#050c17;border-top:1px solid var(--line);text-align:center}footer strong{color:var(--blue)}footer p{color:#64748b;margin-top:9px;font-size:13px}
@media(max-width:900px){.stats,.cards,.tech{grid-template-columns:repeat(2,1fr)}.architecture,.live-panel{grid-template-columns:1fr}.links{display:none}}@media(max-width:600px){.stats,.cards,.tech{grid-template-columns:1fr}.hero{padding-top:80px}.section{margin:80px auto}.arrow{display:none}}
</style>
</head>
<body>
<nav>
<a href="#home" style="text-decoration:none"><div class="logo"><div class="logo-icon">⚡</div>DevOps <span>Hub</span></div></a>
<div class="links"><a href="#home">Home</a><a href="#status">Status</a><a href="#pipeline">Pipeline</a><a href="#architecture">Architecture</a><a href="#technology">Technology</a></div>
<div class="nav-status"><span class="dot"></span>SYSTEM ONLINE</div>
</nav>

<section class="hero" id="home"><div>
<div class="eyebrow">⚡ AUTOMATED DEPLOYMENT PLATFORM</div>
<h1>Build. Test. <span class="gradient">Deploy.</span><br>Automatically. 🚀</h1>
<p>A complete DevOps CI/CD platform demonstrating automated testing, Docker containerization, Docker Hub image delivery, and cloud deployment with Render.</p>
<div class="buttons"><a class="btn btn-primary" href="#pipeline">▶ Explore Pipeline</a><a class="btn btn-secondary" href="https://github.com/mariswari08207-ar/devops-mini-project" target="_blank">◇ View GitHub</a></div>
</div></section>

<div class="stats"><div class="stat"><strong>100%</strong><span>Automated Workflow</span></div><div class="stat"><strong>6</strong><span>Pipeline Stages</span></div><div class="stat"><strong>Docker</strong><span>Containerized App</span></div><div class="stat"><strong>LIVE</strong><span>Render Deployment</span></div></div>

<section class="section" id="status"><div class="section-head"><div class="tag">Platform Health</div><h2>System Status</h2><p>Current state of the main components in the DevOps workflow.</p></div><div class="cards">
<div class="card"><div class="card-icon">🔄</div><div class="status"><i></i> SUCCESS</div><h3>CI/CD Pipeline</h3><p>GitHub Actions automatically validates the application and builds the deployment image.</p></div>
<div class="card"><div class="card-icon">🐳</div><div class="status"><i></i> READY</div><h3>Docker</h3><p>The Flask application is packaged into a reproducible Docker container image.</p></div>
<div class="card"><div class="card-icon">🚀</div><div class="status"><i></i> LIVE</div><h3>Deployment</h3><p>The production web service is deployed and accessible through Render.</p></div>
</div></section>

<section class="section" id="pipeline"><div class="section-head"><div class="tag">Automation Flow</div><h2>CI/CD Pipeline</h2><p>Every change follows a clear path from source code to production.</p></div><div class="pipeline-wrap"><div class="pipeline">
<div class="stage"><div class="emoji">💻</div><b>Code</b><small>Develop</small></div><div class="arrow">→</div><div class="stage"><div class="emoji">🔀</div><b>GitHub</b><small>Push</small></div><div class="arrow">→</div><div class="stage"><div class="emoji">⚙️</div><b>Build</b><small>Compile</small></div><div class="arrow">→</div><div class="stage"><div class="emoji">🧪</div><b>Test</b><small>Validate</small></div><div class="arrow">→</div><div class="stage"><div class="emoji">🐳</div><b>Docker</b><small>Package</small></div><div class="arrow">→</div><div class="stage"><div class="emoji">🚀</div><b>Deploy</b><small>Release</small></div>
</div></div></section>

<section class="section" id="architecture"><div class="section-head"><div class="tag">How It Works</div><h2>DevOps Architecture</h2><p>An end-to-end workflow connecting source control, automation, containers and cloud deployment.</p></div><div class="architecture">
<div class="arch-card"><h3>⚙️ Automation Flow</h3><div class="flow-item"><span class="num">01</span>Developer updates Flask application</div><div class="flow-item"><span class="num">02</span>Code is pushed to GitHub</div><div class="flow-item"><span class="num">03</span>GitHub Actions runs automated checks</div><div class="flow-item"><span class="num">04</span>Docker image is built and delivered</div><div class="flow-item"><span class="num">05</span>Render deploys the web service</div></div>
<div class="arch-card"><h3>☁️ Deployment Environment</h3><div class="flow-item"><span class="num">A</span>GitHub — Source Repository</div><div class="flow-item"><span class="num">B</span>GitHub Actions — CI/CD</div><div class="flow-item"><span class="num">C</span>Docker Hub — Image Registry</div><div class="flow-item"><span class="num">D</span>Render — Cloud Hosting</div><div class="flow-item"><span class="num">E</span>Flask — Web Application</div></div>
</div></section>

<section class="section" id="technology"><div class="section-head"><div class="tag">Technology</div><h2>Technology Stack</h2><p>Tools used to build, test, package and deploy this project.</p></div><div class="tech">
<div class="tech-box"><div class="tech-icon">🐍</div><b>Python Flask</b></div><div class="tech-box"><div class="tech-icon">🐳</div><b>Docker</b></div><div class="tech-box"><div class="tech-icon">🔀</div><b>GitHub Actions</b></div><div class="tech-box"><div class="tech-icon">📦</div><b>Docker Hub</b></div><div class="tech-box"><div class="tech-icon">☁️</div><b>Render</b></div><div class="tech-box"><div class="tech-icon">🌐</div><b>HTML / CSS</b></div><div class="tech-box"><div class="tech-icon">🧪</div><b>Automated Testing</b></div><div class="tech-box"><div class="tech-icon">⚡</div><b>CI/CD</b></div>
</div></section>

<section class="section"><div class="section-head"><div class="tag">Live Environment</div><h2>Deployment Monitor</h2><p>A visual representation of the production deployment state.</p></div><div class="live-panel">
<div class="terminal"><div class="terminal-top"><i></i><i></i><i></i></div><div class="terminal-body"><div><span class="green">✓</span> Checking source repository...</div><div><span class="green">✓</span> GitHub Actions workflow passed</div><div><span class="green">✓</span> Docker image available</div><div><span class="green">✓</span> Container started successfully</div><div><span class="blue">→</span> Production service: <span class="green">ONLINE</span></div></div></div>
<div class="deploy-card"><div class="big">🚀</div><h3>Production is Live</h3><p>This application has successfully moved from source code through the CI/CD pipeline into a live cloud environment.</p><br><div class="status"><i></i> DEPLOYMENT ACTIVE</div></div>
</div></section>

<footer><strong>DevOps Hub</strong><p>DevOps Mini Project © 2026 · Flask · Docker · GitHub Actions · Docker Hub · Render</p></footer>
</body></html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/health")
def health():
    return {"status": "healthy", "service": "devops-mini-project"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
