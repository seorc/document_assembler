# -*- coding: utf-8 -*-
import os
import markdown
from jinja2 import Environment, PackageLoader
import yaml

class MDPretifier(object):

    def __init__(self, project_root='markdwon'):
        self.project_root = project_root
        stream = file(os.path.join(project_root, 'map.yaml'), 'r')
        self.map = yaml.load(stream)
        self.template = self.map.get('template', {'dir': 'templates', 'use': 'main.html'})

    def go(self):

        env = Environment(loader=PackageLoader(self.project_root, self.template['dir']))

        refs = []
        for ref in self.map['refs']:
            refs.append('[{tag}]: {url} "{title}"'.format(**ref))

        ref_list = "\n".join(refs)

        htmls = []
        for sect in self.map['sections']:
            in_file = open(os.path.join(os.path.abspath(self.project_root), sect), 'r')

            md = in_file.read().decode('utf8')
            htmls.append(markdown.markdown(md + "\n" + ref_list))

        tpl = env.get_template(self.template['use'])
        html = "\n".join(htmls)

        out = tpl.render(content=html, **self.map)
        out_file = open(os.path.join(self.project_root, self.map['output']), 'w')
        out_file.write(out.encode('utf8'))

        in_file.close()
        out_file.close()
