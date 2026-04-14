import os
import glob
import re

def process_file(p):
    if p == "index.html":
        return

    with open(p, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content

    # 1. First, extract the links from footer-right and rebuild it
    links_match = re.search(r'<div class="footer-right">\s*(.*?)\s*</div>', content, re.DOTALL)
    if links_match and 'class="footer-links"' not in links_match.group(1):
        links = links_match.group(1)
        social_html = """
          <div class="footer-social">
            <a href="https://www.instagram.com/eonixsystems/" class="social-icon" aria-label="Instagram" target="_blank">
              <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z" />
              </svg>
            </a>
            <a href="https://www.linkedin.com/company/eonix-systems/?viewAsMember=true" class="social-icon" aria-label="LinkedIn" target="_blank">
              <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M4.98 3.5c0 1.381-1.11 2.5-2.48 2.5s-2.48-1.119-2.48-2.5c0-1.38 1.11-2.5 2.48-2.5s2.48 1.12 2.48 2.5zm.02 4.5h-5v16h5v-16zm7.982 0h-4.968v16h4.969v-8.399c0-4.67 6.029-5.052 6.029 0v8.399h4.988v-10.131c0-7.88-8.922-7.593-11.018-3.714v-2.155z" />
              </svg>
            </a>
          </div>"""

        new_footer_right = f'<div class="footer-right">\n          <div class="footer-links">\n            {links.strip()}\n          </div>\n{social_html}\n        </div>'
        content = content[:links_match.start()] + new_footer_right + content[links_match.end():]

    # 2. Remove any old `.footer-social` inside `.footer-bottom`
    footer_bottom_match = re.search(r'<div class="footer-bottom">(.*?)</footer>', content, re.DOTALL)
    if footer_bottom_match:
        bottom_content = footer_bottom_match.group(1)
        if 'class="footer-social"' in bottom_content:
            # We strip it out completely
            clean_bottom = re.sub(r'<div class="footer-social">.*?</div>', '', bottom_content, flags=re.DOTALL)
            # Remove any trailing empty div or comments if it looks weird, but let's just replace the social part.
            content = content[:footer_bottom_match.start()] + f'<div class="footer-bottom">{clean_bottom}</footer>' + content[footer_bottom_match.end():]

    # 3. Fix the "Ac 2026" text back to "© 2026"
    content = content.replace("Ac 2026", "© 2026")
    
    # 4. Remove comment completely so it does not clutter
    content = content.replace("<!-- Keep existing socials formatting -->", "")

    if content != original_content:
        with open(p, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated", p)

for p in glob.glob("*.html"):
    process_file(p)
