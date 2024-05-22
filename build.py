import settings
import os

if settings.debug: print(f"\n  {settings.app_name} - Ready\n")

class HTML:
  def __init__(self):
    self.html = ""

  def resourceImport(self, path):
    resource = ""
    if ".js" in path:
      resource = "".join(["<script>", open(path, "r").read(), "</script>"])
      if settings.debug: print("".join(["  [i] ", path]))
    elif ".css" in path:
      resource = "".join(["<style>", open(path, "r").read(), "</style>"])
      if settings.debug: print("".join(["  [i] ", path]))
    elif ".html" in path:
      resource = open(path, "r").read()
      if settings.debug: print("".join(["  [i] ", path]))
    else:
      resource = "".join(["<h3>Import went wrong for: ", path, "</h3>"])
      if settings.debug: print("".join(["  [!] Import went wrong for: ", path]))
    self.html = self.html + resource
  
  def getBody(self):
    return self.html

  def export(self):
    # Export to html file
    if settings.export_html:
      with open("bin/app.html", "w") as html_export:
        html_export.write(self.html)
    
    # Get wrapper code
    with open('resources/wrapper.pyw','r') as wrap_source:
      wrapper = wrap_source.read()
    
    # Inject settings into wrapper code
    if settings.debug: print("")
    settings_to_inject = [
      [r"{settings.app_name}", str(settings.app_name)],
      [r"{settings.app_proportions[0]}", str(settings.app_proportions[0])],
      [r"{settings.app_proportions[1]}", str(settings.app_proportions[1])],
      [r"{settings.app_resizable}", str(settings.app_resizable)],
      [r"{settings.app_confirm_close}", str(settings.app_confirm_close)],
      [r"{settings.app_allow_inspect}", str(settings.app_allow_inspect)],
      [r"{settings.app_frameless}", str(settings.app_frameless)],
      [r"{settings.app_fullscreen}", str(settings.app_fullscreen)],
      [r"{settings.app_web_engine}", str(settings.app_web_engine)]
    ]
    for string,setting in settings_to_inject:
      wrapper = wrapper.replace(string, setting)
      if settings.debug: print("".join(["  [i] ", string.replace("{","").replace("}", ""), ": ", setting]))

    # Inject resources into wrapper code
    wrapper = wrapper.replace("#!FLAG-HTML", "".join(["html = r'''", self.html, "'''"]))
    if settings.debug: print("  [i] Injected resources")

    # Export result
    with open("".join(["bin/", settings.file_name]), "w") as pywebview_export:
      pywebview_export.write(wrapper)
    
    if settings.debug: print("\n  [+] Exported")

if __name__ == '__main__':
  html = HTML()
  for resource in settings.resources:
    html.resourceImport(resource)
  html.export()

  if settings.preview:
    os.chdir("bin")
    os.startfile(settings.file_name)