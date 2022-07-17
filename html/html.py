import codecs, webbrowser
# to open/create a new html file in the write mode
f = open('index.html', 'w')
  
nombre="Gabriel, Moreno"
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
        <h1>{nombre}</h1>
        <div>Numero de Cliente: {numeroCliente}</div>
        <div>Dni: {DNI}</div>
        <div>Direccion: {direccion}</div>
        <table>
        <tr><td>Fecha</td><td>Tipo</td><td>Estado</td><td>Monto</td><td>Razon</td></tr>
        <tr><td>a</td><td>aaaaaaaaaaaaaaaaaaaa</td><td>aaaaaaaaaaa</td><td>aaaaaaaaaaa</td><td>aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa</td></tr>
        <tr><td>b</td><td></td><td></td><td></td><td>b</td></tr>
        <tr><td>c</td><td></td><td></td><td></td><td>c</td></tr>
        
        </table>
    </body>
</html>
"""
  
# writing the code into the file
f.write(html_template)
# open html file
webbrowser.open('index.html') 