var album=1;
var number=1;
var type=1;

var arr = new Array(5); 
for(var i=1; i<5; i++){
    arr[i] = new Array(5);
  for(var j=1; j<11; j++){
    arr[i][j] = new Array(11);
  }
} // 주의. a b c 순서로 적으면 b c a 로 만들어짐 -> 왜 그런진 정확히 모르겠음

function select_click(a, n, t, c){
	if(c==0){
	album = a;
	number = n;
	}
	else{
		type = t;
	}
}

// 곡/타입 선택 시 함수
$(document).ready(function(){
	$(".sel_context, .sel_context_r").click(function(e) {
		e.preventDefault();

		$("#iframe_main").attr("src", arr[album][number][type]);
	})
});

// chapter 호버시
// $(document).ready(function(){
// 	$(".chapter").hover(function(){
// 		$(this).css('width', '25%');
// 		$(".rside").css('width', '5%');
// 	}, function(){
// 	$(this).css('width', '15%');
// 	$(".rside").css('width', '15%');
// 	});
// });

// chapter 내 #album_1~4 호버시
$(document).ready(function(){
	$("#album_1").hover(function(){
		$(".select_chp").not("#album_1").css('width', '15%');
		$("#album_1").css('width', '55%');
	}, function(){
	$(".select_chp").not("#album_1").css('width', '25%');
	$("#album_1").css('width', '25%');
	});
	
	$("#album_2").hover(function(){
		$(".select_chp").not("#album_2").css('width', '15%');
		$("#album_2").css('width', '55%');
	}, function(){
	$(".select_chp").not("#album_2").css('width', '25%');
	$("#album_2").css('width', '25%');
	});
	
	$("#album_3").hover(function(){
		$(".select_chp").not("#album_3").css('width', '15%');
		$("#album_3").css('width', '55%');
	}, function(){
	$(".select_chp").not("#album_3").css('width', '25%');
	$("#album_3").css('width', '25%');
	});
	
	$("#album_4").hover(function(){
		$(".select_chp").not("#album_4").css('width', '15%');
		$("#album_4").css('width', '55%');
	}, function(){
	$(".select_chp").not("#album_4").css('width', '25%');
	$("#album_4").css('width', '25%');
	});
});

// rside 호버시
$(document).ready(function(){
	$(".rside").hover(function(){
		$(this).css('width', '25%');
		$(".chapter").css('width', '5%');
	}, function(){
	$(this).css('width', '15%');
	$(".chapter").css('width', '15%');
	});
});

// rside 내 #album 호버시
$(document).ready(function(){
	$("#album").hover(function(){
		$(".select_r").not("#album").css('height', '15%');
		$("#album").css('height', '55%');
	}, function(){
	$(".select_r").not("#album").css('height', '25%');
	$("#album").css('height', '25%');
	});
	
	$("#mv").hover(function(){
		$(".select_r").not("#mv").css('height', '15%');
		$("#mv").css('height', '55%');
	}, function(){
	$(".select_r").not("#mv").css('height', '25%');
	$("#mv").css('height', '25%');
	});
	
	$("#live_1").hover(function(){
		$(".select_r").not("#live_1").css('height', '15%');
		$("#live_1").css('height', '55%');
	}, function(){
	$(".select_r").not("#live_1").css('height', '25%');
	$("#live_1").css('height', '25%');
	});
	
	$("#live_2").hover(function(){
		$(".select_r").not("#live_2").css('height', '15%');
		$("#live_2").css('height', '55%');
	}, function(){
	$(".select_r").not("#live_2").css('height', '25%');
	$("#live_2").css('height', '25%');
	});
});

// logo_main 호버시
$(document).ready(function(){
	$(".logo_main").hover(function(){
		$("#logo_text").css('visibility', 'visible');
		$("#logo_text").css('opacity', '100%');
	}, function(){
	$("#logo_text").css('visibility', 'hidden');
	$("#logo_text").css('opacity', '0%');
	});
});
		
// 테스트
// $(document).ready( function() {

// 	$("#hi").load("../common/test.html");  
	
// });