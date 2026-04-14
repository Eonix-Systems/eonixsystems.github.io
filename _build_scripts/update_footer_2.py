import os
import glob
import re

pattern = re.compile(
    r'(<div class="footer-right">\s*)(.*?)(\s*</div>\s*</div>\s*<div class="footer-bottom">\s*<p>© 2026 Eonix Systems Pvt\. Ltd\. All rights reserved\.</p>\s*)(<div class="footer-social">.*?</div>\s*</div>)',
    re.DOTALL
)

def process_file(p):
    with open(p, "r", encoding="utf-8") as f:
        content = f.read()

    match = pattern.search(content)
    if match:
        links_content = match.group(2)
        social_content = match.group(4)
        
        # Remove the closing </div> of footer-bottom from social_content to place it correctly
        social_content_stripped_end_div = re.sub(r'\s*</div>$', '', social_content).strip()

        replacement = (
            f'<div class="footer-right">\n'
            f'        <div class="footer-links">\n'
            f'          {links_content.strip()}\n'
            f'        </div>\n'
            f'        {social_content_stripped_end_div}\n'
            f'      </div>\n'
            f'    </div>\n'
            f'    <div class="footer-bottom">\n'
            f'      <p>© 2026 Eonix Systems Pvt. Ltd. All rights reserved.</p>\n'
            f'    </div>'
        )

        new_content = content[:match.start()] + replacement + content[match.end():]
        with open(p, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Updated", p)
    else:
        print("Not matched in", p)

for p in glob.glob("*.html"):
    if p != "index.html":
        process_file(p)
