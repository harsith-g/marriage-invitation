import base64, os

# Read deity image
img_data = open('deity.png', 'rb').read()
deity_src = 'data:image/png;base64,' + base64.b64encode(img_data).decode()

# Build HTML parts separately
head = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Harish Kalyan & Narmada — Wedding Invitation</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Cinzel:wght@400;600&family=Raleway:wght@200;300;400&display=swap" rel="stylesheet">
<style>
:root{
  --sky:#070c28;--sky2:#0c1848;--sky3:#142060;
  --gold:#d4a843;--goldl:#f0d080;--goldd:#a07828;
  --p1:#f0d080;--p2:#d4a843;--p3:#a07828;--p4:#705018;
  --cream:#f5e8c0;--white:#fff;
}
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{background:var(--sky);color:var(--cream);font-family:'Raleway',sans-serif;overflow-x:hidden;}

#loader{position:fixed;inset:0;background:var(--sky);z-index:9999;display:flex;flex-direction:column;align-items:center;justify-content:center;transition:opacity 1s ease;}
#loader.hide{opacity:0;pointer-events:none;}
.ld-m{font-family:'Cormorant Garamond',serif;font-size:clamp(28px,6vw,60px);color:var(--goldl);animation:pulse 2s ease-in-out infinite;}
.ld-l{width:80px;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent);margin:18px 0;animation:expand 2s ease-in-out infinite;}
.ld-s{font-family:'Cinzel',serif;font-size:10px;letter-spacing:5px;color:var(--gold);opacity:.6;text-transform:uppercase;}
@keyframes pulse{0%,100%{opacity:.5;transform:scale(.95)}50%{opacity:1;transform:scale(1)}}
@keyframes expand{0%,100%{width:40px;opacity:.3}50%{width:120px;opacity:1}}
@keyframes fadeUp{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:translateY(0)}}

#musicBtn{position:fixed;top:18px;right:18px;z-index:1000;width:42px;height:42px;border-radius:50%;background:rgba(7,12,40,.8);border:1px solid var(--gold);color:var(--gold);cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:18px;backdrop-filter:blur(8px);transition:all .3s;}
#musicBtn:hover{box-shadow:0 0 20px rgba(212,168,67,.5);transform:scale(1.1);}

#diorama{position:relative;height:350vh;}
.sticky{position:sticky;top:0;height:100vh;overflow:hidden;}
.dl{position:absolute;inset:0;width:100%;height:100%;will-change:transform;}

#l-sky{z-index:1;background:radial-gradient(ellipse at 50% 38%,#1e3580 0%,#0c1848 36%,#040815 100%);transform:scale(1.12);transition:transform 4s cubic-bezier(.2,.8,.2,1);}
#l-sky.loaded{transform:scale(1);}

#l-names{z-index:3;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;padding-top:clamp(28px,6vh,72px);pointer-events:none;opacity:0;transition:opacity .8s ease;}
.n-blessing{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:clamp(11px,1.8vw,16px);color:var(--goldl);opacity:.8;letter-spacing:.06em;margin-bottom:10px;text-align:center;}
.n-main{font-family:'Cormorant Garamond',serif;font-size:clamp(40px,9vw,102px);font-weight:300;color:var(--white);line-height:1.0;text-align:center;text-shadow:0 2px 40px rgba(212,168,67,.35);}
.n-main em{color:var(--goldl);font-style:italic;}
.n-date{font-family:'Cinzel',serif;font-size:clamp(9px,1.3vw,12px);letter-spacing:5px;color:var(--gold);text-transform:uppercase;margin-top:18px;opacity:.7;}

#l-arch{z-index:4;pointer-events:none;}
#l-balloon{z-index:5;pointer-events:none;}
.balloon-float{position:absolute;left:clamp(16px,7%,90px);bottom:28%;animation:bob 5s ease-in-out infinite;}
@keyframes bob{0%,100%{transform:translateY(0) rotate(-3deg)}50%{transform:translateY(-20px) rotate(3deg)}}

#l-front{z-index:6;pointer-events:none;}

#l-flap{z-index:10;display:flex;flex-direction:column;align-items:center;background:linear-gradient(180deg,#070c28 0%,#0e1f68 60%,transparent 100%);pointer-events:none;}
.flap-top{padding-top:clamp(28px,5.5vh,65px);text-align:center;}
.flap-top .fb{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:clamp(11px,1.8vw,16px);color:var(--goldl);opacity:.8;margin-bottom:10px;animation:fadeUp 1.2s ease forwards .4s;opacity:0;}
.flap-top h1{font-family:'Cormorant Garamond',serif;font-size:clamp(36px,9vw,100px);font-weight:300;color:var(--white);line-height:1.0;text-shadow:0 0 60px rgba(212,168,67,.3);animation:fadeUp 1.4s ease forwards .7s;opacity:0;}
.flap-top h1 em{color:var(--goldl);font-style:italic;}
.flap-top .fp{font-family:'Cinzel',serif;font-size:clamp(9px,1.3vw,12px);letter-spacing:5px;color:var(--gold);text-transform:uppercase;margin-top:14px;animation:fadeUp 1.2s ease forwards 1.3s;opacity:0;}
.flap-edge{position:absolute;bottom:-2px;left:0;right:0;line-height:0;}
.flap-edge svg{width:100%;display:block;}
.scroll-hint{position:absolute;bottom:44px;left:50%;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center;gap:8px;animation:fadeUp 1s ease forwards 3.2s;opacity:0;pointer-events:none;}
.scroll-hint span{font-family:'Cinzel',serif;font-size:9px;letter-spacing:4px;color:var(--gold);opacity:.6;text-transform:uppercase;}
.s-mouse{width:20px;height:32px;border:1.5px solid rgba(212,168,67,.4);border-radius:10px;position:relative;overflow:hidden;}
.s-mouse::after{content:'';position:absolute;top:5px;left:50%;transform:translateX(-50%);width:3px;height:5px;background:var(--gold);border-radius:2px;animation:dot 1.8s ease-in-out infinite;}
@keyframes dot{0%{opacity:1;top:5px}100%{opacity:0;top:20px}}

#below{background:linear-gradient(180deg,#040710 0%,#060c20 100%);position:relative;z-index:20;}
section{padding:clamp(70px,11vw,130px) 24px;text-align:center;position:relative;}
.sec-label{font-family:'Cinzel',serif;font-size:10px;letter-spacing:6px;color:var(--gold);text-transform:uppercase;margin-bottom:14px;}
.sec-title{font-family:'Cormorant Garamond',serif;font-size:clamp(32px,7.5vw,72px);font-weight:300;color:var(--white);line-height:1.1;}
.sec-title em{color:var(--goldl);font-style:italic;}
.orn{display:flex;align-items:center;justify-content:center;gap:14px;margin:26px auto;}
.ol{flex:1;max-width:100px;height:1px;background:linear-gradient(90deg,transparent,var(--gold));}
.ol.r{background:linear-gradient(90deg,var(--gold),transparent);}
.od{width:7px;height:7px;background:var(--gold);transform:rotate(45deg);}

.info-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:16px;max-width:860px;margin:52px auto 0;}
.info-card{background:rgba(255,255,255,.03);border:1px solid rgba(212,168,67,.18);padding:30px 22px;opacity:0;transform:translateY(28px);transition:opacity .7s ease,transform .7s ease;}
.info-card.visible{opacity:1;transform:translateY(0);}
.info-card:hover{background:rgba(212,168,67,.06);border-color:rgba(212,168,67,.4);transform:translateY(-4px);}
.iicon{font-size:26px;margin-bottom:12px;}
.ilabel{font-family:'Cinzel',serif;font-size:9px;letter-spacing:4px;color:var(--gold);text-transform:uppercase;margin-bottom:10px;opacity:.8;}
.ivalue{font-family:'Cormorant Garamond',serif;font-size:clamp(17px,3vw,23px);font-weight:400;color:var(--white);line-height:1.3;}
.isub{font-size:12px;color:rgba(245,241,232,.4);margin-top:5px;}

#countdown{background:rgba(0,0,0,.2);overflow:hidden;}
#countdown::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at center,rgba(212,168,67,.05) 0%,transparent 65%);}
.cd-grid{display:flex;justify-content:center;gap:clamp(12px,4vw,42px);margin-top:52px;flex-wrap:wrap;}
.cd-item{text-align:center;min-width:76px;}
.cd-num{font-family:'Cormorant Garamond',serif;font-size:clamp(46px,10vw,84px);font-weight:300;color:var(--white);line-height:1;position:relative;display:inline-block;}
.cd-num::after{content:'';position:absolute;bottom:-6px;left:10%;right:10%;height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent);}
.cd-label{font-family:'Cinzel',serif;font-size:9px;letter-spacing:4px;color:var(--gold);text-transform:uppercase;margin-top:16px;opacity:.7;}
.cd-sep{font-family:'Cormorant Garamond',serif;font-size:clamp(34px,7vw,62px);color:var(--gold);opacity:.25;align-self:flex-start;margin-top:8px;}

.tl-wrap{max-width:570px;margin:52px auto 0;position:relative;}
.tl-wrap::before{content:'';position:absolute;left:50%;transform:translateX(-50%);top:0;bottom:0;width:1px;background:linear-gradient(180deg,transparent,var(--gold) 10%,var(--gold) 90%,transparent);opacity:.22;}
.tl-item{display:flex;align-items:center;gap:20px;margin-bottom:42px;opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s ease;}
.tl-item.visible{opacity:1;transform:translateY(0);}
.tl-item:nth-child(odd){flex-direction:row-reverse;}
.tl-content{flex:1;text-align:right;padding:20px;background:rgba(255,255,255,.03);border:1px solid rgba(212,168,67,.12);transition:all .4s;}
.tl-item:nth-child(even) .tl-content{text-align:left;}
.tl-content:hover{background:rgba(212,168,67,.05);border-color:rgba(212,168,67,.28);}
.tl-dot{width:13px;height:13px;flex-shrink:0;background:var(--gold);border-radius:50%;box-shadow:0 0 18px rgba(212,168,67,.6);z-index:2;}
.tl-event{font-family:'Cinzel',serif;font-size:9px;letter-spacing:3px;color:var(--gold);text-transform:uppercase;margin-bottom:7px;}
.tl-title{font-family:'Cormorant Garamond',serif;font-size:clamp(17px,3.6vw,23px);color:var(--white);font-weight:400;}
.tl-date{font-size:11px;color:rgba(245,241,232,.4);margin-top:5px;}
.tl-icon{font-size:24px;margin-bottom:7px;}

#rsvp{background:rgba(0,0,0,.15);}
.rsvp-wrap{max-width:510px;margin:0 auto;}
.rsvp-quote{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:clamp(15px,3vw,23px);color:rgba(245,241,232,.6);line-height:1.7;margin:34px 0 44px;}
.rsvp-btn{display:inline-block;padding:15px 50px;border:1px solid var(--gold);color:var(--gold);font-family:'Cinzel',serif;font-size:10px;letter-spacing:5px;text-transform:uppercase;text-decoration:none;position:relative;overflow:hidden;cursor:pointer;background:transparent;transition:color .4s;}
.rsvp-btn::before{content:'';position:absolute;inset:0;background:var(--gold);transform:scaleX(0);transform-origin:left;transition:transform .4s;z-index:-1;}
.rsvp-btn:hover{color:#040810;}
.rsvp-btn:hover::before{transform:scaleX(1);}
.rsvp-form{margin-top:34px;display:none;}
.rsvp-form.show{display:block;animation:fadeUp .6s ease forwards;}
.rsvp-input{width:100%;background:rgba(255,255,255,.04);border:1px solid rgba(212,168,67,.2);padding:12px 17px;color:var(--cream);font-family:'Raleway',sans-serif;font-size:14px;margin-bottom:10px;outline:none;transition:border-color .3s;}
.rsvp-input:focus{border-color:var(--gold);}
.rsvp-input::placeholder{color:rgba(245,241,232,.25);}
.rsvp-submit{width:100%;padding:14px;background:var(--gold);color:#040810;border:none;font-family:'Cinzel',serif;font-size:10px;letter-spacing:4px;text-transform:uppercase;cursor:pointer;transition:all .3s;}
.rsvp-submit:hover{background:var(--goldl);}
.rsvp-success{display:none;}
.rsvp-success.show{display:block;font-family:'Cormorant Garamond',serif;font-size:21px;font-style:italic;color:var(--gold);margin-top:26px;animation:fadeUp .6s ease forwards;}

footer{background:#02040e;padding:52px 24px 32px;text-align:center;border-top:1px solid rgba(212,168,67,.1);}
.fn{font-family:'Cormorant Garamond',serif;font-size:clamp(28px,6vw,50px);font-weight:300;color:var(--white);}
.fn em{color:var(--goldl);font-style:italic;}
.fs{font-family:'Cinzel',serif;font-size:9px;letter-spacing:5px;color:var(--gold);opacity:.4;text-transform:uppercase;margin-top:16px;}

.fade-in{opacity:0;transform:translateY(30px);transition:opacity .8s ease,transform .8s ease;}
.fade-in.visible{opacity:1;transform:translateY(0);}
#details::before{content:'';position:absolute;top:0;left:50%;transform:translateX(-50%);width:1px;height:70px;background:linear-gradient(180deg,transparent,var(--gold));}

@media(max-width:600px){
  .cd-sep{display:none;}
  .tl-wrap::before{left:20px;}
  .tl-item,.tl-item:nth-child(odd){flex-direction:column;align-items:flex-start;padding-left:44px;}
  .tl-dot{position:absolute;left:13px;}
  .tl-item{position:relative;}
  .tl-content,.tl-item:nth-child(even) .tl-content{text-align:left;}
  .info-grid{grid-template-columns:1fr 1fr;}
  .balloon-float{left:8px;}
}
</style>
</head>
<body>
<div id="loader">
  <div class="ld-m">H &amp; N</div>
  <div class="ld-l"></div>
  <div class="ld-s">Loading your invitation</div>
</div>
<button id="musicBtn" title="Toggle Music">&#9834;</button>
<audio id="bgMusic" loop><source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg"></audio>

<div id="diorama">
  <div class="sticky">

    <!-- L1: Sky -->
    <div class="dl" id="l-sky"></div>

    <!-- Stars -->
    <canvas class="dl" id="l-stars" style="z-index:2;pointer-events:none;"></canvas>

    <!-- Clouds -->
    <div class="dl" id="l-clouds" style="z-index:3;pointer-events:none;top:4%;">
      <svg viewBox="0 0 1440 200" width="100%" preserveAspectRatio="none" style="opacity:.1;position:absolute;top:0;left:0;">
        <ellipse cx="150" cy="65" rx="125" ry="40" fill="white"/>
        <ellipse cx="255" cy="50" rx="90" ry="28" fill="white"/>
        <ellipse cx="800" cy="85" rx="165" ry="48" fill="white"/>
        <ellipse cx="950" cy="62" rx="120" ry="36" fill="white"/>
        <ellipse cx="1250" cy="50" rx="105" ry="32" fill="white"/>
      </svg>
    </div>

    <!-- L3: Names (revealed under flap) -->
    <div class="dl" id="l-names">
      <p class="n-blessing">&#2384;&#2350; &#2344;&#2350;&#2330;&#2381;&#2330;&#2367;&#2357;&#2366;&#2351; &middot; With the Blessings of the Almighty</p>
      <h1 class="n-main">Harish Kalyan<br><em>weds</em><br>Narmada</h1>
      <p class="n-date">April 28, 2026 &nbsp;&middot;&nbsp; Chennai, Tamil Nadu</p>
    </div>

    <!-- L4: Architecture arch -->
    <div class="dl" id="l-arch">'''

arch_svg_open = '''
      <svg viewBox="0 0 1440 800" preserveAspectRatio="xMidYMax meet"
           style="position:absolute;bottom:0;left:0;width:100%;height:auto;" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="ag1" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#f0d080"/><stop offset="100%" stop-color="#7a5018"/>
          </linearGradient>
          <linearGradient id="ag2" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#d4a843"/><stop offset="100%" stop-color="#604010"/>
          </linearGradient>
          <linearGradient id="ag3" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#c8a040"/><stop offset="100%" stop-color="#4a3010"/>
          </linearGradient>
          <radialGradient id="archGlow" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#f0d080" stop-opacity="0.3"/>
            <stop offset="100%" stop-color="#d4a843" stop-opacity="0"/>
          </radialGradient>
          <filter id="sh1"><feDropShadow dx="0" dy="-6" stdDeviation="12" flood-color="#000" flood-opacity="0.55"/></filter>
          <filter id="sh2"><feDropShadow dx="0" dy="-10" stdDeviation="22" flood-color="#000" flood-opacity="0.65"/></filter>
          <filter id="glow1"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
          <clipPath id="archClip">
            <path d="M460,800 L460,470 Q460,255 710,215 Q960,255 960,470 L960,800 Z"/>
          </clipPath>
        </defs>
        <!-- Back wave -->
        <path d="M0,800 L0,560 Q180,400 360,445 Q540,490 720,415 Q900,340 1080,415 Q1260,490 1440,445 L1440,800 Z" fill="url(#ag3)" filter="url(#sh1)" opacity="0.85"/>
        <!-- Mid wave -->
        <path d="M0,800 L0,620 Q200,475 400,522 Q600,568 720,502 Q840,435 1040,502 Q1240,568 1440,522 L1440,800 Z" fill="url(#ag2)" filter="url(#sh1)"/>
        <!-- Main platform -->
        <path d="M0,800 L0,672 Q240,572 480,622 Q620,652 720,612 Q820,572 960,622 Q1200,672 1440,612 L1440,800 Z" fill="url(#ag1)" filter="url(#sh2)"/>
        <!-- Platform gold trim -->
        <path d="M0,670 Q240,570 480,620 Q620,650 720,610 Q820,570 960,620 Q1200,670 1440,610" fill="none" stroke="#f8e498" stroke-width="3" opacity="0.95"/>
        <path d="M0,678 Q240,578 480,628 Q620,658 720,618 Q820,578 960,628 Q1200,678 1440,618" fill="none" stroke="#d4a843" stroke-width="1.5" opacity="0.55"/>
        <!-- Platform dot ornaments -->
        <g fill="#f8e498" opacity="0.9">
          <circle cx="240" cy="614" r="5.5"/><circle cx="480" cy="621" r="5.5"/>
          <circle cx="720" cy="611" r="5.5"/><circle cx="960" cy="621" r="5.5"/>
          <circle cx="1200" cy="613" r="5.5"/>
        </g>
        <!-- Arch opening sky -->
        <path d="M460,800 L460,470 Q460,255 710,215 Q960,255 960,470 L960,800 Z" fill="#0c1848" opacity="0.95"/>
        <!-- Glow -->
        <ellipse cx="710" cy="490" rx="200" ry="250" fill="url(#archGlow)"/>
'''

deity_img_tag = '        <image href="' + deity_src + '" x="510" y="215" width="400" height="400" clip-path="url(#archClip)" preserveAspectRatio="xMidYMid meet" opacity="0.92"/>\n'

arch_svg_close = '''        <!-- Arch outer frame -->
        <path d="M460,800 L460,470 Q460,255 710,215 Q960,255 960,470 L960,800" fill="none" stroke="url(#ag1)" stroke-width="9" filter="url(#sh1)"/>
        <!-- Arch inner frame lines -->
        <path d="M482,800 L482,475 Q482,270 710,234 Q938,270 938,475 L938,800" fill="none" stroke="#f0d080" stroke-width="3.5" opacity="0.7"/>
        <path d="M504,800 L504,480 Q504,285 710,252 Q916,285 916,480 L916,800" fill="none" stroke="#d4a843" stroke-width="1.8" opacity="0.45"/>
        <!-- Keystone medallion -->
        <ellipse cx="710" cy="213" rx="50" ry="50" fill="url(#ag1)" filter="url(#sh2)"/>
        <ellipse cx="710" cy="213" rx="42" ry="42" fill="none" stroke="#f0d080" stroke-width="3"/>
        <ellipse cx="710" cy="213" rx="34" ry="34" fill="url(#ag2)"/>
        <g fill="#f8e498" opacity="0.9">
          <path d="M710,200 Q714,207 710,213 Q706,207 710,200Z"/>
          <path d="M710,200 Q718,205 718,213 Q711,210 710,200Z"/>
          <path d="M710,200 Q702,205 702,213 Q709,210 710,200Z"/>
          <circle cx="710" cy="215" r="4.5"/>
        </g>
        <!-- Left column -->
        <rect x="432" y="430" width="38" height="370" rx="6" fill="url(#ag2)" filter="url(#sh1)"/>
        <rect x="436" y="430" width="30" height="370" fill="none" stroke="#f0d080" stroke-width="1.3" opacity="0.33"/>
        <ellipse cx="451" cy="428" rx="24" ry="13" fill="url(#ag1)" filter="url(#glow1)"/>
        <!-- Right column -->
        <rect x="970" y="430" width="38" height="370" rx="6" fill="url(#ag2)" filter="url(#sh1)"/>
        <rect x="974" y="430" width="30" height="370" fill="none" stroke="#f0d080" stroke-width="1.3" opacity="0.33"/>
        <ellipse cx="989" cy="428" rx="24" ry="13" fill="url(#ag1)" filter="url(#glow1)"/>
        <!-- Hanging pendants LEFT -->
        <g filter="url(#glow1)">
          <line x1="548" y1="278" x2="548" y2="342" stroke="#d4a843" stroke-width="1.5"/><circle cx="548" cy="346" r="7.5" fill="#f0d080"/>
          <line x1="578" y1="262" x2="578" y2="316" stroke="#d4a843" stroke-width="1.5"/><circle cx="578" cy="320" r="6.5" fill="#d4a843"/>
          <line x1="563" y1="268" x2="563" y2="325" stroke="#d4a843" stroke-width="1"/><circle cx="563" cy="329" r="5.5" fill="#f0d080" opacity="0.8"/>
        </g>
        <!-- Hanging pendants RIGHT -->
        <g filter="url(#glow1)">
          <line x1="872" y1="278" x2="872" y2="342" stroke="#d4a843" stroke-width="1.5"/><circle cx="872" cy="346" r="7.5" fill="#f0d080"/>
          <line x1="842" y1="262" x2="842" y2="316" stroke="#d4a843" stroke-width="1.5"/><circle cx="842" cy="320" r="6.5" fill="#d4a843"/>
          <line x1="857" y1="268" x2="857" y2="325" stroke="#d4a843" stroke-width="1"/><circle cx="857" cy="329" r="5.5" fill="#f0d080" opacity="0.8"/>
        </g>
        <!-- Decorative foliage LEFT -->
        <g fill="#d4a843" opacity="0.65">
          <circle cx="270" cy="510" r="6.5"/><circle cx="292" cy="486" r="5"/>
          <circle cx="248" cy="532" r="5.5"/><circle cx="304" cy="522" r="4"/>
          <circle cx="228" cy="498" r="4.5"/><circle cx="255" cy="466" r="3.5"/>
          <path d="M258,488 Q272,474 286,482 Q272,496 258,488Z" fill="#f0d080"/>
          <path d="M288,516 Q302,502 316,510 Q302,524 288,516Z" fill="#f0d080"/>
        </g>
        <!-- Decorative foliage RIGHT -->
        <g fill="#d4a843" opacity="0.65">
          <circle cx="1170" cy="510" r="6.5"/><circle cx="1148" cy="486" r="5"/>
          <circle cx="1192" cy="532" r="5.5"/><circle cx="1136" cy="522" r="4"/>
          <circle cx="1212" cy="498" r="4.5"/><circle cx="1185" cy="466" r="3.5"/>
          <path d="M1182,488 Q1168,474 1154,482 Q1168,496 1182,488Z" fill="#f0d080"/>
          <path d="M1152,516 Q1138,502 1124,510 Q1138,524 1152,516Z" fill="#f0d080"/>
        </g>
        <!-- Stars in arch area -->
        <g fill="#f0d080">
          <polygon points="175,448 178,460 190,460 180,468 184,480 175,472 166,480 170,468 160,460 172,460" opacity="0.75"/>
          <polygon points="340,388 343,398 353,398 345,404 348,414 340,408 332,414 335,404 327,398 337,398" opacity="0.6"/>
          <polygon points="1100,448 1103,460 1115,460 1105,468 1109,480 1100,472 1091,480 1095,468 1085,460 1097,460" opacity="0.75"/>
          <polygon points="1265,388 1268,398 1278,398 1270,404 1273,414 1265,408 1257,414 1260,404 1252,398 1262,398" opacity="0.6"/>
        </g>
        <!-- Constellation lines -->
        <g stroke="#d4a843" stroke-width="0.8" opacity="0.3">
          <line x1="115" y1="385" x2="155" y2="425"/><line x1="155" y1="425" x2="205" y2="405"/>
          <line x1="1325" y1="385" x2="1285" y2="425"/><line x1="1285" y1="425" x2="1235" y2="405"/>
        </g>
      </svg>
    </div>'''

balloon = '''
    <!-- L5: Balloon -->
    <div class="dl" id="l-balloon">
      <div class="balloon-float">
        <svg width="105" height="172" viewBox="0 0 105 172" xmlns="http://www.w3.org/2000/svg"
             filter="drop-shadow(0 8px 24px rgba(0,0,0,.55))">
          <rect x="32" y="138" width="42" height="28" rx="4" fill="#c8a040"/>
          <rect x="32" y="138" width="42" height="5" fill="#a07828"/>
          <line x1="41" y1="138" x2="41" y2="166" stroke="#7a5018" stroke-width="1.2"/>
          <line x1="65" y1="138" x2="65" y2="166" stroke="#7a5018" stroke-width="1.2"/>
          <line x1="35" y1="138" x2="49" y2="116" stroke="#d4a843" stroke-width="1.4"/>
          <line x1="71" y1="138" x2="57" y2="116" stroke="#d4a843" stroke-width="1.4"/>
          <path d="M53,9 Q93,20 97,66 Q93,112 53,126 Q13,112 9,66 Q13,20 53,9 Z" fill="#1a3a70"/>
          <path d="M53,9 Q70,22 74,66 Q70,110 53,126 Q36,110 32,66 Q36,22 53,9 Z" fill="#d4a843"/>
          <path d="M53,9 Q59,22 62,66 Q59,110 53,126 Q47,110 44,66 Q47,22 53,9 Z" fill="#1a3a70"/>
          <path d="M53,9 Q55,22 56,66 Q55,110 53,126 Q51,110 50,66 Q51,22 53,9 Z" fill="#f0d080" opacity="0.5"/>
          <path d="M9,66 Q53,60 97,66" fill="none" stroke="#a07828" stroke-width="1.1" opacity="0.5"/>
          <path d="M11,44 Q53,38 95,44" fill="none" stroke="#a07828" stroke-width="1" opacity="0.4"/>
          <path d="M11,88 Q53,82 95,88" fill="none" stroke="#a07828" stroke-width="1" opacity="0.4"/>
          <ellipse cx="53" cy="9" rx="11" ry="7.5" fill="#f0d080"/>
          <ellipse cx="38" cy="36" rx="9" ry="13" fill="rgba(255,255,255,0.18)" transform="rotate(-15,38,36)"/>
        </svg>
      </div>
    </div>'''

front_layer = '''
    <!-- L6: Front waves -->
    <div class="dl" id="l-front">
      <svg viewBox="0 0 1440 270" preserveAspectRatio="none" width="100%"
           style="position:absolute;bottom:0;left:0;" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="fw1" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#d4a843"/><stop offset="100%" stop-color="#5a3c0e"/>
          </linearGradient>
          <linearGradient id="fw2" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#f0d080"/><stop offset="100%" stop-color="#8a6020"/>
          </linearGradient>
          <filter id="fw-sh"><feDropShadow dx="0" dy="-8" stdDeviation="14" flood-color="#000" flood-opacity="0.68"/></filter>
        </defs>
        <path d="M0,270 L0,155 Q80,92 160,133 Q240,172 320,120 Q400,68 480,120 Q560,172 640,122 Q720,72 800,122 Q880,172 960,120 Q1040,68 1120,118 Q1200,166 1280,118 Q1360,70 1440,122 L1440,270 Z" fill="url(#fw1)" filter="url(#fw-sh)"/>
        <path d="M0,270 L0,198 Q90,142 180,178 Q270,212 360,168 Q450,124 540,168 Q630,210 720,168 Q810,124 900,168 Q990,210 1080,168 Q1170,124 1260,168 Q1350,210 1440,172 L1440,270 Z" fill="url(#fw2)" filter="url(#fw-sh)"/>
        <path d="M0,196 Q90,140 180,176 Q270,210 360,166 Q450,122 540,166 Q630,208 720,166 Q810,122 900,166 Q990,208 1080,166 Q1170,122 1260,166 Q1350,208 1440,170" fill="none" stroke="#f8e498" stroke-width="3" opacity="0.95"/>
        <path d="M0,204 Q90,148 180,184 Q270,218 360,174 Q450,130 540,174 Q630,216 720,174 Q810,130 900,174 Q990,216 1080,174 Q1170,130 1260,174 Q1350,216 1440,178" fill="none" stroke="#d4a843" stroke-width="1.5" opacity="0.6"/>
        <g fill="#f8e498" opacity="0.9">
          <circle cx="180" cy="177" r="5.5"/><circle cx="360" cy="167" r="5.5"/>
          <circle cx="540" cy="167" r="5.5"/><circle cx="720" cy="167" r="5.5"/>
          <circle cx="900" cy="167" r="5.5"/><circle cx="1080" cy="167" r="5.5"/>
          <circle cx="1260" cy="167" r="5.5"/>
        </g>
        <g fill="#f0d080" opacity="0.75">
          <polygon points="90,142 92,150 100,150 94,155 97,163 90,158 83,163 86,155 80,150 88,150"/>
          <polygon points="1350,140 1352,148 1360,148 1354,153 1357,161 1350,156 1343,161 1346,153 1340,148 1348,148"/>
        </g>
      </svg>
    </div>'''

flap = '''
    <!-- L7: TOP FLAP -->
    <div class="dl" id="l-flap">
      <canvas id="flapStars" style="position:absolute;inset:0;width:100%;height:100%;"></canvas>
      <div class="flap-top">
        <p class="fb">&#2384;&#2350; &#2344;&#2350;&#2330;&#2381;&#2330;&#2367;&#2357;&#2366;&#2351; &middot; With the Blessings of the Almighty</p>
        <h1>Harish Kalyan<br><em>weds</em><br>Narmada</h1>
        <p class="fp">April 28, 2026 &nbsp;&middot;&nbsp; Chennai, Tamil Nadu</p>
      </div>
      <div class="flap-edge">
        <svg viewBox="0 0 1440 172" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <filter id="fe-sh"><feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#000" flood-opacity="0.82"/></filter>
          </defs>
          <path d="M0,0 L1440,0 L1440,98 Q1310,166 1155,120 Q1038,82 918,125 Q795,166 675,126 Q555,82 435,128 Q312,172 195,130 Q88,94 0,122 Z" fill="#0e1f68" filter="url(#fe-sh)"/>
          <path d="M0,118 Q88,89 195,125 Q312,167 435,123 Q555,77 675,121 Q795,161 918,120 Q1038,77 1155,115 Q1310,162 1440,93" fill="none" stroke="#f0d080" stroke-width="3.5"/>
          <path d="M0,108 Q88,79 195,115 Q312,157 435,113 Q555,67 675,111 Q795,151 918,110 Q1038,67 1155,105 Q1310,152 1440,83" fill="none" stroke="#d4a843" stroke-width="1.8" opacity="0.65"/>
          <g fill="#f0d080">
            <circle cx="195" cy="125" r="6.5"/><circle cx="435" cy="123" r="6.5"/>
            <circle cx="675" cy="121" r="6.5"/><circle cx="918" cy="120" r="6.5"/>
            <circle cx="1155" cy="115" r="6.5"/>
          </g>
        </svg>
      </div>
      <div class="scroll-hint">
        <span>Scroll to Open</span>
        <div class="s-mouse"></div>
      </div>
    </div>

  </div>
</div>'''

below = '''
<div id="below">
  <section id="details">
    <div class="sec-label fade-in">The Celebration</div>
    <h2 class="sec-title fade-in">Harish Kalyan <em>Weds</em> Narmada</h2>
    <div class="orn fade-in"><div class="ol"></div><div class="od"></div><div class="ol r"></div></div>
    <p class="fade-in" style="font-family:'Cormorant Garamond',serif;font-style:italic;font-size:clamp(15px,2.8vw,21px);color:rgba(245,241,232,.55);max-width:490px;margin:0 auto;line-height:1.8;">
      Two hearts entwined by destiny. Join us as we begin this sacred journey, blessed by our families and the divine.
    </p>
    <div class="info-grid">
      <div class="info-card"><div class="iicon">&#128197;</div><div class="ilabel">Wedding Date</div><div class="ivalue">April 28, 2026</div><div class="isub">Tuesday</div></div>
      <div class="info-card"><div class="iicon">&#128374;</div><div class="ilabel">Ceremony Time</div><div class="ivalue">10:30 AM Onwards</div><div class="isub">Auspicious Muhurtham</div></div>
      <div class="info-card"><div class="iicon">&#127963;</div><div class="ilabel">Venue</div><div class="ivalue">Grand Palace Convention Hall</div><div class="isub">Anna Salai, Chennai</div></div>
      <div class="info-card"><div class="iicon">&#128205;</div><div class="ilabel">Location</div><div class="ivalue">Chennai, Tamil Nadu</div><div class="isub">India</div></div>
    </div>
  </section>

  <section id="countdown">
    <div class="sec-label fade-in">Counting Down To Forever</div>
    <h2 class="sec-title fade-in" style="font-size:clamp(24px,5vw,44px);">The Big Day Approaches</h2>
    <div class="cd-grid">
      <div class="cd-item"><div class="cd-num" id="cd-days">032</div><div class="cd-label">Days</div></div>
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
      <div class="tl-item"><div class="tl-content"><div class="tl-icon">&#129812;</div><div class="tl-event">Day One</div><div class="tl-title">Nichayathartham</div><div class="tl-date">April 25, 2026 &middot; 6:00 PM</div></div><div class="tl-dot"></div><div style="flex:1"></div></div>
      <div class="tl-item"><div style="flex:1"></div><div class="tl-dot"></div><div class="tl-content"><div class="tl-icon">&#127804;</div><div class="tl-event">Day Two &middot; Morning</div><div class="tl-title">Nalangu &amp; Haldi</div><div class="tl-date">April 26, 2026 &middot; 9:00 AM</div></div></div>
      <div class="tl-item"><div class="tl-content"><div class="tl-icon">&#127912;</div><div class="tl-event">Day Two &middot; Evening</div><div class="tl-title">Mehendi Night</div><div class="tl-date">April 26, 2026 &middot; 5:00 PM</div></div><div class="tl-dot"></div><div style="flex:1"></div></div>
      <div class="tl-item"><div style="flex:1"></div><div class="tl-dot"></div><div class="tl-content"><div class="tl-icon">&#128330;</div><div class="tl-event">Day Three &middot; The Sacred Union</div><div class="tl-title">Kalyanam</div><div class="tl-date">April 28, 2026 &middot; 10:30 AM</div></div></div>
      <div class="tl-item"><div class="tl-content"><div class="tl-icon">&#127881;</div><div class="tl-event">Day Four</div><div class="tl-title">Grand Reception</div><div class="tl-date">April 29, 2026 &middot; 7:00 PM</div></div><div class="tl-dot"></div><div style="flex:1"></div></div>
    </div>
  </section>

  <section id="rsvp">
    <div class="rsvp-wrap">
      <div class="sec-label fade-in">You're Invited</div>
      <h2 class="sec-title fade-in" style="font-size:clamp(26px,6vw,52px);">Join Our Celebration</h2>
      <div class="orn fade-in"><div class="ol"></div><div class="od"></div><div class="ol r"></div></div>
      <p class="rsvp-quote fade-in">"Your presence would make our celebration complete. We look forward to sharing this beautiful moment with you."</p>
      <button class="rsvp-btn fade-in" id="rsvpToggle">Confirm Your Presence</button>
      <div class="rsvp-form" id="rsvpForm">
        <input class="rsvp-input" type="text" placeholder="Your Full Name" id="rsvpName"/>
        <input class="rsvp-input" type="tel" placeholder="Phone Number"/>
        <input class="rsvp-input" type="number" placeholder="Number of Guests" min="1" max="10"/>
        <button class="rsvp-submit" id="rsvpSubmit">Send RSVP &#10022;</button>
      </div>
      <div class="rsvp-success" id="rsvpSuccess">&#10022; Thank you! We can't wait to celebrate with you. &#10022;</div>
    </div>
  </section>

  <footer>
    <div class="orn" style="margin-bottom:22px;"><div class="ol"></div><div class="od"></div><div class="ol r"></div></div>
    <div class="fn">Harish Kalyan <em>&amp;</em> Narmada</div>
    <div class="fs">April 28, 2026 &nbsp;&middot;&nbsp; Chennai, Tamil Nadu</div>
    <div style="margin-top:32px;font-size:10px;color:rgba(255,255,255,.12);letter-spacing:2px;">Made with &#10084; for our special day</div>
  </footer>
</div>'''

scripts = '''
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
    document.getElementById('loader').classList.add('hide');
    setTimeout(function() {
      var l = document.getElementById('loader'); if(l) l.remove();
      document.getElementById('l-sky').classList.add('loaded');
    }, 1000);
  }, 1800);
});

function initStars(id, n) {
  var c = document.getElementById(id); if(!c) return;
  var ctx = c.getContext('2d'), s = [];
  var resize = function() { c.width = c.offsetWidth; c.height = c.offsetHeight; };
  resize(); window.addEventListener('resize', resize);
  for(var i=0;i<n;i++) s.push({x:Math.random(),y:Math.random(),r:Math.random()*2+.3,sp:Math.random()*.016+.004,ph:Math.random()*Math.PI*2});
  var t=0;
  (function draw(){
    ctx.clearRect(0,0,c.width,c.height);
    s.forEach(function(st){
      var o=.2+.8*(.5+.5*Math.sin(t*st.sp+st.ph));
      ctx.beginPath(); ctx.arc(st.x*c.width,st.y*c.height,st.r,0,Math.PI*2);
      ctx.fillStyle='rgba(255,255,240,'+o+')'; ctx.fill();
    }); t++; requestAnimationFrame(draw);
  })();
}
initStars('l-stars', 320);
initStars('flapStars', 220);

var diorama=document.getElementById('diorama'),
    lFlap=document.getElementById('l-flap'),
    lFront=document.getElementById('l-front'),
    lArch=document.getElementById('l-arch'),
    lBalloon=document.getElementById('l-balloon'),
    lClouds=document.getElementById('l-clouds'),
    lNames=document.getElementById('l-names'),
    ticking=false;

window.addEventListener('scroll', function() {
  if(!ticking) { requestAnimationFrame(onScroll); ticking=true; }
});

function onScroll() {
  var sy=window.scrollY, maxS=diorama.offsetHeight-window.innerHeight;
  var p=Math.min(sy/maxS,1);
  lFlap.style.transform='translateY('+(-p*110)+'%)';
  lFront.style.transform='translateY('+(-p*18)+'%)';
  lArch.style.transform='translateY('+(-p*9)+'%)';
  lBalloon.style.transform='translateY('+(-p*5)+'%)';
  lClouds.style.transform='translateY('+(p*4)+'%)';
  lNames.style.opacity = p>0.22 ? Math.min((p-.22)/.38,1) : 0;
  ticking=false;
}

var obs=new IntersectionObserver(function(es){
  es.forEach(function(e){
    if(e.isIntersecting){
      e.target.classList.add('visible');
      if(e.target.classList.contains('info-grid'))
        e.target.querySelectorAll('.info-card').forEach(function(card,i){setTimeout(function(){card.classList.add('visible');},i*110);});
    }
  });
},{threshold:.12});
document.querySelectorAll('.fade-in,.info-grid,.tl-item').forEach(function(el){obs.observe(el);});

var wd=new Date('2026-04-28T10:30:00');
function ctick(){
  var d=wd-new Date(); if(d<=0) return;
  document.getElementById('cd-days').textContent=String(Math.floor(d/86400000)).padStart(3,'0');
  document.getElementById('cd-hours').textContent=String(Math.floor((d%86400000)/3600000)).padStart(2,'0');
  document.getElementById('cd-minutes').textContent=String(Math.floor((d%3600000)/60000)).padStart(2,'0');
  document.getElementById('cd-seconds').textContent=String(Math.floor((d%60000)/1000)).padStart(2,'0');
}
ctick(); setInterval(ctick,1000);

document.getElementById('rsvpToggle').addEventListener('click',function(){document.getElementById('rsvpForm').classList.toggle('show');});
document.getElementById('rsvpSubmit').addEventListener('click',function(){
  if(!document.getElementById('rsvpName').value.trim()){alert('Please enter your name.');return;}
  document.getElementById('rsvpForm').classList.remove('show');
  document.getElementById('rsvpToggle').style.display='none';
  document.getElementById('rsvpSuccess').classList.add('show');
});

var mb=document.getElementById('musicBtn'),ma=document.getElementById('bgMusic'),pl=false;
mb.addEventListener('click',function(){
  if(pl){ma.pause();mb.textContent='\\u266a';pl=false;}
  else{ma.play().catch(function(){});mb.textContent='\\u25a0';pl=true;}
});
</script>
</body>
</html>'''

full_html = head + arch_svg_open + deity_img_tag + arch_svg_close + balloon + front_layer + flap + below + scripts

out = 'wedding-invitation (1).html'
with open(out, 'w', encoding='utf-8') as f:
    f.write(full_html)
print('Done! Size:', len(full_html)//1024, 'KB')
