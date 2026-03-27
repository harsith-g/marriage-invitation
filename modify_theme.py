import re

with open('wedding-invitation (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

# ─── 1. COLOR THEME: Blue → Red/Gold Warm ───────────────────────────────────
replacements = [
    # CSS variables
    ('--sky:#070c28;', '--sky:#1a0505;'),
    ('--sky2:#0c1848;', '--sky2:#2e0a0a;'),
    ('--sky3:#142060;', '--sky3:#4a1010;'),
    # Sky radial gradient
    ('#1e3580', '#6b1010'),
    ('#0c1848', '#2e0a0a'),
    ('#040815', '#0d0202'),
    # Flap background
    ('#070c28', '#1a0505'),
    ('#0e1f68', '#3d0d0d'),
    # Music btn background
    ('rgba(7,12,40,.8)', 'rgba(26,5,5,.8)'),
    # Below section background
    ('#040710', '#0d0202'),
    ('#060c20', '#1a0505'),
    # Countdown background
    ('#rsvp{background:rgba(0,0,0,.15)', '#rsvp{background:rgba(180,20,20,.05)'),
    # Footer
    ('#02040e', '#0a0202'),
    # Arch sky fill color
    ('#0c1848', '#2e0a0a'),
    # Architecture SVG inner sky
    ("fill='#0c1848'", "fill='#2e0a0a'"),
    ("fill=\"#0c1848\"", "fill=\"#2e0a0a\""),
    # Flap edge fill
    ('#0e1f68', '#3d0d0d'),
    # Info card hover
    ('rgba(42,72,128,0.4)', 'rgba(128,20,20,0.4)'),
    # Gallery inner
    ('rgba(42,72,128,0.4)', 'rgba(128,20,20,0.4)'),
    ('rgba(34,4,4,0.8)', 'rgba(10,2,2,0.9)'),
    # l-sky background gradient
    ('radial-gradient(ellipse at 50% 38%,#1e3580 0%,#0c1848 36%,#040815 100%)',
     'radial-gradient(ellipse at 50% 38%,#7a1818 0%,#3d0a0a 36%,#0d0202 100%)'),
    # Balloon panels (keep blue-ish for contrast on the balloon body)
    # Actually let me change it to a warm red for the balloon
    ('#1a3a70', '#8a1a1a'),
]

for old, new in replacements:
    html = html.replace(old, new)

# ─── 2. REPLACE EMOJI ICONS WITH REAL SVG ICONS ─────────────────────────────
# Calendar SVG
cal_svg = '''<svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="5" width="28" height="25" rx="3" fill="none" stroke="#d4a843" stroke-width="2"/>
  <line x1="2" y1="13" x2="30" y2="13" stroke="#d4a843" stroke-width="2"/>
  <rect x="7" y="2" width="3" height="6" rx="1.5" fill="#d4a843"/>
  <rect x="22" y="2" width="3" height="6" rx="1.5" fill="#d4a843"/>
  <rect x="7" y="17" width="4" height="4" rx="1" fill="#d4a843" opacity="0.8"/>
  <rect x="14" y="17" width="4" height="4" rx="1" fill="#d4a843" opacity="0.8"/>
  <rect x="21" y="17" width="4" height="4" rx="1" fill="#d4a843" opacity="0.8"/>
  <rect x="7" y="23" width="4" height="4" rx="1" fill="#d4a843" opacity="0.8"/>
  <rect x="14" y="23" width="4" height="4" rx="1" fill="#d4a843" opacity="0.8"/>
</svg>'''

# Clock SVG
clock_svg = '''<svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="16" cy="16" r="13" stroke="#d4a843" stroke-width="2"/>
  <line x1="16" y1="8" x2="16" y2="16" stroke="#d4a843" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="16" y1="16" x2="22" y2="20" stroke="#f0d080" stroke-width="2" stroke-linecap="round"/>
  <circle cx="16" cy="16" r="2" fill="#d4a843"/>
</svg>'''

# Venue/building SVG
venue_svg = '''<svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="4" y="12" width="24" height="18" rx="1" fill="none" stroke="#d4a843" stroke-width="2"/>
  <path d="M2 14L16 3L30 14" stroke="#d4a843" stroke-width="2" stroke-linejoin="round"/>
  <rect x="13" y="20" width="6" height="10" rx="1" fill="#d4a843" opacity="0.7"/>
  <rect x="6" y="16" width="5" height="5" rx="1" fill="#d4a843" opacity="0.5"/>
  <rect x="21" y="16" width="5" height="5" rx="1" fill="#d4a843" opacity="0.5"/>
  <line x1="4" y1="30" x2="28" y2="30" stroke="#d4a843" stroke-width="2"/>
</svg>'''

# Location pin SVG
pin_svg = '''<svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M16 2C10.477 2 6 6.477 6 12c0 7.5 10 18 10 18s10-10.5 10-18c0-5.523-4.477-10-10-10z" fill="none" stroke="#d4a843" stroke-width="2"/>
  <circle cx="16" cy="12" r="4" fill="#d4a843"/>
</svg>'''

# Replace emoji div contents for info cards
html = html.replace(
    '<div class="iicon">&#128197;</div>',
    '<div class="iicon">' + cal_svg + '</div>'
)
html = html.replace(
    '<div class="iicon">&#128374;</div>',
    '<div class="iicon">' + clock_svg + '</div>'
)
html = html.replace(
    '<div class="iicon">&#127963;</div>',
    '<div class="iicon">' + venue_svg + '</div>'
)
html = html.replace(
    '<div class="iicon">&#128205;</div>',
    '<div class="iicon">' + pin_svg + '</div>'
)

# Timeline icons — real SVGs
lamp_svg = '''<svg width="34" height="34" viewBox="0 0 34 34" fill="none" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="17" cy="28" rx="6" ry="3" fill="#d4a843" opacity="0.4"/>
  <rect x="15" y="18" width="4" height="10" rx="2" fill="#d4a843" opacity="0.7"/>
  <path d="M9 14 Q9 6 17 6 Q25 6 25 14 Q25 20 17 20 Q9 20 9 14Z" fill="#d4a843" opacity="0.85"/>
  <ellipse cx="17" cy="13" rx="4" ry="4" fill="#f0d080" opacity="0.7"/>
  <rect x="13" y="4" width="8" height="3" rx="1.5" fill="#a07828"/>
</svg>'''

flower_svg = '''<svg width="34" height="34" viewBox="0 0 34 34" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="17" cy="12" r="5" fill="#d4a843"/>
  <ellipse cx="17" cy="4" rx="3.5" ry="5" fill="#f0d080" opacity="0.8"/>
  <ellipse cx="17" cy="20" rx="3.5" ry="5" fill="#f0d080" opacity="0.8"/>
  <ellipse cx="9" cy="12" rx="5" ry="3.5" fill="#f0d080" opacity="0.8"/>
  <ellipse cx="25" cy="12" rx="5" ry="3.5" fill="#f0d080" opacity="0.8"/>
  <ellipse cx="11" cy="6" rx="3.5" ry="5" fill="#d4a843" opacity="0.7" transform="rotate(-45,11,6)"/>
  <ellipse cx="23" cy="6" rx="3.5" ry="5" fill="#d4a843" opacity="0.7" transform="rotate(45,23,6)"/>
  <ellipse cx="11" cy="18" rx="3.5" ry="5" fill="#d4a843" opacity="0.7" transform="rotate(45,11,18)"/>
  <ellipse cx="23" cy="18" rx="3.5" ry="5" fill="#d4a843" opacity="0.7" transform="rotate(-45,23,18)"/>
  <circle cx="17" cy="12" r="3" fill="#fff" opacity="0.5"/>
  <line x1="17" y1="22" x2="17" y2="30" stroke="#a07828" stroke-width="2"/>
  <path d="M12 28 Q17 26 22 28" stroke="#a07828" stroke-width="1.5" fill="none"/>
</svg>'''

mehendi_svg = '''<svg width="34" height="34" viewBox="0 0 34 34" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M8 26 Q10 10 17 6 Q24 10 26 26" fill="none" stroke="#d4a843" stroke-width="2"/>
  <path d="M11 26 Q12 14 17 10 Q22 14 23 26" fill="none" stroke="#f0d080" stroke-width="1.5"/>
  <circle cx="17" cy="6" r="2" fill="#d4a843"/>
  <path d="M14 18 Q17 14 20 18" fill="none" stroke="#d4a843" stroke-width="1.5"/>
  <ellipse cx="17" cy="27" rx="9" ry="4" fill="#d4a843" opacity="0.35"/>
  <path d="M12 22 Q14 20 17 22 Q20 20 22 22" fill="none" stroke="#f0d080" stroke-width="1"/>
</svg>'''

wedding_svg = '''<svg width="34" height="34" viewBox="0 0 34 34" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M5 14 L17 4 L29 14 L29 30 L5 30 Z" fill="none" stroke="#d4a843" stroke-width="2" stroke-linejoin="round"/>
  <rect x="13" y="20" width="8" height="10" rx="1" fill="#d4a843" opacity="0.7"/>
  <path d="M17 4 L17 2" stroke="#f0d080" stroke-width="2"/>
  <circle cx="17" cy="2" r="2" fill="#f0d080"/>
  <path d="M11 17 Q13 14 17 17 Q21 14 23 17" fill="none" stroke="#f0d080" stroke-width="1.5"/>
</svg>'''

reception_svg = '''<svg width="34" height="34" viewBox="0 0 34 34" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M5 28 L5 14 L10 10 L10 14" stroke="#d4a843" stroke-width="2" stroke-linejoin="round" fill="none"/>
  <path d="M10 14 L10 28" stroke="#d4a843" stroke-width="2"/>
  <path d="M14 14 L14 10 L20 7 L26 10 L26 14" stroke="#d4a843" stroke-width="2" stroke-linejoin="round" fill="none"/>
  <path d="M14 14 L26 14 L26 28 L14 28 Z" fill="none" stroke="#d4a843" stroke-width="2"/>
  <rect x="17" y="20" width="6" height="8" rx="1" fill="#d4a843" opacity="0.6"/>
  <ellipse cx="8" cy="9" rx="3" ry="5" fill="#f0d080" opacity="0.7"/>
  <ellipse cx="17" cy="5" rx="4" ry="3" fill="#f0d080" opacity="0.7"/>
</svg>'''

html = html.replace('<div class="tl-icon">&#129812;</div>', '<div class="tl-icon">' + lamp_svg + '</div>')
html = html.replace('<div class="tl-icon">&#127804;</div>', '<div class="tl-icon">' + flower_svg + '</div>')
html = html.replace('<div class="tl-icon">&#127912;</div>', '<div class="tl-icon">' + mehendi_svg + '</div>')
html = html.replace('<div class="tl-icon">&#128330;</div>', '<div class="tl-icon">' + wedding_svg + '</div>')
html = html.replace('<div class="tl-icon">&#127881;</div>', '<div class="tl-icon">' + reception_svg + '</div>')

# ─── 3. FIX TIMELINE ALTERNATE LEFT/RIGHT ───────────────────────────────────
old_tl = '''    <div class="tl-wrap">
      <div class="tl-item"><div class="tl-content"><div class="tl-icon">''' + lamp_svg + '''</div><div class="tl-event">Day One</div><div class="tl-title">Nichayathartham</div><div class="tl-date">April 25, 2026 &middot; 6:00 PM</div></div><div class="tl-dot"></div><div style="flex:1"></div></div>
      <div class="tl-item"><div style="flex:1"></div><div class="tl-dot"></div><div class="tl-content"><div class="tl-icon">''' + flower_svg + '''</div><div class="tl-event">Day Two &middot; Morning</div><div class="tl-title">Nalangu &amp; Haldi</div><div class="tl-date">April 26, 2026 &middot; 9:00 AM</div></div></div>
      <div class="tl-item"><div class="tl-content"><div class="tl-icon">''' + mehendi_svg + '''</div><div class="tl-event">Day Two &middot; Evening</div><div class="tl-title">Mehendi Night</div><div class="tl-date">April 26, 2026 &middot; 5:00 PM</div></div><div class="tl-dot"></div><div style="flex:1"></div></div>
      <div class="tl-item"><div style="flex:1"></div><div class="tl-dot"></div><div class="tl-content"><div class="tl-icon">''' + wedding_svg + '''</div><div class="tl-event">Day Three &middot; The Sacred Union</div><div class="tl-title">Kalyanam</div><div class="tl-date">April 28, 2026 &middot; 10:30 AM</div></div></div>
      <div class="tl-item"><div class="tl-content"><div class="tl-icon">''' + reception_svg + '''</div><div class="tl-event">Day Four</div><div class="tl-title">Grand Reception</div><div class="tl-date">April 29, 2026 &middot; 7:00 PM</div></div><div class="tl-dot"></div><div style="flex:1"></div></div>
    </div>'''

new_tl = '''    <div class="tl-wrap">
      <!-- LEFT: Day 1 -->
      <div class="tl-item tl-left">
        <div class="tl-content">
          <div class="tl-icon">''' + lamp_svg + '''</div>
          <div class="tl-event">Day One</div>
          <div class="tl-title">Nichayathartham</div>
          <div class="tl-date">April 25, 2026 &middot; 6:00 PM</div>
        </div>
        <div class="tl-dot"></div>
        <div class="tl-spacer"></div>
      </div>
      <!-- RIGHT: Day 2 Morning -->
      <div class="tl-item tl-right">
        <div class="tl-spacer"></div>
        <div class="tl-dot"></div>
        <div class="tl-content">
          <div class="tl-icon">''' + flower_svg + '''</div>
          <div class="tl-event">Day Two &middot; Morning</div>
          <div class="tl-title">Nalangu &amp; Haldi</div>
          <div class="tl-date">April 26, 2026 &middot; 9:00 AM</div>
        </div>
      </div>
      <!-- LEFT: Day 2 Evening -->
      <div class="tl-item tl-left">
        <div class="tl-content">
          <div class="tl-icon">''' + mehendi_svg + '''</div>
          <div class="tl-event">Day Two &middot; Evening</div>
          <div class="tl-title">Mehendi Night</div>
          <div class="tl-date">April 26, 2026 &middot; 5:00 PM</div>
        </div>
        <div class="tl-dot"></div>
        <div class="tl-spacer"></div>
      </div>
      <!-- RIGHT: Day 3 -->
      <div class="tl-item tl-right">
        <div class="tl-spacer"></div>
        <div class="tl-dot"></div>
        <div class="tl-content">
          <div class="tl-icon">''' + wedding_svg + '''</div>
          <div class="tl-event">Day Three &middot; The Sacred Union</div>
          <div class="tl-title">Kalyanam</div>
          <div class="tl-date">April 28, 2026 &middot; 10:30 AM</div>
        </div>
      </div>
      <!-- LEFT: Day 4 -->
      <div class="tl-item tl-left">
        <div class="tl-content">
          <div class="tl-icon">''' + reception_svg + '''</div>
          <div class="tl-event">Day Four</div>
          <div class="tl-title">Grand Reception</div>
          <div class="tl-date">April 29, 2026 &middot; 7:00 PM</div>
        </div>
        <div class="tl-dot"></div>
        <div class="tl-spacer"></div>
      </div>
    </div>'''

if old_tl in html:
    html = html.replace(old_tl, new_tl)
    print('Timeline replaced')
else:
    # Try a simpler find on just the tl-wrap section
    start = html.find('<div class="tl-wrap">')
    end = html.find('</div>\n  </section>\n\n  <section id="rsvp">')
    if start != -1 and end != -1:
        html = html[:start] + new_tl + '\n' + html[end:]
        print('Timeline replaced by index')
    else:
        print('Timeline not found, skipping')

# ─── 4. BETTER TIMELINE CSS ─────────────────────────────────────────────────
tl_css_old = '.tl-item{display:flex;align-items:center;gap:20px;margin-bottom:42px;opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s ease;}'
tl_css_new = '''.tl-item{display:flex;align-items:center;gap:20px;margin-bottom:42px;opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s ease;}
.tl-left{flex-direction:row;}
.tl-right{flex-direction:row-reverse;}
.tl-spacer{flex:1;}
.tl-left .tl-content{text-align:right;}
.tl-right .tl-content{text-align:left;}'''
html = html.replace(tl_css_old, tl_css_new)

# Remove old nth-child row-reverse rule
html = html.replace('.tl-item:nth-child(odd){flex-direction:row-reverse;}', '')
html = html.replace('.tl-item:nth-child(even) .tl-content{text-align:left;}', '')

# ─── 5. ADD "Created by Harsith G" ─────────────────────────────────────────
credit = '''
  <!-- ───── CREDIT ───── -->
  <div style="background:#0a0202;padding:28px 24px;text-align:center;border-top:1px solid rgba(212,168,67,0.08);">
    <p style="font-family:'Cinzel',serif;font-size:11px;letter-spacing:5px;color:var(--gold);opacity:0.55;text-transform:uppercase;">
      Crafted with &#10084; by &nbsp;
      <span style="color:var(--goldl);opacity:0.9;font-weight:600;letter-spacing:3px;">Harsith G</span>
    </p>
  </div>
'''
html = html.replace('</body>', credit + '</body>')

# ─── 6. Update iicon CSS for SVG sizing ─────────────────────────────────────
html = html.replace(
    '.iicon{font-size:26px;margin-bottom:12px;}',
    '.iicon{display:flex;justify-content:center;align-items:center;height:38px;margin-bottom:12px;}'
)
html = html.replace(
    '.tl-icon{font-size:24px;margin-bottom:7px;}',
    '.tl-icon{display:flex;justify-content:center;align-items:center;height:40px;margin-bottom:8px;}'
)

with open('wedding-invitation (1).html', 'w', encoding='utf-8') as f:
    f.write(html)
print('All done! Final size:', len(html)//1024, 'KB')
