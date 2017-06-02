<html>
	<head>
		<!-- ajax跨域 注意dataType是jsonp-->
		<meta content="text/html; charset=utf-8" http-equiv="Content-Type">
		<script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.js"></script> 
		<script type="text/javascript">
		function getDeptName(){
			$.ajax({  
				type:'get',  
				url : 'http://duang.zhonganonline.com/project/getGroupInfo.do',  
				dataType : 'jsonp',   
				success  : function(data) {  
					$(data).each(function(){
						//var opt = document.createElement("option");
						//opt.value=this.buName;opt.text=this.buName;
						//document.getElementById('appCategory').options.add(opt);
						console.log(this.buCode+this.buName+'\n');
					})
				},
				error: function (XMLHttpRequest,textStatus, errorThrown) { 
					alert(errorThrown); 
					} 
				}); 
		}
		</script>
	</head>
	<body>
		<span>123456</span>
		<input type="button" value="跨域请求" onclick="getDeptName()"/>
		<span id="appCategory"></span>
	</body>
</html>
