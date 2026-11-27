# fix_profile.py
# Run: python fix_profile.py
# Keep portrait.jpg in the same folder.

import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PHOTO = ROOT / "portrait.jpg"

if not PHOTO.exists():
    raise FileNotFoundError("Place portrait.jpg in the repository folder.")

photo = base64.b64encode(PHOTO.read_bytes()).decode("utf-8")

# ==================== BANNER ====================

banner = f'''<svg xmlns="http://www.w3.org/2000/svg"
xmlns:xlink="http://www.w3.org/1999/xlink"
width="1100" height="340" viewBox="0 0 1100 340">

<defs>
  <linearGradient id="bg" x2="1" y2="1">
    <stop offset="0%" stop-color="#FFFFFF"/>
    <stop offset="100%" stop-color="#E3EBF7"/>
  </linearGradient>

  <clipPath id="portrait">
    <rect x="805" y="25" width="250" height="290" rx="16"/>
  </clipPath>

  <clipPath id="reveal">
    <rect x="805" y="25" width="250" height="290">
      <animate attributeName="height"
      from="0" to="290" dur="2s" fill="freeze"/>
    </rect>
  </clipPath>

  <style>
    text {{
      font-family: 'Segoe UI', Arial, sans-serif;
    }}
  </style>
</defs>

<rect x="1" y="1" width="1098" height="338"
rx="18" fill="url(#bg)" stroke="#D5DFEC"/>

<circle cx="740" cy="70" r="55"
fill="#D5E3F5" opacity=".45"/>

<circle cx="720" cy="260" r="35"
fill="#D5E3F5" opacity=".35"/>

<rect x="42" y="38" width="5" height="20"
rx="2" fill="#426A9C"/>

<text x="60" y="53" font-size="13"
letter-spacing="2" font-weight="600" fill="#64748B">
SOFTWARE ENGINEERING &amp; TECHNOLOGY
</text>

<g>
  <animateTransform attributeName="transform"
  type="translate" from="-15 0" to="0 0"
  dur=".8s" fill="freeze"/>

  <animate attributeName="opacity"
  from="0" to="1" dur=".8s" fill="freeze"/>

  <text x="42" y="120" font-size="62"
  font-weight="700" fill="#142D4E">Jay Gupta</text>
</g>

<text x="46" y="163" font-size="26"
font-weight="600" fill="#426A9C">
Backend Software Developer
</text>

<text x="46" y="201" font-size="17" fill="#475569">
Building scalable, secure and reliable software systems.
</text>

<text x="46" y="227" font-size="17" fill="#475569">
Backend Architecture · API Engineering · System Design
</text>

<g font-size="13" font-weight="600"
fill="#315D96" text-anchor="middle">

  <rect x="46" y="246" width="70" height="30"
  rx="7" fill="#DCE8F8"/>
  <text x="81" y="265">Java</text>

  <rect x="126" y="246" width="90" height="30"
  rx="7" fill="#DCE8F8"/>
  <text x="171" y="265">Node.js</text>

  <rect x="226" y="246" width="100" height="30"
  rx="7" fill="#DCE8F8"/>
  <text x="276" y="265">REST APIs</text>

  <rect x="336" y="246" width="110" height="30"
  rx="7" fill="#DCE8F8"/>
  <text x="391" y="265">Databases</text>

  <rect x="456" y="246" width="85" height="30"
  rx="7" fill="#DCE8F8"/>
  <text x="498.5" y="265">DevOps</text>

</g>

<line x1="46" y1="292" x2="735" y2="292"
stroke="#CBD8E9"/>

<text x="46" y="318" font-size="14" fill="#64748B">
MIT-ADT University · B.Tech IT · 2027 · CGPA 8.79/10
</text>

<rect x="794" y="14" width="272" height="312"
rx="22" fill="#FFFFFF" stroke="#D5DFEC"/>

<rect x="805" y="25" width="250" height="290"
rx="16" fill="#DCE8F8"/>

<g clip-path="url(#portrait)">
  <g clip-path="url(#reveal)">
    <image xlink:href="data:image/jpeg;base64,{photo}"
    x="805" y="25" width="250" height="290"
    preserveAspectRatio="xMidYMid slice"/>
  </g>
</g>

</svg>'''

(ROOT / "banner.svg").write_text(banner, encoding="utf-8")


# ==================== DASHBOARD ====================

metrics = [
    ("800+", "Students Supported", "Campus Applications"),
    ("15+", "REST APIs Developed", "Backend Engineering"),
    ("30%", "Response Time Reduction", "Performance Optimization"),
    ("1,000+", "Simulated Concurrent Users", "Scalability Testing"),
]

dashboard = '''<svg xmlns="http://www.w3.org/2000/svg"
width="1100" height="185" viewBox="0 0 1100 185">

<rect x="1" y="1" width="1098" height="183"
rx="16" fill="#F4F7FC" stroke="#D5DFEC"/>

<g font-family="Segoe UI, Arial, sans-serif">
'''

for i, (value, label, description) in enumerate(metrics):
    x = 18 + i * 270

    dashboard += f'''
    <g transform="translate({x} 18)">

      <animate attributeName="opacity"
      from="0" to="1" begin="{i * 0.15}s"
      dur=".7s" fill="freeze"/>

      <rect width="254" height="149" rx="12"
      fill="#FFFFFF" stroke="#D5DFEC"/>

      <rect x="18" y="18" width="32" height="4"
      rx="2" fill="#426A9C"/>

      <text x="18" y="67" font-size="39"
      font-weight="700" fill="#142D4E">{value}</text>

      <text x="18" y="96" font-size="14"
      font-weight="600" fill="#426A9C">{label}</text>

      <text x="18" y="119" font-size="12"
      fill="#64748B">{description}</text>

    </g>
    '''

dashboard += "</g></svg>"

(ROOT / "dashboard.svg").write_text(
    dashboard, encoding="utf-8"
)


# ==================== PROFESSIONAL PROFILE ====================

profiles = [
    (
        "EDUCATION",
        "B.Tech Information Technology",
        "MIT-ADT University · 2027 · CGPA 8.79/10"
    ),
    (
        "RESEARCH",
        "IEEE IGNITE 2026",
        "Published Research Co-author · CESS"
    ),
    (
        "LEADERSHIP",
        "Technical Head",
        "College Council"
    ),
    (
        "PROBLEM SOLVING",
        "200+ DSA Problems",
        "LeetCode · Data Structures and Algorithms"
    ),
]

profile = '''<svg xmlns="http://www.w3.org/2000/svg"
width="1100" height="250" viewBox="0 0 1100 250">

<rect x="1" y="1" width="1098" height="248"
rx="16" fill="#F4F7FC" stroke="#D5DFEC"/>

<g font-family="Segoe UI, Arial, sans-serif">
'''

for i, (category, title, description) in enumerate(profiles):
    x = 18 + (i % 2) * 540
    y = 18 + (i // 2) * 116

    profile += f'''
    <g transform="translate({x} {y})">

      <animate attributeName="opacity"
      from="0" to="1" begin="{i * 0.15}s"
      dur=".7s" fill="freeze"/>

      <rect width="524" height="100" rx="12"
      fill="#FFFFFF" stroke="#D5DFEC"/>

      <rect x="16" y="19" width="4" height="62"
      rx="2" fill="#426A9C"/>

      <text x="34" y="25" font-size="11"
      letter-spacing="1.5" font-weight="600"
      fill="#64748B">{category}</text>

      <text x="34" y="52" font-size="20"
      font-weight="700" fill="#142D4E">{title}</text>

      <text x="34" y="77" font-size="13"
      fill="#475569">{description}</text>

    </g>
    '''

profile += "</g></svg>"

(ROOT / "profile-scan.svg").write_text(
    profile, encoding="utf-8"
)


# ==================== README ====================

readme = '''<div align="center">

<img src="./banner.svg?v=3" width="100%" alt="Jay Gupta — Backend Software Developer"/>

<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=500&size=18&pause=1500&color=426A9C&center=true&vCenter=true&width=750&lines=Backend+Engineering+%26+Software+Development;Scalable+APIs+%7C+Database+Engineering;System+Design+%7C+Cloud+Infrastructure" alt="Professional headline"/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-426A9C?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jay-gupta-68a41a290/)
[![Email](https://img.shields.io/badge/Email-426A9C?style=for-the-badge&logo=gmail&logoColor=white)](mailto:jayakhileshgupta1@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-142D4E?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Jaygupta2502)

</div>

## Professional Overview

Backend-focused software developer pursuing a **B.Tech in Information Technology at MIT-ADT University, Pune**.

Experienced in developing secure RESTful APIs, role-based applications and database-driven systems with a focus on scalability, performance and reliability.

<img src="./profile-scan.svg?v=3" width="100%" alt="Professional profile"/>

## Engineering Impact

<img src="./dashboard.svg?v=3" width="100%" alt="Engineering impact metrics"/>

## Technical Expertise

<table>
<tr>
<td width="50%" align="center" valign="top">

### Programming Languages

<img src="https://skillicons.dev/icons?i=java,python,js,cpp&theme=light" height="45"/>

Java · Python · JavaScript · SQL  
C++ (Fundamentals)

</td>
<td width="50%" align="center" valign="top">

### Backend Engineering

<img src="https://skillicons.dev/icons?i=nodejs,express&theme=light" height="45"/>

Node.js · Express.js · REST APIs  
JWT · RBAC · Microservices Concepts

</td>
</tr>
<tr>
<td align="center" valign="top">

### Database Engineering

<img src="https://skillicons.dev/icons?i=mysql,mongodb&theme=light" height="45"/>

MySQL · MongoDB  
Indexing · Schema Design · Query Optimization

</td>
<td align="center" valign="top">

### DevOps & Infrastructure

<img src="https://skillicons.dev/icons?i=docker,kubernetes,githubactions&theme=light" height="45"/>

Docker · Kubernetes · CI/CD  
GitHub Actions

</td>
</tr>
<tr>
<td align="center" valign="top">

### Cloud Technologies

<img src="https://skillicons.dev/icons?i=aws,gcp,azure&theme=light" height="45"/>

AWS · Google Cloud · Microsoft Azure  
Cloud Computing Fundamentals

</td>
<td align="center" valign="top">

### Frontend & Development Tools

<img src="https://skillicons.dev/icons?i=react,html,css,git,github&theme=light" height="45"/>

React.js · HTML · CSS  
Git · GitHub

</td>
</tr>
</table>

**Computer Science Fundamentals:**  
DSA · OOP · DBMS · Operating Systems · Computer Networks · System Design · Software Testing

## Professional Experience

### Backend Developer Intern — MIT SAP

**November 2025 – April 2026**

- Developed a MERN-based elective management platform supporting **800+ students**.
- Implemented Student, Coordinator and Support role-based workflows.
- Automated Excel-based bulk student onboarding.
- Implemented server-side validation and data integrity checks.

### Website Developer Intern — MIT-ADT University

**May 2025 – June 2025**

- Developed a role-based event management platform supporting **500+ users**.
- Designed and implemented **15+ RESTful APIs**.
- Reduced average response time by **30%** through database indexing and query optimization.
- Implemented JWT authentication and role-based access control.

## Featured Engineering Projects

<table>
<tr>
<td width="50%" valign="top">

### Career Advancement Scheme

**Faculty Appraisal & Workflow Management**

- Supports 100+ faculty members.
- 9+ API-driven forms.
- Role-based access control.
- Document upload management.
- Structured approval workflows.

<img src="https://skillicons.dev/icons?i=nodejs,express,mongodb,react&theme=light" height="35"/>

</td>
<td width="50%" valign="top">

### Scalable Event Booking

**Performance & Concurrency Engineering**

- 1,000+ simulated concurrent users.
- Caching strategies.
- API rate limiting.
- Load and stress testing.
- Performance optimization.

![Caching](https://img.shields.io/badge/Caching-426A9C?style=flat-square)
![Scalability](https://img.shields.io/badge/Scalability-426A9C?style=flat-square)

</td>
</tr>
</table>

## Research & Publication

### Campus Event Scheduling System (CESS)

**An Automated Role-Based Workflow for Academic Event Management**

IEEE IGNITE 2026 International Conference  
Published: 30 September 2026

[![IEEE Publication](https://img.shields.io/badge/Read_Research_Paper-426A9C?style=for-the-badge&logo=ieee&logoColor=white)](https://doi.org/10.1109/IGNITE69592.2026.11706245)

## Achievements & Leadership

| Achievement | Description |
|:---|:---|
| Research Publication | IEEE IGNITE 2026 |
| Technical Leadership | Technical Head — College Council |
| Problem Solving | 200+ DSA Problems on LeetCode |

## Certifications

| Certification | Organization | Status |
|:---|:---|:---|
| Docker & Kubernetes Masterclass | Coursera | Completed — Apr 2026 |
| Python Programming | IIT Bombay | Completed |
| Data Science Professional Certificate | IBM | In Progress |

## GitHub Analytics

<div align="center">

<img width="49%" src="https://github-readme-stats.vercel.app/api?username=Jaygupta2502&show_icons=true&bg_color=F4F7FC&title_color=315D96&icon_color=426A9C&text_color=475569&border_color=D5DFEC" alt="GitHub statistics"/>

<img width="49%" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Jaygupta2502&layout=compact&bg_color=F4F7FC&title_color=315D96&text_color=475569&border_color=D5DFEC" alt="Top languages"/>

<br/><br/>

<img width="75%" src="https://streak-stats.demolab.com?user=Jaygupta2502&background=F4F7FC&border=D5DFEC&ring=426A9C&fire=426A9C&currStreakLabel=315D96&sideLabels=475569&currStreakNum=142D4E&sideNums=142D4E&dates=64748B" alt="Contribution streak"/>

<br/><br/>

<img width="100%" src="https://github-readme-activity-graph.vercel.app/graph?username=Jaygupta2502&bg_color=F4F7FC&color=475569&line=426A9C&point=315D96&area=true&area_color=DCE8F8&hide_border=true" alt="Contribution activity"/>

</div>

---

<div align="center">

**Building Reliable Software. Engineering Scalable Solutions.**

[![LinkedIn](https://img.shields.io/badge/Connect_on_LinkedIn-426A9C?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jay-gupta-68a41a290/)
[![Email](https://img.shields.io/badge/Get_in_Touch-142D4E?style=for-the-badge&logo=gmail&logoColor=white)](mailto:jayakhileshgupta1@gmail.com)

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:F4F7FC,50:DCE8F8,100:B5CBE7&height=90&section=footer"/>

</div>
'''

(ROOT / "README.md").write_text(readme, encoding="utf-8")

# Validate generated SVG files.

import xml.etree.ElementTree as ET

for filename in ["banner.svg", "dashboard.svg", "profile-scan.svg"]:
    ET.parse(ROOT / filename)
    print(f"Generated and validated: {filename}")

print("Generated: README.md")
print("Original portrait embedded successfully.")
print("All files now use the same light-blue theme.")

# GitHub rendering and external statistics require live verification.
