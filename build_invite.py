import base64, os

# Read deity image as base64
img_path = os.path.join(os.path.dirname(__file__), 'deity.png')
with open(img_path, 'rb') as f:
    deity_b64 = 'data:image/png;base64,' + base64.b64encode(f.read()).decode()

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Harish Kalyan & Narmada — Wedding Invitation</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Cinzel:wght@400;600&family=Raleway:wght@200;300;400&display=swap" rel="stylesheet">
<style>
:root{{
  --sky:#080f2e; --sky2:#0c1a52; --sky3:#152070;
  --gold:#d4a843; --goldl:#f0d080; --goldd:#a07828;
  --paper1:#e8c870; --paper2:#c8a040; --paper3:#a07828;
  --paper4:#785018; --cream:#f5e8c0; --white:#fff;
}}
*,*::before,*::after{{margin:0;padding:0;box-sizing:border-box;}}
html{{scroll-behavior:smooth;}}
body{{background:var(--sky);color:var(--cream);font-family:'Raleway',sans-serif;overflow-x:hidden;}}

/* LOADER */
#loader{{position:fixed;inset:0;background:var(--sky);z-index:9999;display:flex;flex-direction:column;align-items:center;justify-content:center;transition:opacity 1s ease;}}
#loader.hide{{opacity:0;pointer-events:none;}}
.ld-mono{{font-family:'Cormorant Garamond',serif;font-size:clamp(28px,6vw,56px);color:var(--goldl);letter-spacing:.08em;animation:pulse 2s ease-in-out infinite;text-shadow:0 0 40px rgba(212,168,67,.5);}}
.ld-line{{width:80px;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent);margin:18px 0;animation:expand 2s ease-in-out infinite;}}
.ld-sub{{font-family:'Cinzel',serif;font-size:10px;letter-spacing:5px;color:var(--gold);opacity:.6;text-transform:uppercase;}}
@keyframes pulse{{0%,100%{{opacity:.5;transform:scale(.96)}}50%{{opacity:1;transform:scale(1)}}}}
@keyframes expand{{0%,100%{{width:40px;opacity:.3}}50%{{width:120px;opacity:1}}}}

/* MUSIC BTN */
#musicBtn{{position:fixed;top:18px;right:18px;z-index:1000;width:42px;height:42px;border-radius:50%;background:rgba(8,15,46,.8);border:1px solid var(--gold);color:var(--gold);cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:18px;backdrop-filter:blur(8px);transition:all .3s;}}
#musicBtn:hover{{box-shadow:0 0 20px rgba(212,168,67,.5);transform:scale(1.1);}}

/* ─── DIORAMA ─── */
#diorama{{position:relative;height:350vh;}}
.sticky{{position:sticky;top:0;height:100vh;overflow:hidden;}}
.dl{{position:absolute;inset:0;width:100%;height:100%;will-change:transform;}}

/* Sky */
#l-sky{{z-index:1;background:radial-gradient(ellipse at 50% 35%,#1a3080 0%,#0c1a52 38%,#050a1e 100%);transform:scale(1.12);transition:transform 4s cubic-bezier(.2,.8,.2,1);}}
#l-sky.loaded{{transform:scale(1);}}

/* Names overlay (behind flap) */
#l-names{{z-index:3;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;padding-top:clamp(28px,6vh,72px);pointer-events:none;opacity:0;transition:opacity .8s ease;}}
.n-sub{{font-family:'Cinzel',serif;font-size:clamp(9px,1.3vw,12px);letter-spacing:5px;color:var(--gold);text-transform:uppercase;opacity:.8;margin-bottom:14px;}}
.n-main{{font-family:'Cormorant Garamond',serif;font-size:clamp(38px,9vw,100px);font-weight:300;color:var(--white);line-height:1.0;text-align:center;text-shadow:0 2px 40px rgba(212,168,67,.35),0 0 80px rgba(8,15,46,.9);}}
.n-main em{{color:var(--goldl);font-style:italic;}}
.n-date{{font-family:'Cinzel',serif;font-size:clamp(9px,1.3vw,12px);letter-spacing:5px;color:var(--gold);text-transform:uppercase;margin-top:18px;opacity:.7;}}
@keyframes fadeUp{{from{{opacity:0;transform:translateY(18px)}}to{{opacity:1;transform:translateY(0)}}}}

/* Arch / architecture layer */
#l-arch{{z-index:4;pointer-events:none;}}
/* Balloon */
#l-balloon{{z-index:5;pointer-events:none;}}
.balloon-float{{position:absolute;left:clamp(16px,7%,90px);bottom:28%;animation:bob 5s ease-in-out infinite;}}
@keyframes bob{{0%,100%{{transform:translateY(0) rotate(-3deg)}}50%{{transform:translateY(-20px) rotate(3deg)}}}}

/* Front wave layer */
#l-front{{z-index:6;pointer-events:none;}}

/* TOP FLAP */
#l-flap{{z-index:10;display:flex;flex-direction:column;align-items:center;background:linear-gradient(180deg,#080f2e 0%,#0e1f60 60%,transparent 100%);pointer-events:none;}}
.flap-top{{padding-top:clamp(28px,5.5vh,65px);text-align:center;}}
.flap-top h1{{font-family:'Cormorant Garamond',serif;font-size:clamp(36px,9vw,100px);font-weight:300;color:var(--white);line-height:1.0;text-shadow:0 0 60px rgba(212,168,67,.3);animation:fadeUp 1.4s ease forwards .5s;opacity:0;}}
.flap-top h1 em{{color:var(--goldl);font-style:italic;}}
.flap-top p{{font-family:'Cinzel',serif;font-size:clamp(9px,1.3vw,12px);letter-spacing:5px;color:var(--gold);text-transform:uppercase;margin-top:14px;animation:fadeUp 1.2s ease forwards 1.2s;opacity:0;}}
.flap-edge{{position:absolute;bottom:-2px;left:0;right:0;line-height:0;}}
.flap-edge svg{{width:100%;display:block;}}
.scroll-hint{{position:absolute;bottom:44px;left:50%;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center;gap:8px;animation:fadeUp 1s ease forwards 3s;opacity:0;pointer-events:none;}}
.scroll-hint span{{font-family:'Cinzel',serif;font-size:9px;letter-spacing:4px;color:var(--gold);opacity:.6;text-transform:uppercase;}}
.s-mouse{{width:20px;height:32px;border:1.5px solid rgba(212,168,67,.4);border-radius:10px;position:relative;overflow:hidden;}}
.s-mouse::after{{content:'';position:absolute;top:5px;left:50%;transform:translateX(-50%);width:3px;height:5px;background:var(--gold);border-radius:2px;animation:dot 1.8s ease-in-out infinite;}}
@keyframes dot{{0%{{opacity:1;top:5px}}100%{{opacity:0;top:20px}}}}

/* ─── BELOW SECTIONS ─── */
#below{{background:linear-gradient(180deg,#04071a 0%,#060c22 100%);position:relative;z-index:20;}}
section{{padding:clamp(70px,11vw,130px) 24px;text-align:center;position:relative;}}
.sec-label{{font-family:'Cinzel',serif;font-size:10px;letter-spacing:6px;color:var(--gold);text-transform:uppercase;margin-bottom:14px;}}
.sec-title{{font-family:'Cormorant Garamond',serif;font-size:clamp(32px,7.5vw,72px);font-weight:300;color:var(--white);line-height:1.1;}}
.sec-title em{{color:var(--goldl);font-style:italic;}}
.ornament{{display:flex;align-items:center;justify-content:center;gap:14px;margin:26px auto;}}
.ol{{flex:1;max-width:100px;height:1px;background:linear-gradient(90deg,transparent,var(--gold));}}
.ol.r{{background:linear-gradient(90deg,var(--gold),transparent);}}
.od{{width:7px;height:7px;background:var(--gold);transform:rotate(45deg);}}

.info-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:16px;max-width:860px;margin:52px auto 0;}}
.info-card{{background:rgba(255,255,255,.03);border:1px solid rgba(212,168,67,.18);padding:30px 22px;opacity:0;transform:translateY(28px);transition:opacity .7s ease,transform .7s ease;}}
.info-card.visible{{opacity:1;transform:translateY(0);}}
.info-card:hover{{background:rgba(212,168,67,.06);border-color:rgba(212,168,67,.4);transform:translateY(-4px);}}
.iicon{{font-size:26px;margin-bottom:12px;}}
.ilabel{{font-family:'Cinzel',serif;font-size:9px;letter-spacing:4px;color:var(--gold);text-transform:uppercase;margin-bottom:10px;opacity:.8;}}
.ivalue{{font-family:'Cormorant Garamond',serif;font-size:clamp(17px,3vw,23px);font-weight:400;color:var(--white);line-height:1.3;}}
.isub{{font-size:12px;color:rgba(245,241,232,.4);margin-top:5px;}}

/* Countdown */
#countdown{{background:rgba(0,0,0,.2);overflow:hidden;}}
#countdown::before{{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at center,rgba(212,168,67,.05) 0%,transparent 65%);}}
.cd-grid{{display:flex;justify-content:center;gap:clamp(12px,4vw,42px);margin-top:52px;flex-wrap:wrap;}}
.cd-item{{text-align:center;min-width:76px;}}
.cd-num{{font-family:'Cormorant Garamond',serif;font-size:clamp(46px,10vw,84px);font-weight:300;color:var(--white);line-height:1;position:relative;display:inline-block;}}
.cd-num::after{{content:'';position:absolute;bottom:-6px;left:10%;right:10%;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent);}}
.cd-label{{font-family:'Cinzel',serif;font-size:9px;letter-spacing:4px;color:var(--gold);text-transform:uppercase;margin-top:16px;opacity:.7;}}
.cd-sep{{font-family:'Cormorant Garamond',serif;font-size:clamp(34px,7vw,62px);color:var(--gold);opacity:.25;align-self:flex-start;margin-top:8px;}}

/* Timeline */
.tl-wrap{{max-width:570px;margin:52px auto 0;position:relative;}}
.tl-wrap::before{{content:'';position:absolute;left:50%;transform:translateX(-50%);top:0;bottom:0;width:1px;background:linear-gradient(180deg,transparent,var(--gold) 10%,var(--gold) 90%,transparent);opacity:.22;}}
.tl-item{{display:flex;align-items:center;gap:20px;margin-bottom:42px;opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s ease;}}
.tl-item.visible{{opacity:1;transform:translateY(0);}}
.tl-item:nth-child(odd){{flex-direction:row-reverse;}}
.tl-content{{flex:1;text-align:right;padding:20px;background:rgba(255,255,255,.03);border:1px solid rgba(212,168,67,.12);transition:all .4s;}}
.tl-item:nth-child(even) .tl-content{{text-align:left;}}
.tl-content:hover{{background:rgba(212,168,67,.05);border-color:rgba(212,168,67,.28);}}
.tl-dot{{width:13px;height:13px;flex-shrink:0;background:var(--gold);border-radius:50%;box-shadow:0 0 18px rgba(212,168,67,.6);z-index:2;}}
.tl-event{{font-family:'Cinzel',serif;font-size:9px;letter-spacing:3px;color:var(--gold);text-transform:uppercase;margin-bottom:7px;}}
.tl-title{{font-family:'Cormorant Garamond',serif;font-size:clamp(17px,3.6vw,23px);color:var(--white);font-weight:400;}}
.tl-date{{font-size:11px;color:rgba(245,241,232,.4);margin-top:5px;}}
.tl-icon{{font-size:24px;margin-bottom:7px;}}

/* RSVP */
#rsvp{{background:rgba(0,0,0,.15);}}
.rsvp-wrap{{max-width:510px;margin:0 auto;}}
.rsvp-quote{{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:clamp(15px,3vw,23px);color:rgba(245,241,232,.6);line-height:1.7;margin:34px 0 44px;}}
.rsvp-btn{{display:inline-block;padding:15px 50px;border:1px solid var(--gold);color:var(--gold);font-family:'Cinzel',serif;font-size:10px;letter-spacing:5px;text-transform:uppercase;text-decoration:none;position:relative;overflow:hidden;cursor:pointer;background:transparent;transition:color .4s;}}
.rsvp-btn::before{{content:'';position:absolute;inset:0;background:var(--gold);transform:scaleX(0);transform-origin:left;transition:transform .4s;z-index:-1;}}
.rsvp-btn:hover{{color:#040810;}}
.rsvp-btn:hover::before{{transform:scaleX(1);}}
.rsvp-form{{margin-top:34px;display:none;}}
.rsvp-form.show{{display:block;animation:fadeUp .6s ease forwards;}}
.rsvp-input{{width:100%;background:rgba(255,255,255,.04);border:1px solid rgba(212,168,67,.2);padding:12px 17px;color:var(--cream);font-family:'Raleway',sans-serif;font-size:14px;margin-bottom:10px;outline:none;transition:border-color .3s;}}
.rsvp-input:focus{{border-color:var(--gold);}}
.rsvp-input::placeholder{{color:rgba(245,241,232,.25);}}
.rsvp-submit{{width:100%;padding:14px;background:var(--gold);color:#040810;border:none;font-family:'Cinzel',serif;font-size:10px;letter-spacing:4px;text-transform:uppercase;cursor:pointer;transition:all .3s;}}
.rsvp-submit:hover{{background:var(--goldl);}}
.rsvp-success{{display:none;}}
.rsvp-success.show{{display:block;font-family:'Cormorant Garamond',serif;font-size:21px;font-style:italic;color:var(--gold);margin-top:26px;animation:fadeUp .6s ease forwards;}}

footer{{background:#02040e;padding:52px 24px 32px;text-align:center;border-top:1px solid rgba(212,168,67,.1);}}
.fn{{font-family:'Cormorant Garamond',serif;font-size:clamp(28px,6vw,50px);font-weight:300;color:var(--white);}}
.fn em{{color:var(--goldl);font-style:italic;}}
.fs{{font-family:'Cinzel',serif;font-size:9px;letter-spacing:5px;color:var(--gold);opacity:.4;text-transform:uppercase;margin-top:16px;}}

.fade-in{{opacity:0;transform:translateY(30px);transition:opacity .8s ease,transform .8s ease;}}
.fade-in.visible{{opacity:1;transform:translateY(0);}}

#details::before{{content:'';position:absolute;top:0;left:50%;transform:translateX(-50%);width:1px;height:70px;background:linear-gradient(180deg,transparent,var(--gold));}}

@media(max-width:600px){{
  .cd-sep{{display:none;}}
  .tl-wrap::before{{left:20px;}}
  .tl-item,.tl-item:nth-child(odd){{flex-direction:column;align-items:flex-start;padding-left:44px;}}
  .tl-dot{{position:absolute;left:13px;}}
  .tl-item{{position:relative;}}
  .tl-content,.tl-item:nth-child(even) .tl-content{{text-align:left;}}
  .info-grid{{grid-template-columns:1fr 1fr;}}
}}
</style>
</head>
<body>

<div id="loader">
  <div class="ld-mono">H &amp; N</div>
  <div class="ld-line"></div>
  <div class="ld-sub">Loading your invitation</div>
</div>

<button id="musicBtn" title="Toggle Music">♪</button>
<audio id="bgMusic" loop><source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg"></audio>

<div id="diorama">
  <div class="sticky">

    <!-- L1: Sky -->
    <div class="dl" id="l-sky"></div>

    <!-- Stars canvas -->
    <canvas class="dl" id="l-stars" style="z-index:2;pointer-events:none;"></canvas>

    <!-- Clouds (behind arch) -->
    <div class="dl" id="l-clouds" style="z-index:3;pointer-events:none;top:5%;">
      <svg viewBox="0 0 1440 200" width="100%" preserveAspectRatio="none" style="opacity:.1;position:absolute;top:0;left:0;">
        <ellipse cx="160" cy="70" rx="130" ry="42" fill="white"/>
        <ellipse cx="270" cy="54" rx="95" ry="30" fill="white"/>
        <ellipse cx="820" cy="88" rx="170" ry="50" fill="white"/>
        <ellipse cx="980" cy="65" rx="125" ry="38" fill="white"/>
        <ellipse cx="1260" cy="52" rx="108" ry="34" fill="white"/>
      </svg>
    </div>

    <!-- L4: Names (revealed after flap slides) -->
    <div class="dl" id="l-names">
      <p class="n-sub">With the Blessings of the Almighty</p>
      <h1 class="n-main">Harish Kalyan<br><em>weds</em><br>Narmada</h1>
      <p class="n-date">April 28, 2026 &nbsp;·&nbsp; Chennai, Tamil Nadu</p>
    </div>

    <!-- L5: Arch / Architecture -->
    <div class="dl" id="l-arch">
      <svg viewBox="0 0 1440 780" preserveAspectRatio="xMidYMax meet"
           style="position:absolute;bottom:0;left:0;width:100%;height:auto;" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="ag1" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#f0d080"/><stop offset="100%" stop-color="#7a5018"/>
          </linearGradient>
          <linearGradient id="ag2" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#d4a843"/><stop offset="100%" stop-color="#604010"/>
          </linearGradient>
          <linearGradient id="ag3" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#b88c30"/><stop offset="100%" stop-color="#4a3010"/>
          </linearGradient>
          <radialGradient id="archGlow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#f0d080" stop-opacity="0.3"/>
            <stop offset="100%" stop-color="#d4a843" stop-opacity="0"/>
          </radialGradient>
          <filter id="shadow1"><feDropShadow dx="0" dy="-6" stdDeviation="12" flood-color="#000" flood-opacity="0.55"/></filter>
          <filter id="shadow2"><feDropShadow dx="0" dy="-10" stdDeviation="20" flood-color="#000" flood-opacity="0.65"/></filter>
          <filter id="glow1"><feGaussianBlur stdDeviation="6" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
          <clipPath id="archClip">
            <path d="M460,780 L460,460 Q460,250 700,210 Q940,250 940,460 L940,780 Z"/>
          </clipPath>
        </defs>

        <!-- Deepest back wave -->
        <path d="M0,780 L0,540 Q180,380 360,430 Q540,480 720,400 Q900,320 1080,400 Q1260,480 1440,430 L1440,780 Z" fill="url(#ag3)" filter="url(#shadow1)" opacity="0.8"/>

        <!-- Mid wave -->
        <path d="M0,780 L0,600 Q200,460 400,510 Q600,560 720,490 Q840,420 1040,490 Q1240,560 1440,510 L1440,780 Z" fill="url(#ag2)" filter="url(#shadow1)"/>

        <!-- Main platform -->
        <path d="M0,780 L0,660 Q240,560 480,610 Q620,640 720,600 Q820,560 960,610 Q1200,660 1440,600 L1440,780 Z" fill="url(#ag1)" filter="url(#shadow2)"/>

        <!-- Platform gold trim -->
        <path d="M0,658 Q240,558 480,608 Q620,638 720,598 Q820,558 960,608 Q1200,658 1440,598" fill="none" stroke="#f0d080" stroke-width="2.5" opacity="0.95"/>
        <path d="M0,666 Q240,566 480,616 Q620,646 720,606 Q820,566 960,616 Q1200,666 1440,606" fill="none" stroke="#d4a843" stroke-width="1.3" opacity="0.6"/>

        <!-- Arch opening (sky showing through) -->
        <path d="M460,780 L460,460 Q460,250 700,210 Q940,250 940,460 L940,780 Z" fill="var(--sky2)" opacity="0.95"/>

        <!-- Glow inside arch -->
        <ellipse cx="700" cy="480" rx="200" ry="240" fill="url(#archGlow)"/>

        <!-- Deity image clipped inside arch -->
        <image href="{deity_b64}" x="510" y="220" width="380" height="380" clip-path="url(#archClip)" preserveAspectRatio="xMidYMid meet" opacity="0.92"/>

        <!-- Arch outer frame -->
        <path d="M460,780 L460,460 Q460,250 700,210 Q940,250 940,460 L940,780" fill="none" stroke="url(#ag1)" stroke-width="8" filter="url(#shadow1)"/>
        <!-- Arch inner frame -->
        <path d="M480,780 L480,465 Q480,268 700,230 Q920,268 920,465 L920,780" fill="none" stroke="#f0d080" stroke-width="3" opacity="0.7"/>
        <!-- Arch innermost -->
        <path d="M500,780 L500,470 Q500,285 700,250 Q900,285 900,470 L900,780" fill="none" stroke="#d4a843" stroke-width="1.5" opacity="0.45"/>

        <!-- Keystone at arch top -->
        <ellipse cx="700" cy="208" rx="46" ry="46" fill="url(#ag1)" filter="url(#shadow2)"/>
        <ellipse cx="700" cy="208" rx="38" ry="38" fill="none" stroke="#f0d080" stroke-width="2.5"/>
        <ellipse cx="700" cy="208" rx="29" ry="29" fill="url(#ag2)"/>
        <!-- Lotus pattern in keystone -->
        <g fill="#f0d080" opacity="0.9">
          <path d="M700,195 Q704,202 700,208 Q696,202 700,195Z"/>
          <path d="M700,195 Q707,199 707,208 Q701,204 700,195Z"/>
          <path d="M700,195 Q693,199 693,208 Q699,204 700,195Z"/>
          <circle cx="700" cy="210" r="4"/>
        </g>

        <!-- Left column -->
        <rect x="430" y="420" width="36" height="360" rx="5" fill="url(#ag2)" filter="url(#shadow1)"/>
        <rect x="434" y="420" width="28" height="360" fill="none" stroke="#f0d080" stroke-width="1.2" opacity="0.35"/>
        <!-- Col ornament left top -->
        <ellipse cx="448" cy="418" rx="22" ry="12" fill="url(#ag1)" filter="url(#glow1)"/>
        <!-- Right column -->
        <rect x="974" y="420" width="36" height="360" rx="5" fill="url(#ag2)" filter="url(#shadow1)"/>
        <rect x="978" y="420" width="28" height="360" fill="none" stroke="#f0d080" stroke-width="1.2" opacity="0.35"/>
        <!-- Col ornament right top -->
        <ellipse cx="992" cy="418" rx="22" ry="12" fill="url(#ag1)" filter="url(#glow1)"/>

        <!-- Hanging pendants LEFT of arch -->
        <g filter="url(#glow1)">
          <line x1="540" y1="270" x2="540" y2="330" stroke="#d4a843" stroke-width="1.5"/>
          <circle cx="540" cy="334" r="7" fill="#f0d080"/>
          <line x1="570" y1="255" x2="570" y2="306" stroke="#d4a843" stroke-width="1.5"/>
          <circle cx="570" cy="310" r="6" fill="#d4a843"/>
          <line x1="555" y1="260" x2="555" y2="315" stroke="#d4a843" stroke-width="1"/>
          <circle cx="555" cy="319" r="5" fill="#f0d080" opacity="0.8"/>
        </g>
        <!-- Hanging pendants RIGHT of arch -->
        <g filter="url(#glow1)">
          <line x1="860" y1="270" x2="860" y2="330" stroke="#d4a843" stroke-width="1.5"/>
          <circle cx="860" cy="334" r="7" fill="#f0d080"/>
          <line x1="830" y1="255" x2="830" y2="306" stroke="#d4a843" stroke-width="1.5"/>
          <circle cx="830" cy="310" r="6" fill="#d4a843"/>
          <line x1="845" y1="260" x2="845" y2="315" stroke="#d4a843" stroke-width="1"/>
          <circle cx="845" cy="319" r="5" fill="#f0d080" opacity="0.8"/>
        </g>

        <!-- Decorative floral spread LEFT -->
        <g fill="#d4a843" opacity="0.6">
          <circle cx="280" cy="500" r="6"/><circle cx="300" cy="478" r="4.5"/>
          <circle cx="250" cy="520" r="5"/><circle cx="310" cy="510" r="3.5"/>
          <circle cx="230" cy="490" r="4"/><circle cx="260" cy="460" r="3"/>
          <path d="M260,480 Q272,468 284,476 Q272,488 260,480Z" fill="#f0d080"/>
          <path d="M290,505 Q302,493 314,501 Q302,513 290,505Z" fill="#f0d080"/>
        </g>
        <!-- Decorative floral spread RIGHT -->
        <g fill="#d4a843" opacity="0.6">
          <circle cx="1160" cy="500" r="6"/><circle cx="1140" cy="478" r="4.5"/>
          <circle cx="1190" cy="520" r="5"/><circle cx="1130" cy="510" r="3.5"/>
          <circle cx="1210" cy="490" r="4"/><circle cx="1180" cy="460" r="3"/>
          <path d="M1180,480 Q1168,468 1156,476 Q1168,488 1180,480Z" fill="#f0d080"/>
          <path d="M1150,505 Q1138,493 1126,501 Q1138,513 1150,505Z" fill="#f0d080"/>
        </g>

        <!-- Dot ornaments on mid-wave trim -->
        <g fill="#f0d080" opacity="0.85">
          <circle cx="240" cy="601" r="5.5"/><circle cx="480" cy="609" r="5.5"/>
          <circle cx="720" cy="598" r="5.5"/><circle cx="960" cy="609" r="5.5"/>
          <circle cx="1200" cy="601" r="5.5"/>
        </g>

        <!-- Stars scattered left and right of arch -->
        <g fill="#f0d080">
          <polygon points="180,440 183,452 195,452 185,460 189,472 180,464 171,472 175,460 165,452 177,452" opacity="0.7"/>
          <polygon points="340,380 342,389 351,389 344,394 347,403 340,398 333,403 336,394 329,389 338,389" opacity="0.55" transform="scale(0.8) translate(90,90)"/>
          <polygon points="1100,440 1103,452 1115,452 1105,460 1109,472 1100,464 1091,472 1095,460 1085,452 1097,452" opacity="0.7"/>
          <polygon points="1260,380 1262,389 1271,389 1264,394 1267,403 1260,398 1253,403 1256,394 1249,389 1258,389" opacity="0.55" transform="scale(0.8) translate(-200,90)"/>
        </g>

        <!-- Small constellation lines -->
        <g stroke="#d4a843" stroke-width="0.7" opacity="0.35">
          <line x1="120" y1="380" x2="160" y2="420"/>
          <line x1="160" y1="420" x2="210" y2="400"/>
          <line x1="1280" y1="380" x2="1240" y2="420"/>
          <line x1="1240" y1="420" x2="1190" y2="400"/>
        </g>
      </svg>
    </div>

    <!-- L6: Balloon -->
    <div class="dl" id="l-balloon">
      <div class="balloon-float">
        <svg width="100" height="165" viewBox="0 0 100 165" xmlns="http://www.w3.org/2000/svg" filter="drop-shadow(0 8px 24px rgba(0,0,0,.55))">
          <!-- Basket -->
          <rect x="30" y="132" width="40" height="28" rx="4" fill="#c8a040"/>
          <rect x="30" y="132" width="40" height="5" fill="#a07828"/>
          <line x1="38" y1="132" x2="38" y2="160" stroke="#7a5018" stroke-width="1.2"/>
          <line x1="62" y1="132" x2="62" y2="160" stroke="#7a5018" stroke-width="1.2"/>
          <!-- Ropes -->
          <line x1="33" y1="132" x2="46" y2="112" stroke="#d4a843" stroke-width="1.3" opacity="0.9"/>
          <line x1="67" y1="132" x2="54" y2="112" stroke="#d4a843" stroke-width="1.3" opacity="0.9"/>
          <!-- Balloon envelope panels -->
          <path d="M50,8 Q88,18 92,62 Q88,106 50,120 Q12,106 8,62 Q12,18 50,8 Z" fill="#1a4070"/>
          <path d="M50,8 Q66,20 70,62 Q66,104 50,120 Q34,104 30,62 Q34,20 50,8 Z" fill="#d4a843"/>
          <path d="M50,8 Q56,20 58,62 Q56,104 50,120 Q44,104 42,62 Q44,20 50,8 Z" fill="#1a4070"/>
          <path d="M50,8 Q52,20 53,62 Q52,104 50,120 Q48,104 47,62 Q48,20 50,8 Z" fill="#f0d080" opacity="0.5"/>
          <!-- Horizontal ribs -->
          <path d="M8,62 Q50,56 92,62" fill="none" stroke="#a07828" stroke-width="1" opacity="0.5"/>
          <path d="M10,42 Q50,36 90,42" fill="none" stroke="#a07828" stroke-width="1" opacity="0.4"/>
          <path d="M10,82 Q50,76 90,82" fill="none" stroke="#a07828" stroke-width="1" opacity="0.4"/>
          <!-- Top cap -->
          <ellipse cx="50" cy="8" rx="10" ry="7" fill="#f0d080"/>
          <!-- Shine highlight -->
          <ellipse cx="36" cy="34" rx="9" ry="13" fill="rgba(255,255,255,0.18)" transform="rotate(-15,36,34)"/>
        </svg>
      </div>
    </div>

    <!-- L7: Front wavy paper cuts -->
    <div class="dl" id="l-front">
      <svg viewBox="0 0 1440 260" preserveAspectRatio="none" width="100%"
           style="position:absolute;bottom:0;left:0;" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="fw1" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#d4a843"/><stop offset="100%" stop-color="#604010"/>
          </linearGradient>
          <linearGradient id="fw2" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#f0d080"/><stop offset="100%" stop-color="#8a6020"/>
          </linearGradient>
          <filter id="fw-shadow"><feDropShadow dx="0" dy="-8" stdDeviation="14" flood-color="#000" flood-opacity="0.65"/></filter>
        </defs>
        <!-- Back wave -->
        <path d="M0,260 L0,150 Q80,90 160,130 Q240,168 320,118 Q400,68 480,118 Q560,168 640,120 Q720,72 800,120 Q880,168 960,118 Q1040,68 1120,118 Q1200,165 1280,118 Q1360,70 1440,120 L1440,260 Z" fill="url(#fw1)" filter="url(#fw-shadow)" opacity="0.95"/>
        <!-- Front wave -->
        <path d="M0,260 L0,195 Q90,140 180,175 Q270,208 360,165 Q450,122 540,165 Q630,205 720,165 Q810,122 900,165 Q990,205 1080,165 Q1170,122 1260,165 Q1350,205 1440,170 L1440,260 Z" fill="url(#fw2)" filter="url(#fw-shadow)"/>
        <!-- Gold trim top edge -->
        <path d="M0,193 Q90,138 180,173 Q270,206 360,163 Q450,120 540,163 Q630,203 720,163 Q810,120 900,163 Q990,203 1080,163 Q1170,120 1260,163 Q1350,203 1440,168" fill="none" stroke="#f8e498" stroke-width="2.8" opacity="0.95"/>
        <path d="M0,201 Q90,146 180,181 Q270,214 360,171 Q450,128 540,171 Q630,211 720,171 Q810,128 900,171 Q990,211 1080,171 Q1170,128 1260,171 Q1350,211 1440,176" fill="none" stroke="#d4a843" stroke-width="1.4" opacity="0.6"/>
        <!-- Dot ornaments -->
        <g fill="#f8e498" opacity="0.9">
          <circle cx="180" cy="174" r="5"/><circle cx="360" cy="164" r="5"/>
          <circle cx="540" cy="164" r="5"/><circle cx="720" cy="164" r="5"/>
          <circle cx="900" cy="164" r="5"/><circle cx="1080" cy="164" r="5"/>
          <circle cx="1260" cy="164" r="5"/>
        </g>
        <!-- Mini stars on front wave -->
        <g fill="#f0d080" opacity="0.7">
          <polygon points="90,140 92,147 99,147 93,151 96,158 90,154 84,158 87,151 81,147 88,147"/>
          <polygon points="1350,138 1352,145 1359,145 1353,149 1356,156 1350,152 1344,156 1347,149 1341,145 1348,145"/>
        </g>
      </svg>
    </div>

    <!-- L8: TOP FLAP -->
    <div class="dl" id="l-flap">
      <canvas id="flapStars" style="position:absolute;inset:0;width:100%;height:100%;"></canvas>
      <div class="flap-top">
        <h1>Harish Kalyan<br><em>weds</em><br>Narmada</h1>
        <p>April 28, 2026 &nbsp;·&nbsp; Chennai, Tamil Nadu</p>
      </div>
      <div class="flap-edge">
        <svg viewBox="0 0 1440 170" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <filter id="fe-shadow"><feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#000" flood-opacity="0.8"/></filter>
            <linearGradient id="feg" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stop-color="#0e1f60"/><stop offset="100%" stop-color="#c8a040"/>
            </linearGradient>
          </defs>
          <path d="M0,0 L1440,0 L1440,95 Q1310,162 1160,118 Q1040,80 920,122 Q800,162 680,122 Q560,80 440,125 Q320,168 200,128 Q90,92 0,120 Z" fill="#0e1f60" filter="url(#fe-shadow)"/>
          <!-- Main gold border -->
          <path d="M0,115 Q90,87 200,123 Q320,163 440,120 Q560,75 680,117 Q800,157 920,117 Q1040,75 1160,113 Q1310,157 1440,90" fill="none" stroke="#f0d080" stroke-width="3.5"/>
          <!-- Inner gold border -->
          <path d="M0,105 Q90,77 200,113 Q320,153 440,110 Q560,65 680,107 Q800,147 920,107 Q1040,65 1160,103 Q1310,147 1440,80" fill="none" stroke="#d4a843" stroke-width="1.8" opacity="0.65"/>
          <!-- Dot ornaments on flap edge -->
          <g fill="#f0d080">
            <circle cx="200" cy="123" r="6"/><circle cx="440" cy="120" r="6"/>
            <circle cx="680" cy="117" r="6"/><circle cx="920" cy="117" r="6"/>
            <circle cx="1160" cy="113" r="6"/>
          </g>
          <!-- Star ornaments -->
          <g fill="#f8e498" opacity="0.8">
            <polygon points="1300,88 1302,96 1310,96 1304,101 1307,109 1300,104 1293,109 1296,101 1290,96 1298,96" transform="scale(0.7) translate(568,38)"/>
            <polygon points="140,92 142,100 150,100 144,105 147,113 140,108 133,113 136,105 130,100 138,100" transform="scale(0.7) translate(-20,38)"/>
          </g>
        </svg>
      </div>
      <div class="scroll-hint">
        <span>Scroll to Open</span>
        <div class="s-mouse"></div>
      </div>
    </div>

  </div>
</div>

<!-- ═══ BELOW FOLD ═══ -->
<div id="below">
  <section id="details">
    <div class="sec-label fade-in">The Celebration</div>
    <h2 class="sec-title fade-in">Harish Kalyan <em>Weds</em> Narmada</h2>
    <div class="ornament fade-in"><div class="ol"></div><div class="od"></div><div class="ol r"></div></div>
    <p class="fade-in" style="font-family:'Cormorant Garamond',serif;font-style:italic;font-size:clamp(15px,2.8vw,21px);color:rgba(245,241,232,.55);max-width:490px;margin:0 auto;line-height:1.8;">
      Two hearts entwined by destiny. Join us as we begin this sacred journey, blessed by our families and the divine.
    </p>
    <div class="info-grid">
      <div class="info-card"><div class="iicon">📅</div><div class="ilabel">Wedding Date</div><div class="ivalue">April 28, 2026</div><div class="isub">Tuesday</div></div>
      <div class="info-card"><div class="iicon">🕖</div><div class="ilabel">Ceremony Time</div><div class="ivalue">10:30 AM Onwards</div><div class="isub">Auspicious Muhurtham</div></div>
      <div class="info-card"><div class="iicon">🏛️</div><div class="ilabel">Venue</div><div class="ivalue">Grand Palace Convention Hall</div><div class="isub">Anna Salai, Chennai</div></div>
      <div class="info-card"><div class="iicon">📍</div><div class="ilabel">Location</div><div class="ivalue">Chennai, Tamil Nadu</div><div class="isub">India</div></div>
    </div>
  </section>

  <section id="countdown">
    <div class="sec-label fade-in">Counting Down To Forever</div>
    <h2 class="sec-title fade-in" style="font-size:clamp(24px,5vw,44px);">The Big Day Approaches</h2>
    <div class="cd-grid">
      <div class="cd-item"><div class="cd-num" id="cd-days">000</div><div class="cd-label">Days</div></div>
      <div class="cd-sep">:</div>
      <div class="cd-item"><div class="cd-num" id="cd-hours">00</div><div class="cd-label">Hours</div></div>
      <div class="cd-sep">:</div>
      <div class="cd-item"><div class="cd-num" id="cd-minutes">00</div><div class="cd-label">Minutes</div></div>
      <div class="cd-sep">:</div>
      <div class="cd-item"><div class="cd-num" id="cd-seconds">00</div><div class="cd-label">Seconds</div></div>
    </div>
  </section>

  <section id="timeline">
    <div class="sec-label fade-in">Celebrations</div>
    <h2 class="sec-title fade-in">Event Schedule</h2>
    <div class="tl-wrap">
      <div class="tl-item"><div class="tl-content"><div class="tl-icon">🪔</div><div class="tl-event">Day One</div><div class="tl-title">Nichayathartham</div><div class="tl-date">April 25, 2026 · 6:00 PM</div></div><div class="tl-dot"></div><div style="flex:1"></div></div>
      <div class="tl-item"><div style="flex:1"></div><div class="tl-dot"></div><div class="tl-content"><div class="tl-icon">🌼</div><div class="tl-event">Day Two · Morning</div><div class="tl-title">Nalangu &amp; Haldi</div><div class="tl-date">April 26, 2026 · 9:00 AM</div></div></div>
      <div class="tl-item"><div class="tl-content"><div class="tl-icon">🎨</div><div class="tl-event">Day Two · Evening</div><div class="tl-title">Mehendi Night</div><div class="tl-date">April 26, 2026 · 5:00 PM</div></div><div class="tl-dot"></div><div style="flex:1"></div></div>
      <div class="tl-item"><div style="flex:1"></div><div class="tl-dot"></div><div class="tl-content"><div class="tl-icon">🕊️</div><div class="tl-event">Day Three</div><div class="tl-title">Kalyanam</div><div class="tl-date">April 28, 2026 · 10:30 AM</div></div></div>
      <div class="tl-item"><div class="tl-content"><div class="tl-icon">🎉</div><div class="tl-event">Day Four</div><div class="tl-title">Grand Reception</div><div class="tl-date">April 29, 2026 · 7:00 PM</div></div><div class="tl-dot"></div><div style="flex:1"></div></div>
    </div>
  </section>

  <section id="rsvp">
    <div class="rsvp-wrap">
      <div class="sec-label fade-in">You're Invited</div>
      <h2 class="sec-title fade-in" style="font-size:clamp(26px,6vw,52px);">Join Our Celebration</h2>
      <div class="ornament fade-in"><div class="ol"></div><div class="od"></div><div class="ol r"></div></div>
      <p class="rsvp-quote fade-in">"Your presence would make our celebration complete. We look forward to sharing this beautiful moment with you."</p>
      <button class="rsvp-btn fade-in" id="rsvpToggle">Confirm Your Presence</button>
      <div class="rsvp-form" id="rsvpForm">
        <input class="rsvp-input" type="text" placeholder="Your Full Name" id="rsvpName"/>
        <input class="rsvp-input" type="tel" placeholder="Phone Number"/>
        <input class="rsvp-input" type="number" placeholder="Number of Guests" min="1" max="10"/>
        <button class="rsvp-submit" id="rsvpSubmit">Send RSVP ✦</button>
      </div>
      <div class="rsvp-success" id="rsvpSuccess">✦ Thank you! We can't wait to celebrate with you. ✦</div>
    </div>
  </section>

  <footer>
    <div class="ornament" style="margin-bottom:22px;"><div class="ol"></div><div class="od"></div><div class="ol r"></div></div>
    <div class="fn">Harish Kalyan <em>&amp;</em> Narmada</div>
    <div class="fs">April 28, 2026 &nbsp;·&nbsp; Chennai, Tamil Nadu</div>
    <div style="margin-top:32px;font-size:10px;color:rgba(255,255,255,.12);letter-spacing:2px;">Made with ♥ for our special day</div>
  </footer>
</div>

<script>
/* LOADER */
window.addEventListener('load', () => {{
  setTimeout(() => {{
    document.getElementById('loader').classList.add('hide');
    setTimeout(() => {{
      const l = document.getElementById('loader'); if(l) l.remove();
      document.getElementById('l-sky').classList.add('loaded');
    }}, 1000);
  }}, 1800);
}});

/* STARS */
function initStars(id, n) {{
  const c = document.getElementById(id); if(!c) return;
  const ctx = c.getContext('2d');
  let s = [];
  const resize = () => {{ c.width = c.offsetWidth; c.height = c.offsetHeight; }};
  resize(); window.addEventListener('resize', resize);
  for(let i=0;i<n;i++) s.push({{x:Math.random(),y:Math.random(),r:Math.random()*2+.3,sp:Math.random()*.016+.004,ph:Math.random()*Math.PI*2}});
  let t=0;
  (function draw(){{
    ctx.clearRect(0,0,c.width,c.height);
    s.forEach(st=>{{
      const o = .2+.8*(.5+.5*Math.sin(t*st.sp+st.ph));
      ctx.beginPath(); ctx.arc(st.x*c.width,st.y*c.height,st.r,0,Math.PI*2);
      ctx.fillStyle=`rgba(255,255,240,${{o}})`; ctx.fill();
    }}); t++; requestAnimationFrame(draw);
  }})();
}}
initStars('l-stars', 300);
initStars('flapStars', 200);

/* PARALLAX */
const diorama=document.getElementById('diorama'),
      lFlap=document.getElementById('l-flap'),
      lFront=document.getElementById('l-front'),
      lArch=document.getElementById('l-arch'),
      lBalloon=document.getElementById('l-balloon'),
      lClouds=document.getElementById('l-clouds'),
      lNames=document.getElementById('l-names');

let tick=false;
window.addEventListener('scroll',()=>{{if(!tick){{requestAnimationFrame(scroll_);tick=true;}}}});
function scroll_(){{
  const sy=window.scrollY, maxS=diorama.offsetHeight-window.innerHeight;
  const p=Math.min(sy/maxS,1);
  lFlap.style.transform=`translateY(${{-p*110}}%)`;
  lFront.style.transform=`translateY(${{-p*18}}%)`;
  lArch.style.transform=`translateY(${{-p*9}}%)`;
  lBalloon.style.transform=`translateY(${{-p*5}}%)`;
  lClouds.style.transform=`translateY(${{p*4}}%)`;
  lNames.style.opacity = p>0.22 ? Math.min((p-.22)/.38,1) : 0;
  tick=false;
}}

/* OBSERVER */
const obs=new IntersectionObserver(es=>{{
  es.forEach(e=>{{
    if(e.isIntersecting){{
      e.target.classList.add('visible');
      if(e.target.classList.contains('info-grid'))
        e.target.querySelectorAll('.info-card').forEach((c,i)=>setTimeout(()=>c.classList.add('visible'),i*110));
    }}
  }});
}},{{threshold:.12}});
document.querySelectorAll('.fade-in,.info-grid,.tl-item').forEach(el=>obs.observe(el));

/* COUNTDOWN */
const wd=new Date('2026-04-28T10:30:00');
function ctick(){{
  const d=wd-new Date(); if(d<=0) return;
  document.getElementById('cd-days').textContent=String(Math.floor(d/86400000)).padStart(3,'0');
  document.getElementById('cd-hours').textContent=String(Math.floor((d%86400000)/3600000)).padStart(2,'0');
  document.getElementById('cd-minutes').textContent=String(Math.floor((d%3600000)/60000)).padStart(2,'0');
  document.getElementById('cd-seconds').textContent=String(Math.floor((d%60000)/1000)).padStart(2,'0');
}}
ctick(); setInterval(ctick,1000);

/* RSVP */
document.getElementById('rsvpToggle').addEventListener('click',()=>document.getElementById('rsvpForm').classList.toggle('show'));
document.getElementById('rsvpSubmit').addEventListener('click',()=>{{
  if(!document.getElementById('rsvpName').value.trim()){{alert('Please enter your name.');return;}}
  document.getElementById('rsvpForm').classList.remove('show');
  document.getElementById('rsvpToggle').style.display='none';
  document.getElementById('rsvpSuccess').classList.add('show');
}});

/* MUSIC */
const mb=document.getElementById('musicBtn'),ma=document.getElementById('bgMusic');let pl=false;
mb.addEventListener('click',()=>pl?(ma.pause(),mb.textContent='♪',pl=false):(ma.play().catch(()=>{{}}}),mb.textContent='■',pl=true));
</script>
</body>
</html>'''

out_path = os.path.join(os.path.dirname(__file__), 'wedding-invitation (1).html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)
print('Done! File size:', len(html)//1024, 'KB')
