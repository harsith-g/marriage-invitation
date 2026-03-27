import re

with open('wedding-invitation (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── Replace timeline CSS completely ──────────────────────────────────────────
old_css_block = '''.tl-wrap{max-width:570px;margin:52px auto 0;position:relative;}
.tl-wrap::before{content:'';position:absolute;left:50%;transform:translateX(-50%);top:0;bottom:0;width:1px;background:linear-gradient(180deg,transparent,var(--gold) 10%,var(--gold) 90%,transparent);opacity:.22;}
.tl-item{display:flex;align-items:center;gap:20px;margin-bottom:42px;opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s ease;}
.tl-item.visible{opacity:1;transform:translateY(0);}
.tl-left{flex-direction:row;}
.tl-right{flex-direction:row-reverse;}
.tl-spacer{flex:1;}
.tl-left .tl-content{text-align:right;}
.tl-right .tl-content{text-align:left;}
.tl-content{flex:1;text-align:right;padding:20px;background:rgba(255,255,255,.03);border:1px solid rgba(212,168,67,.12);transition:all .4s;}
.tl-item:nth-child(even) .tl-content{text-align:left;}
.tl-content:hover{background:rgba(212,168,67,.05);border-color:rgba(212,168,67,.28);}
.tl-dot{width:13px;height:13px;flex-shrink:0;background:var(--gold);border-radius:50%;box-shadow:0 0 18px rgba(212,168,67,.6);z-index:2;}
.tl-event{font-family:'Cinzel',serif;font-size:9px;letter-spacing:3px;color:var(--gold);text-transform:uppercase;margin-bottom:7px;}
.tl-title{font-family:'Cormorant Garamond',serif;font-size:clamp(17px,3.6vw,23px);color:var(--white);font-weight:400;}
.tl-date{font-size:11px;color:rgba(245,241,232,.4);margin-top:5px;}
.tl-icon{display:flex;justify-content:center;align-items:center;height:40px;margin-bottom:8px;}'''

new_css_block = '''.tl-wrap{max-width:860px;margin:52px auto 0;position:relative;}
.tl-wrap::before{content:'';position:absolute;left:50%;transform:translateX(-50%);top:0;bottom:0;width:2px;background:linear-gradient(180deg,transparent,var(--gold) 8%,var(--gold) 92%,transparent);opacity:.35;}
/* Each row: left-half + dot + right-half */
.tl-item{display:grid;grid-template-columns:1fr 34px 1fr;align-items:center;gap:0;margin-bottom:48px;opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s ease;}
.tl-item.visible{opacity:1;transform:translateY(0);}
.tl-dot{width:16px;height:16px;background:var(--gold);border-radius:50%;box-shadow:0 0 20px rgba(212,168,67,.7);z-index:2;justify-self:center;}
/* LEFT card cells */
.tl-card-left{padding:24px 28px;background:rgba(255,255,255,.035);border:1px solid rgba(212,168,67,.15);text-align:right;margin-right:18px;transition:all .4s;}
.tl-card-left:hover{background:rgba(212,168,67,.06);border-color:rgba(212,168,67,.3);transform:translateX(-4px);}
/* RIGHT card cells */
.tl-card-right{padding:24px 28px;background:rgba(255,255,255,.035);border:1px solid rgba(212,168,67,.15);text-align:left;margin-left:18px;transition:all .4s;}
.tl-card-right:hover{background:rgba(212,168,67,.06);border-color:rgba(212,168,67,.3);transform:translateX(4px);}
/* Empty spacer cell */
.tl-empty{min-height:10px;}
.tl-event{font-family:'Cinzel',serif;font-size:9px;letter-spacing:3px;color:var(--gold);text-transform:uppercase;margin-bottom:7px;}
.tl-title{font-family:'Cormorant Garamond',serif;font-size:clamp(17px,2.6vw,22px);color:var(--white);font-weight:400;}
.tl-date{font-size:11px;color:rgba(245,241,232,.4);margin-top:5px;}
.tl-icon{display:flex;height:38px;margin-bottom:8px;}
.tl-card-left .tl-icon{justify-content:flex-end;}
.tl-card-right .tl-icon{justify-content:flex-start;}
@media(max-width:640px){
  .tl-wrap{max-width:95vw;}
  .tl-item{grid-template-columns:0 24px 1fr;}
  .tl-card-left{display:none;}
  .tl-card-right{margin-left:12px;text-align:left;}
  .tl-card-left.tl-show-mobile{display:block;grid-column:3;margin-left:12px;text-align:left;}
}'''

if old_css_block in html:
    html = html.replace(old_css_block, new_css_block)
    print('CSS replaced')
else:
    # patch individual parts
    css_section = re.search(r'\.tl-wrap\{[^}]+\}.*?\.tl-icon\{[^}]+\}', html, re.DOTALL)
    if css_section:
        html = html[:css_section.start()] + new_css_block + html[css_section.end():]
        print('CSS replaced via regex')
    else:
        print('CSS block NOT found, injecting before </style>')
        html = html.replace('</style>', new_css_block + '\n</style>', 1)

# ── Replace timeline HTML with proper grid structure ─────────────────────────
tl_section_start = html.find('<div class="tl-wrap">')
tl_section_end = html.find('</div>', tl_section_start)
# find the closing </div> for tl-wrap
depth = 0
i = tl_section_start
while i < len(html):
    if html[i:i+4] == '<div':
        depth += 1
    elif html[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            tl_section_end = i + 6
            break
    i += 1

# Read back the SVG contents from HTML (just reuse the ones embedded)
lamp_svg = '''<svg width="32" height="32" viewBox="0 0 34 34" fill="none" xmlns="http://www.w3.org/2000/svg"><ellipse cx="17" cy="28" rx="6" ry="3" fill="#d4a843" opacity="0.4"/><rect x="15" y="18" width="4" height="10" rx="2" fill="#d4a843" opacity="0.7"/><path d="M9 14 Q9 6 17 6 Q25 6 25 14 Q25 20 17 20 Q9 20 9 14Z" fill="#d4a843" opacity="0.85"/><ellipse cx="17" cy="13" rx="4" ry="4" fill="#f0d080" opacity="0.7"/><rect x="13" y="4" width="8" height="3" rx="1.5" fill="#a07828"/></svg>'''
flower_svg = '''<svg width="32" height="32" viewBox="0 0 34 34" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="17" cy="12" r="5" fill="#d4a843"/><ellipse cx="17" cy="4" rx="3.5" ry="5" fill="#f0d080" opacity="0.8"/><ellipse cx="17" cy="20" rx="3.5" ry="5" fill="#f0d080" opacity="0.8"/><ellipse cx="9" cy="12" rx="5" ry="3.5" fill="#f0d080" opacity="0.8"/><ellipse cx="25" cy="12" rx="5" ry="3.5" fill="#f0d080" opacity="0.8"/><circle cx="17" cy="12" r="3" fill="#fff" opacity="0.5"/><line x1="17" y1="22" x2="17" y2="30" stroke="#a07828" stroke-width="2"/></svg>'''
mehendi_svg = '''<svg width="32" height="32" viewBox="0 0 34 34" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M8 26 Q10 10 17 6 Q24 10 26 26" fill="none" stroke="#d4a843" stroke-width="2"/><path d="M11 26 Q12 14 17 10 Q22 14 23 26" fill="none" stroke="#f0d080" stroke-width="1.5"/><circle cx="17" cy="6" r="2" fill="#d4a843"/><ellipse cx="17" cy="27" rx="9" ry="4" fill="#d4a843" opacity="0.35"/></svg>'''
wedding_svg = '''<svg width="32" height="32" viewBox="0 0 34 34" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M5 14 L17 4 L29 14 L29 30 L5 30 Z" fill="none" stroke="#d4a843" stroke-width="2" stroke-linejoin="round"/><rect x="13" y="20" width="8" height="10" rx="1" fill="#d4a843" opacity="0.7"/><circle cx="17" cy="2" r="2" fill="#f0d080"/></svg>'''
reception_svg = '''<svg width="32" height="32" viewBox="0 0 34 34" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M5 28 L5 14 L10 10 L10 14" stroke="#d4a843" stroke-width="2" stroke-linejoin="round" fill="none"/><path d="M10 14 L10 28" stroke="#d4a843" stroke-width="2"/><path d="M14 14 L14 10 L20 7 L26 10 L26 14" stroke="#d4a843" stroke-width="2" stroke-linejoin="round" fill="none"/><path d="M14 14 L26 14 L26 28 L14 28 Z" fill="none" stroke="#d4a843" stroke-width="2"/><rect x="17" y="20" width="6" height="8" rx="1" fill="#d4a843" opacity="0.6"/></svg>'''

def card(side, icon_svg, event, title, date):
    cls = 'tl-card-left' if side == 'left' else 'tl-card-right'
    return f'<div class="{cls}"><div class="tl-icon">{icon_svg}</div><div class="tl-event">{event}</div><div class="tl-title">{title}</div><div class="tl-date">{date}</div></div>'

dot = '<div class="tl-dot"></div>'
empty = '<div class="tl-empty"></div>'

new_tl_html = '''<div class="tl-wrap">

  <!-- Row 1: Day One LEFT -->
  <div class="tl-item">
    ''' + card('left', lamp_svg, 'Day One', 'Nichayathartham', 'April 25, 2026 &middot; 6:00 PM') + '''
    ''' + dot + '''
    ''' + empty + '''
  </div>

  <!-- Row 2: Day Two Morning RIGHT -->
  <div class="tl-item">
    ''' + empty + '''
    ''' + dot + '''
    ''' + card('right', flower_svg, 'Day Two &middot; Morning', 'Nalangu &amp; Haldi', 'April 26, 2026 &middot; 9:00 AM') + '''
  </div>

  <!-- Row 3: Day Two Evening LEFT -->
  <div class="tl-item">
    ''' + card('left', mehendi_svg, 'Day Two &middot; Evening', 'Mehendi Night', 'April 26, 2026 &middot; 5:00 PM') + '''
    ''' + dot + '''
    ''' + empty + '''
  </div>

  <!-- Row 4: Day Three RIGHT -->
  <div class="tl-item">
    ''' + empty + '''
    ''' + dot + '''
    ''' + card('right', wedding_svg, 'Day Three &middot; The Sacred Union', 'Kalyanam', 'April 28, 2026 &middot; 10:30 AM') + '''
  </div>

  <!-- Row 5: Day Four LEFT -->
  <div class="tl-item">
    ''' + card('left', reception_svg, 'Day Four', 'Grand Reception', 'April 29, 2026 &middot; 7:00 PM') + '''
    ''' + dot + '''
    ''' + empty + '''
  </div>

</div>'''

html = html[:tl_section_start] + new_tl_html + html[tl_section_end:]
print('Timeline HTML replaced')

# Also remove old mobile timeline CSS that conflicts
old_mobile = '''  @media(max-width:600px){
  .cd-sep{display:none;}
  .tl-wrap::before{left:20px;}
  .tl-item,.tl-item:nth-child(odd){flex-direction:column;align-items:flex-start;padding-left:44px;}
  .tl-dot{position:absolute;left:13px;}
  .tl-item{position:relative;}
  .tl-content,.tl-item:nth-child(even) .tl-content{text-align:left;}
  .info-grid{grid-template-columns:1fr 1fr;}
  .balloon-float{left:8px;}
}'''
new_mobile = '''  @media(max-width:600px){
  .cd-sep{display:none;}
  .info-grid{grid-template-columns:1fr 1fr;}
  .balloon-float{left:8px;}
}'''
html = html.replace(old_mobile, new_mobile)

with open('wedding-invitation (1).html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done! Size:', len(html)//1024, 'KB')
