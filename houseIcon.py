import os

# Folder containing your HTML files
folder_path = r"C:\Users\Juan\Desktop\Github\TFM_Barrios\mapas_interactivos"

# Code snippet to insert
home_button_html = """
<style>
    .home-icon {
      position: absolute;
      top: 1rem;
      right: 1rem;
      z-index: 10000;
    }
    .home-img {
      top: 10px;
      right: 10px;
      width: 42px;
      height: 42px;
      transition: transform 0.3s ease;
    }
    .home-img:hover {
      transform: scale(1.1);
    }
</style>

<div class="home-icon">
  <a href="https://yokuta.github.io/TFM_Barrios/index.html" title="Inicio">
    <img src="https://yokuta.github.io/imagenes/housee.png" alt="Inicio" class="home-img">
  </a>
</div>
"""

# Loop through all HTML files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".html"):
        file_path = os.path.join(folder_path, filename)

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Avoid duplicating the snippet if it already exists
        if "home-icon" not in content:
            content = content.replace("<body>", "<body>\n" + home_button_html)

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)

print("✅ Home button successfully added to all HTML files.")
