import xml.etree.ElementTree as ET
#Definició de la funció que crea el XML i el mostra per consola

def createXML():
    #S'utilitza la funció Element() per crear un fitxer XML i s'assigna a una variable
    #que actua com a root
    a0 = ET.Element('students')  

    #La funció SubElement() crea un child del tag pare (en aquest cas root)
    b0 = ET.SubElement(a0,'student')
    #La funció set() crea un atribut al tag que la crida
    b0.set('matriculat','NO')  
    #SubElement() crea un child del tag pare (en aquest cas student) 
    c1 = ET.SubElement(b0,'name')
    #La funció text() escriu text al tag que la crida
    c1.text = "Oriol"
    c2 = ET.SubElement(b0,'surname')
    c2.text = "Martinez"
    c3 = ET.SubElement(b0,'email')
    c3.text = "omartine@jbalmes.net"
    c4 = ET.SubElement(b0,'dni')
    c4.text = "12345678D"

    #Es creen cuatre childs més del root amb els mateixos 4 subchilds però amb valors diferents
    #S'utilitzen lesm ateixes funcions per crear i escriure els valors per conseguir l'estructura 
    #d'arbre amb etiquetes de l'XML

    #Segon child de root (root[1])
    d0 = ET.SubElement(a0,'student')
    d0.set('matriculat','NO') 
    #root[1][0] 
    e1 = ET.SubElement(d0,'name')
    e1.text = "Andreu"
    #root[1][1] 
    e2 = ET.SubElement(d0,'surname')
    e2.text = "Serrat"
    #root[1][2] 
    e3 = ET.SubElement(d0,'email')
    e3.text = "aserrat@jbalmes.net"
    #root[1][3] 
    e4 = ET.SubElement(d0,'dni')
    e4.text = "73838388D"

    #Tercer child de root (root[2])
    f0 = ET.SubElement(a0,'student') 
    f0.set('Nota','8.5') 
    #root[2][0] 
    g1 = ET.SubElement(f0,'name')
    g1.text = "Guillem"
    #root[2][1] 
    g2 = ET.SubElement(f0,'surname')
    g2.text = "Rodriguez"
    #root[2][2] 
    g3 = ET.SubElement(f0,'email')
    g3.text = "guirod@jbalmes.net"
    #root[2][3] 
    g4 = ET.SubElement(f0,'dni')
    g4.text = "55544433U"

    #Quart child de root (root[3])
    h0 = ET.SubElement(a0,'student')
    h0.set('Nota','9.2')
    #root[3][0]  
    i1 = ET.SubElement(h0,'name')
    i1.text = "Joan"
    #root[3][1] 
    i2 = ET.SubElement(h0,'surname')
    i2.text = "Colom"
    #root[3][2] 
    i3 = ET.SubElement(h0,'email')
    i3.text = "jcolom@jbalmes.net"
    #root[3][3] 
    i4 = ET.SubElement(h0,'dni')
    i4.text = "66663332P"

    #Cinquè child de root (root[4])
    j0 = ET.SubElement(a0,'student') 
    j0.set('matriculat','NO')  
    #root[4][0] 
    k1 = ET.SubElement(j0,'name')
    k1.text = "Marta"
    #root[4][1] 
    k2 = ET.SubElement(j0,'surname')
    k2.text = "Aranda"
    #root[4][2] 
    k3 = ET.SubElement(j0,'email')
    k3.text = "martaranda@jbalmes.net"
    #root[4][3] 
    k4 = ET.SubElement(j0,'dni')
    k4.text = "99933322D"
    
    #La funcio indent indenta la sportida per consola, la cridem amb la variable
    #que actua com a root
    ET.indent(a0)
    #La funcio dum imprimeix per consola
    ET.dump(a0)
    
    