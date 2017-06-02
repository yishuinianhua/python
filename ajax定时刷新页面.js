<html>
	<!--ajax定时刷新页面 -->
	<head> 
		<script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.js"></script> 
		<script type="text/javascript"> 
			$(document).ready(function () { 
				setInterval("startRequest()",1000); 
			}); 
			function startRequest() 
			{ 
				
				$("#date1").text((new Date()).toString()); 
			} 
		</script> 
	</head> 
	<body>
		<span id="date1"></span>
	</body>
</html>
