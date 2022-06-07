//A5
/**
 * Fetches a JSON file and displays an array of its content
 */
function toArray() 
{
  var arrondissement = document.getElementById("arrondissement").value;

  fetch("/api/installations?arrondissement="+arrondissement+"",
  {
    method: 'GET',        
    headers: 
    {
      'Accept': 'application/json'
    }        
  })
  .then(function(response)
  {
      if(response.ok) 
      {  
        return response.text();
      }
      else if(response.status == 400)
      {
        window.location.replace('400.html');
      }
      else if(response.status == 404)
      {
        window.location.replace('404.html');
      }
      else if(response.status == 500)
      {
        window.location.replace('500.html');
      }
      else
      {
        window.alert('An unexpected error occurred');
      }
  })
  .then(function(jsFile)
  {
      var js = JSON.parse(jsFile);
      console.log(js);
      
      var title = showTitle(arrondissement, true);
      var aquatique = aquatiqueArray(js);
      var glissade  = createTabGlissade(js);

      document.getElementById("instaH2").innerHTML=title;
      document.getElementById("aquaArray").innerHTML=aquatique;
      document.getElementById("glissArray").innerHTML=glissade;
  })       
};

/**
  *Displays a title for a table that contains facilities data
  *@param {string} installations Either a district name or a type of facility
  *@param {boolean} switchs True = is district name, False = is type of facility
  *@returns {string} The title of the table
 */
function showTitle(installations, switchs)
{
  let titre;
  if(switchs) 
  {
    titre = `<h2>Installations dans l'arrondissement : <span>`+ installations +`</span></h2>`;
  }
  else 
  {
    titre = `<h2>Installations de type : <span>`+ installations +`</span></h2>`;
  }
  return titre;
}

/**
 * Make a table with information about a district's facilities
 * @param {*} js A parsed JSON file
 * @returns An array of HTML elements
 */
function aquatiqueArray(js) 
{
  let array = 
  `
  <table>
    <tr>
        <th width="100">ID_UEV</th>
        <th width="100">TYPE</th>
        <th width="100">NOM</th>
        <th width="100">ARRONDISSE</th>
        <th width="100">ADRESSE</th>
        <th width="100">PROPRIETE</th>
        <th width="100">GESTION</th>
        <th width="100">POINT_X</th>
        <th width="100">POINT_Y</th>
        <th width="100">EQUIPEME</th>
        <th width="100">LONG</th>
        <th width="100">LAT</th>
    </tr>
  `;

  for(var i = 0; i < js.Installations_Aquatiques.length; i++) 
  {
    array += 
    `
    <tr> 
    <td>${js.Installations_Aquatiques[i].ID_UEV}</td>
    <td>${js.Installations_Aquatiques[i].TYPE_}</td>
    <td>${js.Installations_Aquatiques[i].NOM}</td>
    <td>${js.Installations_Aquatiques[i].ARRONDISSE}</td>
    <td>${js.Installations_Aquatiques[i].ADRESSE}</td>
    <td>${js.Installations_Aquatiques[i].PROPRIETE}</td>
    <td>${js.Installations_Aquatiques[i].GESTION}</td>
    <td>${js.Installations_Aquatiques[i].POINT_X}</td>
    <td>${js.Installations_Aquatiques[i].POINT_Y}</td>
    <td>${js.Installations_Aquatiques[i].EQUIPEME}</td>
    <td>${js.Installations_Aquatiques[i].LONG}</td>
    <td>${js.Installations_Aquatiques[i].LAT}</td>
    </tr>
    `;
  } 
  array += `</table>`;
  return array;
}

/**
 * Removes the table of facilities created by the function toArray()
 */
function hideArray()
{
  document.getElementById("instaH2").innerHTML="";
  document.getElementById("aquaArray").innerHTML = "";
  document.getElementById("glissArray").innerHTML = "";
}

function createTabGlissade(js) 
{
  let array = 
  `
  <table>
    <tr>
      <th>nom</th>
      <th>nom_arr</th>
      <th>cle</th>
      <th>date_maj</th>
      <th>ouvert</th>
      <th>deblaye</th>
      <th>condition</th>
    </tr>
  `;
 
  for(var i = 0; i < js.Glissades.length; i++) 
  {
    array += 
    `
    <tr> 
    <td>${js.Glissades[i].nom}</td>
    <td>${js.Glissades[i].nom_arr}</td>
    <td>${js.Glissades[i].cle}</td>
    <td>${js.Glissades[i].date_maj}</td>
    <td>${js.Glissades[i].ouvert}</td>
    <td>${js.Glissades[i].deblaye}</td>
    <td>${js.Glissades[i].condition}</td>
    </tr>
    `;
  } 
  array += `</table>`;
  return array;
}



function createTabPatinoire(data) {
  let tab = 
  `
  <h1>Voici la liste des Patinoire :</h1>
  <tr>
    <th>id</th>
    <th>nom_arr</th>
    <th>nom_pat</th>
    <th>date_heure</th>
    <th>ouvert</th>
    <th>deblaye</th>
    <th>arrose</th>
    <th>resurface</th>
   </tr>`;

  if(i == true){
      for (var i=0; i<data.length; i++) {
          tab += `<tr> 
      <td>${data[i][0]} </td>
      <td>${data[i][1]} </td>
      <td>${data[i][2]} </td>
      <td>${data[i][3]} </td>
      <td>${data[i][4]} </td>
      <td>${data[i][5]} </td>
      <td>${data[i][6]} </td>
      <td>${data[i][7]} </td>
      </tr>`;
      }
  }
  else
     for (var i=0; i<data.Patinoire.length; i++) {
         tab += `<tr> 
     <td>${data.Patinoire[i].id} </td>
     <td>${data.Patinoire[i].nom_arr} </td>
     <td>${data.Patinoire[i].nom_pat} </td>
     <td>${data.Patinoire[i].date_heure} </td>
     <td>${data.Patinoire[i].ouvert} </td>
     <td>${data.Patinoire[i].deblaye} </td>
     <td>${data.Patinoire[i].arrose} </td>
     <td>${data.Patinoire[i].resurface} </td>
     </tr>`;
         
     } 

  return tab
}

//A6
/**
 * Fetches a JSON file and displays an array of its content
*/
window.onload=function()
{
  let generate = document.querySelector("div.names button[name='generate']");
  let select = document.querySelector("div.names select[name='select']");

  fetch("/names",
  {       
    headers: 
    {
      'Accept': 'application/json'
    }        
  })
  .then(function(response)
  {
      if(response.ok) 
      {  
        return response.text();
      }
      else if(response.status == 400)
      {
        window.location.replace('400.html');
      }
      else if(response.status == 404)
      {
        window.location.replace('404.html');
      }
      else if(response.status == 500)
      {
        window.location.replace('500.html');
      }
      else
      {
        window.alert('An unexpected error occurred');
      }
  })
  .then(function(jsFile)
  {
    var js = JSON.parse(jsFile);
    console.log(js);

    generate.addEventListener('click', () =>
    {
      let options = js.map(nom => `<option value=${nom.replace(/ /g, '%20')}>${nom}</option>`);
      select.innerHTML = options;
    }); 

    select.addEventListener('change', () => 
    {
      choice=select.options[select.selectedIndex].value;
      toArray2(choice);       
    });
  })
}

/**
 * Fetches a JSON file and displays an array of its content
*/
function toArray2(nom)
{
  //var type = document.getElementById("type").value;

  fetch("/api/installation-nom?nom="+nom+"",
  {
    method: 'GET',        
    headers: 
    {
      'Accept': 'application/json'
    }        
  })
  .then(function(response)
  {
      if(response.ok) 
      {  
        return response.text();
      }
      else if(response.status == 400)
      {
        window.location.replace('400.html');
      }
      else if(response.status == 404)
      {
        window.location.replace('404.html');
      }
      else if(response.status == 500)
      {
        window.location.replace('500.html');
      }
      else
      {
        window.alert('An unexpected error occurred');
      }
  })
  .then(function(jsFile)
  {
      var js = JSON.parse(jsFile);
      console.log(js);
      
      if(js.Installations_Aquatiques) 
      {
        var installations = aquatiqueArray(js);
      }
      if(js.Glissades) 
      {
        var glissade  = createTabGlissade(js);
      }

      if(js.Installations_Aquatiques) 
      {
        document.getElementById("nameArray").innerHTML=installations;
      }
      if(js.Glissades) 
      {
        document.getElementById("nameArray").innerHTML=glissade;
      }
  })
}

/**
 * Removes the table of facilities created by the function toArray3()
 */
 function hideArray2()
 {
   document.getElementById("nameArray").innerHTML = "";
 }

//C1
/**
 * Fetches a JSON file and displays an array of its content
*/
function toArray3()
{
  var type = document.getElementById("type").value;

  fetch("/api/installation-type?type="+type+"",
  {
    method: 'GET',        
    headers: 
    {
      'Accept': 'application/json'
    }        
  })
  .then(function(response)
  {
      if(response.ok) 
      {  
        return response.text();
      }
      else if(response.status == 400)
      {
        window.location.replace('400.html');
      }
      else if(response.status == 404)
      {
        window.location.replace('404.html');
      }
      else if(response.status == 500)
      {
        window.location.replace('500.html');
      }
      else
      {
        window.alert('An unexpected error occurred');
      }
  })
  .then(function(jsFile)
  {
      var js = JSON.parse(jsFile);
      console.log(js);
      
      var title = showTitle(type, false);

      if(js.Installations_Aquatiques) 
      {
        var installations = aquatiqueArray(js);
      }

      if(js.Glissades) 
      {
        var glissade = createTabGlissade(js);
      }

      if(js.Installations_Aquatiques) 
      {
        document.getElementById("typeTitle").innerHTML=title;
        document.getElementById("typeArray").innerHTML=installations;
      }

      if(js.Glissades) 
      {
        document.getElementById("typeTitle").innerHTML=title;
        document.getElementById("typeArray").innerHTML=glissade;
      }
  })
}

/**
 * Removes the table of facilities created by the function toArray3()
 */
 function hideArray3()
 {
   document.getElementById("typeTitle").innerHTML="";
   document.getElementById("typeArray").innerHTML = "";
 }
