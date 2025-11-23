#!/usr/bin/env python3

from json import loads

TEMPLATE = '''
graph G {
    layout=twopi;
    overlap=false;

%s

%s
}
'''

def detail(_id, source):
    name = source['members'][_id]['name']
    return '    %s [shape=box, color=blue, label="%s", href="#%s"];' % (_id, name, _id)

def relationship(_id, associate, relationship):
    return '    %s -- %s [label="%s"];' % (_id, associate, relationship)

def generate(relationships, members, source):
    _id = members[0]
    content = TEMPLATE % (
        '\n'.join([detail(x, source) for x in members]),
        '\n'.join([relationship(_id, k, v) for k, v in relationships.items()])
    )
    open('tree-%s.dot' % _id, 'w').write(content)
    

def process(member, source):
    relationships = source['relationships'][member]
    members = [member] + list(relationships.keys())
    generate(relationships, members, source)




source = loads(open('src/family-tree.json').read())
for member in source['members']:
    process(member, source)