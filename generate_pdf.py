import os
import asyncio
from playwright.async_api import async_playwright

async def generate_pdf():
    # Determine paths dynamically
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(current_dir, 'index.html')
    pdf_path = os.path.join(current_dir, 'CV.pdf')
    
    # Check if index.html exists
    if not os.path.exists(html_path):
        print(f"Error: Could not find index.html at {html_path}")
        return
        
    file_url = f"file://{os.path.abspath(html_path)}"
    
    print("--- Starting PDF Generation ---")
    print(f"Loading local template: {file_url}")
    print(f"Output path: {pdf_path}")
    
    async with async_playwright() as p:
        print("Launching Chromium headless browser...")
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        
        # Load the HTML document and wait for it to render
        await page.goto(file_url, wait_until="networkidle")
        
        # Optional: Add small delay for external fonts to finish drawing
        await page.wait_for_timeout(1000)
        
        print("Rendering print media to vector PDF...")
        # Save to PDF with styling variables matching the style.css printer directives
        await page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            margin={
                "top": "0.4in",
                "right": "0.4in",
                "bottom": "0.4in",
                "left": "0.4in"
            },
            display_header_footer=False
        )
        
        await browser.close()
        
    print("✓ PDF successfully generated and saved to CV.pdf!")

if __name__ == "__main__":
    asyncio.run(generate_pdf())
