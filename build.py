import yaml
import os

def build():
    # Load tools
    with open('tools.yaml', 'r') as f:
        tools = yaml.safe_load(f)
    
    # Generate HTML for tools
    tools_html = ""
    for tool in tools:
        # Determine button style
        button_class = "btn-tool"
        href = f'href="{tool.get("url")}" target="_blank"'
        
        if not tool.get('active', True):
            button_class += " btn-disabled"
            href = "" # No link for disabled tools
            # If it's a button element in original HTML, we should match that structure.
            # In original HTML:
            # Active tools used: <a href="..." class="btn-tool" target="_blank">Open Tool</a>
            # Inactive tools used: <button class="btn-tool btn-disabled">Coming Soon</button>
        
        # Build the card HTML
        style_attr = ' style="opacity: 0.7;"' if not tool.get('active', True) else ''
        
        tools_html += f"""            <div class="tool-card"{style_attr}>
                <h3>{tool['title']}</h3>
                <p>{tool['description']}</p>
"""
        
        if tool.get('active', True):
             tools_html += f"""                <a {href} class="{button_class}">{tool['button_text']}</a>
"""
        else:
             tools_html += f"""                <button class="{button_class}">{tool['button_text']}</button>
"""

        tools_html += """            </div>
            
"""

    # Load template
    with open('template.html', 'r') as f:
        template = f.read()
    
    # Replace placeholder
    output = template.replace('<!-- TOOLS_GRID_CONTENT -->', tools_html.strip())
    
    # Write output
    with open('index.html', 'w') as f:
        f.write(output)
    
    print("Build complete! index.html has been generated.")

if __name__ == "__main__":
    build()
