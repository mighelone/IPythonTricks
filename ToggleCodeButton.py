from IPython.display import HTML

class NotebookObject():

    def __init__(self, code_block):
        self.code_block = code_block


    def _repr_html_(self):
        return self.code_block

ToggleCodeButton = NotebookObject('''<script>
code_show=false;
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
}
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input type="submit" value="Click here to toggle on/off the raw code."></form>''')

EnableEquationNumbers = NotebookObject(""" <script type="text/Javascript"> MathJax.Hub.Config({ TeX: { equationNumbers: { autoNumber: "AMS", useLabelIds: true } }});
</script>""")

class DictTable(dict):
    # Overridden dict class which takes a dict in the form {'a': 2, 'b': 3},
    # and renders an HTML Table in IPython Notebook.

    def __init__(self, d, name=None, caption=None):

        self.d = d
        self.name = name
        self.caption = caption

    def __getattr__(self, item):
        return self.d[item]

    def _repr_html_(self):
        html = ["<table >"]
        if self.caption:
            html.append("<caption>{}</caption>".format(self.caption))
        if self.name: # append a head
            html.append("<tr>")
            html.append("<th> </td>")
            html.append("<th>{}</td>".format(self.name))
            html.append("</tr>")
        for key, value in self.d.iteritems():
            html.append("<tr>")
            html.append("<td>{0}</td>".format(key))
            html.append("<td>{:.4}</td>".format(value))
            html.append("</tr>")
        html.append("</table>")
        return ''.join(html)

def below(*pargs):
    """ takes n html renderable objects and places 
        them below each other """
    
    return ' '.join(pargs) 

class DictValueTable(dict):
    # Overridden dict class which takes a dict in the form {'a': {'val':'foo',
    #                                                             'label':'foo [b]'
    #                                                        },
    # and renders an HTML Table in IPython Notebook.
    value_format = "{:.4}"

    def __getattr__(self, item):
        return self[item]['val']

    def set(self, item, value):
        d = {k: v for k, v in self.iteritems()}
        i = {'val': value, 'label': self[item]['label']}
        d[item] = i
        return DictValueTable(d)

    def _repr_html_(self):
        html = ["<table >"]
        for key, subdict in self.iteritems():
            dis = subdict['label']
            val = subdict['val']
            html.append("<tr>")
            html.append("<td>{0}</td>".format(dis))
            value = "<td>" + self.value_format + "</td>"
            html.append(value.format(float(val)))
            html.append("</tr>")
        html.append("</table>")
        return ''.join(html)
