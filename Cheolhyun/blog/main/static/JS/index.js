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
$(document).ready(function(){
	$(".chapter").hover(function(){
		$(this).css('width', '15%');
		$(".rside").css('width', '5%');
	}, function(){
	$(this).css('width', '10%');
	$(".rside").css('width', '10%');
	});
});

// rside 호버시
$(document).ready(function(){
	$(".rside").hover(function(){
		$(this).css('width', '15%');
		$(".chapter").css('width', '5%');
	}, function(){
	$(this).css('width', '10%');
	$(".chapter").css('width', '10%');
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
		
$(function(){
    $('#main_live').click(function(){
        $("#iframe_main").attr("src","live.html");
    });
});

$(function(){
    $('#main_category').click(function(){
        $("#iframe_main").attr("src","category.html");
    });
});

$(function(){
    $('#main_today').click(function(){
        $("#iframe_main").attr("src","today.html");
    });
});

$(function(){
    $('#main_club').click(function(){
        $("#iframe_main").attr("src","https://pbs.twimg.com/media/E02yfpJVkAAc7OF?format=jpg&name=large");
    });
});

$(function(){
    $('#main_event').click(function(){
        $("#iframe_main").attr("src","https://mediahub.seoul.go.kr/uploads/event/2020/12/ced2af62d51f4a1284893b4a2bad13c1.png");
    });
});