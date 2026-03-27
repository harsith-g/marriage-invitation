import codecs
import re
import os

file_path = 'wedding-invitation (1).html'
with codecs.open(file_path, 'r', 'utf-8') as f:
    text = f.read()

old_len = len(text)

# 1. Colors Updates
text = text.replace('--deep-blue: #5C0B0B;', '--deep-blue: #050A15;')
text = text.replace('--mid-blue: #7a1010;', '--mid-blue: #14244B;')
text = text.replace('--light-blue: #9b1f1f;', '--light-blue: #2A4880;')
text = text.replace('#220404', 'var(--deep-blue)')
text = text.replace('#5C0B0B', 'var(--mid-blue)')
text = re.sub(r'#7a1c1c|#7a1515|#7a1010|#9b1f1f', 'var(--light-blue)', text)
text = re.sub(r'#3d0808|#700d0d', '#0A1329', text)
text = text.replace('rgba(92,11,11', 'rgba(20,36,75')
text = text.replace('rgba(112,13,13', 'rgba(42,72,128')

# 2. CSS Replacement
css_new = """  /* ============ PAPER-CUT DIORAMA ============ */
  #paper-cut-hero {
    height: 300vh;
    position: relative;
    background: var(--deep-blue);
  }
  .sticky-wrapper {
    position: sticky;
    top: 0;
    height: 100vh;
    width: 100%;
    overflow: hidden;
    perspective: 1200px;
  }
  .paper-layer {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    will-change: transform;
    pointer-events: none;
    display: flex;
    justify-content: center;
  }
  
  /* Layer 1: Sky */
  .layer-1 { z-index: 1; transform: scale(1.15); transition: transform 3.5s cubic-bezier(0.2, 0.8, 0.2, 1); background: radial-gradient(circle at center 70%, var(--light-blue) 0%, var(--deep-blue) 70%); }
  .layer-1.scene-loaded { transform: scale(1.0); }
  
  /* Layer 2: Clouds & Balloon */
  .layer-2 { z-index: 2; opacity: 0; transition: opacity 2.5s ease 1s; }
  .layer-2.scene-loaded { opacity: 1; }
  
  /* Layer 3: Back Mountains & Ornaments */
  .layer-3 { z-index: 3; align-items: flex-end; }
  .layer-3 svg { width: 100%; height: 60vh; filter: drop-shadow(0 -8px 20px rgba(0,0,0,0.6)); }
  
  /* Layer 4: Front paper cuts & Couple */
  .layer-4 { z-index: 4; display: flex; flex-direction: column; justify-content: flex-end; align-items: center; }
  .front-cut-wrap { width: 100%; height: 45vh; filter: drop-shadow(0 -15px 35px rgba(0,0,0,0.8)); position: absolute; bottom: 0; left: 0; right: 0; }
  .front-cut-wrap svg { width: 100%; height: 100%; }
  
  /* Extracted Couple Styling */
  .couple-wrap {
    position: absolute;
    bottom: 8%; left: 50%; transform: translateX(-50%);
    width: clamp(250px, 45vw, 400px);
    filter: drop-shadow(0 -5px 15px rgba(0,0,0,0.5));
  }
  .couple-svg { width: 100%; }
  
  /* Layer 5: Top Flap (Card Cover) */
  .layer-5 {
    z-index: 10;
    flex-direction: column;
    align-items: center;
    pointer-events: auto;
    background: linear-gradient(180deg, var(--deep-blue) 0%, var(--mid-blue) 80%, transparent 100%);
    will-change: transform;
    filter: drop-shadow(0 20px 40px rgba(0,0,0,0.95));
  }
  
  /* Paper texture overlay for the top flap */
  .layer-5::before {
    content: ''; position: absolute; inset: 0; z-index: -1;
    background-image: url('data:image/svg+xml;utf8,%3Csvg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"%3E%3Cfilter id="noiseFilter"%3E%3CfeTurbulence type="fractalNoise" baseFrequency="0.75" numOctaves="3" stitchTiles="stitch"/%3E%3C/filter%3E%3Crect width="100%25" height="100%25" filter="url(%23noiseFilter)" opacity="0.06" mix-blend-mode="overlay"/%3E%3C/svg%3E');
    background-color: var(--mid-blue);
    mask-image: linear-gradient(180deg, black 80%, transparent 100%);
    -webkit-mask-image: linear-gradient(180deg, black 80%, transparent 100%);
  }
  
  .card-edge-bottom {
    position: absolute;
    bottom: -150px; left: 0; right: 0;
    height: 150px;
  }
  .card-edge-bottom svg { width: 100%; height: 100%; filter: drop-shadow(0 15px 20px rgba(0,0,0,0.6)); }
  
  .layer-5 .hero-content {
    margin-top: 15vh;
  }
  
  /* Floating balloons */
  .balloon { position: absolute; animation: floatBalloon 25s linear infinite; }
  .cloud-parallax { position: absolute; top: 15%; width: 100%; opacity: 0.15; pointer-events:none; }
"""
s1 = text.find('  /* ============ HERO SECTION ============ */')
s2 = text.find('  /* ============ DETAILS SECTION ============ */')

if s1 != -1 and s2 != -1:
    text = text[:s1] + css_new + "\n" + text[s2:]
else:
    print("Could not find CSS sections to replace.")

# 3. HTML Replacement
html_new = """<!-- ===== PAPER-CUT DIORAMA ===== -->
<section id="paper-cut-hero">
  <div class="sticky-wrapper">
    
    <!-- Layer 1: Sky -->
    <div class="paper-layer layer-1" id="layer1">
      <canvas id="starsCanvas"></canvas>
    </div>
    
    <!-- Layer 2: Clouds & Balloons -->
    <div class="paper-layer layer-2" id="layer2">
      <div id="floatingElements"></div>
      <div class="cloud-parallax">
        <svg viewBox="0 0 1440 200" width="100%" xmlns="http://www.w3.org/2000/svg" style="animation:driftCloud 40s linear infinite;">
          <ellipse cx="200" cy="80" rx="160" ry="50" fill="white"/>
          <ellipse cx="320" cy="60" rx="120" ry="40" fill="white"/>
          <ellipse cx="900" cy="100" rx="200" ry="60" fill="white"/>
          <ellipse cx="1050" cy="75" rx="150" ry="45" fill="white"/>
        </svg>
      </div>
    </div>
    
    <!-- Layer 3: Back Mountains -->
    <div class="paper-layer layer-3" id="layer3">
      <svg viewBox="0 0 1440 400" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M0,400 L0,200 L120,80 L260,180 L440,60 L620,160 L800,40 L980,160 L1160,90 L1340,180 L1440,120 L1440,400Z" fill="var(--light-blue)"/>
        <path d="M0,200 L120,80 L260,180 L440,60 L620,160 L800,40 L980,160 L1160,90 L1340,180 L1440,120" fill="none" stroke="var(--gold)" stroke-width="2.5" opacity="0.7"/>
      </svg>
    </div>
    
    <!-- Layer 4: Front Mountains & Couple -->
    <div class="paper-layer layer-4" id="layer4">
      <div class="front-cut-wrap">
        <svg viewBox="0 0 1440 300" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M0,300 L0,180 L80,100 L200,170 L300,120 L400,180 L500,110 L600,190 L720,130 L860,210 L1000,120 L1120,190 L1260,110 L1440,170 L1440,300Z" fill="var(--deep-blue)"/>
          <path d="M0,180 L80,100 L200,170 L300,120 L400,180 L500,110 L600,190 L720,130 L860,210 L1000,120 L1120,190 L1260,110 L1440,170" fill="none" stroke="var(--gold)" stroke-width="3" opacity="0.9"/>
        </svg>
      </div>
      
      <!-- Existing Couple SVG (Injected below) -->
      [INSERT_COUPLE_SVG]
      
    </div>
    
    <!-- Layer 5: Top Flap (Card Cover) -->
    <div class="paper-layer layer-5" id="layer5">
      <div class="hero-content">
        <div class="hero-blessing" style="opacity: 0; animation: fadeSlideUp 1.2s ease forwards 0.5s;">ஓம் நமச்சிவாய · With the Blessings of the Almighty<br>
        <em style="font-size:1.15em">Mr. & Mrs. Kalyan Sundaram & Mr. & Mrs. Udayakumar Rajan</em></div>
        <div class="hero-invite" style="opacity: 0; animation: fadeSlideUp 1.2s ease forwards 0.9s;">We joyfully invite you to celebrate the union of</div>
        <div class="hero-names" style="opacity: 0; animation: fadeSlideUp 1.4s ease forwards 1.3s;">Harish Kalyan <span class="ampersand">&amp;</span> Narmada</div>
        <div class="hero-divider" style="opacity: 0; animation: fadeIn 1s ease forwards 1.9s;"></div>
        <div class="hero-tagline" style="opacity: 0; animation: fadeSlideUp 1.2s ease forwards 2.1s;">April 28, 2026 · Chennai, Tamil Nadu</div>
      </div>
      
      <div class="card-edge-bottom">
        <svg viewBox="0 0 1440 150" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
          <!-- Main flap body -->
          <path d="M0,0 L1440,0 L1440,80 Q1320,140 1200,100 Q1100,70 980,110 Q860,150 720,120 Q580,90 460,130 Q340,160 240,120 Q120,75 0,100 Z" fill="var(--mid-blue)"/>
          <!-- Gold border line -->
          <path d="M0,95 Q120,70 240,115 Q340,155 460,125 Q580,85 720,115 Q860,145 980,105 Q1100,65 1200,95 Q1320,135 1440,75" fill="none" stroke="var(--gold)" stroke-width="2.5" opacity="0.95"/>
          <!-- Inner intricate line -->
          <path d="M0,85 Q120,60 240,105 Q340,145 460,115 Q580,75 720,105 Q860,135 980,95 Q1100,55 1200,85 Q1320,125 1440,65" fill="none" stroke="var(--gold-dark)" stroke-width="1.5" opacity="0.6"/>
        </svg>
      </div>
      
      <div class="scroll-indicator" style="bottom:-50px; animation-delay: 2.8s;">
        <span>Scroll to Open</span>
        <div class="scroll-mouse"></div>
      </div>
    </div>
  </div>
</section>
"""

# Extract couple svg
couple_match = re.search(r'<div class="couple-wrap".*?</svg>\s*</div>', text, flags=re.DOTALL)
if couple_match:
    couple_html = couple_match.group(0)
    # Remove old id
    couple_html = couple_html.replace('id="coupleLayer"', '')
    html_new = html_new.replace('[INSERT_COUPLE_SVG]', couple_html)

h1 = text.find('<!-- ===== HERO ===== -->')
h2 = text.find('<!-- ===== DETAILS ===== -->')
if h1 != -1 and h2 != -1:
    text = text[:h1] + html_new + "\n" + text[h2:]
else:
    print("Could not find HTML sections to replace.")

# 4. JS Replacement
js_start = text.find('// ===== LOADER =====')
js_end = text.find('// ===== INTERSECTION OBSERVER for scroll animations =====')
js_new = """// ===== LOADER =====
window.addEventListener('load', () => {
  setTimeout(() => {
    document.getElementById('loader').classList.add('hide');
    setTimeout(() => {
      document.getElementById('loader').remove();
      // cinematic class toggle
      const l1 = document.getElementById('layer1');
      const l2 = document.getElementById('layer2');
      if(l1) l1.classList.add('scene-loaded');
      if(l2) l2.classList.add('scene-loaded');
    }, 800);
  }, 2200);
});

// ===== PARALLAX SCROLL =====
let ticking = false;
window.addEventListener('scroll', () => {
  if (!ticking) {
    requestAnimationFrame(updateParallax);
    ticking = true;
  }
});

function updateParallax() {
  const scrollY = window.scrollY;
  const heroSection = document.getElementById('paper-cut-hero');
  if (heroSection) {
    const maxScroll = heroSection.offsetHeight - window.innerHeight;
    let progress = scrollY / maxScroll;
    if (progress > 1) progress = 1;

    const layerTop = document.getElementById('layer5');
    const layerFront = document.getElementById('layer4');
    const layerBack = document.getElementById('layer3');
    const layerClouds = document.getElementById('layer2');

    if (layerTop) layerTop.style.transform = `translateY(${-progress * 160}%)`;
    if (layerFront) layerFront.style.transform = `translateY(${-progress * 25}%) scale(${1 + progress*0.1})`;
    if (layerBack) layerBack.style.transform = `translateY(${-progress * 10}%)`;
    if (layerClouds) layerClouds.style.transform = `translateY(${progress * 5}%)`;
  }
  ticking = false;
}
"""

if js_start != -1 and js_end != -1:
    text = text[:js_start] + js_new + "\n" + text[js_end:]
else:
    print("Could not find JS sections to replace.")

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(text)

print(f"Updated successfully! Old len {old_len}, new len {len(text)}")
