import base64, os

brain = r'C:\Users\LENOVO\.gemini\antigravity\brain\79284293-905c-43d3-a5a6-9fcf14d18c9d'

def b64img(filename):
    path = os.path.join(brain, filename)
    with open(path, 'rb') as f:
        return 'data:image/png;base64,' + base64.b64encode(f.read()).decode()

couple_src  = b64img('gallery_couple_1774643774286.png')
mandap_src  = b64img('gallery_mandap_1774643818024.png')
rings_src   = b64img('gallery_rings_1774643844305.png')
mehendi_src = b64img('gallery_mehendi_1774643874519.png')

gallery_css = '''
/* Gallery Section */
#gallery { padding: clamp(70px,11vw,130px) 24px; text-align:center; background: rgba(0,0,0,0.25); }
.gallery-subtitle { font-family:'Cinzel',serif; font-size:10px; letter-spacing:5px; color:var(--gold); opacity:.7; text-transform:uppercase; margin-top:10px; margin-bottom:52px; }
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  max-width: 1100px;
  margin: 0 auto;
  align-items: start;
}
.g-card {
  position: relative;
  overflow: hidden;
  cursor: pointer;
  border: 1px solid rgba(212,168,67,0.18);
  box-shadow: 0 8px 40px rgba(0,0,0,0.5);
  opacity: 0;
  transform: translateY(30px);
  transition: opacity .8s ease, transform .8s ease;
}
.g-card.visible { opacity:1; transform:translateY(0); }
.g-card:nth-child(1) { border-radius: 8px; }
.g-card:nth-child(2) { border-radius: 8px; margin-top: 24px; }
.g-card:nth-child(3) { border-radius: 8px; }
.g-card:nth-child(4) { border-radius: 8px; margin-top: 16px; }
.g-card img {
  width: 100%; display:block;
  transition: transform .6s cubic-bezier(.25,.46,.45,.94);
  object-fit: cover;
  aspect-ratio: 3/4;
}
.g-card:nth-child(2) img,
.g-card:nth-child(4) img { aspect-ratio: 3/5; }
.g-card:hover img { transform: scale(1.06); }
.g-overlay {
  position: absolute; inset:0;
  background: linear-gradient(180deg, transparent 40%, rgba(10,2,2,0.85) 100%);
  opacity:0; transition: opacity .4s ease;
  display: flex; align-items: flex-end; padding: 18px;
}
.g-card:hover .g-overlay { opacity:1; }
.g-caption {
  font-family:'Cormorant Garamond',serif;
  font-style:italic; font-size: 15px;
  color: var(--goldl); letter-spacing:.05em;
}
.g-border-top {
  position:absolute; top:0; left:0; right:0; height:2px;
  background: linear-gradient(90deg, transparent, var(--gold), transparent);
  transform: scaleX(0); transform-origin: left;
  transition: transform .5s ease;
}
.g-card:hover .g-border-top { transform: scaleX(1); }
@media(max-width:768px){
  .gallery-grid { grid-template-columns: 1fr 1fr; gap: 12px; }
  .g-card:nth-child(2),
  .g-card:nth-child(4) { margin-top: 0; }
}
@media(max-width:480px){
  .gallery-grid { grid-template-columns: 1fr; }
  .g-card img { aspect-ratio: 4/3; }
}
'''

gallery_html = (
    '\n<!-- ===== GALLERY ===== -->\n'
    '<section id="gallery">\n'
    '  <div class="sec-label fade-in">Memories</div>\n'
    '  <h2 class="sec-title fade-in">Our Moments</h2>\n'
    '  <p class="gallery-subtitle fade-in">A Glimpse of the Love We Share</p>\n'
    '  <div class="gallery-grid">\n'
    '    <div class="g-card">\n'
    '      <div class="g-border-top"></div>\n'
    '      <img src="' + couple_src + '" alt="The Couple" loading="lazy"/>\n'
    '      <div class="g-overlay"><span class="g-caption">The Couple</span></div>\n'
    '    </div>\n'
    '    <div class="g-card">\n'
    '      <div class="g-border-top"></div>\n'
    '      <img src="' + mandap_src + '" alt="Wedding Mandap" loading="lazy"/>\n'
    '      <div class="g-overlay"><span class="g-caption">The Sacred Mandap</span></div>\n'
    '    </div>\n'
    '    <div class="g-card">\n'
    '      <div class="g-border-top"></div>\n'
    '      <img src="' + rings_src + '" alt="Wedding Rings" loading="lazy"/>\n'
    '      <div class="g-overlay"><span class="g-caption">Bound for Life</span></div>\n'
    '    </div>\n'
    '    <div class="g-card">\n'
    '      <div class="g-border-top"></div>\n'
    '      <img src="' + mehendi_src + '" alt="Bridal Mehendi" loading="lazy"/>\n'
    '      <div class="g-overlay"><span class="g-caption">Mehendi Blessings</span></div>\n'
    '    </div>\n'
    '  </div>\n'
    '</section>\n'
)

with open('wedding-invitation (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

# Inject CSS before </style>
html = html.replace('</style>', gallery_css + '\n</style>', 1)

# Inject gallery section right before the countdown section
html = html.replace('<section id="countdown">', gallery_html + '<section id="countdown">')

# Add gallery cards to observer
html = html.replace(
    "document.querySelectorAll('.fade-in,.info-grid,.tl-item').forEach(function(el){obs.observe(el);});",
    "document.querySelectorAll('.fade-in,.info-grid,.tl-item,.g-card').forEach(function(el){obs.observe(el);});"
)

with open('wedding-invitation (1).html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Gallery injected! Size:', len(html)//1024, 'KB')
