function getKey(elm){
    var url='cgi-bin/getKeys.py';
    $.getJSON(url,null,function(data,status){
	    data.forEach(function(sm){
		    var s=sm[0] +'='+sm[1]+',';
		    var tg=sm[0];
		    var al=$('<a>').attr('href',tg).attr('value',tg);
		    al.append(s);
		    al.click(function(){
			    var val=$(this).attr('value');
			    var url='cgi-bin/searchWord.py?word='+val;
			    $.getJSON(url,null,hideIMG);
			    return false;
			});
		    $("#keyArea").append(al);
		    
		});
	});
}

function hideIMG(data,status){
    $("#showRanking > a").each(function(index,elm){
	    elm.hidden=false;
	});
    $("#showRanking > a").each(function(index,elm){
	    elm.hidden=true;
	});
    var sminfos=new Array();
    data.forEach(function(smid){
	    sm='show_ranking_'+smid;
	    sminfos.push(sm);
	});
    $("#showRanking > a").each(function(index,elm){
	    sminfos.forEach(function(smid){
		    if(elm.id==smid){
			elm.hidden=false;
		    }
		});
	});
}
function searchWord(elm){
    var val=elm.val();
    var url='cgi-bin/searchWord.py?word='+val;
    $.getJSON(url,null,hideIMG);
}
function showRanking(data,status){
    data.forEach(function(sminfo){
	    var title=sminfo['title'];
	    var thumb=sminfo['thumb'];
	    var link=sminfo['link'];
	    var smid="show_ranking_"+sminfo['smid'];
	    var thumb=$('<img>').attr('src',thumb).attr('title',title).attr('width',96);
	    var tha=$('<a>').attr('id',smid).attr('href',link).attr('target','_blank');
	    tha.append(thumb);
	    $('#showRanking').append(tha);
	});
}

function readRanking(){
    var url='cgi-bin/readRanking.py';
    $.getJSON(url,null,showRanking);

}