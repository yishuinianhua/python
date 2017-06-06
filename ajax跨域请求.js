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
		
		
    function displayAutoTest(taskId){
       // alert("taskId"+taskId);
        $.ajax({
            type : 'GET',
			timeout:10000,
            url	: 'http://10.139.162.239:5010/task/webApiForDuang',
            async: false,
            dataType : 'json',
            data : {'taskId':taskId},
            success : function() {
                alert("success");
            },
            error: function () {
                alert("fail");
            }

        });
    }
	
	function xiugai(ttt){
		//$("#td01").text("gugu");
		$(ttt).parent().next().text("789");
		//$(ttt).parent().next().text());
	}
	
	$(document).ready(function(){
			//$('.uatlist-table tr td:last-child').each(function(){
				//alert("123");
				//alert($(this).text());
				$('.uatlist-table tr').find('td:eq(1)').each(function(){
					//alert($(this).html().split('='));
					
					num = parseInt($(this).html().replace(/[^0-9]/ig,""));
					//alert(num);
					var status = $(this).next();
					
					//alert(status.text());
					status.text("add");
			})
	})
	
	$(document).ready(function(){
		$('#test123').click(function(){
			var result = {"success":true, "data":[null,null]}
				
		})
		
		$("#p01").click(function(){
			reportLink="http://www.baidu.com";
			$('#p01').html("1111<br>"+"2222<br>"+"<a href='"+reportLink+"' target='_blank' style='color:red;'>查看结果</a>");
		
		})
		trace("初始化方法进入二"); 
	})
	function trace(obj){ 
		console.log(obj); 
	} 
		</script>
	</head>
	<body>
		<span>123456</span>
		<input type="button" value="跨域请求" onclick="displayAutoTest('taskId=20170525163101330')"/>
		<span id="appCategory"></span>
		<p id="p01">1111111111</p>
		<p id="test123">2222222</p>
		
		
		<table border="1" class="uatlist-table">
			<tr>
				<td><input type="button" value="按钮" onclick="xiugai(this)"/></td>
				<td class="td01"><a href="/project/detail?projectId=1422">link</a></td>
				<td>gugu</td>
			</tr>
			<tr>
				<td><a href="javascript:void(0)" onclick="xiugai(this)">5</a></td>
				<td><a href="/project/detail?projectId=1421">link</a></td>
				<td>guagua</td>
			</tr>
			<tr>
				<td>456</td>
				<td><a href="/project/detail?projectId=1420">link</a></td>
				<td>bobo</td>
			</tr>
			<tr>
				<td>status</td>
				<td>status1</td>
				<td>niuniu</td>
			</tr>
		</table>
	</body>
</html>
