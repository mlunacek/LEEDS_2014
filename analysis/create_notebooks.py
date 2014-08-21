import subprocess
import glob
import jinja2 as jin

tmp = jin.Template("""
<tr>
  <td><a href="analysis/{{pages}}" target="_blank">{{pages}}</a></td>
  <td></td>
  <td></td>
  <td></td>
</tr>
""")

books = glob.glob('../../master/*.ipynb')

for b in books:
  cmd = 'ipython nbconvert {}'.format(b)
  pid = subprocess.Popen(cmd, shell=True)
  pid.wait()

pages = glob.glob('*.html')

for p in pages:
  print tmp.render(pages=p)
