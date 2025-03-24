from jinja2 import Template

template = Template(r"""
\documentclass[a4paper,10pt]{article}
\usepackage{xcolor}
\usepackage{geometry}
\geometry{left=0.5in, right=0.5in, top=0.5in, bottom=0.5in}
\usepackage{titlesec}
\usepackage{enumitem}
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    urlcolor=blue
}

\definecolor{myblue}{RGB}{30,144,255}
\titleformat{\section}{\large\bfseries\color{myblue}}{}{0em}{}[\titlerule]

\begin{document}

\begin{center}
    {\Huge \textbf{{{{ name }}}}}\\
    \vspace{0.2cm}
    \textcolor{myblue}{\large{{{ title }}}}\\
    \vspace{0.2cm}
    \texttt{Email: {{{ email }}} | Phone: {{{ phone }}} | LinkedIn: \href{{{{ linkedin }}}}{{LinkedIn}}}
\end{center}

\section*{Education}
\textbf{{{{ education.degree }}}} - {{{ education.institution }}} ({{{ education.year }}})

\section*{Skills}
\begin{itemize}
    {% for skill in skills %}
    \item {{{ skill }}}
    {% endfor %}
\end{itemize}

\section*{Experience}
{% for job in experience %}
\textbf{{{{ job.role }}}} - {{{ job.company }}} ({{{ job.year }}})\\
{{{ job.description }}}
\vspace{0.2cm}
{% endfor %}

\section*{Projects}
{% for project in projects %}
\textbf{{{{ project.name }}}}\\
{{{ project.description }}}
\vspace{0.2cm}
{% endfor %}

\end{document}
""")

data = {
    "name": "John Doe",
    "title": "Software Engineer",
    "email": "johndoe@example.com",
    "phone": "+1234567890",
    "linkedin": "https://linkedin.com/in/johndoe",
    "education": {
        "degree": "Master of Computer Science",
        "institution": "XYZ University",
        "year": "2023"
    },
    "skills": ["Python", "Machine Learning", "Django", "ReactJS"],
    "experience": [
        {"role": "Software Developer", "company": "ABC Corp", "year": "2022-2023", "description": "Worked on AI-based applications."},
        {"role": "Intern", "company": "XYZ Ltd", "year": "2021-2022", "description": "Developed backend APIs."}
    ],
    "projects": [
        {"name": "AI Chatbot", "description": "Developed an NLP-based chatbot using Python and TensorFlow."},
        {"name": "E-commerce Website", "description": "Built a full-stack web application using React and Django."}
    ]
}

latex_code = template.render(data)

with open("resume.tex", "w") as f:
    f.write(latex_code)

print("LaTeX resume generated successfully!")
