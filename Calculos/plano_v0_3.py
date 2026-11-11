"""Plano CAD FV-01/FV-02 para el TFM UNIR, v0.3.

Ejecutar: python Calculos/plano_v0_3.py
Requiere ezdxf, reportlab, pypdfium2. DXF en milímetros, modelo 1:1.
Las láminas se trazan a 1:50 en A3. FV-02 es un esquema sin escala física.
"""
import json,math,sys
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import pypdfium2 as pdfium

ROOT=Path(__file__).resolve().parents[1]
LIBS=ROOT/".tfm-build-v03"/"cadlibs"
if LIBS.exists():
    sys.path.insert(0,str(LIBS))
import ezdxf
from ezdxf.enums import TextEntityAlignment

X=json.loads((ROOT/"Calculos"/"Resultados_v0.3.json").read_text(encoding="utf-8"))
OUT=ROOT/"Planos"
OUT.mkdir(exist_ok=True)
SCALE=50
W,H=21000,14850
COLORS={"BASE":("#17384c",7),"MODULOS":("#176a96",5),"RAILES":("#687c85",8),
        "CC":("#b54934",1),"CA":("#145f91",5),"PE":("#287558",3),
        "COTAS":("#344d5a",7),"TEXTO":("#162b37",7),"CONTROL":("#aa6c21",30)}
pdfmetrics.registerFont(TTFont("Calibri","C:/Windows/Fonts/calibri.ttf"))
pdfmetrics.registerFont(TTFont("CalibriB","C:/Windows/Fonts/calibrib.ttf"))

class Scene:
    def __init__(self):
        self.entities=[]
    def line(self,x1,y1,x2,y2,layer="BASE",width=15):
        self.entities.append(("line",(x1,y1,x2,y2),layer,width))
    def rect(self,x,y,w,h,layer="BASE",width=15):
        self.entities.append(("poly",[(x,y),(x+w,y),(x+w,y+h),(x,y+h),(x,y)],layer,width))
    def circle(self,x,y,r,layer="BASE",width=15):
        self.entities.append(("circle",(x,y,r),layer,width))
    def text(self,x,y,text,size=135,layer="TEXTO",bold=False,align="left"):
        self.entities.append(("text",(x,y,str(text),size,bold,align),layer,15))
    def arrow(self,x1,y1,x2,y2,layer="COTAS",head=105):
        self.line(x1,y1,x2,y2,layer)
        t=math.atan2(y2-y1,x2-x1)
        for a in (t+.42,t-.42):
            self.line(x2,y2,x2-head*math.cos(a),y2-head*math.sin(a),layer)
    def dimension(self,x1,y1,x2,y2,offset,text):
        if abs(y1-y2)<1:
            yy=y1+offset
            self.line(x1,y1,x1,yy+100,"COTAS")
            self.line(x2,y2,x2,yy+100,"COTAS")
            self.arrow(x1,yy,x2,yy);self.arrow(x2,yy,x1,yy)
            self.text((x1+x2)/2,yy+120,text,200,"COTAS",align="center")
        else:
            xx=x1+offset
            self.line(x1,y1,xx-100,y1,"COTAS")
            self.line(x2,y2,xx-100,y2,"COTAS")
            self.arrow(xx,y1,xx,y2);self.arrow(xx,y2,xx,y1)
            self.text(xx-120,(y1+y2)/2,text,200,"COTAS",align="right")

def frame(s,number,title,scale):
    s.rect(500,500,W-1000,H-1000,width=25)
    s.line(500,2250,W-500,2250)
    s.line(12500,500,12500,2250)
    s.line(16200,500,16200,2250)
    s.text(850,1820,"UNIR · Máster Universitario en Energías Renovables",160,bold=True)
    s.text(850,1470,"Autoconsumo fotovoltaico de vivienda en Ciudad del Este",160)
    s.text(850,1080,title,190,bold=True)
    s.text(850,710,"Clara María De Los Ángeles Rolón Duré · Entrega v0.3",145)
    s.text(12800,1810,"INGENIERÍA DE DISEÑO",160,bold=True)
    s.text(12800,1460,"Unidad del modelo  mm",150)
    s.text(12800,1110,"Cotas expresadas en metros",150)
    s.text(12800,760,"Ubicación exacta reservada",150)
    s.text(16600,1710,number,350,bold=True)
    s.text(16600,1210,"Escala "+scale,180)
    s.text(16600,800,"Lámina "+("1 de 2" if number=="FV-01" else "2 de 2"),160)

def roof_plan():
    s=Scene();frame(s,"FV-01","Implantación, anclajes y sección de cubierta","1:50 en A3")
    ox,oy=2200,2700
    def xx(x):return ox+x*1000
    def yy(y):return oy+y*1000
    s.rect(ox,oy,5060,9180,width=25)
    # El norte del faldón es la parte superior del esquema.
    depth=2.279*math.cos(math.atan(.30));short=1.134*math.cos(math.atan(.30))
    y=X["roof"]["end_margin"]
    frames=[];rows=[]
    for j in range(3):
        if j==2:
            s.rect(xx(1.20),yy(9.18-y-.60),3442,600,"PE")
            y+=.60
        top=y; y+=depth
        row=[]
        numbers=([1,2,3],[6,5,4],[7,8,9])[j]
        for k,n in enumerate(numbers):
            x=1.20+k*1.154
            row.append((x,9.18-y,1.134,depth,n))
        frames.extend(row);rows.append((1.20,9.18-y,3.442,depth))
        if j in (0,2):y+=.02
    frames.append((1.20,9.18-y-short,2.279,short,10))
    rows.append((1.20,9.18-y-short,2.279,short))
    for x,y,w,h in rows:
        for ratio in (.25,.75):
            rail_y=yy(y+h*ratio)
            s.line(xx(x-.10),rail_y,xx(x+w+.10),rail_y,"RAILES",25)
            anchors=4 if w>3 else 3
            for a in range(anchors):
                ax=x-.10+.15+(w-.10)*a/(anchors-1)
                s.circle(xx(ax),rail_y,30,"RAILES")
    s.rect(xx(.30),yy(.25),800,8680,"PE")
    s.text(xx(.70),yy(7.90),"PASO",125,"PE",align="center")
    s.text(xx(.70),yy(7.65),"0,80 m",125,"PE",align="center")
    pts={}
    for x,y,w,h,n in frames:
        s.rect(xx(x),yy(y),w*1000,h*1000,"MODULOS",20)
        for r in (.25,.5,.75):
            s.line(xx(x),yy(y+h*r),xx(x+w),yy(y+h*r),"MODULOS",5)
        s.text(xx(x+w/2),yy(y+h/2),f"M{n:02d}",200,"MODULOS",True,"center")
        pts[n]=(xx(x+w/2),yy(y+h/2))
    for n in range(1,10):
        s.line(*pts[n],*pts[n+1],"CC",12)
    s.text(xx(3.00),yy(4.15),"0,60 m",130,"PE",align="center")
    # Recorrido de CC desde la cubierta a la bajada.
    s.line(*pts[10],xx(.35),yy(.40),"CC",15)
    s.circle(xx(.35),yy(.40),70,"CC")
    s.text(xx(.35),yy(.02),"Bajada CC",105,"CC")
    s.dimension(ox,oy+9180,ox+5060,oy+9180,500,"5,06 m")
    s.dimension(ox,oy,ox,oy+9180,-650,"9,18 m")
    angle=math.radians(-1.66)
    nx,ny=8700,11000
    s.arrow(nx,ny,nx+900*math.sin(angle),ny+900*math.cos(angle),head=180)
    s.text(nx-25,12200,"N",240,align="center",bold=True)
    s.text(10100,12830,"10 × 550 Wp = 5,50 kWp · 1 cadena en PV1",190,bold=True)
    s.text(10100,12480,"Módulo de proyecto  2.279 × 1.134 mm",165)
    s.text(10100,12140,"Pendiente  30 % · β = 16,70° · rumbo alero 91,66°",155)
    s.text(10100,11800,"Franja disponible  5,06 × 9,18 m en planta",155)
    s.text(10100,11460,"Superficie de módulos  25,84 m² · proyección 24,75 m²",155)
    s.text(10100,10980,"LEYENDA DE IMPLANTACIÓN",170,bold=True)
    for j,(label,layer) in enumerate((("M01–M10  módulos y conexión de cadena","MODULOS"),
                                    ("Rieles y puntos de anclaje de diseño","RAILES"),
                                    ("Bandas reservadas para servicio","PE"),
                                    ("Recorrido de CC y punto de bajada","CC"))):
        yy0=10550-j*350
        s.line(10100,yy0+40,10600,yy0+40,layer,25)
        s.text(10800,yy0,label,145,layer)
    s.text(10100,8700,"Sección A–A en el sentido de la pendiente",170,bold=True)
    x0,y0=10100,4500
    endx,endy=x0+9180,y0+2754
    s.line(x0,y0,endx,endy,"BASE",25)
    s.line(x0,y0-100,endx,endy-100,"BASE",12)
    for x,y,w,h,n in frames:
        # En esta sección se proyecta la longitud del módulo sobre la pendiente.
        if n not in (1,6,7,10):continue
        z1=9.18-(y+h);z2=9.18-y
        s.line(x0+z1*1000,y0+z1*300+120,x0+z2*1000,y0+z2*300+120,"MODULOS",35)
    s.dimension(x0,y0,x0+9180,y0,-400,"9,18 m en proyección horizontal")
    s.text(10500,7900,"La sección muestra la pendiente y el montaje coplanar.",150)
    s.text(10500,7580,"Anclajes a estructura resistente y remates según replanteo.",150)
    notes=[
        "Ocho tramos de riel. Compra de referencia  8 perfiles RS-327 de 4,80 m.",
        "Cantidad de diseño  30 anclajes, 16 grapas finales y 12 intermedias.",
        "Aplicar la ficha Romagnole y verificar el soporte real y el viento NP 196.",
        "Ruta CC de cálculo  25 m de ida. Cable solar Cu 6 mm² por polo.",
        "La localización de la bajada se ajusta en el replanteo de obra.",
    ]
    for i,n in enumerate(notes):s.text(10100,3900-i*270,n,135)
    return s

def electric():
    s=Scene();frame(s,"FV-02","Esquema unifilar, conductores, protecciones y control","S/E")
    def box(x,y,w,h,title,sub,layer="BASE"):
        s.rect(x,y,w,h,layer,20)
        s.text(x+w/2,y+h-350,title,205,layer,True,"center")
        for i,txt in enumerate(sub):
            s.text(x+w/2,y+h-700-i*245,txt,160,layer,False,"center")
    box(1000,10900,2600,1700,"RED ANDE",["380/220 V · 50 Hz","3F + N"],"CA")
    box(4200,10900,2900,1700,"MEDIDA Y PCC",["Contador de facturación","Sensor DTSU666-H","TC de cada fase"],"CA")
    box(7900,10900,3600,1700,"TABLERO PRINCIPAL",["Punto de conexión FV","Protección general existente","a verificar en tablero"],"CA")
    box(15400,10900,4300,1700,"CARGAS DE VIVIENDA",["3F + N + PE","Reparto de diseño  38/33/29 %"],"CA")
    for x1,x2 in ((3600,4200),(7100,7900),(11500,15400)):s.line(x1,11750,x2,11750,"CA",30)
    s.text(12900,12000,"Suministro a cargas",160,"CA",align="center")
    box(1000,6100,3400,1900,"GENERADOR FV",["10 × YHP550W","Una cadena en serie","501 V Voc STC"],"CC")
    box(5100,6100,3400,1900,"SECCIONAMIENTO CC",["QCC  ≥ 600 V CC / 25 A","DPS FV tipo 2","Ucpv ≥ 600 V"],"CC")
    box(9400,6100,4200,1900,"INV1 · HUAWEI M1",["SUN2000-5KTL-M1","Corriente alta  13,5/19,5 A","5 kW · 380/220 V"],"CA")
    box(14700,6100,4900,1900,"RAMA CA FV",["QAC  16 A · 3F + corte N","ID  tipo A · 100 mA · 4P","DPS tipo 2 para TT"],"CA")
    s.line(4400,7050,5100,7050,"CC",25)
    s.text(4750,8340,"CC  25 m de ida",155,"CC",align="center")
    s.line(8500,7050,9400,7050,"CC",25)
    s.text(6900,5640,"2 × 6 mm² Cu · H1Z2Z2-K",170,"CC",align="center")
    s.line(13600,7050,14700,7050,"CA",25)
    s.line(17150,8000,17150,9910,"CA",25)
    s.line(17150,9910,9700,9910,"CA",25)
    s.line(9700,9910,9700,10900,"CA",25)
    s.text(13700,10180,"CA  20 m · 5G4 mm² Cu · 8,5 A de cálculo",170,"CA",align="center")
    # Enlace de medida y control de un solo inversor con Dongle.
    s.line(5650,10900,5650,9080,"CONTROL",15)
    s.line(5650,9080,11300,9080,"CONTROL",15)
    s.line(11300,9080,11300,8000,"CONTROL",15)
    s.text(8450,9320,"RS-485 + SDongleA-05 · límite por fase",165,"CONTROL",align="center")
    # Barra de protección sin seccionamiento.
    s.line(1000,4570,19400,4570,"PE",30)
    for x,y in ((2700,6100),(6800,6100),(11500,6100),(17150,6100),(8900,10900)):
        s.line(x,y,x,4570,"PE",15)
    s.text(1000,4200,"BARRA PE  · equipotencialidad de marcos, rieles, inversor y tableros",170,"PE",True)
    s.line(3100,4570,3100,3630,"PE",20)
    s.line(2800,3630,3400,3630,"PE",20)
    s.line(2870,3510,3330,3510,"PE",20)
    s.line(2950,3390,3250,3390,"PE",20)
    s.text(3600,3550,"Electrodo TT  · objetivo RA ≤ 10 Ω",155,"PE")
    s.text(9000,3860,"Ajustes de red, poder de corte y tierra según ANDE y ensayo.",155)
    s.text(9000,3550,"Habilitar estado seguro a 0 % ante pérdida de medida.",155)
    s.text(9000,3240,"Conservar la separación N–PE en el esquema TT del usuario.",155)
    s.text(1000,2700,"Esquema de diseño. Los equipos CC permanecen energizados bajo irradiación.",150)
    return s

def render(scene,pdf):
    k=mm/SCALE
    for kind,data,layer,width in scene.entities:
        color=COLORS[layer][0]
        pdf.setStrokeColor(color);pdf.setFillColor(color)
        pdf.setLineWidth(max(.35,width*k))
        if kind=="line":
            pdf.line(*(v*k for v in data))
        elif kind=="poly":
            p=pdf.beginPath();p.moveTo(data[0][0]*k,data[0][1]*k)
            for x,y in data[1:]:p.lineTo(x*k,y*k)
            pdf.drawPath(p)
        elif kind=="circle":
            x,y,r=data;pdf.circle(x*k,y*k,r*k,stroke=1,fill=0)
        else:
            x,y,txt,size,bold,align=data
            pdf.setFont("CalibriB" if bold else "Calibri",size*k)
            getattr(pdf,{"left":"drawString","center":"drawCentredString","right":"drawRightString"}[align])(x*k,y*k,txt)

def memoria(root):
    from PIL import Image, ImageDraw, ImageFont
    im=Image.new("RGB",(1420,680),"white")
    d=ImageDraw.Draw(im)
    def f(n,b=False):return ImageFont.truetype("C:/Windows/Fonts/"+("calibrib.ttf" if b else "calibri.ttf"),n)
    blue="#176a96";navy="#17384c";green="#287558";orange="#a56a20";red="#b54934"
    def box(x,y,w,h,title,lines,col):
        d.rounded_rectangle((x,y,x+w,y+h),radius=9,fill="#f4f8fa",outline=col,width=3)
        d.text((x+w/2,y+14),title,font=f(29,True),fill=col,anchor="ma")
        for i,t in enumerate(lines):d.text((x+w/2,y+58+i*32),t,font=f(26),fill=navy,anchor="ma")
    def line(x1,y1,x2,y2,col):d.line((x1,y1,x2,y2),fill=col,width=4)
    box(25,25,350,132,"RED Y MEDIDA",["ANDE · 380/220 V, 50 Hz","DTSU666-H · 3 fases"],blue)
    box(540,25,355,132,"TABLERO DE VIVIENDA",["Punto de conexión FV","Derivación a las cargas"],blue)
    box(1060,25,335,132,"CARGAS",["Demanda por fase","Diseño 38/33/29 %"],blue)
    line(375,92,540,92,blue);line(895,92,1060,92,blue)
    box(25,322,350,178,"GENERADOR FV",["10 × 550 Wp","Una cadena en PV1","QCC y DPS fotovoltaico"],red)
    box(540,322,355,178,"INVERSOR M1",["SUN2000-5KTL-M1","5 kW · 380/220 V","Corriente alta"],blue)
    box(1060,322,335,178,"RAMA CA FV",["16 A y diferencial","Tipo A · 100 mA","DPS CA para TT"],blue)
    line(375,411,540,411,red);line(895,411,1060,411,blue)
    line(1227,322,1227,230,blue);line(1227,230,720,230,blue);line(720,230,720,157,blue)
    d.text((1030,195),"CA · 20 m · 5G4 mm² Cu",font=f(25),fill=blue,anchor="ma")
    line(201,157,201,245,orange);line(201,245,720,245,orange);line(720,245,720,322,orange)
    d.text((420,264),"RS-485 y SDongleA-05",font=f(25),fill=orange,anchor="ma")
    d.text((282,536),"CC · 25 m de ida · 6 mm² Cu por polo",font=f(25),fill=red,anchor="ma")
    line(35,590,1385,590,green)
    for x in (200,720,1227):line(x,500,x,590,green)
    d.text((710,615),"Barra PE y tierra TT · continuidad en marcos, rieles, inversor y tableros",font=f(26),fill=green,anchor="ma")
    im.save(root/"Planos"/"Esquema_memoria_v0.3.png",optimize=True)

def main():
    scenes=[roof_plan(),electric()]
    doc=ezdxf.new("R2013")
    doc.units=4
    doc.header["$MEASUREMENT"]=1
    doc.styles.new("TFM",dxfattribs={"font":"calibri.ttf"})
    for name,(_,color) in COLORS.items():
        doc.layers.new(name,dxfattribs={"color":color,"lineweight":20})
    msp=doc.modelspace()
    for index,sc in enumerate(scenes):
        off=index*23000
        for kind,data,layer,width in sc.entities:
            attrs={"layer":layer,"lineweight":max(5,min(211,width))}
            if kind=="line":
                x1,y1,x2,y2=data;msp.add_line((x1+off,y1),(x2+off,y2),dxfattribs=attrs)
            elif kind=="poly":
                msp.add_lwpolyline([(x+off,y) for x,y in data],dxfattribs=attrs)
            elif kind=="circle":
                x,y,r=data;msp.add_circle((x+off,y),r,dxfattribs=attrs)
            else:
                x,y,txt,size,bold,align=data
                ent=msp.add_text(txt,dxfattribs={**attrs,"height":size,"style":"TFM"})
                ent.set_placement((x+off,y),align={"left":TextEntityAlignment.LEFT,
                          "center":TextEntityAlignment.CENTER,"right":TextEntityAlignment.RIGHT}[align])
    memoria(ROOT)
    dxf=OUT/"Instalacion_FV_v0.3.dxf"
    doc.saveas(dxf)
    audit=ezdxf.readfile(dxf).audit()
    assert not audit.has_errors
    assert len(list(doc.modelspace().query("LWPOLYLINE[layer=='MODULOS']")))==10
    pdf=OUT/"Planos_instalacion_FV_v0.3.pdf"
    c=canvas.Canvas(str(pdf),pagesize=(420*mm,297*mm))
    c.setTitle("Planos de instalación FV · Vivienda Ciudad del Este")
    c.setAuthor("Clara María De Los Ángeles Rolón Duré")
    for scene in scenes:
        render(scene,c);c.showPage()
    c.save()
    p=pdfium.PdfDocument(str(pdf))
    for i in range(2):
        page=p[i];bmp=page.render(scale=2)
        im=bmp.to_pil().copy().convert("RGB")
        im.save(OUT/f"FV-0{i+1}_v0.3.png",optimize=True)
        # Fragmentos de lectura del cuerpo de la memoria.
        if i==0:
            crop=(im.width*0.045,im.height*.105,im.width*.46,im.height*.824)
        else:
            crop=(im.width*.035,im.height*.12,im.width*.965,im.height*.77)
        im.crop(tuple(map(int,crop))).save(OUT/f"Figura_FV-0{i+1}_v0.3.png",optimize=True)
        bmp.close();page.close()
    p.close()
    print("DXF válido",len(doc.modelspace()),"entidades. PDF A3 de 2 láminas.")
    print(dxf.name,pdf.name)
if __name__=="__main__":
    main()
