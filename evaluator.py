from lark import Transformer, v_args
import sys

@v_args(inline=True)
class Evaluador(Transformer):

    def start(self, expr):
        return expr
    
    def expr(self, operation):
        return operation
    
    def operation(self, op, filename):
       print(op.get("taskname"))
       print(op.get("taskproperties"))
       file = filename.children[0].value
       print(file)
       return op

    def extract(self, action, props):
       # Obtenemos lo que queremos obtener
       taskname = action.children[0].value
       # Obtenemos las propiedades  que eso que queremos obtener
       taskproperties = self.build_props_dict(props)
       return { 'taskname': taskname, 'taskproperties' : taskproperties}
    
    def generate(self, action, props):
        taskname = action.children[0].value
        taskproperties = self.build_props_dict(props)
        print(taskproperties.get('contains', None))

        lang_to = taskproperties.get('lang_to', None)
        lang_from = taskproperties.get('lang_from', None)
        audio = taskproperties.get('format', None)
        print(lang_to, lang_from, audio)
        if not(lang_to or lang_from) and audio:
            return SyntaxError("No se puede hacer una traduccion sin especificar en que idioma esta el archivo, y sin especificar el idioma a traducir")
        
        return { 'taskname': taskname, 'taskproperties' : taskproperties}

    

    def build_props_dict(self, props):
        properties = {}
        for propiertie in props.children:
            key = propiertie.children[0].value
            value = propiertie.children[1].value
            properties[key] = value

        return properties    