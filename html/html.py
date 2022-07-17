import codecs, webbrowser
# to open/create a new html file in the write mode
f = open('index.html', 'w')
  
nombre="Gabriel"
numeroCliente="450066"
DNI="2947744"
direccion="tu casita 12345"
# the html code which will go in the file GFG.html
html_template = f"""
<html>
    <head>
        <title>Title</title>
        <link rel="stylesheet" href="/html/style.css">
    </head>
    <body>
        <h1></h1>
        <div>{nombre}</div>
        <div>{numeroCliente}</div>
        <div>{DNI}</div>
        <div>{direccion}
        <table>
        <tr><td>Fecha</td><td>Tipo</td><td>Estado</td><td>Monto</td><td>Razon</td></tr>
        <tr><td></td><td></td><td></td><td></td><td></td></tr>
        </table>
    </body>
</html>
"""
  
# writing the code into the file
f.write(html_template)
# open html file
webbrowser.open('index.html') 