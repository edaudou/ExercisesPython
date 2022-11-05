import json
datos_json='{"nombre":"carlos","edad":23}'
datos=json.loads(datos_json)
print(datos)

with open("a.json") as fichero:
    datos=json.load(fichero)
    print(datos)
fichero.close

fichero=open("b.json","w")
json.dump(datos_json,fichero)
