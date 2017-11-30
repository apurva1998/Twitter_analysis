<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8" />
	<title>
		Twitter Analysis Of Road Congestion Severity Estimation
	</title>
	<style>
      body { margin: 0; padding: 0; font: 12px/1.2 Meiryo, Tahoma, sans-serif; }
      #header { background: #2086f3; font-size: 30px; color: #ffffff; padding: 12px; }
      #map { margin: 4px; float: right; z-index: 800; }
      #content { margin: 4px; width: 240px; float: left; overflow-y: auto; }
    </style>
	<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
	<script type="text/javascript" src="html2canvas.js"></script>
	<script type="text/javascript" src="jquery.plugin.html2canvas.js"></script>
	
<script type="text/javascript">

function remove(){
	document.getElementById("road_lbl").style.display = "None";
	document.getElementById("remove_btn").style.display = "None";
	document.getElementById("road_lbl_sev").style.display = "None";
}

function add(){
	var e = document.getElementById("road_dd");
	var strUser = e.options[e.selectedIndex].text;
	document.getElementById("road_lbl").innerHTML = strUser;
	document.getElementById("road_lbl_sev").innerHTML = strUser;
	document.getElementById("road_lbl").style.display = "block";
	document.getElementById("road_lbl_sev").style.display = "block";
	document.getElementById("remove_btn").style.display = "block";
	myMap();
	myMap_Color();
}

function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
	var s = today.getSeconds();
    document.getElementById('time').innerHTML = "<h2>Current Time </h2><h3> " + h + ":" + m + ":" + s +"</h3>";
	var tym;
	if(m<=29){
		tym = ""+ h + " : 30 to " + (h+1) + " : 00";
	}
	if(m>29){
		tym = "" + (h+1) + " : 00 to " + (h+1) + " : 30";
	}
	document.getElementById('time_range').innerHTML = "<h2>Estimation For </h2><h3>" + tym + "</h3>";
}
setInterval(startTime, 1000);

function capture() {
    $('#map_color').html2canvas({
        onrendered: function (canvas) {
            $('#img_val').val(canvas.toDataURL("image/png"));
            document.getElementById("myForm").submit();
        }
    });
}

</script>

</head>
<body onload="startTime()" style="overflow: hidden;">
	
<form method="POST" enctype="multipart/form-data" action="<?php echo $_SERVER['PHP_SELF']; ?>" id="myForm">
    <input type="hidden" name="img_val" id="img_val" value="" />
</form>
	<?php
 
//Get the base-64 string from data
$filteredData=substr($_POST['img_val'], strpos($_POST['img_val'], ",")+1);
 
//Decode the string
$unencodedData=base64_decode($filteredData);
 
//Save the image
file_put_contents('img.png', $unencodedData);

?>
	<table width=100% cellpadding=0 cellspacing=1>
		<tr style="background: #2C3E50;  /* fallback for old browsers */background: -webkit-linear-gradient(to right, #FD746C, #2C3E50);  /* Chrome 10-25, Safari 5.1-6 */background: linear-gradient(to right, #FD746C, #2C3E50); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */">
			<td colspan=2>
				<font size=5 color="white"><b>&nbsp;&nbsp;Twitter Analysis Of Road Congestion Severity Estimation</b></font>
			</td>
		</tr>
		<tr align="left">
			<td width="600px">
				<div id="map" style="width:600px;height:600px"></div>
				<script src="http://api.longdo.com/map/?key=10dc711504c21ed52209d679ec3d50da"></script>
				
					<script type="text/javascript">
      var map;
      function myMap() {
        
        map = new longdo.Map({
          layer : [
            longdo.Layers.NORMAL_EN,
			longdo.Layers.TRAFFIC,
			
          ],
		  language : 'en',
          placeholder : document.getElementById('map'),
		  lastview : false,
        });
        
		map.bound({minLon: 99, minLat: 16, maxLon: 100, maxLat: 17});
		
        setTimeout(map.Overlays.load, 1000, longdo.Overlays.events);
        setTimeout(map.Overlays.load, 2000, longdo.Overlays.cameras);
        
        map.Route.enableContextMenu();
        map.Route.auto(true);
		map.Route.language('en');
		map.zoom(9);
		map.language('en');
		
		setTimeout(function() { capture(); }, 120000);
		
      }	 

		var map_color;
      function myMap_Color() {
        
        map_color = new longdo.Map({
          layer : [
			longdo.Layers.TRAFFIC,
          ],
          placeholder : document.getElementById('map_color'),
		  lastview : false,
        });
        
		map_color.bound({minLon: 99, minLat: 16, maxLon: 100, maxLat: 17});
        map_color.Route.auto(true);
		map_color.zoom(9);
		map_color.Ui.Zoombar.visible (false);
		map_color.Ui.Geolocation.visible (false);
		map_color.Ui.LayerSelector.visible (false);
		map_color.Ui.Fullscreen.visible (false);
		map_color.Ui.Crosshair.visible (false);
		map_color.Ui.Scale.visible (false);
		map_color.Ui.DPad.visible (false);
		map_color.Ui.Toolbar.visible (false);
		map_color.Ui.CustomControl.visible (false);
		map_color.Ui.ButtonType.visible (false);
		map_color.Ui.MenuBar.visible (false);
		map_color.Ui.TagPanel.visible (false);
		map_color.Ui.ZoombarMini.visible (false);
		map_color.Ui.PopupMini.visible (false);
		map_color.Ui.Tooltip.visible (false);
		map_color.Ui.ContextMenu.visible (false);
		map_color.Ui.Notice.visible (false);
		map_color.Ui.Legend.visible (false);
		
      }
	  </script>

		

			</td>
			<td  style="vertical-align: text-top;">
				<table width=100%>
					<tr>
						<td>
						<h2>Road name</h2>
						</td>
					</tr>
					<tr>
						<td>
						<select id="road_dd" style="width:400px;border-radius:5px">
						<option value="Pahonyothin Road" selected="selected">Pahonyothin Road</option>
						</select>
						<input type="button" value="Add" id="add_btn" onClick="add()" style="border-radius:5px"/>
						</td>
					</tr>
					<tr>
						<td>
						<br>
						<h2>Road to be estimated</h2>
						</td>
					</tr>
					<tr>
						<td>
						<table width=100% border=1 cellspacing=0 style="border-radius:5px">
							<tr style="background: #76b852;  /* fallback for old browsers */background: -webkit-linear-gradient(to right, #8DC26F, #76b852);  /* Chrome 10-25, Safari 5.1-6 */background: linear-gradient(to right, #8DC26F, #76b852); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */">
							<b>
								<td>
								Road name
								</td>
								<td>
								Remove
								</td>
							</b>
							</tr>
						<tr>
							<td>
							<div id="road_lbl" style="display:none"></div>
							</td>
							<td>
							<input type="button" id="remove_btn" value="X" onclick="remove()" style="display:none ;border: 1px solid; border-radius:10px; color:red" />
							</td>
						</tr>
						</table>
						</td>
					</tr>	
					<tr>
						<td>
						<br>
							<div id="time"></div>
						</td>
					</tr>
					<tr>
						<td>
							<div id="time_range"></div>
						</td>
					</tr>
					<tr>
						<td>
						<table width=100% border=1 cellspacing=0 style="border-radius:5px">
							<tr style="background: #76b852;  /* fallback for old browsers */background: -webkit-linear-gradient(to right, #8DC26F, #76b852);  /* Chrome 10-25, Safari 5.1-6 */background: linear-gradient(to right, #8DC26F, #76b852); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */">
								<b>
								<td>
									Road name
								</td>
								<td>
									Severity
								</td>
								</b>
							</tr>
							<tr>
								<td>
									<div id="road_lbl_sev" style="display:none"></div>
								</td>
								<td>
									<b><div id="severity"></div></b>
								</td>
							</tr>
						</table>
						</td>
					</tr>
				</table>
			</td>
		</tr>
	</table>
	<br>
	<br>
	<br>
	<br>
	<br>
<div id="map_color" style="width:300px;height:300px"></div>
</body>
</html>