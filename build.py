import yaml
import os

def build():
    # Load tools
    with open('tools.yaml', 'r') as f:
        tools = yaml.safe_load(f)
    
    # Generate HTML for tools
    tools_html = ""
    for tool in tools:
        # Build the card HTML
        style_attr = ' style="opacity: 0.7;"' if not tool.get('active', True) else ''
        
        tools_html += f"""            <div class="tool-card"{style_attr}>
                <h3>{tool['title']}</h3>
                <p>{tool['description']}</p>
"""
        
        if tool.get('active', True):
            # Create button container if there are multiple buttons
            has_url = tool.get('url')
            has_github = tool.get('github')
            
            if has_url or has_github:
                tools_html += f"""                <div class="button-group">
"""
                
                # Add main tool button if URL exists
                if has_url:
                    tools_html += f"""                    <a href="{has_url}" class="btn-tool" target="_blank">{tool['button_text']}</a>
"""
                
                # Add GitHub button if GitHub link exists (always use dark style)
                if has_github:
                    github_text = "View on GitHub" if has_url else tool['button_text']
                    tools_html += f"""                    <a href="{has_github}" class="btn-github" target="_blank">{github_text}</a>
"""
                
                tools_html += f"""                </div>
"""
        else:
            tools_html += f"""                <button class="btn-tool btn-disabled">{tool['button_text']}</button>
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
