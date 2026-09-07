import os
import asyncio
from playwright.async_api import async_playwright

async def generate_pdf():
    # Determine paths dynamically
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(current_dir, 'index.html')
    pdf_path_full = os.path.join(current_dir, 'CV.pdf')
    pdf_path_onepage = os.path.join(current_dir, 'CV-OnePage.pdf')
    
    # Check if index.html exists
    if not os.path.exists(html_path):
        print(f"Error: Could not find index.html at {html_path}")
        return
        
    file_url = f"file://{os.path.abspath(html_path)}"
    
    print("--- Starting PDF Generation ---")
    print(f"Loading local template: {file_url}")
    print(f"Output full path: {pdf_path_full}")
    print(f"Output 1-page path: {pdf_path_onepage}")
    
    async with async_playwright() as p:
        print("Launching Chromium headless browser...")
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        
        # Load the HTML document and wait for it to render
        await page.goto(file_url, wait_until="networkidle")
        
        # Optional: Add small delay for external fonts to finish drawing
        await page.wait_for_timeout(1000)
        
        # 1. Render Full Detailed CV (2 Pages)
        print("Rendering Full CV to vector PDF...")
        await page.pdf(
            path=pdf_path_full,
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            display_header_footer=False
        )
        print(f"✓ Full CV successfully generated and saved to {os.path.basename(pdf_path_full)}!")
        
        # 2. Render Condensed CV (1 Page)
        print("Applying condensed layout for 1-page CV...")
        await page.evaluate("document.body.classList.add('cv-condensed')")
        await page.wait_for_timeout(300)
        
        print("Rendering Condensed 1-Page CV to vector PDF...")
        await page.pdf(
            path=pdf_path_onepage,
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            display_header_footer=False
        )
        print(f"✓ 1-Page Condensed CV successfully generated and saved to {os.path.basename(pdf_path_onepage)}!")
        
        await browser.close()
        
    print("✓ All CV PDFs successfully generated!")

if __name__ == "__main__":
    asyncio.run(generate_pdf())
