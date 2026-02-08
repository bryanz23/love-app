from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<style>

/* ================= FONDO ================= */
body{
    margin:0;
    background:#FFF0F5;
    font-family:"Segoe UI", sans-serif;
}


/* ================= HOME ================= */
.home{
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
}

.card{
    background:white;
    padding:50px;
    border-radius:25px;
    text-align:center;
    box-shadow:0 12px 40px rgba(0,0,0,.15);
}

button{
    padding:12px 26px;
    border:none;
    border-radius:12px;
    cursor:pointer;
}

.yes{background:#D46A92;color:white;}
.no{background:#eee;margin-left:10px;}



/* ================= STORY ================= */
.story{
    display:none;
    height:100vh;
    padding:40px;
}

.container{
    display:flex;
    height:100%;
}


/* ================= TIMELINE ================= */
.timeline{
    width:35%;
    position:relative;
    overflow-y:auto;
}

/* línea punteada */
.timeline:before{
    content:"";
    position:absolute;
    left:40px;
    top:0;
    bottom:0;
    border-left:4px dashed white;
}

/* evento */
.event{
    margin:50px 0 50px 90px;
    position:relative;
}

/* circulito */
.event:before{
    content:"";
    position:absolute;
    left:-55px;
    top:15px;
    width:18px;
    height:18px;
    background:white;
    border-radius:50%;
}

.event img,
.event video{
    width:180px;       /* mismo ancho para todos */
    height:180px;      /* mismo alto para todos */
    object-fit:cover;  /* mantiene proporción sin deformar */
    border-radius:12px;
    cursor:pointer;
    transition:.3s;
}


.event img:hover{
    transform:scale(1.08);
}

.event p{
    font-size:14px;
    color:#555;
}


/* ================= CARTA ================= */
.letter{
    width:65%;
    background:#fffafc;
    border-radius:20px;
    padding:50px;
    margin-left:30px;
    box-shadow:0 10px 35px rgba(0,0,0,.15);
}


/* ================= MODAL ================= */
.modal{
    display:none;
    position:fixed;
    inset:0;
    background:rgba(0,0,0,.6);
    justify-content:center;
    align-items:center;
}

.modal-content{
    background:white;
    padding:20px;
    border-radius:20px;
    max-width:75%;
    max-height:90vh;   /* límite vertical */
    overflow-y:auto;   /* scroll si texto largo */
    text-align:center;
}


.modal img,
.modal video{
    max-width:100%;
    max-height:65vh;   /* 🔥 nunca supera la pantalla */
    object-fit:contain; /* mantiene proporción completa */
    border-radius:15px;
}


/* =========================================================
   💕 NUEVO: GALERÍA ROMÁNTICA (MISMA PÁGINA)
   SOLO AÑADIDO — NO MODIFICA LO DEMÁS
========================================================= */

.gallery{
    display:none;
    position:fixed;
    inset:0;
    background:linear-gradient(135deg,#ff9ecb,#ffd6e8);
    overflow:hidden;
}

.gallery h1{
    text-align:center;
    color:white;
    margin-top:25px;
}

.photo{
    position:absolute;
    width:250px;
    border-radius:20px;
    animation:float 7s ease-in-out infinite;
}

@keyframes float{
    0%{transform:translateY(-40px);}
    50%{transform:translateY(40px);}
    100%{transform:translateY(-40px);}
}

.heart{
    position:absolute;
    font-size:22px;
    animation:fall 6s linear infinite;
}

@keyframes fall{
    0%{top:-10%;}
    100%{top:110%;}
}

.love-btn{
    background:#ff4d88;
    color:white;
}

</style>
</head>

<body>


<!-- ================= INICIO ================= -->
<div class="home" id="home">

<div class="card">
<h2>Para la niña más linda del mundo, DYANA ❤️</h2>
<p>Esto es un detalle especial para la dueña de mi corazon ¿Te gustaría descubrir que es?</p>

<button class="yes" onclick="goStory()">❤️ Sí</button>
<button class="no" onclick="alert('Debes presionar Sí 😊')">🐱 No</button>
</div>

</div>



<!-- ================= STORY ================= -->
<div class="story" id="story">

<div class="container">


<!-- ========= TIMELINE ========= -->
<div class="timeline">


<!-- MOMENTO 1 VIDEO -->
<div class="event">
<b>Inicio de nuestra historia</b><br>
    <video controls onclick="openVideo(this,'Recuerdas aquel 6 de febrero del 2025, traje un regalo único y especial para ti ❤️. Me hizo muy feliz verte asi.')">
    <source src="/static/video1.mp4" type="video/mp4">
</video>
</div>


<!-- MOMENTO 2 -->
<div class="event">
<b>Tu nombre en mi corazón 💖</b><br>
<img src="/static/NombreRoca.jpeg"
onclick="openPhoto(this,'Al igual que en las rocas, tu nombre tambien estaba plasmado en mi ❤️')">
</div>


<!-- MOMENTO 3 -->
<div class="event">
<img src="/static/Aeropuerto.jpeg"
onclick="openPhoto(this,'Cuando hiciste un viaje a Brasil, la primera vez que me hiciste el abandono y te acompañe hasta el aeropuerto 💕')">
</div>


<!-- MOMENTO 4 -->
<div class="event">
<b>Primer viaje 🚌</b><br>
<img src="/static/Churin.jpeg"
onclick="openPhoto(this,'Nuestro primer viaje juntos, donde tú y yo decidimos unirnos por primera vez 🥰')">
</div>

<!-- MOMENTO 4 -->
<div class="event">
<b>Paseo al lugar de mis orígenes ✈️</b><br>
<img src="/static/TPP1.jpeg"
onclick="openPhoto(this,'La primera noche que llegamos a Tarapoto 🌳, probamos la rica comida y tragos típicos del lugar.')">
</div>

<!-- MOMENTO 4 -->
<div class="event">
<img src="/static/Piscina.jpeg"
onclick="openPhoto(this,'Disfrutamos de la piscina en la noche bajo el cielo azul 🌕 comiendo uno de tus platos que te encantaron Las canastitas.')">
</div>

<!-- MOMENTO 4 -->
<div class="event">
<img src="/static/Mirador.jpeg"
onclick="openPhoto(this,'Como una serie romántica, un beso se dió ante los ojos de la grandiosa ciudad.')">
</div>

<!-- MOMENTO 4 -->
<div class="event">
<img src="/static/Lamas1.jpeg"
onclick="openPhoto(this,'Visitamos el famoso castillo de Lamas 🏰, yo tan feliz contemplando lo hermosa que eres 😍.')">
</div>

<!-- MOMENTO 4 -->
<div class="event">
<img src="/static/Lamas2.jpeg"
onclick="openPhoto(this,'Esa sonrisa que me mata, sí, esa sonrisa tuya única que me alegra el alma 😄.')">
</div>

<!-- MOMENTO 4 -->
<div class="event">
<b>Nuestras aventuras😸</b><br>
<img src="/static/Eden.jpeg"
onclick="openPhoto(this,'Fotito en una salida con amigos en el Edén, siempre con tu sonrisa hermosa 💕.')">
</div>

<!-- MOMENTO 4 -->
<div class="event">
<img src="/static/Chillis.jpeg"
onclick="openPhoto(this,'Fotito de nosotros despues de una cenita 💕.')">
</div>

<!-- MOMENTO 4 -->
<div class="event">
<img src="/static/Parque.jpeg"
onclick="openPhoto(this,'Fotito con mi gatita 😸 paseando.')">
</div>

<!-- MOMENTO 4 -->
<div class="event">
<img src="/static/SanMarcos.jpeg"
onclick="openPhoto(this,'Nostros en un concierto random en San Marcos jajajaja.')">
</div>

<!-- MOMENTO 4 -->
<div class="event">
<img src="/static/Depa.jpeg"
onclick="openPhoto(this,'Antes de que mi amor se vaya a su reunión y me haga el abandono, yo vigilandole desde el frente jajaja.')">
</div>


<!-- MOMENTO 4 -->
<div class="event">
<img src="/static/Halloween.jpeg"
onclick="openPhoto(this,'Disfraces listos para lucirlos toda la noche 😊, mi amor de princesa Jazmín.')">
</div>

<!-- MOMENTO 4 -->
<div class="event">
<img src="/static/Halloween2.jpeg"
onclick="openPhoto(this,'Otra fotito porque me encanta 😍.')">
</div>

<!-- MOMENTO 4 -->
<div class="event">
<img src="/static/AñoNuevo.jpeg"
onclick="openPhoto(this,'Nuestro primer Año Nuevo juntos como pareja, en el 2024 te lo dije, fuiste lo mejor que ha pasado 💗, lo volvi a confirmar en el 2025, y ahora en el 2026 sé que no me equivoque 😊.')">
</div>

<!-- MOMENTO 4 -->
<div class="event">
<img src="/static/Palais.jpeg"
onclick="openPhoto(this,'Fotito con mi amor celebrando nuestros logros 😊, nuestros ingresos a nuevos trabajos para seguir creciendo juntos 💗.')">
</div>

<!-- MOMENTO 4 -->
<div class="event">
<img src="/static/Videollamada.jpeg"
onclick="openPhoto(this,'Asi como todas las noches, como todas nuestras llamadas y videollamadas 📱❤️, cada vez que vemos series, películas 💻 o simplemente contarnos sobre nuestro día, solo contigo mi niña bonita 😊.')">
</div>

</div>



<!-- ========= CARTA ========= -->
<div class="letter">

<h2>Carta de Amor 💗</h2>

<p>
Hola amor, si soy yo, Bryan 😸, espero que al despertar puedas leer esta carta 💌. Siempre he tratado de expresar como me siento y quiero decirtelo en palabras.
</p>
La primera vez que te ví, no se me paso por la cabeza de que llegarias a ser tan importante para mí, ni que pasaríamos por todo lo que pasamos hasta ahora. Al principio no hablabamos casi nada, pero poco a poco fuimos conociendo más el uno del otro. Me fui enamorando de ti.
</p>

<p>
No olvido la primera vez que trate de decirte para salir, empezó con un "¿Te gustaría salir a tomar algo? 😊", ovbiamente sin sonar tan mandado jajaja. Recuerdo que estaba esperando fuera del lugar que habíamos quedado, te llame cuando estuve fuera y tu preguntando porque no me encontrabas, la verdad estaba mirandote de lejos, me encontraba nervioso. Fue un bonito momento y una oportunidad especial de poder conocerte junto a tus amigas.
</p>

<p>
Nuestra segunda salida si fue algo más privado entre nosotros y nuevamente te dije si querías salir a tomar algo jajaja. Lo importante fue que esos meses tuvimos la suerte de coincidir nuestros descansos en Lima. Esa noche que fuimos a Palais por primera vez, sentí algo diferente, sentí que hubo una conexión entre nosotros. Nuestra historia de amor, empezaba a escribirse.
</p>

<p>
Tuvimos nuestra salida al cine, en el centro cívico, lo recuerdas al igual que yo? esa noche habías ido a recoger tus lentes tambien n.n Ese día confirmamos lo que me temía, que nuestras guardias no coincidían 😔. Pero eso no iba a detenerme e hice lo imposible para poder cambiar mi guardia y estar contigo, y lo conseguí 😊.
</p>

<p>
Tuvimos nuestro primer viaje juntos, nos fuimos a las aguas termales, donde estaba seguro de que yo queria pasar mis días a tu lado y no quería a nadie más. Fue un 07 de febrero donde te pregunte, si querias ser mi enamorada, y desde ese día fui muy feliz porque ya te tenía conmigo 😊💗.
</p>

<p>
Desde ese momento, tuvimos muchas aventuras, salidas, experiencias juntos, y cada momento lo recuerdo claramente como lo puedes ver en nuestras fotos, y de cada uno te podría decir cientos de cosas y describir mucho más, porque los recuerdo y los tengo en mi 💗.
</p>

<p>
Pero no todo fue color de rosa, tuvimos nuestros momentos donde nuestra relación se puso a prueba, momentos donde hubieron discusiones, peleas, desacuerdos pero a pesar de todo, en cada momento supimos salir adelante, los dos como pareja, los dos haciendole frente al problema, los dos frente al mundo, porque yo te tengo a ti y tu me tienes a mí. Yo soy tuyo y tú eres mía 💗. 
Sé que ahora estamos pasando un mal momento, y es otra de las pruebas que debemos superar como pareja, el destino quiere que nos elijamos nuevamente y que luchemos juntos, tú a mi lado. 
</p>

<p>
No soy perfecto, pero desde que decidimos unirnos hace 1 año atras, no me imagino un futuro sin ti 💗. Quiero estar contigo siempre, quiero verte todos los días de mi vida, quiero que seas la mujer que vea todas las mañanas al despertar, quiero irme a dormir teniendote a mi lado, quiero que seas la mujer que cuide a nuestros hijos, quiero todo contigo 💗, porque eres tú y yo se que eres tú. Me he equivocado muchas veces y sigo aprendiendo de mis errores para no volver a cometerlos, porque sé que me dolería bastante si algún dia no te tengo conmigo.
</p>

<p>
Siendo hoy 08 de febrero del 2025 a las 02:45 a.m. momento en que escribo con mi corazón en la mano esta carta para tí, así como cumplimos nuestro primer año, quiero que me permitas estar todos nuestros años que estan por venir a tu lado. Quiero hacerte muy feliz, quierdo darte lo mejor de mí, y ser el hombre que te mereces.

<p>
Te extraño mucho mi princesa hermosa. Te Amo 💗
</p> 

<br><br>
<button class="love-btn" onclick="goGallery()">❤️ Dale Click ❤️</button>


<button onclick="goHome()">🔙 Volver</button>

</div>


</div>
</div>

<!-- ================= GALERIA NUEVA ================= -->
<div class="gallery" id="gallery">

<h1>Una mamacita mi novia 💕</h1>

<button onclick="backStory()" 
        style="position:absolute; top:20px; left:20px; z-index:999;">
🔙 Volver
</button>

<!-- CAMBIA SOLO LOS NOMBRES -->
<img src="/static/Ella1.jpeg" class="photo" style="top:5%; left:5%;">
<img src="/static/Ella2.jpeg" class="photo" style="top:20%; left:40%;">
<img src="/static/Ella3.jpeg" class="photo" style="top:40%; left:70%;">
<img src="/static/Ella4.jpeg" class="photo" style="top:60%; left:15%;">
<img src="/static/Ella5.jpeg" class="photo" style="top:75%; left:45%;">
<img src="/static/Ella6.jpeg" class="photo" style="top:10%; left:80%;">
<img src="/static/Ella7.jpeg" class="photo" style="top:30%; left:25%;">
<img src="/static/Ella8.jpeg" class="photo" style="top:55%; left:60%;">
<img src="/static/Ella9.jpeg" class="photo" style="top:70%; left:80%;">
<img src="/static/Ella10.jpeg" class="photo" style="top:15%; left:55%;">
<img src="/static/Ella11.jpeg" class="photo" style="top:80%; left:30%;">

</div>

<!-- 🎵 MUSICAS -->
<audio id="musicStory" src="/static/Reik.mp3" loop></audio>
<audio id="musicGallery" src="/static/Rio.mp3" loop></audio>


<!-- ================= MODAL ================= -->
<div class="modal" id="modal">
<div class="modal-content" id="modalContent"></div>
</div>



<script>

function goStory(){
    home.style.display="none";
    story.style.display="block";

    musicGallery.pause();

    musicStory.currentTime = 0;  // 🔥 empieza desde segundo 30 (cámbialo)
    musicStory.play();
}

function goHome(){
    story.style.display="none";
    home.style.display="flex";
}

function goGallery(){
    story.style.display="none";
    gallery.style.display="block";

    musicStory.pause();

    musicGallery.currentTime = 0; // 🔥 empieza desde segundo 10
    musicGallery.play();

    for(let i=0;i<25;i++){
        let h=document.createElement("div");
        h.innerHTML="❤️";
        h.className="heart";
        h.style.left=Math.random()*100+"%";
        gallery.appendChild(h);
    }
}


function openPhoto(img,text){
    modal.style.display="flex";
    modalContent.innerHTML =
        "<img src='"+img.src+"'><p>"+text+"</p>";
}

function backStory(){
    gallery.style.display="none";
    story.style.display="block";

    musicGallery.pause();
    musicStory.play();
}


function openVideo(video,text){
    modal.style.display="flex";
    modalContent.innerHTML =
        "<video controls autoplay src='"+video.querySelector('source').src+"'></video><p>"+text+"</p>";
}

modal.onclick = ()=> modal.style.display="none";

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)

app.run(debug=True)
