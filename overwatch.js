$(document).ready(function() {
    $("#image-row").addClass("hidden");
  });

function press(){
    //Initialize and shuffle roles// 

    //TANKS//
    tanks = ["D.Va","Orisa","Reinhardt","Roadhog","Sigma","Winston","Wrecking Ball","Zarya"];
    tankList = _.shuffle(tanks)
    var tank1 = tankList.pop()
    var tank2 = tankList.pop()

    //DAMAGE//
    dmgs = ["Ashe","Bastion","Doomfist","Genji","Hanzo","Junkrat","Cassidy","Mei","Pharah","Reaper","Soldier: 76", "Sombra","Symmetra","Torbjörn","Tracer","Widowmaker"];
    dmgList = _.shuffle(dmgs)
    var dmg1 = dmgList.pop()
    var dmg2 = dmgList.pop()


    //SUPPORT//
    supports = ["Ana","Baptiste","Brigitte","Lucio","Mercy","Moira","Zenyatta"];
    supportList = _.shuffle(supports)
    var heal1 = supportList.pop()
    var heal2 = supportList.pop()

    /*# This part assigns the new text*/
    $("#tank1").text(tank1);
    $("#tank2").text(tank2);
    $("#dmg1").text(dmg1);
    $("#dmg2").text(dmg2);
    $("#heal1").text(heal1);
    $("#heal2").text(heal2);

    //Assign Images//
    $("#image-row").removeClass("hidden");
    document.getElementById("heal1-img").src="overwatch-images/" + heal1.toLowerCase().replace(/\s/g, "") + ".webp";
    document.getElementById("heal2-img").src="overwatch-images/" + heal2.toLowerCase().replace(/\s/g, "") + ".webp";
    document.getElementById("dmg1-img").src="overwatch-images/" + dmg1.toLowerCase().replace(/\s/g, "").replace(":","") + ".webp";
    document.getElementById("dmg2-img").src="overwatch-images/" + dmg2.toLowerCase().replace(/\s/g, "").replace(":","") + ".webp";
    document.getElementById("tank1-img").src="overwatch-images/" + tank1.toLowerCase().replace(/\s/g, "") + ".webp";
    document.getElementById("tank2-img").src="overwatch-images/" + tank2.toLowerCase().replace(/\s/g, "") + ".webp";
  };


