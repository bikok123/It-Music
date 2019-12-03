function cs_change_music(music)
   {
     document.getElementById("audio");
     console.log("123456");
     document.getElementById("source").setAttribute("src", music);
     document.getElementById("audio").load();
     document.getElementById("audio").play();

   }
