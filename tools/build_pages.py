#!/usr/bin/env python3
"""Génère les pages HTML du site ITS (en-tête, pied de page et icônes communs).
Usage : python3 tools/build_pages.py   (écrit dans site/)"""
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "site"
TEL, TEL_H = "+33695607875", "06 95 60 78 75"
MAIL = "assistance@itservices75.fr"

ICONS = {
 "cap": '<path d="M22 10 12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/><path d="M22 10v6"/>',
 "nodes": '<circle cx="6" cy="18" r="3"/><circle cx="18" cy="18" r="3"/><circle cx="12" cy="5" r="3"/><path d="M10.5 7.6 7.5 15.4M13.5 7.6l3 7.8M9 18h6"/>',
 "layers": '<path d="m12 2 10 5-10 5L2 7z"/><path d="m2 12 10 5 10-5"/><path d="m2 17 10 5 10-5"/>',
 "headset": '<path d="M3 14v-2a9 9 0 0 1 18 0v2"/><rect x="2" y="14" width="5" height="7" rx="2"/><rect x="17" y="14" width="5" height="7" rx="2"/><path d="M19 21a4 4 0 0 1-4 2h-2"/>',
 "users": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
 "building": '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M12 6h.01M16 6h.01M8 10h.01M12 10h.01M16 10h.01M8 14h.01M12 14h.01M16 14h.01"/>',
 "laptop": '<rect x="4" y="4" width="16" height="11" rx="2"/><path d="M2 19h20"/>',
 "play": '<rect x="2" y="4" width="20" height="13" rx="2"/><path d="m10 8 5 2.5-5 2.5z"/><path d="M8 21h8M12 17v4"/>',
 "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
 "arrow": '<path d="M5 12h14M12 5l7 7-7 7"/>',
 "send": '<path d="m22 2-7 20-4-9-9-4z"/><path d="M22 2 11 13"/>',
 "gear": '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/>',
 "chev": '<path d="m6 9 6 6 6-6"/>',
 "menu": '<path d="M4 6h16M4 12h16M4 18h16"/>',
 "x": '<path d="M18 6 6 18M6 6l12 12"/>',
 "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
 "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
 "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
 "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
 "bot": '<rect x="3" y="8" width="18" height="12" rx="3"/><path d="M12 8V4M8 4h8M9 14h.01M15 14h.01"/>',
 "zap": '<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
 "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
 "wrench": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z"/>',
 "download": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/>',
 "wifi": '<path d="M5 12.6a10 10 0 0 1 14 0M1.4 9a15 15 0 0 1 21.2 0M8.5 16.1a5 5 0 0 1 7 0M12 20h.01"/>',
 "chart": '<path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 5-6"/>',
 "doc": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
 "target": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
 "spark": '<path d="M12 3l1.9 5.8L20 11l-6.1 2.2L12 19l-1.9-5.8L4 11l6.1-2.2z"/>',
 "handshake": '<path d="m11 17 2 2a1 1 0 1 0 3-3"/><path d="m14 14 2.5 2.5a1 1 0 1 0 3-3l-3.9-3.9a3 3 0 0 0-4.2 0l-.9.9a1 1 0 1 1-3-3l2.8-2.8a5.8 5.8 0 0 1 7.1-.9l.5.3a2 2 0 0 0 1.4.3L22 4"/><path d="m21 3 1 11h-2M3 3 2 14l6.5 6.5a1 1 0 1 0 3-3M3 4h8"/>',
 "lock": '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
 "monitor": '<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/>',
}

def sprite():
    return ('<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>'
            + "".join(f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in ICONS.items())
            + '</defs></svg>')

def ic(name, cls="ic"):
    return f'<svg class="{cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'

FLAGS = ('<div class="flags">'
 '<svg viewBox="0 0 40 40" aria-label="France"><clipPath id="cf"><circle cx="20" cy="20" r="20"/></clipPath><g clip-path="url(#cf)"><rect width="14" height="40" fill="#1f4fbf"/><rect x="13" width="14" height="40" fill="#fff"/><rect x="26" width="14" height="40" fill="#e0262f"/></g></svg>'
 '<svg viewBox="0 0 40 40" aria-label="Algérie"><clipPath id="cd"><circle cx="20" cy="20" r="20"/></clipPath><g clip-path="url(#cd)"><rect width="20" height="40" fill="#0b7d3e"/><rect x="20" width="20" height="40" fill="#fff"/><circle cx="21" cy="20" r="8" fill="#d21034"/><circle cx="23.2" cy="20" r="6.4" fill="#fff"/><path d="m26.5 16.6 1 2.6 2.8.1-2.2 1.7.8 2.7-2.4-1.6-2.3 1.6.8-2.7-2.2-1.7 2.8-.1z" fill="#d21034"/></g></svg>'
 '</div>')

NAV = [("index.html", "Accueil"), ("formations.html", "Formations"), ("SOL", "Solutions"),
       ("services.html", "Services"), ("a-propos.html", "À propos"), ("contact.html", "Contact")]
SOL = [("solutions.html#automatisation", "nodes", "Automatisation & IA", "Workflows, agents IA, chatbots"),
       ("solutions.html#crm", "layers", "Conception de CRM", "Clients, devis, facturation, suivi"),
       ("solutions.html#web", "globe", "Sites web & outils", "Sites vitrines, espaces clients")]

def header(active):
    items = []
    for href, label in NAV:
        if href == "SOL":
            cls = ' class="active"' if active == "solutions.html" else ""
            menu = "".join(f'<a href="{h}">{ic(i)}<span><strong>{t}</strong><small>{d}</small></span></a>' for h, i, t, d in SOL)
            items.append(f'<div class="dd"><button{cls} aria-expanded="false" aria-haspopup="true">Solutions {ic("chev")}</button><div class="dd-menu">{menu}</div></div>')
        else:
            cls = ' class="active" aria-current="page"' if href == active else ""
            items.append(f'<a href="{href}"{cls}>{label}</a>')
    drawer = []
    for href, label in NAV:
        if href == "SOL":
            drawer.append('<a href="solutions.html">Solutions</a>')
            drawer += [f'<a class="sub" href="{h}">{t}</a>' for h, i, t, d in SOL]
        else:
            drawer.append(f'<a href="{href}">{label}</a>')
    return f'''<a class="skip" href="#main">Aller au contenu</a>
<header class="site">
 <div class="container hdr">
  <a class="brand" href="index.html" aria-label="Informatique Team Services — accueil"><img src="logo-its.png" alt="Informatique Team Services — ITS" width="236" height="62"></a>
  <nav class="main" aria-label="Navigation principale">{"".join(items)}</nav>
  <a class="btn btn-blue" href="contact.html">Demander un devis {ic("send")}</a>
  <button class="burger" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="drawer">{ic("menu")}</button>
 </div>
 <div class="drawer" id="drawer">{"".join(drawer)}<a class="btn btn-blue" href="contact.html">Demander un devis {ic("send")}</a></div>
</header>'''

FOOTER = f'''<footer class="site">
 <div class="container">
  <div class="fgrid4">
   <div><span class="flogo"><img src="logo-its.png" alt="Informatique Team Services" width="175" height="46" loading="lazy"></span>
    <p>Formation professionnelle, automatisation & IA, conception de CRM et assistance informatique pour les entreprises, les indépendants et les organismes de formation.</p></div>
   <div><h4>Formations</h4><ul>
    <li><a href="formations.html#ia">IA & ChatGPT</a></li><li><a href="formations.html#bureautique">Bureautique</a></li>
    <li><a href="formations.html#crm">CRM & outils métiers</a></li><li><a href="formations.html#automatisation">Automatisation no-code</a></li></ul></div>
   <div><h4>Solutions & services</h4><ul>
    <li><a href="solutions.html#automatisation">Automatisation & IA</a></li><li><a href="solutions.html#crm">Conception de CRM</a></li>
    <li><a href="solutions.html#web">Sites web</a></li><li><a href="services.html">Assistance informatique</a></li></ul></div>
   <div><h4>Contact</h4><p><a href="tel:{TEL}">{TEL_H}</a><br><a href="mailto:{MAIL}">{MAIL}</a><br>Intervention France & Algérie<br>Présentiel et à distance</p></div>
  </div>
  <div class="copy"><span>© <span id="y">2026</span> Informatique Team Services — Tous droits réservés.</span><span><a href="a-propos.html">À propos</a> · <a href="mentions-legales.html">Mentions légales & confidentialité</a></span></div>
 </div>
</footer>
<div class="mbar"><a class="btn btn-line" href="tel:{TEL}">{ic("phone")}Appeler</a><a class="btn btn-blue" href="contact.html">Demander un devis</a></div>'''

def page(file, title, desc, body, active=None):
    html = f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="__SITE_URL__/{'' if file == 'index.html' else file}">
<meta name="theme-color" content="#0b6cf0">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta property="og:type" content="website"><meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="Informatique Team Services">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="__SITE_URL__/{'' if file == 'index.html' else file}">
<meta property="og:image" content="__SITE_URL__/hero-its.jpg"><meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Montserrat:wght@700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css?v=4">
{LDJSON if file == 'index.html' else ''}
</head>
<body>
{sprite()}
{header(active or file)}
<main id="main">
{body}
</main>
{FOOTER}
<script src="assets/main.js?v=4" defer></script>
</body>
</html>
'''
    (SITE / file).write_text(html, encoding="utf-8")

LDJSON = f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"ProfessionalService","name":"Informatique Team Services","alternateName":"ITS","url":"__SITE_URL__/","logo":"__SITE_URL__/logo-its.png","image":"__SITE_URL__/hero-its.jpg","telephone":"{TEL}","email":"{MAIL}","areaServed":[{{"@type":"Country","name":"France"}},{{"@type":"Country","name":"Algérie"}}],"description":"Formation professionnelle, automatisation et IA, conception de CRM et assistance informatique.","knowsAbout":["Formation IA","ChatGPT","Bureautique","CRM","Automatisation n8n","Make","Assistance informatique"]}}</script>'''

def cta(title="Un projet, une formation, un besoin ?", text="Parlez-nous de votre situation : nous vous répondons sous 24 h avec une proposition claire et sans engagement.", besoin=None):
    q = f"?besoin={besoin}" if besoin else ""
    return f'''<section class="section"><div class="container"><div class="cta">
 <div><h2>{title}</h2><p>{text}</p></div>
 <div class="actions"><a class="btn btn-white" href="contact.html{q}">Demander un devis {ic("send")}</a><a class="btn btn-line" style="background:transparent;color:#fff;border-color:#fff" href="tel:{TEL}">{ic("phone")}{TEL_H}</a></div>
</div></div></section>'''

def checks(items):
    return '<ul class="checks">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def page_hero(crumb, eyebrow, h1, text):
    return f'''<section class="page-hero"><div class="container">
 <div class="crumbs"><a href="index.html">Accueil</a> › {crumb}</div>
 <div class="eyebrow">{eyebrow}</div><h1>{h1}</h1><p>{text}</p>
</div></section>'''

# ---------- ACCUEIL ----------
SVC4 = [("c-blue", "cap", "Formation Professionnelle", "Développez vos compétences (IA, ChatGPT, bureautique, CRM, outils métiers…).", "formations.html"),
        ("c-violet", "nodes", "Automatisation & IA", "Gagnez du temps et de la productivité avec des workflows intelligents (n8n, Make, API, IA…).", "solutions.html#automatisation"),
        ("c-green", "layers", "Conception de CRM", "Des solutions CRM sur mesure (gestion clients, devis, facturation, commandes, suivi d’activité…).", "solutions.html#crm"),
        ("c-orange", "headset", "Assistance Informatique", "Dépannage, installation, configuration, maintenance et accompagnement au quotidien.", "services.html")]
svc_html = "".join(f'<a class="svc {c}" href="{h}"><div class="top">{ic(i)}<h3>{t}</h3></div><p>{d}</p><span class="go">{ic("arrow")}</span></a>' for c, i, t, d, h in SVC4)

PERKS = [("users", "Entreprises", "& indépendants"), ("building", "Organismes", "de formation"),
         ("laptop", "Présentiel", "& distanciel"), ("play", "E-learning", "(à votre rythme)"),
         ("shield", "Solutions", "sur mesure"), ("FLAGS", "Intervention", "France & Algérie")]
perks_html = "".join(f'<div class="perk">{FLAGS if i == "FLAGS" else ic(i)}{a}<span>{b}</span></div>' for i, a, b in PERKS)

home = f'''<section class="hero hero-xl">
 <div class="hero-bg" aria-hidden="true"><img src="hero-its-wide.jpg" alt="" width="902" height="489" fetchpriority="high"></div>
 <div class="container hero-grid">
 <div class="hero-txt">
  <div class="eyebrow">Votre partenaire digital</div>
  <h1>Formation, Automatisation, Conception de <span class="blue">CRM</span> &amp; Assistance Informatique</h1>
  <p class="lead">Nous vous accompagnons pour développer vos compétences, automatiser vos processus, concevoir vos solutions CRM sur mesure et assurer le bon fonctionnement de votre informatique.</p>
  <div class="actions"><a class="btn btn-blue" href="formations.html">{ic("cap")}Découvrir nos formations</a><a class="btn btn-line" href="solutions.html">{ic("gear")}Nos solutions</a></div>
 </div>
 </div>
 <div class="hero-mobile-img"><img src="hero-its.jpg" alt="Ordinateur portable affichant la plateforme ITS : formation, automatisation & IA, CRM sur mesure et assistance IT" width="882" height="490" loading="lazy"></div>
</section>

''' + f'''<section aria-label="Nos domaines"><div class="container services4">{svc_html}</div></section>
<section aria-label="Nos atouts"><div class="container perks">{perks_html}</div></section>

<section class="section alt"><div class="container">
 <div class="head center"><div class="eyebrow">Pour qui ?</div><h2>Des solutions adaptées à chaque structure</h2><p>Que vous soyez une PME, un indépendant ou un organisme de formation, nous construisons avec vous la réponse adaptée à vos enjeux.</p></div>
 <div class="grid3">
  <div class="card t-blue"><div class="badge">{ic("users")}</div><h3>Entreprises & indépendants</h3><p>Montée en compétences des équipes, outils de gestion sur mesure et automatisation des tâches répétitives.</p>{checks(["Formation intra-entreprise","CRM, devis et facturation","Automatisations et agents IA"])}</div>
  <div class="card t-violet"><div class="badge">{ic("building")}</div><h3>Organismes de formation</h3><p>Intervention de formateurs experts et outils pour digitaliser la gestion de vos sessions.</p>{checks(["Animation de modules IA et numérique","Supports et parcours e-learning","Outils de suivi des apprenants"])}</div>
  <div class="card t-orange"><div class="badge">{ic("monitor")}</div><h3>Particuliers</h3><p>Un accompagnement simple et rassurant pour votre informatique du quotidien.</p>{checks(["Dépannage et installation","Initiation à l’IA et au numérique","Assistance à distance"])}</div>
 </div>
</div></section>

<section class="section"><div class="container split">
 <div class="why">
  <div class="card"><div class="badge">{ic("cap")}</div><h3>Pédagogie</h3><p>Organisme de formation déclaré, nous rendons vos équipes autonomes.</p></div>
  <div class="card t-violet"><div class="badge">{ic("zap")}</div><h3>Technique</h3><p>Automatisations, IA et CRM conçus et mis en production par nos soins.</p></div>
  <div class="card"><div class="badge" style="background:var(--green-l);color:var(--green)">{ic("handshake")}</div><h3>Proximité</h3><p>Un interlocuteur unique qui explique sans jargon.</p></div>
  <div class="card t-orange"><div class="badge">{ic("headset")}</div><h3>Suivi</h3><p>Assistance et évolutions après la mise en service.</p></div>
 </div>
 <div>
  <div class="eyebrow">Pourquoi ITS</div>
  <h2 style="font-size:clamp(28px,3vw,38px)">Un interlocuteur unique, de la formation à la mise en production</h2>
  <p class="lead">Nous réunissons la pédagogie d’un organisme de formation et le savoir-faire technique d’un intégrateur : vos équipes apprennent les outils que nous mettons en place pour elles.</p>
  {checks(["Des solutions construites à partir de vos usages réels","Un accompagnement humain, sans jargon","Présentiel, distanciel ou e-learning, selon vos contraintes","Un suivi après la mise en service"])}
  <div class="actions"><a class="btn btn-blue" href="a-propos.html">En savoir plus {ic("arrow")}</a></div>
 </div>
</div></section>

<section class="section alt"><div class="container">
 <div class="head center"><div class="eyebrow">Notre méthode</div><h2>Un accompagnement clair en 4 étapes</h2></div>
 <div class="steps">
  <div class="step"><h3>Diagnostic gratuit</h3><p>Nous échangeons sur vos besoins, vos outils et vos objectifs.</p></div>
  <div class="step"><h3>Proposition sur mesure</h3><p>Programme de formation ou solution technique, avec un devis détaillé.</p></div>
  <div class="step"><h3>Réalisation</h3><p>Formation, développement ou intervention, avec des points d’étape réguliers.</p></div>
  <div class="step"><h3>Suivi & évolution</h3><p>Évaluation, ajustements et accompagnement dans la durée.</p></div>
 </div>
</div></section>
{cta()}'''

page("index.html", "ITS — Informatique Team Services | Formation, Automatisation, CRM & Assistance informatique",
     "Formation professionnelle (IA, ChatGPT, bureautique, CRM), automatisation & IA (n8n, Make), conception de CRM sur mesure et assistance informatique. Présentiel, distanciel et e-learning, en France et en Algérie.", home)

# ---------- FORMATIONS ----------
COURSES = [
 ("ia", "c-blue", "spark", "L’IA générative au service de votre activité", "Utiliser ChatGPT, Copilot ou Gemini pour rédiger, synthétiser, analyser et gagner du temps, en toute sécurité.", ["Tous niveaux", "Présentiel / distanciel", "Intra & inter"],
  ["Comprendre le fonctionnement des IA génératives", "Rédiger des prompts efficaces", "Automatiser les tâches de rédaction et d’analyse", "Bonnes pratiques : confidentialité et RGPD"]),
 ("bureautique", "c-green", "doc", "Bureautique & Microsoft 365", "Word, Excel, Outlook, Teams, OneDrive : maîtriser les fonctions qui changent le quotidien.", ["Débutant à avancé", "Présentiel / distanciel"],
  ["Excel : formules, tableaux croisés, graphiques", "Word : documents longs et modèles", "Outlook & Teams : organisation et collaboration", "Partage et travail collaboratif dans le cloud"]),
 ("crm", "c-violet", "layers", "CRM & outils métiers", "Prendre en main un CRM et structurer la relation client, du prospect à la facture.", ["Utilisateurs & managers", "Sur votre propre outil"],
  ["Organiser contacts, opportunités et pipeline", "Devis, commandes et facturation", "Tableaux de bord et suivi d’activité", "Bonnes pratiques de saisie et de suivi"]),
 ("automatisation", "c-orange", "nodes", "Automatiser ses processus avec le no-code et l’IA", "Concevoir ses premiers workflows (n8n, Make) et connecter ses outils pour supprimer les tâches répétitives.", ["Intermédiaire", "Ateliers pratiques"],
  ["Identifier les tâches automatisables", "Créer des workflows n8n / Make", "Connecter API, emails, tableurs et CRM", "Intégrer l’IA dans un workflow"]),
 ("numerique", "c-blue", "monitor", "Les bases du numérique", "Prendre en main l’ordinateur, internet, la messagerie et les démarches en ligne en toute sérénité.", ["Débutant", "Individuel ou petit groupe"],
  ["Ordinateur, fichiers et dossiers", "Navigation internet et messagerie", "Démarches administratives en ligne", "Sécurité : mots de passe, arnaques"]),
 ("sur-mesure", "c-green", "target", "Formation sur mesure", "Un programme construit à partir de vos outils, de vos métiers et de vos objectifs.", ["Intra-entreprise", "Organismes de formation"],
  ["Analyse du besoin et des niveaux", "Programme et supports personnalisés", "Cas pratiques issus de votre activité", "Évaluation et bilan de fin de formation"]),
]
courses_html = "".join(f'''<article class="course" id="{cid}"><div class="badge {c}">{ic(i)}</div><div>
 <h3>{t}</h3><p>{d}</p><div class="meta">{"".join(f'<span class="tag">{m}</span>' for m in meta)}</div>{checks(obj)}
 <div class="actions" style="margin-top:18px"><a class="btn btn-line" href="contact.html?besoin=Formation">Demander le programme {ic("arrow")}</a></div></div></article>''' for cid, c, i, t, d, meta, obj in COURSES)

formations = page_hero("Formations", "Formation professionnelle", "Des formations concrètes pour maîtriser les outils d’aujourd’hui",
  "IA et ChatGPT, bureautique, CRM, automatisation : des parcours pratiques, construits à partir de vos cas réels et adaptés au niveau de chaque participant.") + f'''
<section aria-label="Formats"><div class="container perks" style="padding-top:44px">{"".join(f'<div class="perk">{ic(i)}{a}<span>{b}</span></div>' for i,a,b in [("laptop","Présentiel","dans vos locaux"),("play","Distanciel","en classe virtuelle"),("monitor","E-learning","à votre rythme"),("users","Intra","ou inter-entreprises"),("target","Programmes","sur mesure"),("shield","Organisme","de formation déclaré")])}</div></section>
<section class="section alt" style="padding-top:64px"><div class="container">
 <div class="head"><div class="eyebrow">Catalogue</div><h2>Nos formations</h2><p>Chaque programme est ajusté à votre contexte : durée, niveau, outils et exemples sont définis avec vous lors du diagnostic.</p></div>
 <div class="grid2">{courses_html}</div>
</div></section>
<section class="section"><div class="container split">
 <div>
  <div class="eyebrow">Notre pédagogie</div>
  <h2 style="font-size:clamp(28px,3vw,38px)">Apprendre en pratiquant</h2>
  <p class="lead">Nos formations alternent apports, démonstrations et exercices sur des situations tirées de votre activité. Chaque participant repart avec des usages directement applicables.</p>
  {checks(["Positionnement des participants avant la formation","Exercices pratiques et cas réels","Supports remis à chaque participant","Évaluation des acquis et attestation de fin de formation"])}
 </div>
 <div class="panel"><h3>Organismes de formation</h3><p style="color:#d6e4ff">Vous cherchez un intervenant expert en IA, en outils numériques ou en CRM ? Nous animons des modules au sein de vos parcours et vous aidons à digitaliser vos formations.</p>
  {checks(["Formateur expert disponible en présentiel et à distance","Conception de modules et de supports","Création de parcours e-learning"])}
  <div class="actions"><a class="btn btn-white" href="contact.html?besoin=Formation">Nous consulter {ic("arrow")}</a></div></div>
</div></section>
<section class="section alt"><div class="container"><div class="head center"><div class="eyebrow">Questions fréquentes</div><h2>Formations : vos questions</h2></div><div class="faq">
 <details><summary>Les formations sont-elles adaptées aux débutants ?</summary><p>Oui. Un positionnement est réalisé en amont et le programme est adapté au niveau de chaque groupe, du grand débutant à l’utilisateur avancé.</p></details>
 <details><summary>Où se déroulent les formations ?</summary><p>Dans vos locaux, à distance en classe virtuelle ou en e-learning. Nous intervenons en France et en Algérie.</p></details>
 <details><summary>Peut-on construire une formation spécifique à notre entreprise ?</summary><p>Oui, c’est même notre approche privilégiée : le programme est construit à partir de vos outils et de vos situations de travail.</p></details>
 <details><summary>Les personnes en situation de handicap peuvent-elles suivre vos formations ?</summary><p>Oui. Contactez-nous en amont afin que nous étudiions ensemble les adaptations nécessaires.</p></details>
</div></div></section>
{cta("Vous souhaitez former vos équipes ?", "Recevez un programme adapté à vos objectifs et à votre budget.", "Formation")}'''
page("formations.html", "Formations IA, ChatGPT, bureautique, CRM & automatisation | ITS",
     "Formations professionnelles en IA générative, ChatGPT, Microsoft 365, CRM et automatisation no-code (n8n, Make). Présentiel, distanciel et e-learning.", formations)

# ---------- SOLUTIONS ----------
solutions = page_hero("Solutions", "Nos solutions", "Automatisation, IA et CRM sur mesure",
  "Des outils pensés pour votre activité : moins de tâches répétitives, des données centralisées et des processus qui tournent tout seuls.") + f'''
<section class="section" id="automatisation"><div class="container split">
 <div>
  <div class="eyebrow">Automatisation & IA</div>
  <h2 style="font-size:clamp(28px,3vw,38px)">Gagnez du temps avec des workflows intelligents</h2>
  <p class="lead">Nous connectons vos outils (emails, tableurs, CRM, sites web, API) et intégrons l’intelligence artificielle là où elle apporte un vrai gain.</p>
  {checks(["Workflows automatisés avec n8n, Make et API","Agents IA : tri des emails, réponses, extraction de documents","Chatbots pour votre site web et vos clients","Relances, notifications et rapports automatiques","Vous gardez toujours la validation finale"])}
  <div class="actions"><a class="btn btn-blue" href="contact.html?besoin=Automatisation%20%26%20IA">Automatiser un processus {ic("arrow")}</a></div>
 </div>
 <div class="grid2">
  <div class="card t-violet"><div class="badge">{ic("bot")}</div><h3>Agents IA</h3><p>Des assistants qui traitent emails, demandes et documents.</p></div>
  <div class="card t-violet"><div class="badge">{ic("zap")}</div><h3>Workflows</h3><p>Vos outils se parlent et les tâches s’enchaînent seules.</p></div>
  <div class="card t-violet"><div class="badge">{ic("mail")}</div><h3>Emails & relances</h3><p>Réponses préparées, relances et suivis automatiques.</p></div>
  <div class="card t-violet"><div class="badge">{ic("chart")}</div><h3>Rapports</h3><p>Tableaux de bord générés et envoyés automatiquement.</p></div>
 </div>
</div></section>
<section class="section alt" id="crm"><div class="container split rev">
 <div>
  <div class="eyebrow">Conception de CRM</div>
  <h2 style="font-size:clamp(28px,3vw,38px)">Un CRM qui colle à votre façon de travailler</h2>
  <p class="lead">Nous concevons des outils de gestion sur mesure : vos clients, vos devis, vos factures et votre activité réunis au même endroit, accessibles partout.</p>
  {checks(["Gestion des clients et des prospects","Devis, commandes et facturation","Suivi d’activité et tableaux de bord","Espace client et accès sécurisés","Formation de vos équipes à la prise en main"])}
  <div class="actions"><a class="btn btn-blue" href="contact.html?besoin=Conception%20de%20CRM">Concevoir mon CRM {ic("arrow")}</a></div>
 </div>
 <div class="panel"><h3>Comment nous travaillons</h3>
  <ol style="padding-left:20px;margin:14px 0 0;color:#e3edff;line-height:2">
   <li>Analyse de vos processus et de vos besoins</li><li>Maquette et validation avec vous</li><li>Développement et import de vos données</li><li>Formation des utilisateurs</li><li>Maintenance et évolutions</li></ol></div>
</div></section>
<section class="section" id="web"><div class="container">
 <div class="head"><div class="eyebrow">Sites web & outils</div><h2>Une présence en ligne qui génère des contacts</h2><p>Sites vitrines rapides, responsives et optimisés pour le référencement, connectés à vos outils.</p></div>
 <div class="grid3">
  <div class="card t-blue"><div class="badge">{ic("globe")}</div><h3>Sites vitrines</h3><p>Un site professionnel, rapide et lisible sur mobile, pensé pour la prise de contact.</p></div>
  <div class="card t-green"><div class="badge">{ic("target")}</div><h3>Référencement local</h3><p>Une structure et des contenus optimisés pour être trouvé par vos clients.</p></div>
  <div class="card t-violet"><div class="badge">{ic("lock")}</div><h3>Espaces clients</h3><p>Formulaires, prises de rendez-vous et accès sécurisés reliés à votre CRM.</p></div>
 </div>
</div></section>
{cta("Un processus à automatiser ou un outil à créer ?", "Décrivez-nous votre besoin : nous vous proposons une solution adaptée et chiffrée.", "Automatisation%20%26%20IA")}'''
page("solutions.html", "Automatisation & IA, conception de CRM et sites web | ITS",
     "Automatisation de processus avec n8n, Make et l’IA, agents IA, conception de CRM sur mesure (clients, devis, facturation) et sites web professionnels.", solutions)

# ---------- SERVICES ----------
services = page_hero("Services", "Assistance informatique", "Une informatique qui fonctionne, tout simplement",
  "Dépannage, installation, configuration, maintenance et accompagnement au quotidien, pour les entreprises comme pour les particuliers.") + f'''
<section class="section"><div class="container">
 <div class="head"><div class="eyebrow">Nos interventions</div><h2>Assistance informatique complète</h2><p>Sur site ou à distance, nous intervenons rapidement et vous expliquons simplement ce qui a été fait.</p></div>
 <div class="grid3">
  <div class="card t-orange"><div class="badge">{ic("wrench")}</div><h3>Dépannage</h3><p>Ordinateur lent, panne, virus, écran bleu : diagnostic et réparation.</p>{checks(["Diagnostic complet","Suppression de virus","Récupération de données"])}</div>
  <div class="card t-orange"><div class="badge">{ic("download")}</div><h3>Installation & configuration</h3><p>Postes, logiciels, imprimantes et messagerie prêts à l’emploi.</p>{checks(["Mise en service PC / Mac","Installation de logiciels","Messagerie et Microsoft 365"])}</div>
  <div class="card t-orange"><div class="badge">{ic("wifi")}</div><h3>Réseau & Internet</h3><p>Box, Wi-Fi, partage de fichiers et accès à distance fiables.</p>{checks(["Configuration Wi-Fi","Partage et NAS","Accès à distance sécurisé"])}</div>
  <div class="card t-orange"><div class="badge">{ic("shield")}</div><h3>Sécurité & sauvegarde</h3><p>Protégez vos données et vos postes contre les pertes et les attaques.</p>{checks(["Sauvegardes automatiques","Antivirus et mises à jour","Bonnes pratiques de sécurité"])}</div>
  <div class="card t-orange"><div class="badge">{ic("gear")}</div><h3>Maintenance</h3><p>Un suivi régulier pour éviter les pannes plutôt que les subir.</p>{checks(["Mises à jour planifiées","Contrôle de l’état des postes","Conseils d’équipement"])}</div>
  <div class="card t-orange"><div class="badge">{ic("headset")}</div><h3>Assistance à distance</h3><p>Une intervention rapide sur votre poste, sans déplacement.</p>{checks(["Connexion sécurisée","Intervention rapide","Explications pas à pas"])}</div>
 </div>
</div></section>
<section class="section alt"><div class="container">
 <div class="head center"><div class="eyebrow">Comment ça se passe</div><h2>Une intervention en 4 étapes</h2></div>
 <div class="steps">
  <div class="step"><h3>Vous nous contactez</h3><p>Par téléphone ou via le formulaire, en décrivant le problème.</p></div>
  <div class="step"><h3>Diagnostic</h3><p>Nous identifions la cause et vous proposons une solution chiffrée.</p></div>
  <div class="step"><h3>Intervention</h3><p>À distance ou sur site, selon la situation.</p></div>
  <div class="step"><h3>Conseils</h3><p>Nous vous expliquons comment éviter que le problème ne se reproduise.</p></div>
 </div>
</div></section>
{cta("Un problème informatique ?", "Appelez-nous ou décrivez votre problème : nous revenons vers vous rapidement.", "Assistance%20informatique")}'''
page("services.html", "Assistance informatique : dépannage, installation, maintenance | ITS",
     "Dépannage informatique, installation, configuration, réseau, sécurité, sauvegarde, maintenance et assistance à distance pour entreprises et particuliers.", services)

# ---------- À PROPOS ----------
apropos = page_hero("À propos", "Qui sommes-nous", "Le numérique au service de votre activité",
  "Informatique Team Services (ITS) accompagne entreprises, indépendants et organismes de formation dans la montée en compétences et la transformation digitale.") + f'''
<section class="section"><div class="container split">
 <div>
  <div class="eyebrow">Notre mission</div>
  <h2 style="font-size:clamp(28px,3vw,38px)">Rendre l’informatique et l’IA utiles, simples et accessibles</h2>
  <p class="lead">ITS a été fondée par un consultant-formateur fort de plus de 20 ans d’expérience dans le conseil informatique et la formation professionnelle. Notre conviction : un outil n’apporte de valeur que si les personnes qui l’utilisent le maîtrisent.</p>
  <p>C’est pourquoi nous réunissons formation, conception de solutions et assistance au sein d’une même équipe. Organisme de formation déclaré, nous intervenons en France et en Algérie, en présentiel comme à distance.</p>
 </div>
 <div><img class="feature-img" src="hero-its.jpg" alt="Plateforme ITS" width="882" height="490" loading="lazy"></div>
</div></section>
<section class="section alt"><div class="container">
 <div class="head center"><div class="eyebrow">Nos valeurs</div><h2>Ce qui guide notre travail</h2></div>
 <div class="grid4">
  <div class="card t-blue"><div class="badge">{ic("target")}</div><h3>Pragmatisme</h3><p>Des solutions utiles, adaptées à votre réalité et à votre budget.</p></div>
  <div class="card t-violet"><div class="badge">{ic("handshake")}</div><h3>Proximité</h3><p>Un interlocuteur disponible, qui explique sans jargon.</p></div>
  <div class="card t-green"><div class="badge">{ic("cap")}</div><h3>Transmission</h3><p>Nous rendons vos équipes autonomes sur leurs outils.</p></div>
  <div class="card t-orange"><div class="badge">{ic("lock")}</div><h3>Confiance</h3><p>Confidentialité de vos données et respect du RGPD.</p></div>
 </div>
</div></section>
<section aria-label="Nos atouts" style="padding-top:60px"><div class="container perks">{perks_html}</div></section>
{cta()}'''
page("a-propos.html", "À propos d’Informatique Team Services (ITS)",
     "ITS accompagne entreprises, indépendants et organismes de formation : formation, automatisation & IA, CRM et assistance informatique, en France et en Algérie.", apropos)

# ---------- CONTACT ----------
contact = page_hero("Contact", "Contact & devis", "Parlons de votre projet",
  "Formation, automatisation, CRM ou assistance : décrivez votre besoin, nous vous répondons sous 24 h ouvrées avec une proposition sans engagement.") + f'''
<section class="section"><div class="container contact-grid">
 <div class="info">
  <h2>Nos coordonnées</h2><p>Un échange rapide suffit souvent pour cerner votre besoin.</p>
  <div class="ci"><span class="b">{ic("phone")}</span><span><small>Téléphone</small><a href="tel:{TEL}">{TEL_H}</a></span></div>
  <div class="ci"><span class="b">{ic("mail")}</span><span><small>Email</small><a href="mailto:{MAIL}">{MAIL}</a></span></div>
  <div class="ci"><span class="b">{ic("pin")}</span><span><small>Zone d’intervention</small>France & Algérie · présentiel et à distance</span></div>
  <div class="ci"><span class="b">{ic("clock")}</span><span><small>Délai de réponse</small>Sous 24 h ouvrées</span></div>
 </div>
 <form class="devis" id="form-devis" method="POST" action="https://formsubmit.co/{MAIL}">
  <input type="hidden" name="_subject" value="Nouvelle demande — site ITS">
  <input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false">
  <input type="hidden" name="_next" value="__SITE_URL__/merci.html">
  <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
  <div class="fgrid">
   <div class="field full"><label>Vous êtes <span class="req">*</span></label><div class="seg">
    <label><input type="radio" name="profil" value="Entreprise / indépendant" checked> Entreprise / indépendant</label>
    <label><input type="radio" name="profil" value="Organisme de formation"> Organisme de formation</label>
    <label><input type="radio" name="profil" value="Particulier"> Particulier</label></div></div>
   <div class="field"><label for="nom">Nom et prénom <span class="req">*</span></label><input id="nom" name="nom" required autocomplete="name"></div>
   <div class="field"><label for="societe">Structure</label><input id="societe" name="structure" autocomplete="organization"></div>
   <div class="field"><label for="email">Email <span class="req">*</span></label><input id="email" name="email" type="email" required autocomplete="email"></div>
   <div class="field"><label for="tel">Téléphone</label><input id="tel" name="telephone" type="tel" autocomplete="tel"></div>
   <div class="field full"><label for="besoin">Votre besoin <span class="req">*</span></label><select id="besoin" name="besoin" required>
    <option value="">Choisissez…</option><option>Formation</option><option>Automatisation &amp; IA</option><option>Conception de CRM</option><option>Site web</option><option>Assistance informatique</option><option>Autre</option></select></div>
   <div class="field full"><label for="message">Votre message <span class="req">*</span></label><textarea id="message" name="message" required placeholder="Contexte, objectifs, nombre de personnes, délais…"></textarea></div>
   <div class="field full"><label class="consent"><input type="checkbox" name="consentement" value="oui" required> <span>J’accepte que mes données soient utilisées pour traiter ma demande, conformément à la <a href="mentions-legales.html#donnees">politique de confidentialité</a>.</span></label></div>
  </div>
  <div class="form-foot"><small id="form-status" role="status">Réponse sous 24 h · Sans engagement</small><button class="btn btn-blue" type="submit">Envoyer ma demande {ic("send")}</button></div>
 </form>
</div></section>'''
page("contact.html", "Contact & demande de devis | Informatique Team Services",
     "Contactez ITS pour une formation, une automatisation, un CRM sur mesure ou une assistance informatique. Réponse sous 24 h.", contact)

# ---------- MENTIONS LÉGALES ----------
todo = '<span style="background:#fff4d6;padding:1px 6px;border-radius:4px;color:#8a5a00;font-weight:700">[À COMPLÉTER]</span>'
mentions = page_hero("Mentions légales", "Informations légales", "Mentions légales & confidentialité", "Informations sur l’éditeur du site, l’hébergement et le traitement de vos données.") + f'''
<section class="section"><div class="container" style="max-width:860px">
<h2>Éditeur du site</h2><p>Informatique Team Services (ITS)<br>Forme juridique : {todo}<br>Siège social : {todo}<br>SIRET : {todo}<br>
Numéro de déclaration d’activité (organisme de formation) : {todo} — cet enregistrement ne vaut pas agrément de l’État.<br>
Téléphone : <a href="tel:{TEL}">{TEL_H}</a> — Email : <a href="mailto:{MAIL}">{MAIL}</a><br>Directeur de la publication : {todo}</p>
<h2>Hébergement</h2><p>Site auto-hébergé par Informatique Team Services sur son propre serveur. Diffusion et sécurisation du trafic assurées par Cloudflare, Inc. — 101 Townsend St, San Francisco, CA 94107, États-Unis.</p>
<h2>Propriété intellectuelle</h2><p>L’ensemble des contenus de ce site (textes, logo, visuels) est la propriété d’Informatique Team Services, sauf mention contraire. Toute reproduction sans autorisation est interdite.</p>
<h2 id="donnees">Données personnelles</h2><p>Les informations transmises via le formulaire de contact (nom, structure, email, téléphone, besoin, message) sont utilisées uniquement pour répondre à votre demande et, le cas échéant, établir un devis. Elles sont acheminées par email via le service FormSubmit et conservées 3 ans à compter du dernier contact. Aucune donnée n’est vendue ni cédée à des tiers.</p>
<p>Conformément au RGPD, vous disposez d’un droit d’accès, de rectification, d’effacement, d’opposition et de portabilité. Pour l’exercer : <a href="mailto:{MAIL}">{MAIL}</a>. Vous pouvez également saisir la CNIL (cnil.fr).</p>
<h2>Cookies</h2><p>Ce site n’utilise pas de cookies publicitaires ni de suivi. Les polices de caractères sont chargées depuis Google Fonts ; Cloudflare peut déposer des cookies strictement techniques liés à la sécurité.</p>
</div></section>'''
page("mentions-legales.html", "Mentions légales & confidentialité | ITS", "Mentions légales et politique de confidentialité d’Informatique Team Services.", mentions, active="-")

merci = f'''<section class="section"><div class="container" style="max-width:640px;text-align:center">
 <div style="width:72px;height:72px;border-radius:50%;background:#e9f8ef;color:#169b4b;display:grid;place-items:center;margin:0 auto 20px;font-size:36px;font-weight:800">✓</div>
 <h1 style="font-size:34px">Merci, votre demande est bien envoyée</h1>
 <p class="lead" style="margin:0 auto 26px">Nous revenons vers vous sous 24 h ouvrées. Pour une urgence, appelez-nous au <a class="blue" href="tel:{TEL}">{TEL_H}</a>.</p>
 <a class="btn btn-blue" href="index.html">Retour à l’accueil {ic("arrow")}</a>
</div></section>'''
page("merci.html", "Demande envoyée | ITS", "Votre demande a bien été envoyée.", merci, active="-")

nf = f'''<section class="section"><div class="container" style="max-width:640px;text-align:center">
 <div style="font-family:Montserrat,sans-serif;font-size:90px;font-weight:800;color:var(--blue);line-height:1">404</div>
 <h1 style="font-size:30px">Cette page n’existe pas</h1><p class="lead" style="margin:0 auto 26px">Elle a peut-être été déplacée. Revenez à l’accueil ou contactez-nous.</p>
 <a class="btn btn-blue" href="/index.html">Retour à l’accueil {ic("arrow")}</a>
</div></section>'''
page("404.html", "Page introuvable | ITS", "Page introuvable.", nf, active="-")

# robots & sitemap
pages = ["", "formations.html", "solutions.html", "services.html", "a-propos.html", "contact.html", "mentions-legales.html"]
(SITE / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
  + "".join(f" <url><loc>__SITE_URL__/{p}</loc></url>\n" for p in pages) + "</urlset>\n", encoding="utf-8")
print("Pages générées :", ", ".join(p or "index.html" for p in pages), "+ merci.html, 404.html")
