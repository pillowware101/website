<html>
		<head>
			<script src='searchengine.js' type='text/javascript'></script>
		</head>
		<body>
			<?php
			$results = file_get_contents("results.json");
          $resultarray = json_decode($filelist, true);
          foreach($resultarray as $value){
            $result=array_pop($resultarray);
            link($result, 
          }
			?>
			
		</body>
</html>
