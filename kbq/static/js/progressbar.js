
window.simple=function(){
    waitingDialog.show('Please Wait');
    setTimeout(function () {
        waitingDialog.hide();
    }, 2000);
}

window.animateText=function(){
    waitingDialog.show('Please Wait');
    var animation=waitingDialog.animate();
    setTimeout(function () {
        waitingDialog.hide();
        waitingDialog.stopAnimate(animation);
    }, 5000);
}

window.adv_animateText=function(){
    waitingDialog.show('');
    var animation=waitingDialog.animate(function(container){
        container.html(new Date());
    },1000);
    setTimeout(function () {
        waitingDialog.stopAnimate(animation);
        waitingDialog.hide();
        
    }, 6000);
}

window.progress=function(){
      waitingDialog.show();
    //---------------------------------
     waitingDialog.progress(0);
     setTimeout(function(){
        waitingDialog.progress(10);
         waitingDialog.message('Initialize your ENV..')
     },1000);
    //------------------------------------------
    var mocks=[{message:'Initialize your ENV..',prog:10},{message:'Upload required info...',prog:30},{message:'Please wait..',prog:40},{prog:50},{prog:55},{prog:56},{prog:57},{prog:61},{prog:70},{prog:75},{prog:77},{prog:80},{prog:88},{prog:89},{prog:91},{prog:92},{prog:94},{prog:95},{prog:96},{prog:99},{prog:100}] ;
    mocks.forEach(function(e,i){
         setTimeout(function(){
            if(e.message){
               waitingDialog.message(e.message)
            }else{
               waitingDialog.message(e.prog+'% ...')
            }
             waitingDialog.progress(e.prog);
         },(i+1)*2000)
    });
    
     setTimeout(function () {

             waitingDialog.hide();
        
    }, (mocks.length+0.5)*2000);
     
}
