import os

file_path = 'index.html.html'
if not os.path.exists(file_path):
    file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Diorama SVG aspect ratios and classes to fill portrait mobile screens elegantly
# Arch SVG: change height auto -> 100vh for mobile
html = html.replace(
    '''<svg viewBox="0 0 1440 800" preserveAspectRatio="xMidYMax meet"
           style="position:absolute;bottom:0;left:0;width:100%;height:auto;" xmlns="http://www.w3.org/2000/svg">''',
    '''<svg viewBox="0 0 1440 800" class="svg-arch" preserveAspectRatio="xMidYMax slice"
           style="position:absolute;bottom:0;left:0;width:100%;height:100vh;" xmlns="http://www.w3.org/2000/svg">'''
)

# Front waves SVG: make height 35vh on mobile so it doesn't stretch too much, or use slice
html = html.replace(
    '''<svg viewBox="0 0 1440 270" preserveAspectRatio="none" width="100%"
           style="position:absolute;bottom:0;left:0;" xmlns="http://www.w3.org/2000/svg">''',
    '''<svg viewBox="0 0 1440 270" class="svg-waves" preserveAspectRatio="none" style="position:absolute;bottom:0;left:0;width:100%;" xmlns="http://www.w3.org/2000/svg">'''
)

# Flap edge SVG:
html = html.replace(
    '''<svg viewBox="0 0 1440 172" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">''',
    '''<svg viewBox="0 0 1440 172" class="svg-flap" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">'''
)

# 2. Add explicit mobile CSS media queries
mobile_css = '''
/* --- MOBILE OPTIMIZATIONS --- */
.svg-waves { height: 35vh; }
.svg-flap { height: 16vh; }

@media(max-width: 768px) {
  /* Diorama Portrait Scaling */
  .svg-arch { preserveAspectRatio: "xMidYMax slice"; }
  .n-main { font-size: 16vw !important; line-height: 1.1; margin-top: 10px; }
  .n-blessing { font-size: 3.2vw; margin-bottom: 5px; padding: 0 20px; }
  .flap-top h1 { font-size: 15vw !important; line-height: 1.1; margin-top: 5px; }
  .flap-top .fb { font-size: 3.2vw; margin-bottom: 5px; padding: 0 10px; }
  
  /* Timeline fixes for mobile (cards take full width) */
  .tl-wrap { margin-top: 40px; }
  .tl-wrap::before { left: 24px; opacity: 0.5; }
  .tl-item { grid-template-columns: 48px 1fr !important; gap: 0 !important; margin-bottom: 30px !important; }
  .tl-dot { grid-column: 1; margin-left:16px; width: 14px; height: 14px; }
  .tl-card-left, .tl-card-right { 
    grid-column: 2; margin: 0 !important; padding: 20px 18px !important; text-align: left !important;
  }
  .tl-card-left .tl-icon, .tl-card-right .tl-icon { justify-content: flex-start !important; }
  .tl-empty { display: none; }
  
  /* Sections padding */
  section { padding: 60px 16px !important; }
  #details { padding-top: 100px !important; }
  .sec-title { font-size: 11vw !important; }
  
  /* Below section Names */
  .fn { font-size: 10vw !important; }
  
  /* Button size */
  .rsvp-btn { padding: 14px 28px !important; width: 100%; box-sizing: border-box; }
}

@media(min-width: 769px) {
  .svg-waves { height: 270px; }
  .svg-flap { height: 172px; }
}
'''

# Inject mobile CSS right before closing </style>
html = html.replace('</style>', mobile_css + '\n</style>', 1)

# Ensure viewport meta is correct
if 'viewport-fit=cover' not in html:
    html = html.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">'
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Optimized for mobile. Final size:', len(html)//1024, 'KB')
