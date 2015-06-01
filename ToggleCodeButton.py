from IPython.display import HTML

class NotebookObject():

    def __init__(self, code_block):
        self.code_block = code_block


    def _repr_html_(self):
        return self.code_block 

TogleCodeButton = NotebookObject('''<script>
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
