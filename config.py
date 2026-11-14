import json

with open("config.json", "r", encoding="utf-8") as archivo:
    _datos = json.load(archivo)


firstColorGradient = _datos["firstColorGradient"]
secondColorGradient = _datos["secondColorGradient"]
gradientSpeed = _datos["gradientSpeed"]
